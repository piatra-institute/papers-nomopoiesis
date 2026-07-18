---
title: |
  Nomopoiesis:\
  Dynamics That Rewrite Their Own Dynamics
author: PIATRA . INSTITUTE
date: July 2026
---

## Abstract

An ordinary dynamical system moves a state under a rule that stands still. Many of the systems that matter most in biology and society do the other thing: they edit the rule as they run. A population reshapes the environment that selects it, a colony lays trails that redraw who can reach whom, a market invents instruments that change what a trade is. This paper names that process nomopoiesis, from nomos (established law or custom) and poiesis (making), and gives it a formal object. A nomopoietic system holds an ordinary state $x_t$ and a law parameter $\lambda_t$ that its own trajectory edits, $x_{t+1} = F_{\lambda_t}(x_t)$ and $\lambda_{t+1} = \mathcal{N}(\lambda_t, x_t)$, the first equation change under a law and the second change of the law. It counts as genuinely nomopoietic only when a nontrivial causal path $x_t \to \lambda_{t+1} \to x_{t+k}$ runs through the law, so that what the system does now sets the rules for what it can do later, which excludes systems whose law is turned by an outside clock. The obvious objection, that the pair $(x,\lambda)$ is merely a larger autonomous system, is correct in form and is answered by a typed distinction between object-level and rule-level variables together with the causal relation between them; the strong cases, where the reachable dimension, the admissible variables, the interaction topology, or the action alphabet changes, resist the flattening in content even where they permit it in form. A depth of parametric, structural, or generative rewriting orders the cases. Niche construction is the worked instance. Life rarely rewrites physis, the beaver does not amend fluid mechanics, but it routinely writes a local nomos inside physis, since the dam resets boundaries, flow, transport cost, and the selection the beaver's descendants will meet. A minimal, deterministic simulation makes four consequences concrete and checkable. The derivative of long-run fitness splits into a direct term and a niche-mediated term whose signs can oppose, so that a trait deleterious at fixed environment ($dw/d\theta = -0.6$) is favoured once the environment it builds is counted ($+5.4$), the analytic split matching a finite-difference of the constructed equilibrium. Ecological inheritance is an impulse-response kernel whose persistence sets a threshold, a costly constructor here favoured only above an environmental persistence of $0.68$. A nomopoietic gain separates a state-edited law, where a one-off action compounds to $4.5$ times its initial trajectory effect by forty steps, from an externally forced twin, where it decays to nothing. And a replicator game whose payoff matrix is written by play sustains a cooperation-defection oscillation of amplitude $0.95$ that every frozen game forbids, each fixating instead at all-defect or all-cooperate. The claim the framework defends is that evolution is not only motion across a landscape but the endogenous editing of the landscape's rules, and that this is a testable structural property rather than a metaphor.

## Systems that edit their own rules

Write an autonomous dynamical system as $z_{t+1} = F(z_t)$, a state and a fixed rule for advancing it. The rule is furniture: it sits outside the state and does not change while the state moves through it. A great deal of mathematics assumes this shape, and for good reason, since it is the shape that makes trajectories and their attractors well defined. It is also the wrong shape for a beaver.

A beaver in a valley is a state in an environment, and the pair evolves reciprocally, which the niche-construction literature has modelled for two decades as coupled organism and environment, $x_{t+1} = F(x_t, e_t)$ and $e_{t+1} = G(e_t, x_t)$ (Odling-Smee, Laland, & Feldman, 2003). This already breaks the furniture assumption once, because the environment that helps advance the organism is itself advanced by the organism. The stronger step is to notice that what the organism edits is not only an environmental variable but the rule under which its own future variables move. Let $\lambda_t$ collect the effective law of the local world: the environmental dynamics, the interaction topology, the feasible actions, the transport costs and boundaries, the payoff or fitness map, and the list of state variables that exist at all. Then the system is

$$
x_{t+1} = F_{\lambda_t}(x_t), \qquad \lambda_{t+1} = \mathcal{N}(\lambda_t, x_t).
$$

