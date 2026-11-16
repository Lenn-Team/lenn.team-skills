# Song structure

Structure decides whether a repeat rewards or bores. The structure plan and energy curve are made in the brief – before the lyrics.

## 1. Basic forms

| Form | Sequence | Fits |
|---|---|---|
| Verse–chorus | V–C–V–C–B–C | almost everything |
| With pre-chorus | V–P–C–V–P–C–B–C | pop, Schlager, rock – the pre builds tension |
| With post-chorus | V–P–C–PC–V–P–C–PC–B–C–PC | modern pop, dance – post-chorus as second, often wordless hook |
| AABA (32 bars) | A–A–B–A | jazz, musical, chanson, retro pop – hook in A, B as contrast |
| Strophic | V–V–V–V (refrain line at the end of each verse) | folk, singer-songwriter, shanty |
| Rap | intro–hook–V(16)–hook–V(16)–hook | hip-hop |
| Electronic | intro–build–drop–break–build–drop–outro | EDM, house, techno |
| Ballad | V–C–V–C–B–C (last chorus lifted or pulled back) | ballads of all genres |

## 2. Hook placement
- Title in the first or last chorus line.
- First chorus in streaming pop ideally before 0:45–1:00 (see `impact.md`).
- Hook preview: hook motif instrumental or as a single line in the intro.
- Post-chorus or outro repeat the hook in reduced form (chant, syllables, "oh" line – only if it belongs to the hook, not as filler).

## 3. Energy curve
Note it in the brief as a simple line per section, scale 1–5:

```
Intro 2 · V1 2 · Pre 3 · C1 4 · V2 3 · Pre 3 · C2 4 · Bridge 2→5 · C3 5 · Outro 2
```

Rules:
- Not everything at the same energy.
- Verse 2 usually one step above verse 1 (more instruments, counter-voice).
- Before the last chorus a low point or break (bridge, breakdown, silence) – so the last chorus hits harder. Alternative: last chorus deliberately reduced (intimate ending).
- Translate the curve into performance cues (`suno.md`): e.g. `[Verse 1 – sparse, close vocal]`, `[Chorus – full band, wide]`, `[Bridge – stripped, piano only]`, `[Final Chorus – key change, gang vocals]`.

## 4. Varying repeats
- Chorus lyrics identical, but vary the arrangement (instruments, harmonies, key change, halftime).
- Optional: last chorus with one changed word that gets new meaning through the bridge.
- Verses never identical.

## 5. Intro and ending
- **Intro:** short, clear purpose (hook motif, atmosphere, vocals straight away). For generators: `[Intro]` without lyrics (Suno) or with an explicit `{instrumental intro}` cue (ElevenLabs – empty tags get sung), or with one line; avoid long intros.
- **Choose the ending deliberately:** fade-out, hard stop, return of the first line, closing punchline, a cappella chorus. In Suno set `[Outro]` and `[End]`, otherwise the song sometimes stops mid-sentence.

## 6. Timing and length
Rules of thumb: a 4-line section at 120 BPM lasts about 8 bars ≈ 16 seconds. Instrumental sections (solo, drop, break) add about 20–40 seconds each. Word budgets by duration: `craft.md`.

## 7. Concept albums and series
- From track 2 on, weave in 1–3 callbacks to earlier tracks (motif, image, character, place) – subtly, in a new context, never quoted verbatim and never explained.
- Density: early tracks 1–2, middle 2–3, late 2–4 callbacks; the last track picks up an element from track 1.
- Every track must work without the others.
- Keep motifs and callbacks in a table in the album brief (motif – introduced in – picked up in).

## 8. Derive production notes
Structure plan + energy curve directly give the section cues for generators or for human producers (`production-notes.md`).
