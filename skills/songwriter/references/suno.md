# Suno

Research status: November 2026 (model family v6). Many details come from community guides and tests, not official documentation. **If something doesn't work as described, check limits, models and features against help.suno.com.**

## 1. Models and plans
- **v6** (Pro/Premier, default) – balanced, for final versions.
- **v6-wild** (Pro/Premier) – more varied, for first ideas; then possibly a cover on v6.
- **v6-mini** (all plans, the only option on the free plan).
- **Rights:** only songs created during an active Pro/Premier subscription may be used commercially and released; a later subscription does not apply retroactively. Details: `release.md`.

## 2. Fields (custom mode)

| Field | Content | Limit (reported) |
|---|---|---|
| Title | song title | – |
| Styles | sound description | 1,000 characters |
| Lyrics | generator version of the lyrics with tags | 5,000 characters |
| Exclude Styles | unwanted elements (Pro/Premier) | 1,000 characters |

Each field has one job. If Styles, Lyrics and Exclude contradict each other, the result gets worse, not more controlled.

## 3. Style prompt
**Order (= weighting):**
1. Voice (gender/range, texture, delivery) – first, otherwise the vocals get buried in the mix
2. Main genre + 1–2 subgenres/modifiers (+ era)
3. Tempo (BPM) and optionally key/mode
4. 2–3 key instruments with playing style
5. Production/mix (room, closeness, warmth, width)
6. Language, if not English

**Rules:**
- 4–10 descriptors; from about 12 it gets arbitrary. Each descriptor must add something – stacks of synonyms ("sad, melancholic, sorrowful") count as one.
- Concrete texture terms instead of judgements: "gravelly baritone, belting chorus" instead of "powerful vocals"; "close-mic'd, dry" instead of "intimate vibe".
- No artist names (they get replaced), no empty phrases ("epic, amazing, emotional masterpiece").
- The emotional arc belongs in the performance cues of the lyrics, not in Styles.
- Duets: "male and female duet vocals" in Styles, singer changes via tags in the lyrics.
- English terms in the Styles field work most reliably, also for non-English songs; name the sung language as well ("German lyrics").

**Example:**
```
Warm female alto, breathy verses, full belted chorus, German lyrics, modern German pop with indie-folk touches, 96 BPM, fingerpicked acoustic guitar, upright piano, soft brushed drums, subtle strings in final chorus, close-mic'd, warm and dry mix
```

## 4. Exclude Styles
- 2–4 entries, as plain terms: `choir`, `autotune`, `EDM drop`, `screaming`.
- Negations in the Styles field ("no drums") are largely ignored by v6 – use the Exclude field.
- The effect is probabilistic, not guaranteed.
- Don't exclude what the Styles field asks for.

## 5. Lyrics field (generator version)
- **Section tags** in square brackets: `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Post-Chorus]`, `[Bridge]`, `[Breakdown]`, `[Instrumental Break]`, `[Guitar Solo]`, `[Drop]`, `[Outro]`, `[Fade Out]`, `[End]`. Suno calls them "song structure labels"; they guide, they don't guarantee.
- **Performance cues** inside the tag, at most three per section: `[Verse 1 – sparse, whispered]`, `[Chorus – full band, gang vocals]`, `[Final Chorus – key change up]`.
- **Singer changes:** `[Verse 2 – male vocal]`, `[Chorus – duet]`.
- **Only sung lyrics and tags.** Stage directions as running text or in round brackets are often sung. Use round brackets only for backing vocals/echoes: `I stay here (stay here)`.
- **Instrumental passages:** tag without lyrics, e.g. `[Instrumental Break – piano]`.
- **Ending:** set `[Outro]` + `[End]`, otherwise the song sometimes ends abruptly or keeps going.
- **Stretching and stress:** hyphens for held syllables ("sta-ay"), commas for short pauses, ellipses for fading out. CAPITALS sound like shouting – only deliberately.
- **Word protection:** if Suno changes lyrics, add "Sing exactly as written." at the start of the lyrics or in Styles. (Effect varies.)
- **Atmosphere:** name sounds (rain, crowd) both in Styles and as a tag in the lyrics.

