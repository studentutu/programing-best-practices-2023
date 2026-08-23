---
name: vbee-api
description: Use VBee's HTTPS APIs for Vietnamese and multilingual text-to-speech, speech-to-text, voice discovery, asynchronous jobs, callbacks, polling, and realtime/streaming audio. Trigger when an agent must integrate with api.vbee.vn, studio.vbee.vn, or api-docs.vbee.vn, generate speech, transcribe WAV/PCM audio, select a VBee voice, or troubleshoot VBee API requests.
---

# VBee API Agent Skill

Use this skill to plan and execute VBee API integrations. Prefer the current VBEE API documentation over the legacy API. Treat every token, App ID, uploaded audio, callback URL, and generated audio URL as sensitive.

## Required execution workflow

1. Identify the operation: list voices, synthesize speech, transcribe audio, retrieve an asynchronous result, receive a callback, or stream speech recognition.
2. For every TTS or voiceover request, confirm the user's **language** and **voiceover preference** before synthesis. If either is missing or ambiguous, ask a concise clarification question and do not call TTS yet. If the user names only a language, retrieve/filter the voice catalog by `language_code` and present a small choice of suitable voices with display name, gender, dialect/accent, and demo URL when available. If the user names a voice but not its language, verify the voice code in the catalog and confirm the associated language. Preserve an explicitly selected voice across follow-up requests unless the user changes it.
3. Confirm credentials are available as environment variables or secure connector inputs. Never ask the user to paste a live token into chat and never hard-code credentials. The required request identity is `Authorization: Bearer <token>` plus `App-Id: <app-id>`.
4. Choose the transport from the input size and latency requirement:
   - Use TTS Realtime (`mode: sync`) for text up to 300 characters when audio is needed immediately.
   - Use TTS Batch (`mode: async`) for longer text, media production, or bulk work; provide `webhookUrl` and retain `requestId`.
   - Use STT Realtime for WAV audio shorter than 10 seconds and under 10 MB.
   - Use STT Batch for longer WAV audio under 100 MB; use `webhookUrl` or poll by `transcriptId` when supported by the deployed API.
   - Use STT Streaming over WebSocket for live mono 16-bit PCM at 8 kHz or 16 kHz.
5. Validate locally before sending. Trim TTS text; reject empty text. Check that the selected `voiceCode` exists and matches the confirmed language. Check mode, output format, bitrate, speed, sample rate, audio type, file size, audio duration, and required callback fields against `references/api_reference.md`.
6. Call the documented endpoint with the exact header casing and content type. For multipart STT, send either `audioContent` or `audioUrl` as documented; do not send a WAV header in streaming PCM chunks.
7. Normalize the result into a useful agent response: operation, confirmed language, selected voice name/code, request/transcript ID, status, output URL or transcript, expiry caveat, and next action. Do not expose bearer tokens or raw sensitive payloads in logs.
8. For asynchronous work, persist the ID and use the callback as the primary completion signal. If polling is necessary, back off rather than issuing tight loops. Treat `PROCESSING`/`PENDING` as nonterminal, `COMPLETED`/`SUCCESS` as terminal success, and `FAILED`/`FAILURE` as terminal failure.
9. Verify callback authenticity using an application-level secret or network control if the deployment provides one. Make the handler idempotent using `request_id`/`transcriptId`, return a fast 2xx response, and process heavy work out of band.

## Routing rules

| User need | VBee path | Important constraint |
| --- | --- | --- |
| Find a voice | `GET https://vbee.vn/api/public/v1/voices` | Authenticated; paginate with `cursor`; filter by ownership, language, gender, or code. |
| Short TTS | `POST https://api.vbee.vn/v1/tts` | JSON; `mode: sync`; text ≤ 300 chars; response is audio binary. |
| Long TTS | `POST https://api.vbee.vn/v1/tts` | JSON; `mode: async`; text ≤ 100,000 chars; `webhookUrl` required. |
| TTS job status/audio | `GET https://api.vbee.vn/v1/tts/requests/{requestId}` | Authenticated; audio links are temporary. |
| File transcription | `POST https://api.vbee.vn/v1/stt` | multipart/form-data; WAV; async for batch, sync for short audio. |
| Live transcription | `wss://api.vbee.vn/v1/stt/realtime?token=<token>&appId=<app-id>` | Configure first, wait for `READY`, then send timed PCM chunks. |

