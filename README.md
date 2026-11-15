# lenn.team-skills

Sammlung eigener Claude-Skills von Lenn.Team. Jeder Skill liegt in einem eigenen Ordner unter `skills/` mit `SKILL.md`, Referenzen und eigenem `CHANGELOG.md`. Neue Skills zusätzlich in `.claude-plugin/marketplace.json` und in der Tabelle unten eintragen.

## Skills

| Skill | Ordner | Version | Zweck |
|---|---|---|---|
| Barde – Songwriter | [`skills/songwriter/`](skills/songwriter/) | 0.1.0 | Songtexte in allen Genres und Sprachen, Prompts für Suno und ElevenLabs, bis zur Veröffentlichung auf Spotify |

## Installation
Das Repo ist zugleich ein Plugin-Marktplatz für Claude Code (`.claude-plugin/marketplace.json`).

- **Claude Code, alle Skills verfügbar machen:**
  ```
  /plugin marketplace add Lenn-Team/lenn.team-skills
  ```
  danach einzelne Skills installieren, z. B. `/plugin install songwriter@lenn-team-skills`.
- **Claude Code, ein Skill in einem Schritt:** `/plugin install songwriter --marketplace Lenn-Team/lenn.team-skills`
- **Claude Code, manuell:** gewünschten Ordner aus `skills/` nach `~/.claude/skills/<skill>/` kopieren, oder: „Install the skill https://github.com/Lenn-Team/lenn.team-skills/tree/main/skills/<skill>“.
- **Claude (App/Web):** Skill-Ordner einzeln als ZIP packen und unter *Anpassen → Skills → Skill hochladen* einfügen.

## Lizenz
[MIT](LICENSE) – gilt für alle Skills dieser Sammlung. Die Lizenz betrifft den Skill selbst, nicht die Songs oder Texte, die jemand damit erstellt. Der Name „Lenn.Team“ ist davon nicht erfasst.
