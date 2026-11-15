#!/usr/bin/env python3
"""Barde – Songwriter: mechanical lyric check.

Checks song lyrics (generator version with [tags] or sing-along lyrics with
blank lines) for measurable points: syllables per line (approximation), word
count, lines per section, repeated end words, cliché hits, echo between verse
and chorus, title position, character count for Suno.

Does not replace reading. Syllable counting is a heuristic.

Usage:
    python3 textcheck.py lyrics.txt [--lang de|en] [--title "Title"]
                         [--bpm 96] [--genre pop] [--duration 3:20]
Python standard library only.
"""
from __future__ import annotations

import argparse
import re
import statistics
import sys
from dataclasses import dataclass, field

# ----------------------------------------------------------------- clichés
CLICHES_EN = [
    "neon", "echo", "echoes", "shadow", "shadows", "whisper", "whispers",
    "ghost", "ghosts", "silver", "crystal", "velvet", "ember", "embers",
    "ashes", "ignite", "wildfire", "inferno", "starlight", "stardust",
    "galaxy", "cosmic", "universe", "infinity", "eternal", "endless",
    "tapestry", "symphony", "canvas", "kaleidoscope", "labyrinth",
    "shattered", "broken pieces", "fragments", "unbreakable", "unstoppable",
    "rise up", "soar", "chasing dreams", "chasing shadows", "light in the dark",
    "through the storm", "weather the storm", "tidal wave", "ocean of tears",
    "city lights", "midnight city", "electric", "heartbeat", "soul on fire",
    "heart of gold", "set me free", "break the chains", "we are one",
    "destiny", "embrace", "linger", "haunting", "vibrant", "serenade",
]
CLICHES_DE = [
    "neonlicht", "echo", "schatten der vergangenheit", "flüstern", "geister",
    "kristall", "samt", "glut", "asche", "funken", "entfachen", "feuer in mir",
    "sternenstaub", "sternenhimmel", "universum", "unendlichkeit", "ewigkeit",
    "für immer und ewig", "grenzenlos", "zerbrochen", "scherben", "splitter",
    "unzerbrechlich", "flügel", "frei wie ein vogel", "träume jagen",
    "durch die nacht", "dunkelheit", "licht am ende des tunnels",
    "sturm der gefühle", "ozean aus tränen", "herzschlag", "seele brennt",
    "herz aus gold", "gemeinsam sind wir stark", "hand in hand", "schicksal",
    "bestimmung", "sinfonie", "melodie meines lebens", "kaleidoskop",
    "labyrinth",
]
RHYME_PAIRS = [
    ("fire", "desire"), ("heart", "apart"), ("heart", "start"),
    ("night", "light"), ("love", "above"), ("pain", "rain"),
    ("soul", "whole"), ("sky", "fly"), ("forever", "together"),
    ("herz", "schmerz"), ("nacht", "macht"), ("liebe", "triebe"),
    ("glück", "zurück"), ("sonne", "wonne"), ("licht", "gesicht"),
    ("zeit", "ewigkeit"), ("leben", "geben"),
]

STOP_DE = set("""der die das den dem des ein eine einer einem einen und oder aber
ich du er sie es wir ihr mich dich sich uns euch mir dir mein dein sein ihr unser
nicht noch nur schon auch so ja doch mal wie wo was wer wenn dann als bis von
mit für auf aus bei nach zu zum zur im in am an ist bin bist sind war hab habe
hat haben wird werden kann will muss soll""".split())
STOP_EN = set("""the a an and or but i you he she it we they me him her us them
my your his its our their not no yes so just only also as if then than to of in
on at by for with from up down out over is am are was were be been have has had
do does did will would can could shall should may might must this that these
those oh yeah""".split())

