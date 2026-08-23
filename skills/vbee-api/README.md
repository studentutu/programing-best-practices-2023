# VBee API Agent Skill

This directory contains a reusable AI Agent skill for integrating with [VBee's API documentation](https://api-docs.vbee.vn/llms.txt). It covers text-to-speech, speech-to-text, voice discovery, asynchronous callbacks, request polling, and realtime speech streaming.

## What it provides

The skill gives an agent a practical workflow for selecting the correct VBee API, validating request constraints, handling credentials safely, interpreting statuses and errors, and returning useful results. For text-to-speech requests, it requires the agent to ask for the target **language** and **voiceover** when either is missing or ambiguous. It can query VBee's voice catalog and present a short list of matching voices before synthesis.

## Package contents

| File | Purpose |
| --- | --- |
| `SKILL.md` | Core trigger description, decision logic, execution workflow, privacy rules, and error-handling guidance. |
| `references/api_reference.md` | Detailed endpoints, payload fields, limits, callback schemas, WebSocket messages, examples, and source links. |

## Supported operations

| Operation | Current VBee endpoint | Notes |
| --- | --- | --- |
| Voice discovery | `GET https://vbee.vn/api/public/v1/voices` | Filter by language, gender, ownership, or voice code; paginate with a cursor. |
| Short TTS | `POST https://api.vbee.vn/v1/tts` | Synchronous mode; text up to 300 characters; binary audio response. |
| Long TTS | `POST https://api.vbee.vn/v1/tts` | Asynchronous mode; text up to 100,000 characters; callback URL required. |
| TTS status | `GET https://api.vbee.vn/v1/tts/requests/{requestId}` | Retrieves status and a fresh audio URL when available. |
| File STT | `POST https://api.vbee.vn/v1/stt` | WAV input using multipart form data; sync or async mode. |
| Streaming STT | `wss://api.vbee.vn/v1/stt/realtime` | Raw mono 16-bit PCM at 8 kHz or 16 kHz. |

## Credential handling

Provide the App ID and bearer token through environment variables or a secure secret store. The skill uses `VBEE_TOKEN` and `VBEE_APP_ID` as conventional names, but host applications may map them differently. Never commit credentials, expose tokens in logs, or paste live tokens into source files.

## Documentation source

The skill was built from VBee's machine-readable documentation index and current API pages. The reference file preserves the relevant source links so endpoint behavior can be checked when VBee changes its API.
