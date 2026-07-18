# Nomopoiesis

Dynamics That Rewrite Their Own Dynamics. The paper coins nomopoiesis (from nomos, established law or custom, and poiesis, making) for the endogenous production and revision of a system's own effective laws of motion: a system carries an ordinary state and a law parameter that its own trajectory edits, and it counts as genuinely nomopoietic only when a causal path runs from the state now, through the law, to the state later. It grants the reduction objection (the enlarged state-plus-law is formally just a bigger ordinary system) and answers it with a typed distinction between object-level and rule-level variables, ordered by a depth of parametric, structural, and generative rewriting. Niche construction is the worked instance ("ecological nomopoiesis": life writes a local law inside physics without rewriting physics), carrying a transition-operator formulation, a viability-kernel reading, the direct-versus-niche-mediated selection decomposition, and the niche-response kernel of ecological inheritance. It ships a deterministic simulation demonstrating a selection sign-reversal, a persistence threshold for costly construction, a nomopoietic gain distinguishing a state-edited law from an externally forced one, and a replicator game whose payoff matrix is rewritten by play.

## Simulation

```bash
cd simulation
uv run run_all.py        # -> output/results.json + output/figures/*.png
```

Deterministic (closed-form or solved to tolerance; nothing sampled). The models are illustrative and instantiate the paper's definitions; they are not fit to data. Every number cited in the paper is a key in `simulation/output/results.json`.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build nomopoiesis`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
