# ElevenLabs Music

Research status: November 2026 (Music v2.5 as the current model; `music_v1` is deprecated). Official docs: elevenlabs.io/docs → Music → Best practices / Composition plans.

## 1. When ElevenLabs instead of Suno
- Clearer licensing (agreements with labels and publishers), many languages, stems.
- Precise control of tempo, key and section lengths.
- Good for instrumentals, background music, stems and comparison versions.
- **Release on Spotify from the Creator plan** (according to comparison sites; check the current terms before release). Film/TV/radio are excluded on self-serve plans.

## 2. How the prompt is read
A prompt answers five questions: **genre, mood, instrumentation, tempo, production era.** Whatever is left open, the model fills with the most average choice. So set all five deliberately – but don't overload; length alone doesn't make it better.

## 3. Rules
- **Production vocabulary** works directly: *sidechained, close-mic'd, bone-dry, tape saturation, plate reverb, wide stereo*. Alternatively describe the room.
- **BPM and key** ("92 BPM, in D minor") – kept precisely according to ElevenLabs.
- **Vocals:** texture and delivery (*breathy, raspy, whispered, belted*); several voices ("two singers harmonizing").
- **Describe the structure chronologically**, as you would explain it to a band; name pauses and silence explicitly.
- **Timing:** "lyrics begin at 15 seconds", "instrumental only after 1:45"; instrumentals with "instrumental only".
- **Stems:** "solo piano in C minor, 90 BPM" or "a cappella female vocals".
- **No artist or band names, no copyrighted lyrics** – leads to an error or a counter-suggestion.
- **Audio reference:** own material only; uploads are checked for copyright before generating.

## 4. Composition plan (for full control)
Instead of a free-text prompt, a structured plan of ordered sections (up to 30 "chunks" with v2.5). Per section:
- `text`: section name in square brackets + lyric lines (e.g. `"[Verse 1]\nLine 1\nLine 2"`)
- `duration_ms`: length
- `positive_styles` / `negative_styles`: local style
- `context_adherence`: how closely the section sticks to the overall context

`respect_sections_durations = false` gives better sound quality with less exact lengths.

Practical route: have a plan generated from a prompt, then overwrite the sections with your own lyrics.

**Package format for ElevenLabs** (in the production package, section B):
```
Global prompt: <genre, mood, instruments, tempo/key, era, vocals, mix>
Length: <mm:ss>
Sections:
1. [Intro] – 0:08 – style: … – no lyrics
2. [Verse 1] – 0:20 – style: … – lyrics: …
…
Negative (global): …
```

## 5. Tools in the session
If an ElevenLabs connector is attached, first check which music tools it actually offers (read tool list/descriptions; fetch the connector's model guide if available). Some connector variants offer no music generation at all – then output the package for copy and paste. Use only existing functions, confirm before generating (credits).

## 6. Comparing Suno ↔ ElevenLabs
For a fair comparison use the same lyrics and the same sound profile, create both packages in parallel and let the user rate them in the same listening log (voice, intelligibility, genre fidelity, mix, structure, overall impression).

## Sources
- ElevenLabs Docs: Music – Best practices; Composition plans; Music quickstart (elevenlabs.io/docs)
- Comparison sites Nov 2026 (e.g. TeamDay, Rework, undetectr) on plans and release rights