The first equation is change under a law. The second is change of the law, and $\mathcal{N}$ is the operator that performs it. Call the operator, and the process it runs, nomopoiesis. The word joins nomos, which across Greek usage spans law, rule, custom, and established order, to poiesis, making or bringing into being, and it says what the process does: it makes the rule. The adjective nomopoietic already appears occasionally in legal theory for rule-instituting procedures, and the redeployment here sharpens it to a property of dynamical systems.

The name is chosen against a specific background. Greek thought set physis, nature and its spontaneous constitution, against nomos, the conventions and laws a community lays down, and the antithesis was a live controversy among the sophists (Kerferd, 1981). A niche constructor sits exactly on the seam. It does not touch physis; the beaver's dam obeys the same hydrodynamics the undammed stream did. What the dam changes is the local nomos, the effective boundary conditions, retention times, transport costs, and species interactions under which life in that valley must now proceed. Life writes law inside nature without rewriting nature, and that is the sense in which niche construction is ecological nomopoiesis.

## What makes the editing genuine

Not every system with a time-varying rule is nomopoietic. A rule can change because an experimenter turns a dial, because a season advances, because an exogenous signal arrives; the system $x_{t+1} = F_t(x_t)$ has a rule indexed by $t$, and $t$ is set by a clock the system does not touch. The distinction that matters is causal closure of the editing loop. A system is genuinely nomopoietic when there is a nontrivial path

$$
x_t \longrightarrow \lambda_{t+1} \longrightarrow x_{t+k},
$$

so that the state's own history writes the law that the state's own future obeys. The organism must do something now that changes a future rule, and that changed rule must make a difference to what the organism does later. When the arrow from $x_t$ into $\lambda_{t+1}$ is absent, the law is externally driven and the system is a nonautonomous ordinary system wearing a costume.

This closes off three easy overclaims, and each has a counterpart guardrail in the niche-construction literature. A change in the environment that no future state reads is not construction, only a trace; the loop must return to the organism. A statistical association between what the organism did and what the environment later looked like is not construction if an unobserved common cause produced both; information is not causation, and the honest quantity is a path-specific causal effect through the environmental mediator, ideally under intervention (Lee, Flack, & Krakauer, 2022). And a change with no consequence for viability or reproduction is not evolutionarily significant construction, however large it looks, because the currency is lineage growth rather than displacement of a variable. Fitness here is the long-run invasion growth rate of a rare type in the environment a resident sets, a lineage-growth quantity rather than a utility the organism is imagined to maximise (Metz, Nisbet, & Geritz, 1992).

## Why this is not merely a larger state space

An objection arrives immediately and it is correct. The pair of update equations can be stacked,

$$
(x_{t+1}, \lambda_{t+1}) = H(x_t, \lambda_t),
$$

and $H$ is an ordinary autonomous system on the enlarged space $X \times \Lambda$. Any finite hierarchy of rule-editing embeds this way. If nomopoiesis meant only that some coordinate changed, it would be a redescription with no content, since every dynamical system has coordinates that change.

The content is in a typed distinction the flattening discards. In $H$ the coordinates $x$ and $\lambda$ are formally alike, points in a product space. In the system they model they are not alike: $x$ ranges over object-level states, configurations the rule acts on, while $\lambda$ ranges over the rule itself, the structure that decides how object-level states move. The causal relation is asymmetric and it is the phenomenon. Reading $(x,\lambda) = H(\cdot)$ as one flat system is available and it deletes the very structure, the difference between a position and the law of motion for positions, that the model exists to track. This is the same reason a program and its input are not usefully described as one undifferentiated bit-string even though a universal machine treats them as one tape.

The typing does more than label. The cases that most resist the flat reading are those where $\lambda$ edits what $x$ even is. When construction changes the reachable dimension, the admissible variables, the interaction topology, or the alphabet of available actions, the object space $X_{\lambda}$ is itself a function of the law, and a transition

$$
(x_t, \lambda_t) \longrightarrow (x_{t+1}, \lambda_{t+1}), \qquad x_t \in X_{\lambda_t},\ x_{t+1} \in X_{\lambda_{t+1}},\ X_{\lambda_t} \neq X_{\lambda_{t+1}},
$$

