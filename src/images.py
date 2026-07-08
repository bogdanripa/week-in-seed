"""
images.py — turns the confirmed deals into a clean, publishable header chart.

Why a generated chart instead of scraped/stock images: it's always relevant,
never copyright-encumbered, and reinforces the data. If you want an AI-generated
hero image instead, swap `header_chart` for a call to your image model of choice
(see `ai_hero_image` stub at the bottom) — the pipeline only needs a PNG path back.
"""
from __future__ import annotations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, FG, MUTED = "#0e1116", "#e6e6e6", "#8a93a3"
PALETTE = ["#3ddc97", "#5b8def", "#5b8def", "#f6c453", "#c98bdb", "#5b8def"]


def header_chart(deals: list[dict], caption: str, out_path: str, title: str) -> str:
    """deals: [{"label": "Company (stage)", "amount_musd": float}, ...]"""
    deals = sorted(deals, key=lambda d: d["amount_musd"])[:6]
    labels = [d["label"] for d in deals]
    amounts = [float(d["amount_musd"]) for d in deals]

    fig, ax = plt.subplots(figsize=(9, 5), dpi=160)
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    bars = ax.bar(labels, amounts, color=PALETTE[:len(deals)], width=0.62, zorder=3)
    for b, amt in zip(bars, amounts):
        ax.text(b.get_x()+b.get_width()/2, b.get_height()+max(amounts)*0.015,
                f"${amt:g}M", ha="center", va="bottom", color=FG, fontsize=12, fontweight="bold")

    ax.set_title(title, color=FG, fontsize=15, fontweight="bold", pad=16, loc="left")
    ax.set_ylabel("Round size (US$M)", color=FG, fontsize=11)
    ax.tick_params(colors=FG, labelsize=10.5)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#2a2f3a")
    ax.grid(axis="y", color="#20242c", linewidth=0.8, zorder=0)
    ax.set_ylim(0, max(amounts) * 1.2)
    fig.text(0.125, 0.02, caption, color=MUTED, fontsize=8)
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(out_path, facecolor=BG, bbox_inches="tight")
    plt.close(fig)
    return out_path


def ai_hero_image(prompt: str, out_path: str) -> str:
    """Stub: plug in your preferred image model (e.g. Gemini image, DALL·E, SDXL).
    Return the local PNG path. Left unimplemented so phase 1 stays dependency-light."""
    raise NotImplementedError("Wire in an image model here if you want a hero image.")
