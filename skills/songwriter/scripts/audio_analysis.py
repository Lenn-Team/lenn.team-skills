#!/usr/bin/env python3
"""Barde – Songwriter: technical analysis of an audio file used as a reference.

Measures what can be measured: duration, tempo, key estimate, loudness,
energy curve, likely section boundaries, brightness.
Detects no instruments, no vocal style and no mood.

Usage:
    python3 audio_analysis.py song.mp3 [--json result.json] [--window 8]

Requires: librosa (pip install librosa), optionally pyloudnorm.
Use only with files the user lawfully owns.
"""
from __future__ import annotations

import argparse
import json
import sys

try:
    import numpy as np
    import librosa
except ImportError:  # pragma: no cover
    sys.exit("librosa missing: pip install librosa  (optional: pyloudnorm)")

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
# Krumhansl-Kessler key profiles
MAJOR = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MINOR = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])


def mmss(sec: float) -> str:
    return f"{int(sec // 60)}:{int(sec % 60):02d}"


def estimate_key(y: np.ndarray, sr: int) -> dict:
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr).mean(axis=1)
    scores = []
    for i in range(12):
        for mode, profile in (("major", MAJOR), ("minor", MINOR)):
            r = np.corrcoef(chroma, np.roll(profile, i))[0, 1]
            scores.append((r, i, mode))
    scores.sort(reverse=True)
    (r, i, mode), second = scores[0], scores[1]
    gap = r - second[0]
    confidence = "high" if gap > 0.08 else "medium" if gap > 0.03 else "low"
    return {"key": f"{NOTES[i]} {mode}", "correlation": round(float(r), 3),
            "gap_to_second": round(float(gap), 3),
            "second_choice": f"{NOTES[second[1]]} {second[2]}",
            "confidence": confidence}


def loudness(y: np.ndarray, sr: int) -> dict:
    peak = round(float(20 * np.log10(np.max(np.abs(y)) + 1e-12)), 1)
    try:
        import pyloudnorm as pyln
        return {"lufs_integrated": round(float(pyln.Meter(sr).integrated_loudness(y)), 1),
                "peak_dbfs": peak}
    except ImportError:
        rms = float(np.sqrt(np.mean(y ** 2)))
        return {"rms_dbfs": round(20 * np.log10(rms + 1e-12), 1), "peak_dbfs": peak,
                "note": "pyloudnorm not installed – RMS instead of LUFS"}


def analyse(path: str, window: float) -> dict:
    y, sr = librosa.load(path, sr=22050, mono=True)
    duration = len(y) / sr
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    tempo = float(np.atleast_1d(tempo)[0])

    rms = librosa.feature.rms(y=y)[0]
    t_rms = librosa.frames_to_time(np.arange(len(rms)), sr=sr)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

    # Energy curve in windows, scaled 1–5
    windows = []
    start = 0.0
    while start < duration:
        end = min(start + window, duration)
        mask = (t_rms >= start) & (t_rms < end)
        windows.append((start, end, float(rms[mask].mean()) if mask.any() else 0.0))
        start = end
    values = np.array([v for _, _, v in windows])
    if values.max() > values.min():
        levels = 1 + np.round(4 * (values - values.min()) / (values.max() - values.min()))
    else:
        levels = np.full_like(values, 3)
    energy = [{"from": mmss(a), "to": mmss(b), "level": int(lv)}
              for (a, b, _), lv in zip(windows, levels)]

    # Section boundaries via chroma+MFCC clustering
    features = np.vstack([librosa.feature.chroma_cqt(y=y, sr=sr),
                          librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)])
    k = int(np.clip(round(duration / 25), 3, 12))
    bounds = librosa.segment.agglomerative(features, k)
    seconds: list[float] = []
    for t in sorted(librosa.frames_to_time(bounds, sr=sr)):
        if t < 1.0:
            continue
        if seconds and t - seconds[-1] < 4.0:  # close together → merge
            continue
        seconds.append(float(t))

    first_high = next((e["from"] for e in energy if e["level"] >= 4), None)
    bright = float(np.median(centroid))
    character = ("dark/warm" if bright < 1500 else "balanced" if bright < 2800
                 else "bright/brilliant")

    return {
        "file": path,
        "duration": mmss(duration),
        "tempo_bpm": round(tempo, 1),
        "tempo_note": (f"half tempo {tempo / 2:.0f} / double tempo {tempo * 2:.0f} "
                       "possible – check by ear or source"),
        "key": estimate_key(y, sr),
        "loudness": loudness(y, sr),
        "brightness_hz": round(bright),
        "sound_character": character,
        "energy_curve": energy,
        "first_high_energy": first_high,
        "section_boundaries": [mmss(t) for t in seconds],
    }


def report(e: dict) -> str:
    k, l = e["key"], e["loudness"]
    loud = (f"{l['lufs_integrated']} LUFS" if "lufs_integrated" in l
            else f"{l['rms_dbfs']} dBFS RMS ({l['note']})")
    lines = [
        f"# Audio analysis: {e['file']}", "",
        f"- Duration: {e['duration']}",
        f"- Tempo: {e['tempo_bpm']} BPM ({e['tempo_note']})",
        f"- Key (estimate): {k['key']} – confidence {k['confidence']} "
        f"(second choice: {k['second_choice']})",
        f"- Loudness: {loud}, peak {l['peak_dbfs']} dBFS",
        f"- Sound: {e['sound_character']} (spectral centroid ~{e['brightness_hz']} Hz)",
        f"- First high energy level from: {e['first_high_energy'] or '–'}",
        f"- Likely section boundaries: {', '.join(e['section_boundaries']) or '–'}",
        "", "## Energy curve (1–5)", "",
        " · ".join(f"{x['from']} {x['level']}" for x in e["energy_curve"]),
        "", "_Estimates. No statement about instruments, vocals or mood. "
        "Don't put a low-confidence key into prompts._",
    ]
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("file")
    p.add_argument("--json", help="also save the result as JSON")
    p.add_argument("--window", type=float, default=8.0,
                   help="window length for the energy curve in seconds")
    a = p.parse_args()
    result = analyse(a.file, a.window)
    print(report(result))
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