is a map between different spaces rather than a step within one. A fixed enlarged $X \times \Lambda$ can still contain all of this by taking $X$ large enough to hold every $X_{\lambda}$ at once, but the price is a state space specified in advance to contain possibilities the model was built to say are produced rather than presupposed. The prior term nearest to this idea, the meta-dynamical adaptive system, was introduced for exactly the case where a higher level modifies lower-level dynamics and the state-space dimension can change (Moulay & Baguelin, 2005). Nomopoiesis names the process rather than the system and insists on the causal-and-typed reading that keeps it from collapsing.

A depth follows from what is rewritten. Parametric nomopoiesis (depth one) leaves the form of $F$ fixed and moves its parameters, as when organisms shift a temperature or a resource density. Structural nomopoiesis (depth two) keeps the state space but changes the geometry, boundary conditions, constraints, or interaction graph that define $F$, as a trail changes a cost metric or a dam changes a boundary. Generative nomopoiesis (depth three) changes the state space or the action alphabet itself, as a new symbiosis, signalling channel, or technology adds a variable that did not exist. The three are progressively harder to flatten and progressively harder to formalise, and the third is where evolution stops solving problems in a fixed arena and starts changing what counts as a problem. That register, possibility expanding under selection for function rather than motion within a fixed set of functions, is the one recent work on functional information has tried to make quantitative (Wong et al., 2023).

## Niche construction is ecological nomopoiesis

The clearest worked instance is the one the machinery was built around. Cast the population as a distribution $\mu_t$ over states advancing under a transition operator, and let the operator itself be edited by the population through a heritable constructor policy $\pi_\theta$,

$$
\mu_{t+1} = \mu_t P_t, \qquad P_{t+1} = \mathcal{N}(P_t, \mu_t, \pi_\theta).
$$

The population does not only change which states are common. It changes the operator that will govern which states are common next. Selection then acts on constructor policies through their long-run invasion fitness in the environment a resident policy generates, and the adaptive-dynamics gradient of that fitness is what points evolution (Geritz, Kisdi, Meszéna, & Metz, 1998). That a constructed environment feeds back into selection, fixing otherwise-deleterious alleles and creating or removing polymorphisms, is the founding formal result of niche-construction theory (Laland, Odling-Smee, & Feldman, 1999), and the reach of a constructor's effect beyond its own body is the extended phenotype (Dawkins, 1982).

One reframing avoids a false commitment. Rather than assume organisms maximise anything, define the niche through viability. Let $z = (x,e)$ be the joint organism-environment state and let $K$ be the set of viable states. The viability kernel is the set of initial conditions from which some admissible policy keeps the trajectory in $K$ for all future time (Aubin, 1991),

$$
\operatorname{Viab}(K) = \{\, z_0 : \exists\, u(\cdot)\ \text{with}\ z_t \in K\ \text{for all}\ t \geq 0 \,\}.
$$

Construction is then the organism-induced enlargement, displacement, or stabilisation of this kernel, and its familiar descriptors become geometric: niche breadth is the kernel's size, resilience is the distance from the current state to its boundary, construction efficiency is kernel gain per unit work. No utility function is posited, and selection is free to install mechanistic policies that keep a lineage viable without any implication of foresight. When the object edited is an interaction graph rather than a scalar field, the same picture runs on adaptive networks, where node states and topology coevolve and adding or cutting an edge creates or destroys a feasible transition (Gross & Blasius, 2008).

## The niche-mediated component of selection

The heart of the formalism is a decomposition that says how much of selection runs through the constructed world. Suppose the environment a resident trait $\theta$ builds settles to an equilibrium $e^*(\theta)$ defined by $G(e^*, \theta) = 0$, and let fitness be $w(\theta, e)$. Differentiating the realised fitness $w(\theta, e^*(\theta))$ and using the implicit-function theorem on the equilibrium condition gives

$$
\frac{dw}{d\theta} = \underbrace{\frac{\partial w}{\partial \theta}}_{\text{direct}} \; \underbrace{- \frac{\partial w}{\partial e}\left(\frac{\partial G}{\partial e}\right)^{-1}\frac{\partial G}{\partial \theta}}_{\text{niche-mediated}}.
$$

The first term is what the trait does to reproduction directly. The second is what it does by moving the equilibrium environment, and it records the sign and strength of the feedback, amplified when the environment is persistent and sensitive. For fluctuating or spatial environments the inverse becomes a resolvent or adjoint-sensitivity operator, but the split survives.

