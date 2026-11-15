# Barde – Songwriter

A Claude skill for song lyrics and AI music prompts: from interview and research through song structure to lyrics in any genre and language, prompts for Suno or ElevenLabs, a clean sing-along lyric sheet and a release checklist for Spotify. The result should sound like a skilled human writer, not like a language model. Lyrics are written in the language the user writes in.

## What it does
- **Interview** in short rounds (clickable choices where available) that asks for stories and details
- **Research:** genre profiles, traits of reference songs, live trend research, facts for real-world topics
- **Music psychology** (earworms, repetition, expectation/surprise, attention in streaming) turned into writing rules
- **Song brief** with structure plan and energy curve before any lyrics
- **Lyrics** chorus first, with a checklist, anti-cliché tests and up to three revision passes
- **Production package** for Suno (styles, exclude, tagged lyrics, pronunciation, sliders) and ElevenLabs (prompt or composition plan)
- **Sing-along lyrics** without tags or phonetic spelling
- **Production notes** for bands and producers
- **Release:** rights, distributor, AI disclosure, release sheet, timeline incl. Spotify pitch
- **Scripts:** `textcheck.py` (mechanical lyric check, standard library) and `audio_analysis.py` (tempo, key, energy of a reference file, needs librosa)

## Example prompts
- "Write a song for my sister's 40th birthday – she loves sailing and always loses her keys."
- "Here are my lyrics. Check them and make me a Suno prompt for a warm indie-folk version."
- "Schreib mir einen deutschen Pop-Song über die letzte Fähre nach Hause." (German in → German lyrics out)

## Installation
- **Claude Code:** "Install the skill https://github.com/Lenn-Team/lenn.team-skills/tree/main/skills/songwriter"
  or via the marketplace: `/plugin marketplace add Lenn-Team/lenn.team-skills`, then `/plugin install songwriter@lenn-team-skills`.
- **Claude app:** download this folder as a ZIP and upload it under Settings → Skills.

## Structure
```
SKILL.md          workflow, principles, checklist, output formats
references/       interview, research, trends, impact, audio references, genres,
                  structure, craft, anti-ai, languages/, suno, elevenlabs,
                  production notes, release
templates/        song brief, production package, release sheet
scripts/          textcheck.py, audio_analysis.py
examples/         a complete original example (German)
```

## Up to date?
Platform rules, models and limits (Suno, ElevenLabs, Spotify, distributors) change quickly. Research status: November 2026. The skill tells Claude to verify anything that may have changed at runtime.

## Credits
Built on and extended from:
- `lyric-writer`, `suno-engineer` and Suno references in [bitwize-music-studio/claude-ai-music-skills](https://github.com/bitwize-music-studio/claude-ai-music-skills) (CC0)
- [kisongerstellen/deutsche-songtexte-skill](https://github.com/kisongerstellen/deutsche-songtexte-skill) (MIT)
- a skill pack with `lyric-drafter`, `song-structure-planner` and `production-notes-writer`
- own research on music psychology, Suno, ElevenLabs, Spotify and distribution (sources in the reference files)

All text was rewritten; figures and rules note their origin. Example lyrics are original.
