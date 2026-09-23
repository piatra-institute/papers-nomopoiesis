# Nomopoiesis

Dynamics That Rewrite Their Own Dynamics.

Many systems in biology and society alter the rules that govern their own dynamics. A population reshapes the environment that selects it, and a market invents instruments that change what a trade is. We call this process nomopoiesis, from nomos (established law or custom) and poiesis (making), and formalize it as a state $x_t$ and a law parameter $\lambda_t$ that the trajectory edits: $x_{t+1} = F_{\lambda_t}(x_t)$ and $\lambda_{t+1} = \mathcal{N}(\lambda_t, x_t)$. A system is nomopoietic only when a causal path $x_t \to \lambda_{t+1} \to x_{t+k}$ runs through the law, which excludes laws driven by an external clock. The pair $(x,\lambda)$ can always be flattened into a larger autonomous system; the distinction is retained by typing object-level and rule-level variables and by the causal relation between them, and it matters most when construction changes the state space, the interaction topology or the action alphabet. Niche construction is the worked instance. In four deterministic models, a trait with direct selection gradient $-0.6$ has a total gradient of $+5.4$ once the environment it builds is counted; a costly constructor is favoured only above an environmental persistence of $0.68$; a one-off action under a state-edited law grows to $4.5$ times its initial effect after forty steps, while in an externally forced twin with the same law time-course it decays below $10^{-11}$; and a replicator game whose payoff matrix is written by play sustains cooperation cycles of amplitude $0.95$, whereas every frozen game fixates or, at one neutral environment, stays put. Endogenous editing of the rules of selection is a testable structural property of evolving systems.

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

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build nomopoiesis`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
