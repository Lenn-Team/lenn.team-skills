# Reference songs and audio

Claude cannot hear audio. Two routes still make references usable – similar to style references in image generators, only through description instead of the image itself.

## Route 1: Research known songs

The user names title and artist – and ideally **what** they like about it.

1. Collect traits via web search: tempo (BPM), key, time signature, length, genre, instrumentation and production (reviews, producer interviews, credits), vocal style, structure.
   BPM/key databases exist (e.g. songbpm, tunebat, musicstax) – values are algorithmic estimates; half-/double-tempo confusion happens.
2. Write a trait profile:

```
Reference: <title – artist> (internal only)
User likes: <e.g. "the dry, close vocal and the bass">
Tempo/feel: 96 BPM, halftime groove
Key/mode: F minor (source: …)
Instruments: electric piano, sub-bass, dry drums, guitar licks
Vocals: female, alto, breathy in verses, fuller in chorus
Production/era: modern, little reverb, close-miked
Structure: short intro (4 bars), post-chorus hook
→ Take: groove, vocal closeness, post-chorus idea
→ Don't take: melody, lyric lines, title, voice
```

3. Only the traits go into the style prompt – never artist or song names. Suno rewrites artist names anyway; ElevenLabs rejects copyrighted material.

## Route 2: Measure an audio file

The user uploads an audio file (own demos, voice memos, purchased tracks, generations from Suno/ElevenLabs for comparison).

```bash
python3 scripts/audio_analysis.py <file> [--json result.json]
```

Delivers: duration, tempo estimate (with half-/double-tempo note), key estimate with confidence, loudness (LUFS if `pyloudnorm` is available, otherwise RMS), energy curve in windows, likely section boundaries, spectral brightness.

Interpretation:
- Energy curve → structure plan (where the song builds, where it drops).
- Time of the first big energy step → when the first chorus/drop starts.
- Brightness (spectral centroid) → "warm/dark" vs. "bright/brilliant" in the prompt.
- Don't put a low-confidence key estimate into the prompt.

State the limits openly: the script detects no instruments, no vocal style and no mood. The values are estimates.

Requires: `pip install librosa` (optionally `pyloudnorm`). Run only in the sandbox/workspace; don't install anything on the user's computer without asking.

## Rights
- Analysing and describing other people's recordings is unproblematic; **uploading** them as an audio source to Suno or ElevenLabs is not – both require rights to the material or check uploads for copyright.
- Use only own material as audio source in the generator (hummed melody, own demo). Then set "Audio Influence" in Suno (`suno.md`).