Ecological inheritance is the part of this that crosses generations, and it has an impulse-response form. Let the environment propagate construction actions forward linearly, $e_{t+1} = R e_t + B a_t$, so a unit action propagates as $R^{k-1} B$ after $k$ steps, and let fitness read the environment through a sensitivity $q$. The delayed effect of an action on later fitness is the niche-response kernel

$$
\mathcal{K}_k = q^\top R^{k-1} B,
$$

which records the strength, sign, delay, and generational reach of a construction (Lehmann, 2008). A costly constructor is favoured when the discounted, recipient-weighted benefit outruns the cost,

$$
-c + \sum_{k=1}^{\infty} \beta^k\, r_k\, \mathcal{K}_k > 0,
$$

with $c$ the present cost, $\beta$ a generational discount, and $r_k$ the association between the constructor and whoever holds the altered environment $k$ generations on. The condition makes the dependence legible: future benefit counts only when the environment persists to hold it ($R$) and stays with descendants or relatives ($r_k$). Whether such a trait is a distinct evolutionary force or a special case of standard theory is a real debate, and the decomposition is neutral on it; it separates the channels so that either reading can be stated precisely.

## What the models show

Four small, deterministic models make the framework's claims concrete. Each instantiates a definition above with named values; none is fit to data, and every number is a key in the accompanying `results.json`. The point is not to discover a biological fact but to show that the definitions are consistent and to fix what the corresponding measurements would look like.

The selection decomposition can reverse a sign. In a coupled trait-environment model where the trait is directly costly but builds an environment that pays, the direct gradient is $dw/d\theta = -0.6$, so within-a-fixed-environment reasoning calls the trait deleterious and predicts it is selected away. The niche-mediated term is $+6.0$, and the total gradient is $+5.4$: once the environment the trait constructs is allowed to track the trait, the same trait is favoured. The analytic total matches a finite-difference of the numerically solved equilibrium fitness to six figures, so the reversal is a fact about the model rather than a rounding artifact. Ecological inheritance then sets a threshold (Figure 1). Sweeping the environmental persistence, the spectral radius of $R$, the net selection on a costly constructor crosses zero at a critical persistence of $0.68$: below it the environment forgets the construction faster than the benefit can return and the trait is selected against ($-0.47$ at persistence $0.3$), above it ecological inheritance brings the benefit to descendants and the trait invades ($+0.60$ at persistence $0.9$). The closed-form geometric sum $\beta r\, q^\top (I - \beta r R)^{-1} B$ agrees with an explicit four-hundred-generation lineage sum.

![The niche-mediated channel and the persistence threshold. Left: the selection gradient $dw/d\theta$ splits into a direct term ($-0.6$, the trait is costly), a niche-mediated term ($+6.0$, the constructed environment pays), and their total ($+5.4$); the analytic total equals a finite-difference of the constructed-equilibrium fitness. Within-fixed-environment reasoning gets the sign wrong. Right: net selection on a costly constructor against environmental persistence (spectral radius of $R$); it crosses zero at persistence $0.68$, so ecological inheritance must be strong enough for delayed benefit to outrun present cost.](../simulation/output/figures/selection.png){width=100%}

A nomopoietic gain separates law-editing from external forcing. Define $G_N(k)$ as the ratio of a late to an early separation between a lineage that takes a one-off construction action and a counterfactual that does not. In a system where the state edits the law, the perturbation compounds through the law and the separation grows to $4.5$ times its initial value by forty steps (Figure 2). In an externally forced twin with the identical law time-course but no path from state to law, the same action decays away, its separation falling below $10^{-11}$ over the same span. The two systems agree instant by instant on how the rule varies and disagree completely on whether a present action has a future, which is the causal-path criterion made quantitative.

![Nomopoietic gain distinguishes a state-edited law from an externally forced one. Trajectory separation from a counterfactual after a single construction action, on a log scale. In the state-editing system the action compounds and the separation grows to $G_N(40) = 4.5$ times its initial value. In the forced twin (same law time-course, external clock) it decays to zero. Only the closed causal loop lets the present reach the future.](../simulation/output/figures/gain.png){width=72%}