## 6. Pronunciation
- Write names, abbreviations, numbers, foreign and ambiguous words phonetically – in **every** occurrence, including chorus repeats.
- Keep a pronunciation table in the production package (word | generator spelling | reason).
- The sing-along lyrics keep the correct spelling.
- German: see `languages/german.md`, section 7.

## 7. Sliders (advanced options)
- **Weirdness** (default 50): how far the model departs from the expected. Start 40–55; higher for experiments.
- **Style Influence** (default 50): how strongly the Styles field is weighted. Start 50–65; raise if the genre drifts.
- **Audio Influence** (default 25, only with an audio upload): how strongly the uploaded recording shapes the result. 50–70 for melody fidelity, lower for free reinterpretation.
- **Variety:** active by default on v6; Suno then rewrites the style prompt itself. With a deliberately built style prompt set it to 0/off.
- **Max Mode:** double credits, recommended for songs over about 2 minutes, covers and consistent vocals.
- Change only one slider per test run.

## 8. Further features
- **Audio upload:** own recording (melody, demo, voice memo) as a basis. Basic up to 60 s, Pro/Premier up to 8 min (reported). Rights to the material required.
- **Cover:** existing song in a new style; with Variety off melody and structure are more likely to be kept.
- **Extend:** lengthen a song; quality can drop from about 6–7 minutes, at most 2–3 extends.
- **Voices / custom models:** your own voice or your own model trained on your own catalogue. With a voice, leave gender/range out of Styles. Never clone other people's voices.
- **Studio / song editor:** regenerate sections selectively; listen before export (occasional language glitches).

## 9. Known weaknesses
- The model's word preferences (*neon, echo, ghost, silver, shadow, whisper, crystal, velvet*) – avoid them in your own lyrics from the start.
- Rock/metal sometimes sound washed out, vocals drift towards generic post-grunge.
- Extreme genre fusions get muddy.
- With non-English lyrics, occasional English pronunciation of single words.

## 10. Troubleshooting (one change per round)

| Problem | Action |
|---|---|
| Vocals too quiet / buried | Voice at the start of Styles; "lead vocal upfront" |
| Genre drifts | Simplify Styles, repeat the main genre, Style Influence up, Variety off |
| Chorus doesn't lift | Performance cue in the chorus tag ("full band, wide, harmonies"); thin out the verse |
| Arrangement too busy | Name pauses ("bass drops out"), fewer instruments |
| Song ends abruptly | `[Outro]` + `[End]`, possibly `[Fade Out]` |
| Lyrics changed/skipped | Shorten sections, check character count, "Sing exactly as written." |
| Word mispronounced | Phonetic spelling, everywhere |
| Unwanted choirs/effects | Exclude: `choir`, `autotune` … |

## 11. Variant strategy
Prepare 2–3 style variants per song that differ in **one** axis (e.g. tempo, instrumentation, vocal texture). 1–2 generations per variant, then continue selectively. Have the user rate results in a short listening log (voice, genre fidelity, mix, structure, intelligibility; 1–5 each).

## 12. Suno MCP (official connector, beta)
Since late October 2026 Suno offers an official MCP server (early access). If Suno tools are available in the session:
- Read the tool descriptions and use only the parameters actually offered – don't invent fields.
- Finish the production package and have the user confirm it **before** generating (credits).
- Pass title, styles, lyrics (generator version) and exclude separately where the tool allows it.
- Generated songs land in the user's Suno library; note links/IDs in the package.
- Update this section once the tools are known.

## Sources
- bitwize-music-studio/claude-ai-music-skills: `reference/suno/best-practices.md`, `reference/suno/models.md`, `skills/suno-engineer/SKILL.md` (GitHub, CC0)
- Jack Righteous: guides on v6 audio upload, sliders and meta tags (jackrighteous.com)
- Suno MCP beta: reports by Glitchwire and The AI Musicpreneur (October 2026)
