# Example: "Noch einmal drücken" (German)

An original example showing the path from brief to production package. The user wrote in German, so the lyrics are German (see "Language" in `SKILL.md`). The generator version is in `generator-version.txt` next to this file.

"Noch einmal drücken" means "press it once more" – the timer light switch in a stairwell that goes out after 30 seconds.

## Brief (excerpt)
- **Core message:** if you don't want to say goodbye, you buy time in 30-second pieces – until you don't need it any more.
- **Emotional turn:** hesitant goodbye in the stairwell → a year later both live there.
- **Point of view:** I to you, present tense.
- **Specific material:** stairwell timer light, orange-glowing switch, humming lamp, neighbour Mrs Kowalski with her dog, name plate stuck on with tape.
- **Hook:** "Noch einmal drücken" – peculiarity: an everyday action as a gesture of love.
- **Music:** modern German pop with indie-folk touches, 92 BPM, muted electric guitar, piano, soft drums, strings only in the last chorus; warm baritone, conversational.
- **Structure/energy:** Intro 1 · V1 2 · Pre 3 · C 4 · V2 3 · Pre 3 · C 4 · Bridge 2 · C 5 · Outro 1
- **Impact:** vocals after approx. 6 s, title in chorus line 1 (approx. 0:35), clip = chorus; surprise = the last chorus line changes ("und ich hab mich getraut" – "and I dared").
- **Trend stance:** timeless.

## Production package (Suno)

**Title**
```
Noch einmal drücken
```

**Styles**
```
Warm male baritone, conversational and close, German lyrics, modern German pop with indie-folk touches, 92 BPM, muted electric guitar, upright piano, soft kick and shaker, round warm bass, subtle strings only in final chorus, dry intimate mix
```

**Exclude Styles**
```
choir, autotune, EDM drop
```

**Settings:** v6 · Weirdness 45 · Style Influence 60 · Variety off · Max Mode on

**Pronunciation table**

| Word | Generator spelling | Reason |
|---|---|---|
| Kowalski | Ko-wall-ski | secure stress on the 2nd syllable |

## Sing-along lyrics

```
Noch einmal drücken

Dritter Stock, du stehst schon in der Jacke,
der Schlüsselbund klimpert in deiner Hand.
Unten bellt der Hund von Frau Kowalski,
wir reden leise, Schulter an der Wand.

Dann macht es klick, und es wird dunkel,
dreißig Sekunden sind zu kurz.

Noch einmal drücken,
der Knopf glüht orange im Flur,
noch ein Satz, ein halber Kuss,
dann läuft wieder die Uhr.
Noch einmal drücken,
die alte Lampe summt so laut,
du stehst schon auf der ersten Stufe,
und keiner, der sich traut.

Ein Jahr später, Kisten bis zur Decke,
dein Name klebt mit Tesa an der Tür.
Frau Kowalski sagt, sie hat's gewusst,
und ihr Hund bellt, als könnt er was dafür.

Dann macht es klick, und es wird dunkel,
und keiner von uns muss mehr los.

Noch einmal drücken,
der Knopf glüht orange im Flur,
noch ein Satz, ein halber Kuss,
dann läuft wieder die Uhr.
Noch einmal drücken,
die alte Lampe summt so laut,
du stehst schon auf der ersten Stufe,
und keiner, der sich traut.

Wir haben mehr Zeit als Treppenstufen,
der Schalter wär egal.
Doch bringst du nachts den Müll runter,
drück ich oben. Jedes Mal.

Noch einmal drücken,
der Knopf glüht orange im Flur,
noch ein Satz, ein halber Kuss,
dann läuft wieder die Uhr.
Noch einmal drücken,
die alte Lampe summt so laut,
du stehst schon auf der ersten Stufe,
und ich hab mich getraut.

Noch einmal drücken.
```

## Check result (excerpt)
- `textcheck.py --lang de`: 238 words (target 3:15 → 150–250), verses built in parallel (10 syllables), no cliché hits, no echo between pre-chorus and chorus.
- Finding "chorus 8 lines > genre maximum 6": **kept on purpose** – the chorus is 2 × 4 lines with the hook repeated at the start of each half; at 92 BPM there is enough room.
- Rhyme pair "laut/traut" (perfect rhyme) chosen over "Takt/gesagt" (near rhyme, different vowel length).
- "Uhr/Flur" and "Tür/dafür": perfect rhymes; "Hand/Wand": perfect rhyme; bridge "egal/Mal": perfect rhyme on a long a.
- Musical fit open (no melody available).