## Language and voiceover selection

Before calling TTS, follow this decision logic:

1. Check whether the user supplied both a target language and a voiceover choice. Accept a specific catalog voice code, a catalog display name, or a preference such as gender, region, accent, or speaking style.
2. If the language is missing, ask: `Which language should the voiceover use?` If the request is multilingual, ask whether the user wants one voice per language or a single voice where supported.
3. If the voiceover is missing, ask: `Which voiceover would you like?` Then query `GET https://vbee.vn/api/public/v1/voices` using the chosen language and relevant filters. Present no more than five good candidates and include each voice's name, gender, language/dialect, code, and demo link when available.
4. If the user gives a voice description rather than a code, map it to catalog results. Do not invent or silently substitute a voice. If no exact match exists, explain the closest alternatives and ask the user to choose.
5. Confirm the final selection in one compact line before synthesis, for example: `Language: Vietnamese (vi-VN); voiceover: HN - Ngọc Huyền; format: MP3.` Proceed without another confirmation only when the user has already clearly specified these choices in the same request.
6. Use the catalog `code` as `voiceCode` in the TTS payload. For realtime TTS, additionally verify that the selected voice is in the documented realtime-supported set.

For synchronous TTS, send JSON with `text`, `voiceCode`, `mode: "sync"`, and optional `outputFormat`, `bitrate`, `speed`, and `sampleRate`. Save the binary response to a file rather than attempting to parse it as JSON. Realtime supports `mp3`, `wav`, and `pcm`; the current documented voice set for realtime is limited, so query the voice catalog when the requested voice is uncertain.

For batch TTS, send `mode: "async"`, `webhookUrl`, `voiceCode`, and optional audio controls. The create response normally contains `requestId` and `status: "PROCESSING"`. A successful callback includes `request_id`, `status`, and `audio_link`; a status lookup returns `audioLink` when `status` is `COMPLETED`. Download or copy the audio promptly: documented batch audio links expire after about 3 minutes, while the generated audio is retained for about 3 days and can be re-addressed through Get request.

## STT handling

For batch or realtime file STT, use `multipart/form-data` with `audioContent` or `audioUrl`, `mode`, and optional `webhookUrl`. The current documentation specifies WAV input and accepted sample rates of 8000, 16000, 22050, 32000, 44100, and 48000 Hz. Realtime file STT is limited to audio under 10 seconds and 10 MB. Batch STT files must be under 100 MB. Return both the combined `transcript` and timestamped `utterances` when available.

For streaming STT, connect with the token and App ID in the WebSocket URL. Send one `STREAMING_CONFIG`, wait for `READY`, then send `AUDIO_CHUNK` messages containing base64 raw little-endian signed 16-bit mono PCM. Keep chunk timing regular, preferably 80–100 ms. Handle `INTERIM_RESULT` as provisional, `FINAL_RESULT` as immutable, send `DONE` after audio ends, answer/emit keep-alive `PING`/`PONG` as required, and stop after `STREAM_END`. Respect the 90-second session limit and reconnect only for retryable errors.

## Error handling

Map `401 UNAUTHORIZED` to credential/header/App ID checks. Map `400 BAD_REQUEST` to payload, size, mode, format, voice, sample-rate, or syntax validation. Treat `429 TTS_CCR_MAX_LIMIT_REACHED` and `STT_MAX_CCR_REACHED` as retryable concurrency pressure with exponential backoff. Treat provider-unavailable, recognize-failed, and internal errors as retryable only when the reference marks them retryable. Do not retry invalid credentials, invalid audio configuration, missing jobs, expired/unsupported inputs, or insufficient credits without changing the request or account state.

When documentation appears inconsistent, use the concrete current endpoint and payload shown in the current page, record the discrepancy, and avoid guessing. Read `references/api_reference.md` for exact field tables, examples, callback schemas, streaming messages, and source links.

## Credential and privacy rules

Use `VBEE_TOKEN` and `VBEE_APP_ID` or an equivalent secret store by convention, but honor the host application's naming. Redact `Authorization`, token query parameters, callback secrets, signed audio URLs, and raw audio/transcript data from logs. Ask for explicit confirmation before sending user-provided audio or text to VBee if the task involves sensitive personal, financial, health, or confidential information.
