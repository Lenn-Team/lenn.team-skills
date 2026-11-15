# lenn.team-skills

A collection of Claude skills by Lenn.Team. Each skill lives in its own folder under `skills/` with a `SKILL.md`, references and its own `CHANGELOG.md`. New skills are also added to `.claude-plugin/marketplace.json` and to the table below.

## Skills

| Skill | Folder | Version | Purpose |
|---|---|---|---|
| Barde – Songwriter | [`skills/songwriter/`](skills/songwriter/) | 0.1.0 | Song lyrics in any genre and language, prompts for Suno and ElevenLabs, through to a Spotify release |

## Installation
Replace `<skill>` with the folder name of a skill from the table above (for example `songwriter`). This repository is our own plugin marketplace for Claude Code (`.claude-plugin/marketplace.json`, name `lenn-team-skills`); it is not part of Anthropic's official directory.

### Claude Code (terminal, desktop, Remote Control)

**Recommended – add the marketplace once, then install and update skills from it:**
```
/plugin marketplace add Lenn-Team/lenn.team-skills
/plugin install <skill>@lenn-team-skills
```
After that, `/plugin` lists all skills of this collection under `lenn-team-skills`, including new skills and new versions. Update with `/plugin marketplace update lenn-team-skills`.

**Quick – one skill by link:** tell Claude
> Install the skill https://github.com/Lenn-Team/lenn.team-skills/tree/main/skills/<skill>

**Manual:** copy the folder `skills/<skill>/` to `~/.claude/skills/<skill>/` (only for you) or to `.claude/skills/<skill>/` in a project (for everyone working on it).

### Claude app (claude.ai on web, desktop, mobile)
The app cannot install from a GitHub link. Upload the skill as a ZIP instead:
1. Download the repository (green **Code** button → **Download ZIP**) and unpack it.
2. Zip the single folder `skills/<skill>/` (the ZIP must contain the folder with `SKILL.md` inside).
3. In Claude: **Settings → Capabilities → Skills → Upload skill**, choose the ZIP and switch the skill on.
For a new version, upload the new ZIP again.

## Versions
Each skill is versioned on its own. Tags follow `<skill>-vX.Y.Z`, e.g. `songwriter-v0.1.0`.

## License
[MIT](LICENSE) – applies to all skills in this collection. The license covers the skills themselves, not the songs or texts anyone creates with them. The name "Lenn.Team" is not covered.

## Auf Deutsch
Sammlung eigener Claude-Skills von Lenn.Team. Die Skills sind auf Englisch beschrieben, arbeiten aber in der Sprache des Nutzers – wer Deutsch schreibt, bekommt deutsche Ergebnisse. `<skill>` steht für den Ordnernamen aus der Tabelle, etwa `songwriter`.

- **Claude Code, empfohlen:** einmal `/plugin marketplace add Lenn-Team/lenn.team-skills`, dann `/plugin install <skill>@lenn-team-skills`. Unter `/plugin` stehen danach alle Skills der Sammlung, auch neue und neue Fassungen; aktualisieren mit `/plugin marketplace update lenn-team-skills`.
- **Claude Code, schnell:** Claude den Link geben: „Installiere den Skill https://github.com/Lenn-Team/lenn.team-skills/tree/main/skills/<skill>“.
- **Claude-App:** Repository als ZIP laden (**Code → Download ZIP**), den Ordner `skills/<skill>/` einzeln zippen und unter **Einstellungen → Fähigkeiten → Skills → Skill hochladen** auswählen; bei einer neuen Fassung erneut hochladen.

Der Marktplatz ist unser eigener, nicht das offizielle Verzeichnis von Anthropic.