Play can rewrite the game it is played in. Take replicator dynamics for a cooperation frequency on a payoff matrix that the environment interpolates between a defection-dominant dilemma and a cooperation-favouring game, and let the play write the environment. At any frozen environment the game is an ordinary one and fixates, to all-defect when the environment is poor and to all-cooperate when it is rich. With the feedback closed, the coupled system neither fixates nor rests: cooperation and environment cycle with an amplitude of $0.95$ around a mean cooperation of $0.50$ (Figure 3), a sustained oscillation of the kind first shown for game-environment feedback (Weitz, Eksin, Paarporn, Brown, & Ratcliff, 2016) and sharpened by models in which the current play and the current game jointly select the next game (Su, McAvoy, Wang, & Nowak, 2019). The population does not settle on a strategy inside a fixed game. It keeps changing which game exists.

![Play rewrites the payoff matrix. Cooperation frequency $p$ and environment $n$ under replicator dynamics whose payoff matrix the environment interpolates, with the environment driven by the play. Every frozen game fixates at a corner (dashed lines at $0$ and $1$); the coupled system sustains an oscillation of amplitude $0.95$ that no frozen game admits. The rule and the state co-move.](../simulation/output/figures/game.png){width=90%}

## What construction costs, and how it composes

Three further pieces keep the account honest about what construction costs, how it composes, and when it matters at scale. Construction takes work because a constructed state relaxes back toward the environment's passive dynamics unless it is held. If $P_0$ is the passive path distribution and $P_\pi$ the distribution under a construction policy, a stochastic-control reading prices the policy by a path-space divergence, $\mathcal{C}(\pi) \propto D_{\mathrm{KL}}(P_\pi \,\|\, P_0)$, the cost of forcing trajectories away from where they would drift on their own (Todorov, 2009). A variational free-energy account of the same organism-environment loop has been developed through active inference, useful for perception-action coupling and best treated as one available formulation rather than a foundation for all of construction (Constant, Ramstead, Veissière, Campbell, & Friston, 2018).

Because organisms are open systems that exchange matter, energy, and information rather than closed dynamical systems, the framework needs a way to nest constructors without treating a cell, a tissue, an organism, and an ecosystem as one monolith. The compositional tools of open games supply it: a constructor is a lens, a forward map that acts on the environment paired with a backward map that returns altered constraints and selection pressures, and lenses compose along shared interfaces in a symmetric monoidal category (Ghani, Hedges, Winschel, & Zahn, 2018). Composition guarantees that a model built for one scale glues to a model at the next without predicting the biology by itself.

At scale, most construction is a haze of small local actions, and the question is which of them survive coarse-graining to become macroscopic niche variables, trails, fields, conventions, regimes. This is a renormalization question: under coarse-graining the organism-environment couplings transform, and a given constructor effect is irrelevant if it washes out, marginal if it persists without amplification, or relevant if it grows to dominate the large-scale description (Wilson, 1975). A niche, in this reading, is an organism-produced causal memory that survives coarse-graining, and a small set of dimensionless quantities coordinates the regimes: the persistence ratio $\Pi = \tau_E/\tau_G$ of environmental memory to generation time, the feedback gain $\Gamma$ of the closed loop, and the capture $Q$ of delayed benefit that returns to the constructor's lineage. Large $\Pi$ with small $Q$ is public infrastructure open to exploitation; large $\Pi$ with large $Q$ is an inherited niche; high positive $\Gamma$ is runaway feedback or a tipping point; high negative $\Gamma$ is homeostatic regulation. The persistence threshold computed above is the $\Pi$ axis of this diagram crossing the line where a costly constructor pays.

Two terminological neighbours are worth holding apart. Nomopoiesis is not autopoiesis: an autopoietic system produces its own components and thereby its own boundary (Maturana & Varela, 1980), while a nomopoietic system produces its own laws, and a system can do either without the other. And it is not the metadynamics of molecular simulation, an enhanced-sampling method for escaping free-energy minima that happens to share a stem (Laio & Parrinello, 2002); the collision is lexical, and the name here is built from nomos to point at law rather than at motion.

