# Brief

Written before research begins. See the workspace docs (run `papers docs`):
research-pipeline.md §1.

## Question

Ordinary dynamical systems move a state under a fixed rule. Many of the systems that matter, organisms and their environments, institutions and their members, markets and their instruments, instead edit the rule as they run. Is there a precise, general notion of a system that produces and revises its own effective laws of motion, and does that notion survive the obvious objection that any such system is just a larger fixed dynamical system in disguise?

## Claim

Name the process nomopoiesis, from nomos (law, custom, established order) and poiesis (making). A nomopoietic system carries an ordinary state $x_t$ and a law parameter $\lambda_t$ that its own trajectory edits: $x_{t+1} = F_{\lambda_t}(x_t)$ and $\lambda_{t+1} = \mathcal N(\lambda_t, x_t)$. It is genuinely nomopoietic only when there is a nontrivial causal path $x_t \to \lambda_{t+1} \to x_{t+k}$, so that what the system does now changes the rules governing what it can do later; this excludes systems whose law is driven by an external clock. The reduction objection, that $(x, \lambda)$ is just a bigger autonomous system $H$, is granted and then answered: nomopoiesis is a typed distinction between object-level and rule-level variables together with the causal relation between them, and the strong cases (changes of dimension, admissible variables, interaction topology, action alphabet) resist the flattening in content even where they admit it in form. A three-level depth, parametric, structural, generative, orders the cases. Niche construction is the worked instance: life rarely rewrites physis (the beaver does not change fluid mechanics) but routinely writes a new local nomos inside it (the dam changes boundaries, flow, transport costs, and the selection its lineage later meets), so niche construction is ecological nomopoiesis. A small simulation makes four consequences concrete: the derivative of long-run fitness splits into a direct and a niche-mediated term that can carry opposite signs; ecological inheritance is an impulse-response kernel whose persistence sets a threshold above which a costly constructor is favoured; a nomopoietic gain distinguishes a state-edited law (a present action compounds into the future) from an externally forced one (it decays); and a replicator game whose payoff matrix is written by play sustains oscillation that every frozen game forbids.

## Kind

formal-model (ships a simulation). `has_simulation: true`, `claims_target: results.json`. The simulation is illustrative and instantiates the definitions; every number it produces is a key in `results.json`. The literature results and the formal apparatus are cited or defined, not simulation output.

## Cornerstone literature

- Niche construction: Odling-Smee, Laland & Feldman (2003); Laland, Odling-Smee & Feldman (1999); Lehmann (2008, niche-mediated selection, posthumous extended phenotype); Dawkins (1982, extended phenotype).
- Adaptive dynamics and fitness: Metz, Nisbet & Geritz (1992); Geritz, Kisdi, Meszéna & Metz (1998).
- Game-environment feedback and endogenous games: Weitz, Eksin, Paarporn, Brown & Ratcliff (2016); Su, McAvoy, Wang & Nowak (2019, game transitions).
- Viability theory: Aubin (1991).
- Adaptive networks: Gross & Blasius (2008). Compositional / open systems: Ghani, Hedges, Winschel & Zahn (2018, open games).
- Niche as memory: Lee, Flack & Krakauer (2022). Active inference lens: Constant, Ramstead, Veissière, Campbell & Friston (2018).
- Control cost as KL from passive dynamics: Todorov (2009). Renormalization / coarse-graining: Wilson (1975).
- Prior terminology to distinguish: Moulay & Baguelin (2005, meta-dynamical adaptive systems); Laio & Parrinello (2002, metadynamics, a name collision to avoid); Maturana & Varela (1980, autopoiesis).
- Open-endedness / possibility-space expansion: Wong et al. (2023). Greek physis-nomos antithesis: Kerferd (1981).
