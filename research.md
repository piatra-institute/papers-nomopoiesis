# Research

Findings, tiered by source proximity. See the workspace docs (`papers docs`): research-pipeline.md §2.
T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only).
A claim that reaches the paper rests on a T1 or T2 source. All locators web-verified against the publisher record on 2026-07-18 (provenance in `sources.md`, corrections in `audit.md`).

## Findings

### Niche construction and ecological inheritance (the worked instance)

- [T1] Laland, Odling-Smee & Feldman (1999), PNAS 96(18):10242-10247. A two-locus model in which niche construction generates selection: an allele that modifies the environment can fix otherwise-deleterious alleles, create or remove polymorphisms, and leave an "ecological inheritance." Supports: reciprocal organism-environment causation; the niche-mediated component of selection.
- [T2] Odling-Smee, Laland & Feldman (2003), *Niche Construction: The Neglected Process in Evolution*, Princeton (MPB-37). The book-length statement; ecological inheritance as a second inheritance system. Supports: the framing that organisms modify the selective environments of descendants.
- [T1] Lehmann (2008), *Evolution* 62(3):549-566. Inclusive-fitness adaptive dynamics of niche-constructing traits in structured populations; present benefits traded against delayed indirect effects on relatives and descendants ("posthumous extended phenotype"). Supports: the niche-response kernel, the association/relatedness factor r_k, the persistence-and-recipient logic of the selection condition.
- [T3] Dawkins (1982), *The Extended Phenotype*, W. H. Freeman. Gene effects reach beyond the organism's body. Supports: the extended-phenotype reading of a written environment.

### Fitness and adaptive dynamics (the guardrail on "fitness is not utility")

- [T1] Metz, Nisbet & Geritz (1992), TREE 7(6):198-202. Fitness for general ecological scenarios is the long-run invasion growth rate of a rare type in a set resident environment. Supports: invasion fitness s(theta',theta); the guardrail that fitness is lineage growth, not subjective utility.
- [T1] Geritz, Kisdi, Meszéna & Metz (1998), *Evol. Ecol.* 12(1):35-57. Evolutionarily singular strategies; the selection gradient as the derivative of invasion fitness. Supports: the adaptive-dynamics approximation dot-theta ∝ gradient of s.

### Games whose rules are changed by play

- [T1] Weitz, Eksin, Paarporn, Brown & Ratcliff (2016), PNAS 113(47):E7518-E7525. Replicator dynamics with game-environment feedback: an environmental state driven by play feeds back into the payoffs, producing an "oscillating tragedy of the commons," a persistent cycle absent from either the fixed game or the isolated environment. Supports: simulation demonstration 4 (the coupled game oscillates while every frozen game fixates).
- [T1] Su, McAvoy, Wang & Nowak (2019), PNAS 116(51):25398-25404. "Evolutionary dynamics with game transitions": the current behaviors and the current game jointly determine which game is played next. Supports: the strong nomopoietic reading A_{t+1} = N_A(A_t, p_t, e_t), the population changing which game exists.

### Viability, networks, composition, memory, cost, coarse-graining

- [T2] Aubin (1991), *Viability Theory*, Birkhäuser. The viability kernel: initial states from which an admissible control keeps the system inside a constraint set indefinitely. Supports: the niche as a controlled viability kernel; construction as enlargement/displacement/stabilization of that kernel.
- [T2] Gross & Blasius (2008), *J. R. Soc. Interface* 5(20):259-271. Adaptive coevolutionary networks: node states and topology coevolve. Supports: structural nomopoiesis on interaction graphs; the affordance-graph extension.
- [T2] Ghani, Hedges, Winschel & Zahn (2018), LICS 2018 (arXiv:1603.04641). Compositional game theory: open games as morphisms with forward play and backward coutility, composing in a symmetric monoidal category (lenses). Supports: the compositional/lens architecture for nesting constructors across scales.
- [T2] Lee, Flack & Krakauer (2022), arXiv:2209.00476. Niche construction as outsourcing memory into persistent, actively-modified environmental states; an optimal memory-duration scaling. Supports: the niche as writable external memory (read/write), and the causal-path requirement A_t → E_{t+1:t+k} → W_{t+k}.
- [T2] Constant, Ramstead, Veissière, Campbell & Friston (2018), *J. R. Soc. Interface* 15(141):20170685. A variational (active-inference) account of niche construction. Supports: the free-energy lens, presented as one formulation rather than a foundation.
- [T2] Todorov (2009), PNAS 106(28):11478-11483. Linearly-solvable MDPs: optimal control cost is a KL divergence between controlled and passive path distributions. Supports: the thermodynamic construction cost C(pi) ∝ D_KL(P_pi ‖ P_0).
- [T3] Wilson (1975), *Rev. Mod. Phys.* 47(4):773-840. The renormalization group. Supports: the coarse-graining program, which constructor couplings remain relevant at larger scales.

### Terminology (what nomopoiesis is and is not)

- [T2] Moulay & Baguelin (2005), *Physica D* 207(1-2):79-90. "Meta-dynamical adaptive system": higher-level rules modify lower-level dynamics, including state-space dimension changes. Supports: the nearest existing prior term; nomopoiesis sharpens it to endogenous law production.
- [T3] Laio & Parrinello (2002), PNAS 99(20):12562-12566. "Metadynamics" for escaping free-energy minima in molecular simulation. Cited only to flag the name collision (avoid "metadynamics").
- [T3] Maturana & Varela (1980), *Autopoiesis and Cognition*, Reidel. Autopoiesis: a system that produces its own components. Cited to distinguish nomopoiesis (production of laws) from autopoiesis (production of parts).
- [T3] Wong et al. (2023), PNAS 120(43):e2310223120. A proposed law of increasing functional information; combinatorial possibility expands under selection for function. Supports: generative nomopoiesis / open-ended possibility-space expansion (phrased as functional-information expansion, per the source).
- [T3] Kerferd (1981), *The Sophistic Movement*, Cambridge. The physis-nomos (nature vs convention/law) controversy in Greek thought. Supports: the physis/nomos framing (life writes a local nomos inside physis).

### Simulation (this paper's own computation; not literature)

- Selection decomposition: with rho 0.8, direct gradient -0.6, niche-mediated +6.0, total +5.4; sign reversal; analytic total gradient equals the finite-difference of realized equilibrium fitness. Keys in `simulation/output/results.json`.
- Persistence threshold: costly constructor (cost 1.4, discount 0.9, association 0.8) favoured above environmental spectral radius 0.677; closed-form geometric sum matches the truncated lineage sum.
- Nomopoietic gain: genuine (state-edited law) G_N(40) = 4.53 (grows); externally forced twin decays to ~0 (G_N(40) ~ 1e-12).
- Game rewritten: coupled cooperation oscillates (amplitude 0.95, mean 0.50); every frozen game fixates (0 at low environment, 1 at high).