# --------------------------------------------- section limits (max lines)
LIMITS = {
    # genre: (verse, chorus, bridge, pre)
    "pop": (8, 6, 4, 4), "schlager": (8, 6, 4, 4), "rock": (8, 6, 4, 4),
    "indie": (8, 6, 4, 4), "rap": (8, 8, 6, 4), "hiphop": (8, 8, 6, 4),
    "punk": (6, 4, 4, 2), "metal": (8, 6, 4, 4), "folk": (8, 6, 4, 4),
    "country": (8, 6, 4, 4), "edm": (6, 4, 4, 0), "elektronisch": (6, 4, 4, 0),
    "lofi": (4, 4, 2, 0), "rnb": (8, 6, 4, 4), "ballad": (6, 6, 4, 0),
    "ballade": (6, 6, 4, 0),
}
WORDS_BY_DURATION = [  # (up to seconds, non-rap (min,max), rap (min,max))
    (150, (120, 180), (200, 300)),
    (210, (150, 250), (250, 400)),
    (300, (220, 400), (400, 600)),
    (420, (350, 500), (550, 750)),
]
DENSITY_BPM = [(80, 4), (94, 6), (110, 6), (140, 8), (999, 4)]

TAG_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$")
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüßÀ-ÿ']+")


@dataclass
class Section:
    name: str
    kind: str
    start: int
    lines: list[tuple[int, str]] = field(default_factory=list)


def section_type(name: str) -> str:
    # Only look at the name part before a performance cue
    n = re.split(r"\s[–—-]\s|:", name.lower(), maxsplit=1)[0]
    for kind, pattern in [
        ("pre", r"\bpre[- ]?(chorus|refrain)\b|^pre\b"),
        ("post", r"\bpost[- ]?(chorus|refrain)\b"),
        ("chorus", r"\b(chorus|refrain|hook)\b"),
        ("verse", r"\b(verse|strophe|vers)\b"),
        ("bridge", r"\b(bridge|brücke)\b"),
        ("intro", r"\bintro\b"),
        ("outro", r"\b(outro|end|fade)\b"),
    ]:
        if re.search(pattern, n):
            return kind
    return "other"


def parse(text: str) -> list[Section]:
    lines = text.splitlines()
    has_tags = any(TAG_RE.match(z) for z in lines)
    sections: list[Section] = []
    current: Section | None = None
    counter = 0
    for nr, raw in enumerate(lines, 1):
        z = raw.rstrip()
        m = TAG_RE.match(z)
        if m:
            current = Section(m.group(1).strip(), section_type(m.group(1)), nr)
            sections.append(current)
            continue
        if not z.strip():
            if not has_tags:
                current = None
            continue
        if current is None:
            counter += 1
            current = Section(f"Block {counter}", "other", nr)
            sections.append(current)
        current.lines.append((nr, z.strip()))
    return sections


# ---------------------------------------------------------------- syllables
DIPHTHONGS_DE = ("äu", "eu", "ei", "ai", "au", "ie", "aa", "ee", "oo", "ey", "ay")
VOWELS_DE = "aeiouäöüy"
VOWELS_EN = "aeiouy"


def syllables_de(word: str) -> int:
    w = word.lower()
    n, i = 0, 0
    while i < len(w):
        if w[i] in VOWELS_DE:
            group = ""
            while i < len(w) and w[i] in VOWELS_DE:
                group += w[i]
                i += 1
            j = 0
            while j < len(group):
                if group[j:j + 2] in DIPHTHONGS_DE:
                    j += 2
                else:
                    j += 1
                n += 1
        else:
            i += 1
    return max(1, n)


def syllables_en(word: str) -> int:
    w = word.lower().strip("'")
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    gruppen = re.findall(r"[aeiouy]+", w)
    return max(1, len(gruppen))


def line_syllables(zeile: str, lang: str) -> int:
    ohne_klammer = re.sub(r"\([^)]*\)", " ", zeile)
    f = syllables_de if lang == "de" else syllables_en
    return sum(f(w) for w in WORD_RE.findall(ohne_klammer))


def words(zeile: str) -> list[str]:
    return [w.lower().strip("'") for w in WORD_RE.findall(zeile)]


def end_word(zeile: str) -> str:
    ohne_klammer = re.sub(r"\([^)]*\)", " ", zeile)
    w = words(ohne_klammer)
    return w[-1] if w else ""


def duration_sec(s: str) -> int:
    if ":" in s:
        m, sec = s.split(":", 1)
        return int(m) * 60 + int(sec)
    return int(s)


