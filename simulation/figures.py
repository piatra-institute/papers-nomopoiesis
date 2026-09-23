"""Figures for *Nomopoiesis*. Each reads the results dict from ``analyses.run()``
and writes one PNG. No data are recomputed here."""
from __future__ import annotations

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#1a1a1a"
DIRECT = "#b3202c"     # direct / within-fixed-environment
NICHE = "#1f4e79"      # niche-mediated / constructed
NEUTRAL = "#6a6a6a"
GRID = "#d9d9d9"


def _style(ax) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9)
    ax.grid(True, color=GRID, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)


def plot_selection(results: dict, path: str) -> None:
    sd = results["selection_decomposition"]
    pt = results["persistence_threshold"]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 3.8))

    labels = ["direct", "niche-mediated", "total"]
    vals = [sd["_direct"], sd["_niche"], sd["_total"]]
    colors = [DIRECT, NICHE, INK]
    a1.axhline(0, color=NEUTRAL, lw=0.9)
    a1.bar(labels, vals, color=colors, width=0.6)
    a1.set_ylabel(r"selection gradient $dw/d\theta$")
    a1.set_title("components of the selection gradient", fontsize=10, color=INK)
    a1.annotate("analytic = finite-difference", xy=(0.5, 0.06),
                xycoords="axes fraction", ha="center", fontsize=8.5, color=NEUTRAL)

    sr = np.array(pt["_persistences"])
    net = np.array(pt["_net"])
    a2.axhline(0, color=NEUTRAL, lw=0.9)
    a2.plot(sr, net, color=NICHE, lw=1.8)
    crit = pt["critical_persistence_exact"]
    a2.axvline(crit, color=DIRECT, lw=1.2, ls="--")
    a2.annotate(rf"critical persistence $\approx {crit:.2f}$",
                xy=(crit, net.max() * 0.55), xytext=(crit - 0.02, net.max() * 0.6),
                ha="right", fontsize=9, color=DIRECT)
    a2.set_xlabel(r"environmental persistence (spectral radius of $R$)")
    a2.set_ylabel("net selection on costly constructor")
    a2.set_title("net selection against environmental persistence", fontsize=10, color=INK)
    for ax in (a1, a2):
        _style(ax)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_gain(results: dict, path: str) -> None:
    ng = results["nomopoietic_gain"]
    sg = np.array(ng["_sep_genuine"])
    sf = np.array(ng["_sep_forced"])
    k = np.arange(len(sg))
    fig, ax = plt.subplots(figsize=(6.2, 3.9))
    # the separation is zero at k = 0, before the action acts, so the log plot
    # starts at k = 1
    ax.plot(k[1:], sg[1:], color=NICHE, lw=1.9, label="genuine (state edits the law)")
    ax.plot(k[1:], sf[1:], color=DIRECT, lw=1.9, ls="--", label="forced (external clock)")
    ax.set_yscale("log")
    ax.set_xlabel("time steps after a one-off construction action")
    ax.set_ylabel("trajectory separation from counterfactual")
    ax.set_title("separation after a one-off action: state-edited vs forced law",
                 fontsize=10, color=INK)
    ax.annotate(rf"$G_N(40)={ng['gain_genuine_k40']:.1f}$ (state-edited law)",
                xy=(0.97, 0.80), xycoords="axes fraction", ha="right",
                fontsize=9, color=INK)
    ax.legend(frameon=False, fontsize=9, loc="lower left")
    _style(ax)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_game(results: dict, path: str) -> None:
    gr = results["game_rewritten"]
    p = np.array(gr["_p"])
    n = np.array(gr["_n"])
    t = np.arange(len(p))
    fig, ax = plt.subplots(figsize=(6.8, 3.9))
    ax.plot(t, p, color=NICHE, lw=1.6, label="cooperation frequency $p$")
    ax.plot(t, n, color=NEUTRAL, lw=1.3, ls=":", label="environment $n$")
    ax.axhline(gr["fixed_game_high_env_fixation"], color=DIRECT, lw=1.1, ls="--")
    ax.axhline(gr["fixed_game_low_env_fixation"], color=DIRECT, lw=1.1, ls="--",
               label="fixation points of frozen games")
    ax.set_xlabel("time (coarse steps)")
    ax.set_ylabel("frequency / state")
    ax.set_ylim(-0.05, 1.3)
    ax.set_title("cooperation and environment in the coupled replicator game",
                 fontsize=10, color=INK)
    ax.legend(frameon=False, fontsize=8.5, loc="upper center", ncol=3)
    _style(ax)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
