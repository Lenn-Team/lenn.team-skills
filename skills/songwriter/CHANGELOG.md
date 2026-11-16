# Changelog

## 0.1.1 – 2026-11-16
Field notes from the first real session ("Dreh die Welt leise", Suno v6 and ElevenLabs Music v2.5).
- Hard gate: no chorus without an interview, even if a draft exists; a draft is material, not a brief
- Phase 9: agree on a credit budget before a series, log actual credits, repair sections instead of regenerating, no pasted-in SFX breaths, log per round
- New phase 9b: transcribe the result and compare it with the lyrics; sing-along lyrics follow what is actually sung
- `references/elevenlabs.md`: composition plans are API-only (fixed), music editor in the web app, official lyric syntax plus what works in practice (breaths unreliable, empty tags get sung, short sections drop lines), prompt order and mode, credit values, flow organisation, Suno comparison
- `references/suno.md`: field note on ignored cues and voice quality
- Production package template: budget and links, sung-vs-written table, log with credits and rating
- ElevenLabs instrumental parts get an explicit `{…}` cue instead of an empty tag (package format, `genres.md`, `structure.md`)
- `textcheck.py`: `{…}` cue lines are ignored for syllables and word count; empty section tags are reported (relevant for ElevenLabs)

## 0.1.0 – 2026-11-16
First version.
- Workflow in eleven phases (task, interview, research, brief, chorus, verses, check, revision, production package, generation, release)
- Lyrics in the user's language; instructions in English
- Section "Working in Claude" (choice questions, task list, documents, visualisation, connectors)
- 16 reference files incl. genre profiles, music psychology, anti-AI rules, languages (German, English, others), Suno v6, ElevenLabs Music v2.5, Spotify release
- Templates for song brief, production package and release sheet
- Scripts `textcheck.py` and `audio_analysis.py`
- Original example "Noch einmal drücken" (German)
