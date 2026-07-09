"""
images.py — generates the abstract header image for each issue.

Not a chart: layered generative art (flow-field strokes + glowing forms) seeded
by the week's concept string, so every issue gets a unique but reproducible
image. No external image API, no copyright questions — pure matplotlib/numpy.
"""
from __future__ import annotations
import hashlib

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# background, stroke colors, glow colors — curated moods
PALETTES = {
    "ember":  ("#120b0d", ["#ff6b35", "#f7b267", "#f4845f", "#912f40", "#f9dcc4"], "#ff9e57"),
    "deep":   ("#070d16", ["#1f6feb", "#58a6ff", "#79c0ff", "#1b4965", "#bee9e8"], "#3b82f6"),
    "dawn":   ("#16121f", ["#f72585", "#b5179e", "#7209b7", "#4361ee", "#4cc9f0"], "#f72585"),
    "moss":   ("#0b1210", ["#2d6a4f", "#40916c", "#74c69d", "#b7e4c7", "#d8f3dc"], "#52b788"),
    "solar":  ("#0f0e0a", ["#ffba08", "#faa307", "#f48c06", "#e85d04", "#dc2f02"], "#ffba08"),
    "mist":   ("#101318", ["#8d99ae", "#bdc6d1", "#5c677d", "#33415c", "#dee2e6"], "#a3b1c6"),
}


def abstract_header(concept: str, out_path: str, mood: str | None = None,
                    width_px: int = 1456, height_px: int = 819) -> str:
    """Render abstract generative art seeded by `concept`.

    concept: one evocative sentence distilling the week's themes — it only
    seeds the randomness (and should vary week to week); it is not drawn.
    mood: optional palette name from PALETTES; picked from the seed if omitted.
    """
    seed = int(hashlib.sha256(concept.encode()).hexdigest()[:12], 16)
    rng = np.random.default_rng(seed)
    if mood not in PALETTES:
        mood = list(PALETTES)[seed % len(PALETTES)]
    bg, colors, glow = PALETTES[mood]

    dpi = 160
    fig = plt.figure(figsize=(width_px / dpi, height_px / dpi), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    aspect = width_px / height_px
    ax.set_xlim(0, aspect)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    # soft glowing forms behind the strokes
    for _ in range(rng.integers(2, 5)):
        cx, cy = rng.uniform(0.1, aspect - 0.1), rng.uniform(0.15, 0.85)
        r = rng.uniform(0.10, 0.30)
        for rr, alpha in ((r * 2.6, 0.04), (r * 1.7, 0.07), (r, 0.14)):
            ax.add_patch(plt.Circle((cx, cy), rr, color=glow, alpha=alpha, lw=0))

    # flow field: sum of random sinusoids -> smooth angle field
    k = rng.uniform(1.2, 4.5, size=4)
    ph = rng.uniform(0, 2 * np.pi, size=4)
    swirl = rng.uniform(0.8, 1.8)

    def angles(x, y):
        return swirl * np.pi * (
            np.sin(k[0] * x + ph[0]) + np.cos(k[1] * y + ph[1])
            + 0.6 * np.sin(k[2] * (x + y) + ph[2])
            + 0.6 * np.cos(k[3] * (x - y) + ph[3])) / 2.2

    n, steps, dt = 1100, 70, 0.006
    x = rng.uniform(-0.15, aspect + 0.15, n)
    y = rng.uniform(-0.15, 1.15, n)
    traj = np.empty((steps + 1, 2, n))
    traj[0] = x, y
    for s in range(1, steps + 1):
        a = angles(x, y)
        x = x + dt * np.cos(a)
        y = y + dt * np.sin(a)
        traj[s] = x, y

    color_idx = rng.integers(0, len(colors), n)
    widths = rng.uniform(0.5, 2.4, n)
    alphas = rng.uniform(0.06, 0.30, n)
    for i in range(n):
        ax.plot(traj[:, 0, i], traj[:, 1, i], color=colors[color_idx[i]],
                lw=widths[i], alpha=alphas[i], solid_capstyle="round", zorder=2)

    # a few bright accent arcs on top
    for _ in range(rng.integers(4, 9)):
        i = rng.integers(0, n)
        ax.plot(traj[:, 0, i], traj[:, 1, i], color=colors[rng.integers(0, len(colors))],
                lw=rng.uniform(2.2, 3.6), alpha=0.55, solid_capstyle="round", zorder=3)

    # subtle vignette
    ax.add_patch(plt.Rectangle((0, 0), aspect, 1, fill=False, ec=bg, lw=60, alpha=0.35, zorder=4))

    plt.savefig(out_path, facecolor=bg, dpi=dpi)
    plt.close(fig)
    return out_path
