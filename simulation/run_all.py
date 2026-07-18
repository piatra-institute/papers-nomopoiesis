"""Orchestrator: reproduces every number and all three figures in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/{selection,gain,game}.png. Every
numeric value cited in the paper is a key in the JSON file. The computation is
deterministic: closed-form or solved to tolerance, nothing is sampled.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_selection, plot_gain, plot_game

OUT = Path(__file__).parent / "output"


def _strip_private(obj):
    if isinstance(obj, dict):
        return {k: _strip_private(v) for k, v in obj.items() if not k.startswith("_")}
    return obj


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(_strip_private(results), indent=2))
    plot_selection(results, str(OUT / "figures" / "selection.png"))
    plot_gain(results, str(OUT / "figures" / "gain.png"))
    plot_game(results, str(OUT / "figures" / "game.png"))

    sd = results["selection_decomposition"]
    pt = results["persistence_threshold"]
    ng = results["nomopoietic_gain"]
    gr = results["game_rewritten"]
    print(f"selection: direct {sd['direct_gradient']}, niche-mediated "
          f"{sd['niche_mediated_gradient']}, total {sd['total_gradient']}; "
          f"sign reversal {sd['sign_reversal']}; analytic=numeric "
          f"{sd['analytic_matches_numeric']}")
    print(f"threshold: costly constructor favoured above persistence "
          f"{pt['critical_persistence']} (net {pt['net_selection_at_sr_0.3']} at 0.3, "
          f"{pt['net_selection_at_sr_0.9']} at 0.9); closed form matches sum "
          f"{pt['closed_form_matches_truncated_sum']}")
    print(f"gain:      genuine G_N(40) = {ng['gain_genuine_k40']} (grows), "
          f"forced {ng['gain_forced_k40']} (decays {ng['forced_decays']})")
    print(f"game:      coupled cooperation mean {gr['coupled_coop_mean']}, amplitude "
          f"{gr['coupled_coop_amplitude']} (oscillation {gr['coupled_persistent_oscillation']}); "
          f"frozen games fixate at {gr['fixed_game_low_env_fixation']} (low env) and "
          f"{gr['fixed_game_high_env_fixation']} (high env)")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
