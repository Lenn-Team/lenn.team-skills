# lenn.team-skills

A collection of Claude skills by Lenn.Team. Each skill lives in its own folder under `skills/` with a `SKILL.md`, references and its own `CHANGELOG.md`. New skills are also added to `.claude-plugin/marketplace.json` and to the table below.

## Skills

| Skill | Folder | Version | Purpose |
|---|---|---|---|
| Barde – Songwriter | [`skills/songwriter/`](skills/songwriter/) | 0.1.0 | Song lyrics in any genre and language, prompts for Suno and ElevenLabs, through to a Spotify release |

## Installation
This repository is also a plugin marketplace for Claude Code (`.claude-plugin/marketplace.json`).

- **Claude Code, make all skills available:**
  ```
  /plugin marketplace add Lenn-Team/lenn.team-skills
  ```
  then install single skills, e.g. `/plugin install songwriter@lenn-team-skills`.
- **Claude Code, one skill in one step:** `/plugin install songwriter --marketplace Lenn-Team/lenn.team-skills`
- **Claude Code, by link or manually:** "Install the skill https://github.com/Lenn-Team/lenn.team-skills/tree/main/skills/<skill>", or copy the folder from `skills/` to `~/.claude/skills/<skill>/`.
- **Claude app:** download a skill folder as a ZIP and upload it under Settings → Skills.

## Versions
Each skill is versioned on its own. Tags follow `<skill>-vX.Y.Z`, e.g. `songwriter-v0.1.0`.

## License
[MIT](LICENSE) – applies to all skills in this collection. The license covers the skills themselves, not the songs or texts anyone creates with them. The name "Lenn.Team" is not covered.

## Auf Deutsch
Sammlung eigener Claude-Skills von Lenn.Team. Die Skills sind auf Englisch beschrieben, arbeiten aber in der Sprache des Nutzers – wer Deutsch schreibt, bekommt deutsche Ergebnisse. Installation wie oben beschrieben; in der Claude-App den Skill-Ordner als ZIP unter Einstellungen → Skills hochladen.