What the framework buys is a shift in the object of study. Evolution read as motion across a fixed landscape asks which point a lineage reaches. Evolution read as nomopoiesis asks how the lineage rewrites the landscape's metric, boundaries, transition rules, and alphabet of possibilities, and then which of those rewrites persist and return. The simulations show the shift has consequences one can check: a selection gradient that reverses sign when the constructed environment is counted, a persistence threshold that decides whether a costly constructor pays, a gain that separates a law a system edits from a law a clock turns, an oscillation that only the coupled game admits. Life does not usually rewrite the laws of physics. It writes, and keeps rewriting, the local laws under which it must next act.

## References

Aubin, J.-P. (1991). *Viability Theory*. Boston: Birkhäuser.

Constant, A., Ramstead, M. J. D., Veissière, S. P. L., Campbell, J. O., & Friston, K. J. (2018). A variational approach to niche construction. *Journal of the Royal Society Interface*, 15(141), 20170685.

Dawkins, R. (1982). *The Extended Phenotype: The Gene as the Unit of Selection*. Oxford: W. H. Freeman.

Geritz, S. A. H., Kisdi, É., Meszéna, G., & Metz, J. A. J. (1998). Evolutionarily singular strategies and the adaptive growth and branching of the evolutionary tree. *Evolutionary Ecology*, 12(1), 35--57.

Ghani, N., Hedges, J., Winschel, V., & Zahn, P. (2018). Compositional game theory. In *Proceedings of the 33rd Annual ACM/IEEE Symposium on Logic in Computer Science*, 472--481.

Gross, T., & Blasius, B. (2008). Adaptive coevolutionary networks: a review. *Journal of the Royal Society Interface*, 5(20), 259--271.

Kerferd, G. B. (1981). *The Sophistic Movement*. Cambridge: Cambridge University Press.

Laio, A., & Parrinello, M. (2002). Escaping free-energy minima. *Proceedings of the National Academy of Sciences*, 99(20), 12562--12566.

Laland, K. N., Odling-Smee, F. J., & Feldman, M. W. (1999). Evolutionary consequences of niche construction and their implications for ecology. *Proceedings of the National Academy of Sciences*, 96(18), 10242--10247.

Lee, E. D., Flack, J. C., & Krakauer, D. C. (2022). Outsourcing memory through niche construction. *arXiv preprint* arXiv:2209.00476.

Lehmann, L. (2008). The adaptive dynamics of niche constructing traits in spatially subdivided populations: evolving posthumous extended phenotypes. *Evolution*, 62(3), 549--566.

Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. Dordrecht: D. Reidel.

Metz, J. A. J., Nisbet, R. M., & Geritz, S. A. H. (1992). How should we define "fitness" for general ecological scenarios? *Trends in Ecology & Evolution*, 7(6), 198--202.

Moulay, E., & Baguelin, M. (2005). Meta-dynamical adaptive systems and their applications to a fractal algorithm and a biological model. *Physica D: Nonlinear Phenomena*, 207(1--2), 79--90.

Odling-Smee, F. J., Laland, K. N., & Feldman, M. W. (2003). *Niche Construction: The Neglected Process in Evolution*. Princeton, NJ: Princeton University Press.

Su, Q., McAvoy, A., Wang, L., & Nowak, M. A. (2019). Evolutionary dynamics with game transitions. *Proceedings of the National Academy of Sciences*, 116(51), 25398--25404.

Todorov, E. (2009). Efficient computation of optimal actions. *Proceedings of the National Academy of Sciences*, 106(28), 11478--11483.

Weitz, J. S., Eksin, C., Paarporn, K., Brown, S. P., & Ratcliff, W. C. (2016). An oscillating tragedy of the commons in replicator dynamics with game-environment feedback. *Proceedings of the National Academy of Sciences*, 113(47), E7518--E7525.

Wilson, K. G. (1975). The renormalization group: critical phenomena and the Kondo problem. *Reviews of Modern Physics*, 47(4), 773--840.

Wong, M. L., Cleland, C. E., Arend, D., Bartlett, S., Cleaves, H. J., Demarest, H., Prabhu, A., Lunine, J. I., & Hazen, R. M. (2023). On the roles of function and selection in evolving systems. *Proceedings of the National Academy of Sciences*, 120(43), e2310223120.
