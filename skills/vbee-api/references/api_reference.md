# VBee API Reference

This reference reflects the current documentation exposed by [VBee API docs](https://api-docs.vbee.vn/llms.txt). Prefer these current endpoints over the legacy pages unless the user explicitly asks for legacy compatibility.

## Authentication and application setup

Create an API application at [studio.vbee.vn/apps](https://studio.vbee.vn/apps). The application provides an App ID and a JWT-like bearer token whose lifetime is selected during application creation. Tokens may be fixed-term, permanent, or custom-expiry. Send both headers on authenticated HTTP requests:

```http
Authorization: Bearer <access_token>
App-Id: <app-id>
```

Use `Content-Type: application/json` for TTS and `multipart/form-data` for file STT. The API service is HTTPS; the current API host used in examples is `api.vbee.vn`.

## Voice catalog

`GET https://vbee.vn/api/public/v1/voices`

The endpoint accepts `voiceOwnership` (`VBEE`, `COMMUNITY`, or `PERSONAL`), `code`, `languageCode`/`language_code` as documented, `gender` (`male` or `female`), `limit` from 1 to 100 (default 20), and a pagination `cursor`. The response has `result.pagination` with `has_next_page`, `has_prev_page`, `next_cursor`, and `prev_cursor`, plus `result.voices`. Each voice includes `code`, `name`, `gender`, `language_code`, `demo`, and `credit_factor`.

Example:

```bash
curl --location 'https://vbee.vn/api/public/v1/voices?voiceOwnership=VBEE&languageCode=vi-VN&limit=20' \
  --header 'Authorization: Bearer <access_token>' \
  --header 'App-Id: <app-id>'
```

Always use a catalog `code`; do not infer a voice code from a display name. Realtime TTS documentation names a narrower supported set, including HN - Ngọc Huyền, SG - Tường Vy, HN - Mai Phương, SG - Lan Trinh, and SG - Thảo Trinh.

## Text-to-Speech: Batch

`POST https://api.vbee.vn/v1/tts`

Send JSON with the following fields:

| Field | Required | Rules |
| --- | --- | --- |
| `text` | Yes | Trimmed, nonempty, maximum 100,000 characters. |
| `mode` | Yes | Must be `async`. |
| `webhookUrl` | Yes | Callback URL for completion. |
| `voiceCode` | Yes | Existing catalog voice code. |
| `outputFormat` | No | `mp3` or `wav`; default `mp3`. |
| `bitrate` | No | 8, 16, 32, 64, or 128 kbps; default 128. |
| `speed` | No | 0.25–1.9; default 1.0. |
| `sampleRate` | No | 8000, 16000, 22050, 24000, 32000, 44100, or 48000 Hz, subject to voice support. |
| `emphasisIntensity` | No | Integer 0–100 in multiples of 10; only supported voices. |
| `clientPause` | No | Object with `majorBreak`, `mediumBreak`, `paragraphBreak`, `sentenceBreak` in seconds. |

`clientPause` defaults are respectively 0.3, 0.25, 0.6, and 0.45 seconds. The first two accept 0.1–10 seconds; paragraph breaks accept 0–10; sentence breaks accept 0.1–10.

A successful creation response normally looks like:

```json
{"requestId":"<uuid>","status":"PROCESSING"}
```

The documented batch audio URL expires after approximately 3 minutes. The generated audio is retained for approximately 3 days; call Get request to obtain a fresh URL.

## Text-to-Speech: Realtime

`POST https://api.vbee.vn/v1/tts`

Send JSON with `text`, `mode: "sync"`, and `voiceCode`; text must be at most 300 characters. Optional fields are `outputFormat` (`mp3`, `wav`, or `pcm`; default `mp3`), `bitrate` (8, 16, 32, 64, or 128; default 128), `speed` (0.25–1.9; default 1.0), and supported `sampleRate`. The response is audio binary data, returned as chunks. Save stdout to a binary file and do not parse it as JSON unless the HTTP status indicates an error.

```bash
curl -X POST 'https://api.vbee.vn/v1/tts' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <access_token>' \
  -H 'App-Id: <app-id>' \
  --data '{"text":"Xin chào.","voiceCode":"hn_female_ngochuyen_full_48k-fhg","mode":"sync","outputFormat":"mp3"}' \
  --output output.mp3
```

## TTS job lookup and callback

Get job status with:

```http
GET https://api.vbee.vn/v1/tts/requests/{requestId}
```

A processing response has `requestId` and `status: "PROCESSING"`. A completed response has `status: "COMPLETED"` and `audioLink`. A failed request is returned as an error object, commonly with `BAD_REQUEST` and a message such as `Request is not found`.

The batch callback is an HTTP POST to the supplied `webhookUrl`. The documented body uses snake_case:

```json
{
  "app_id":"<app-id>",
  "request_id":"<request-id>",
  "characters":123,
  "voice_code":"<voice-code>",
  "audio_type":"mp3",
  "speed_rate":1.0,
  "sample_rate":"48000",
  "bitrate":128,
  "created_at":"<timestamp>",
  "status":"SUCCESS",
  "audio_link":"<temporary-url>"
}
```

`status` is documented as `SUCCESS` or `FAILURE`. Make handlers idempotent by request ID and acknowledge quickly.

## Speech-to-Text: file APIs

`POST https://api.vbee.vn/v1/stt`

Use `multipart/form-data` and send either `audioContent` (WAV file) or `audioUrl` (HTTP(S) URL to a WAV file). Accepted sample rates are 8000, 16000, 22050, 32000, 44100, and 48000 Hz.

For batch STT, send `mode: async`; files must be under 100 MB. For realtime file STT, send sync mode as supported by the deployment; audio must be under 10 seconds and under 10 MB. `webhookUrl` is optional in the documented file APIs.

A result may contain `transcriptId`, `status`, combined `transcript`, timestamped `utterances` with `text`, `startTime`, and `endTime`, and `audioDurationSeconds`. Status values are `PENDING`, `PROCESSING`, `COMPLETED`, and `FAILED`.

Example batch request:

```bash
curl -X POST 'https://api.vbee.vn/v1/stt' \
  -H 'Authorization: Bearer <access_token>' \
  -H 'App-Id: <app-id>' \
  -F 'audioContent=@recording.wav' \
  -F 'mode=async' \
  -F 'webhookUrl=https://example.com/stt-callback'
```

## Speech-to-Text: streaming WebSocket

Connect to:

```text
wss://api.vbee.vn/v1/stt/realtime?token=<token>&appId=<app-id>
```

Send one configuration message and wait for `READY`:

```json
{
  "type":"STREAMING_CONFIG",
  "config":{
    "sampleRateHertz":16000,
    "sampleSizeByte":2,
    "channel":1,
    "interimResults":true,
    "vadConfig":{"noInputTimeoutMs":10000,"speechCompleteTimeoutMs":800},
    "sessionId":"optional-client-id"
  }
}
```

Only 8000 or 16000 Hz, 16-bit samples (`sampleSizeByte: 2`), and mono (`channel: 1`) are supported. After `READY`, send regular messages such as:

```json
{"type":"AUDIO_CHUNK","audioContent":"<base64-raw-pcm>"}
```

The audio must be raw little-endian signed 16-bit PCM without a WAV header. Recommended chunks are 1280 bytes at 8 kHz (80 ms) or 3200 bytes at 16 kHz (100 ms). `INTERIM_RESULT` is provisional and may change; `FINAL_RESULT` is final for the utterance. After the last audio, send `{"type":"DONE"}`. Keep idle connections alive with `PING`/`PONG` when needed. The server eventually sends `STREAM_END`; sessions over 90 seconds receive `SESSION_TIMEOUT`.

Streaming errors include `UNAUTHORIZED`, `STT_INSUFFICIENT_SECONDS`, `STT_MAX_CCR_REACHED`, `STT_INVALID_SAMPLE_RATE`, `STT_INVALID_CHANNEL`, `STT_INVALID_SAMPLE_SIZE`, `PROVIDER_UNAVAILABLE`, `PROVIDER_UNKNOWN`, `SESSION_TIMEOUT`, `NO_INPUT_TIMEOUT`, `RECOGNIZE_FAILED`, `JOB_NOT_FOUND`, and `INTERNAL_ERROR`. Retry only errors documented as retryable.

## Common HTTP errors

| Code | HTTP status | Agent action |
| --- | --- | --- |
| `UNAUTHORIZED` | 401 | Verify bearer token, App ID, and header presence; do not blindly retry. |
| `BAD_REQUEST` | 400 | Correct fields, limits, mode, format, voice, sample rate, or syntax. |
| `TTS_CCR_MAX_LIMIT_REACHED` | 429 | Back off and retry later; concurrency limit reached. |
| `TTS_SPEND_CREDITS_FAILED` | 500 | Report credit/account issue; retry only with evidence of transient failure. |
| `INTERNAL_SERVER_ERROR` | 500 | Retry with bounded exponential backoff, then surface the failure. |

## Source pages

[Documentation index](https://api-docs.vbee.vn/llms.txt) · [Authentication and App ID](https://api-docs.vbee.vn/tao-ung-dung-app-id-va-token.md) · [TTS Batch](https://api-docs.vbee.vn/vbee-api/text-to-speech/batch-api.md) · [TTS Realtime](https://api-docs.vbee.vn/vbee-api/text-to-speech/realtime-api.md) · [TTS Get request](https://api-docs.vbee.vn/vbee-api/text-to-speech/get-request.md) · [TTS Callback](https://api-docs.vbee.vn/vbee-api/text-to-speech/callback-api.md) · [STT Batch](https://api-docs.vbee.vn/vbee-api/speech-to-text/batch-api.md) · [STT Realtime](https://api-docs.vbee.vn/vbee-api/speech-to-text/realtime-api.md) · [STT Streaming](https://api-docs.vbee.vn/vbee-api/speech-to-text/streaming-api.md) · [Voices](https://api-docs.vbee.vn/vbee-api/voices/get-list-voices.md)