# -------------------------------------------------------------------- check
def check(text: str, lang: str, title: str | None, bpm: int | None,
           genre: str | None, duration: str | None) -> str:
    sections = parse(text)
    all_lines = [(nr, z, a) for a in sections for nr, z in a.lines]
    stop = STOP_DE if lang == "de" else STOP_EN
    out: list[str] = ["# Lyric check", ""]
    findings: list[str] = []

    # Basic data
    wordlist = [w for _, z, _ in all_lines for w in words(z)]
    chars = len(text)
    choruses = [a for a in sections if a.kind == "chorus"]
    out += [
        "## Overview",
        f"- Sections: {len(sections)} · Lines: {len(all_lines)} · "
        f"Words: {len(wordlist)} · Characters: {chars}",
        f"- Chorus sections: {len(choruses)}",
    ]
    if wordlist:
        ttr = len(set(wordlist)) / len(wordlist)
        out.append(f"- Word variety (distinct/all words): {ttr:.2f}")
    if chars > 5000:
        findings.append(f"Character count {chars} > 5000 (Suno lyrics limit).")
    out.append("")

    # Length vs duration
    is_rap = (genre or "").lower() in ("rap", "hiphop")
    if duration:
        sec = duration_sec(duration)
        for limit, normal, rap in WORDS_BY_DURATION:
            if sec <= limit:
                lo, hi = rap if is_rap else normal
                break
        else:
            lo, hi = (550, 750) if is_rap else (350, 500)
        out.append(f"- Target {duration} → {lo}–{hi} words")
        if len(wordlist) > hi:
            findings.append(f"Word count {len(wordlist)} above guide value {hi} for {duration}.")
        elif len(wordlist) < lo:
            findings.append(f"Word count {len(wordlist)} below guide value {lo} for {duration} "
                           "(fine for electronic genres).")

    # Sections
    out += ["## Sections", "",
            "| Section | Type | Lines | Syllables per line |", "|---|---|---|---|"]
    limits = LIMITS.get((genre or "pop").lower().replace("-", "").replace("&", ""),
                          LIMITS["pop"])
    max_bpm = None
    if bpm:
        for threshold, mx in DENSITY_BPM:
            if bpm < threshold:
                max_bpm = mx
                break
    for a in sections:
        syll = [line_syllables(z, lang) for _, z in a.lines]
        out.append(f"| {a.name} | {a.kind} | {len(a.lines)} | "
                   f"{', '.join(map(str, syll)) or '–'} |")
        idx = {"verse": 0, "chorus": 1, "bridge": 2, "pre": 3}.get(a.kind)
        if idx is not None and limits[idx] and len(a.lines) > limits[idx]:
            findings.append(f"{a.name}: {len(a.lines)} lines > genre maximum "
                           f"{limits[idx]}.")
        if a.kind == "verse" and max_bpm and len(a.lines) > max_bpm:
            findings.append(f"{a.name}: {len(a.lines)} lines at {bpm} BPM "
                           f"(guide max. {max_bpm}) – too dense?")
        sung = [(nr, z, s) for (nr, z), s in zip(a.lines, syll)
                    if not re.fullmatch(r"\(.*\)", z)]
        if len(sung) >= 3:
            med = statistics.median(s for _, _, s in sung)
            for nr, z, s in sung:
                if abs(s - med) > 3:
                    findings.append(f"L. {nr} ({a.name}): {s} syllables, section median "
                                   f"{med:g} – outlier?")
    out.append("")

    # Verses built alike? Parallel lines ±2
    verses = [a for a in sections if a.kind == "verse"]
    if len(verses) >= 2:
        lengths = {len(s.lines) for s in verses}
        if len(lengths) > 1:
            findings.append("Verses have different line counts: " +
                           ", ".join(f"{s.name}={len(s.lines)}" for s in verses))
        base = verses[0]
        for s in verses[1:]:
            for (n1, z1), (n2, z2) in zip(base.lines, s.lines):
                s1, s2 = line_syllables(z1, lang), line_syllables(z2, lang)
                if abs(s1 - s2) > 2:
                    findings.append(f"L. {n1}/{n2}: parallel verse lines with "
                                   f"{s1} vs. {s2} syllables (> ±2).")

    # End words
    for a in sections:
        if a.kind == "chorus" and choruses and a is not choruses[0]:
            continue
        ends = [(nr, end_word(z)) for nr, z in a.lines if not re.fullmatch(r"\(.*\)", z)]
        for i, (n1, e1) in enumerate(ends):
            for distance, (n2, e2) in enumerate(ends[i + 1:i + 4], 1):
                if e1 and e1 == e2:
                    what = "consecutive lines" if distance == 1 else "rhyme position (self-rhyme?)"
                    findings.append(f"L. {n1}/{n2}: same end word '{e1}' – {what}.")
                for p in RHYME_PAIRS:
                    if {e1, e2} == set(p):
                        findings.append(f"L. {n1}/{n2}: worn-out rhyme pair "
                                       f"'{e1}/{e2}'.")

    # Clichés
    cliche_list = CLICHES_DE + CLICHES_EN if lang == "de" else CLICHES_EN + CLICHES_DE
    hits = []
    for nr, z, _ in all_lines:
        zl = " " + " ".join(words(z)) + " "
        for k in cliche_list:
            if f" {k} " in zl:
                hits.append(f"L. {nr}: '{k}'")
    if hits:
        findings.append("Cliché hits (replace or justify): " +
                       "; ".join(sorted(set(hits), key=lambda t: int(t.split()[1][:-1]))))

    # Stage directions / bracket lines
    for nr, z, _ in all_lines:
        if re.fullmatch(r"\(.*\)", z):
            findings.append(f"L. {nr}: whole line in brackets – may get sung. "
                           "Use only for backing vocals.")
        if re.search(r"\b(instrumental|guitar solo|spoken word|whispered|"
                     r"a cappella|fade out|key change)\b", z,
                     re.IGNORECASE) and not z.startswith("("):
            findings.append(f"L. {nr}: possible stage direction in the lyrics: '{z}'")

    # Echo verse/pre → chorus
    for i, a in enumerate(sections):
        if a.kind not in ("verse", "pre", "bridge"):
            continue
        nxt = next((b for b in sections[i + 1:] if b.kind == "chorus"), None)
        if not nxt or sections[i + 1:].index(nxt) > 1:
            continue
        tail = {w for _, z in a.lines[-2:] for w in words(z)
                if len(w) > 3 and w not in stop}
        head = {w for _, z in nxt.lines[:2] for w in words(z)
                  if len(w) > 3 and w not in stop}
        shared = tail & head
        if shared:
            findings.append(f"Echo {a.name} → {nxt.name}: shared words "
                           f"{', '.join(sorted(shared))} – chorus anticipated?")

    # Title
    if title:
        tl = " ".join(words(title))
        occurrences = [(nr, a) for nr, z, a in all_lines
                     if tl and tl in " ".join(words(z))]
        if not occurrences:
            findings.append(f"Title '{title}' does not occur in the lyrics.")
        else:
            nr, a = occurrences[0]
            pos = [n for n, _, _ in all_lines].index(nr) + 1
            out.append(f"- Title: {len(occurrences)}× in the lyrics, first at L. {nr} "
                       f"(lyric line {pos}, section {a.name}).")
            if not any(a.kind == "chorus" for _, a in occurrences):
                findings.append("Title is not in the chorus.")
            if choruses:
                r = choruses[0]
                first, last = r.lines[0][1], r.lines[-1][1]
                if tl not in " ".join(words(first)) and tl not in " ".join(words(last)):
                    findings.append("Title not in the first or last chorus line.")

    # End tag
    if any(TAG_RE.match(z) for z in text.splitlines()):
        names = [a.name.lower() for a in sections]
        if not any(n.startswith("end") for n in names):
            findings.append("No [End] tag – song may end abruptly (Suno).")

    out += ["", "## Findings", ""]
    out += [f"- {b}" for b in findings] or ["- No mechanical issues found."]
    out += ["", "_Syllable counts are approximations. Findings are hints, not verdicts – "
            "'kept on purpose' is a valid result._"]
    return "\n".join(out)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("file")
    p.add_argument("--lang", choices=["de", "en"], default="en",
                   help="lyric language for syllable counting")
    p.add_argument("--title")
    p.add_argument("--bpm", type=int)
    p.add_argument("--genre", help="pop, schlager, rock, indie, rap, punk, metal, "
                                   "folk, country, edm, lofi, rnb, ballad")
    p.add_argument("--duration", help="target duration mm:ss")
    a = p.parse_args()
    with open(a.file, encoding="utf-8") as f:
        text = f.read()
    print(check(text, a.lang, a.title, a.bpm, a.genre, a.duration))
    return 0


if __name__ == "__main__":
    sys.exit(main())
