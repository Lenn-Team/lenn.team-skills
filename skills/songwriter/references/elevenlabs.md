# ElevenLabs Music

Research status: November 2026 (Music v2.5 as the current model; `music_v1` is deprecated and will be removed on 31 January 2027). Official docs: elevenlabs.io/docs → Music → Best practices / Composition plans. Section 7 collects field notes from real sessions – they take precedence over general guidance where the two disagree.

## 1. When ElevenLabs instead of Suno
- Clearer licensing (agreements with labels and publishers), many languages, stems.
- Precise control of tempo, key and section lengths.
- Good for instrumentals, background music, stems and comparison versions.
- **Release on Spotify from the Creator plan** (according to comparison sites; check the current terms before release). Film/TV/radio are excluded on self-serve plans.

## 2. How the prompt is read
A prompt answers five questions: **genre, mood, instrumentation, tempo, production era.** Whatever is left open, the model fills with the most average choice. So set all five deliberately – but don't overload; length alone doesn't make it better.

From practice:
- **What comes first dominates.** "German rap, …" at the start produced pure rap; "EDM festival anthem, …" first produced too much EDM. Put the main genre first and blends as modifiers later.
- **Calm words for short moments colour the whole song.** "pad swells", "long calm pauses" for one passage made the entire track slow and sad. Describe local moments in the section, not in the global prompt.
- **State the mode.** Without "major key" the result is often minor; naming a minor key ("A minor") guarantees it. Don't assume minor for emotional songs – ask or decide in the brief.
- The narrated arrangement recommended in the docs ("start with just …, then bring in …") did not improve results in practice.

## 3. Rules
- **Production vocabulary** works directly: *sidechained, close-mic'd, bone-dry, tape saturation, plate reverb, wide stereo*. Alternatively describe the room.
- **BPM and key** ("92 BPM, in D minor") – kept precisely according to ElevenLabs.
- **Vocals:** texture and delivery (*breathy, raspy, whispered, belted*); several voices ("two singers harmonizing").
- **Describe the structure chronologically**, as you would explain it to a band; name pauses and silence explicitly.
- **Timing:** "lyrics begin at 15 seconds", "instrumental only after 1:45"; instrumentals with "instrumental only".
- **Stems:** "solo piano in C minor, 90 BPM" or "a cappella female vocals".
- **No artist or band names, no copyrighted lyrics** – leads to an error or a counter-suggestion.
- **Audio reference:** own material only; uploads are checked for copyright before generating.

## 4. Composition plan (API only)
Composition plans are an **API feature** (SDK, `music/compose`, connectors that expose it). The web app has no composition-plan input – there, use the prompt plus lyrics and the music editor (section 5).

Instead of a free-text prompt, a structured plan of ordered sections (up to 30 "chunks", total 3 s–10 min, 3–120 s per chunk; requires `music_v2` or `music_v2_5`). Per chunk:
- `text`: section name, lyrics and inline cues (syntax below)
- `duration_ms`: length
- `positive_styles` / `negative_styles`: local style (max. 50 each)
- `context_adherence`: `low`, `medium` or `high` (default) – how closely the chunk follows the surrounding chunks

`respect_sections_durations = false` gives better sound quality with less exact lengths. Via the API a plan can be generated from a prompt and then overwritten with your own lyrics.

**Lyric syntax (official):**
- Section names in square brackets: `[Verse 1]`, `[Chorus]`, `[Bridge]`
- Lyrics as plain text, one line per line break
- Non-lyrical sounds in round brackets: `(ooh)`, `(hmmm hmmm)`
- Short inline cues in curly braces: `{guitar solo}`, `{instrumental break}`
- Vocal style for a whole section goes into `positive_styles`, not into the text.

**What happens in practice** (13 rounds, German pop song, Nov 2026):
- **Breaths and other non-verbal sounds are not reliably controllable.** `[inhale]`/`[exhale]` on its own line produced an audible breath exactly once and not again on an unchanged repeat; adjectives (`[long inhale]`), `{inhale}` and `(hhhhh)` had no effect. Say so honestly instead of promising it.
- **Empty section tags get sung as murmuring** (e.g. a lone `[Build-up]`). For instrumental parts write the cue explicitly: `[Drop]` followed by `{instrumental synth drop}`.
- **Too little length → dropped lines,** especially in pre-chorus and bridge. Give sections enough time (roughly 2–2.5 s per sung line at mid tempo) and check in phase 9b.
- **Same-named sections are sung differently each time** – repeated choruses are not copies.

**Package format for ElevenLabs** (in the production package, section B):
```
Global prompt: <genre, mood, instruments, tempo/key, era, vocals, mix>
Length: <mm:ss>
Sections:
1. [Intro] – 0:08 – style: … – text: {instrumental intro}
2. [Verse 1] – 0:20 – style: … – lyrics: …
…
Negative (global): …
```
Instrumental sections always get an explicit `{…}` cue, never an empty tag. In the web app, paste the global prompt into the prompt field and the lyrics with section names below it; set lengths later in the music editor.

## 5. Web app: music editor (repair instead of regenerating)
In the ElevenLabs web app a finished song can be edited section by section: click a section, change its lyrics and its section style ("Edit styles of this section"), drag its length, and regenerate only that section. This was the most effective tool in practice – e.g. to restore missing lines in pre-chorus and bridge.

Rule: **if the song as a whole works, repair sections in the editor instead of generating a new song.** Generations made through the connector return a `product_link` to the music project; note it in the package so the user can open the song in the editor.

## 6. Tools in the session
If an ElevenLabs connector is attached, first check which music tools it actually offers (read tool list/descriptions; fetch the connector's model guide if available). Some connector variants offer no music generation at all – then output the package for copy and paste. Use only existing functions, confirm before generating (credits).

**Credits (field values, Nov 2026):** about 3,000–3,400 credits per music generation of ~3:30 – the tool's estimate was almost twice as high. A transcription estimated at 75 credits was billed at 1,221. One night of iterating cost about 80,000 credits. Therefore: treat estimates as unreliable, agree on a budget before a series (SKILL.md phase 9), and log actual charges.

**Organising the flow:** create text nodes for prompt and lyrics from the start and connect them to the music nodes, instead of loose cards per version. Name nodes uniquely per version and mark the favourite.

**Transcription for checking:** use speech-to-text on the chosen version (SKILL.md phase 9b). Whispered parts are often missed; contractions get normalised.

## 7. Comparing Suno ↔ ElevenLabs
For a fair comparison use the same lyrics and the same sound profile, create both packages in parallel and let the user rate them in the same listening log (voice, intelligibility, genre fidelity, mix, structure, overall impression).

**Field result (one German pop song, Nov 2026):** ElevenLabs was clearly preferred. Suno largely ignored the performance cues in the tags, the voice sounded "typically AI", and breaths were not possible. With ElevenLabs, the section editor made targeted repairs possible. One test is not a rule – keep comparing per song.

## Sources
- ElevenLabs Docs: Music – Best practices; Composition plans; Music quickstart (elevenlabs.io/docs)
- ElevenLabs Docs: Composition plans – "Writing lyrics" (section names, sounds, inline directions; limits)
- Comparison sites Nov 2026 (e.g. TeamDay, Rework, undetectr) on plans and release rights
- Field notes: session "Dreh die Welt leise" (Lenn.Team, 16 Nov 2026) – 13 generation rounds with Suno v6 and ElevenLabs Music v2.5
