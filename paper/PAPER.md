---
title: |
  Nomopoiesis:\
  Dynamics That Rewrite Their Own Dynamics
author: PIATRA . INSTITUTE
date: July 2026
---

## Abstract

Many systems in biology and society alter the rules that govern their own dynamics. A population reshapes the environment that selects it, and a market invents instruments that change what a trade is. We call this process nomopoiesis, from nomos (established law or custom) and poiesis (making), and formalize it as a state $x_t$ and a law parameter $\lambda_t$ that the trajectory edits: $x_{t+1} = F_{\lambda_t}(x_t)$ and $\lambda_{t+1} = \mathcal{N}(\lambda_t, x_t)$. A system is nomopoietic only when a causal path $x_t \to \lambda_{t+1} \to x_{t+k}$ runs through the law, which excludes laws driven by an external clock. The pair $(x,\lambda)$ can always be flattened into a larger autonomous system; the distinction is retained by typing object-level and rule-level variables and by the causal relation between them, and it matters most when construction changes the state space, the interaction topology or the action alphabet. Niche construction is the worked instance. In four deterministic models, a trait with direct selection gradient $-0.6$ has a total gradient of $+5.4$ once the environment it builds is counted; a costly constructor is favoured only above an environmental persistence of $0.68$; a one-off action under a state-edited law grows to $4.5$ times its initial effect after forty steps, while in an externally forced twin with the same law time-course it decays below $10^{-11}$; and a replicator game whose payoff matrix is written by play sustains cooperation cycles of amplitude $0.95$, whereas every frozen game fixates or, at one neutral environment, stays put. Endogenous editing of the rules of selection is a testable structural property of evolving systems.

## 1. Introduction

An autonomous dynamical system $z_{t+1} = F(z_t)$ consists of a state and a fixed rule for advancing it. The rule lies outside the state and does not change while the state moves. Much of dynamical systems theory assumes this form, because it is the form under which trajectories and attractors are well defined. It does not fit a beaver.

A beaver in a valley is a state in an environment, and the two evolve reciprocally. The niche-construction literature has modelled this for two decades as coupled organism and environment, $x_{t+1} = F(x_t, e_t)$ and $e_{t+1} = G(e_t, x_t)$ (Odling-Smee, Laland, & Feldman, 2003), so that the environment which advances the organism is itself advanced by the organism. A further step recognizes that the organism edits the rule under which its own future variables move, in addition to an environmental variable. Let $\lambda_t$ collect the effective law of the local world: the environmental dynamics, the interaction topology, the feasible actions, the transport costs and boundaries, the payoff or fitness map, and the list of state variables that exist at all. The system is then

$$
x_{t+1} = F_{\lambda_t}(x_t), \qquad \lambda_{t+1} = \mathcal{N}(\lambda_t, x_t).
$$

The first equation describes change under a law and the second change of the law, performed by the operator $\mathcal{N}$. We call the operator, and the process it runs, nomopoiesis. The word joins nomos, which across Greek usage spans law, rule, custom and established order, to poiesis, making or bringing into being. The adjective nomopoietic appears occasionally in legal theory for rule-instituting procedures; here it denotes a property of dynamical systems.

The term refers to a specific contrast. Greek thought set physis, nature and its spontaneous constitution, against nomos, the conventions and laws a community lays down, and the antithesis was a live controversy among the sophists (Kerferd, 1981). A niche constructor operates at the junction of the two. It leaves physis unchanged: the beaver's dam obeys the same hydrodynamics as the undammed stream. The dam changes the local nomos, the effective boundary conditions, retention times, transport costs and species interactions under which life in the valley proceeds. In this sense niche construction is ecological nomopoiesis: organisms write local law within fixed physical law.

## 2. The causal criterion for rule editing

A time-varying rule does not by itself make a system nomopoietic. A rule can change because an experimenter turns a dial, a season advances or an exogenous signal arrives; the system $x_{t+1} = F_t(x_t)$ has a rule indexed by $t$, and $t$ is set by a clock the system does not affect. The relevant distinction is causal closure of the editing loop. A system is nomopoietic when there is a nontrivial path

$$
x_t \longrightarrow \lambda_{t+1} \longrightarrow x_{t+k},
$$

so that the state's history writes the law its future obeys. The organism must do something now that changes a future rule, and the changed rule must affect what the organism does later. When the arrow from $x_t$ to $\lambda_{t+1}$ is absent, the law is externally driven and the system is an ordinary nonautonomous system.

The criterion excludes three overclaims, each with a counterpart in the niche-construction literature. A change in the environment that no future state reads is a trace and does not count as construction, because the loop must return to the organism. A statistical association between what the organism did and what the environment later looked like does not establish construction if an unobserved common cause produced both; the appropriate quantity is a path-specific causal effect through the environmental mediator, ideally measured under intervention (Lee, Flack, & Krakauer, 2022). A change with no consequence for viability or reproduction is not evolutionarily significant construction however large it is, because the relevant currency is lineage growth. Fitness is accordingly defined as the long-run invasion growth rate of a rare type in the environment set by a resident, a lineage-growth quantity with no implication that organisms maximize a utility (Metz, Nisbet, & Geritz, 1992).

## 3. Relation to an enlarged state space

The two update equations can be stacked,

$$
(x_{t+1}, \lambda_{t+1}) = H(x_t, \lambda_t),
$$

and $H$ is an ordinary autonomous system on the enlarged space $X \times \Lambda$. Any finite hierarchy of rule editing embeds in this way. If nomopoiesis meant only that some coordinate changes, it would be a redescription without content, since every dynamical system has changing coordinates.

The content lies in a typed distinction that the flattening discards. In $H$ the coordinates $x$ and $\lambda$ are formally alike, points in a product space. In the modelled system $x$ ranges over object-level states, the configurations the rule acts on, and $\lambda$ ranges over the rule, the structure that determines how object-level states move. The causal relation between them is asymmetric, and the asymmetry is the phenomenon of interest. Reading $(x,\lambda) = H(\cdot)$ as one flat system is permissible, but it deletes the difference between a position and the law of motion for positions, which the model is built to track. For the same reason a program and its input are usefully kept distinct, even though a universal machine treats them as one tape.

The typing matters most when $\lambda$ edits what $x$ is. When construction changes the reachable dimension, the admissible variables, the interaction topology or the alphabet of available actions, the object space $X_{\lambda}$ is itself a function of the law, and a transition

$$
(x_t, \lambda_t) \longrightarrow (x_{t+1}, \lambda_{t+1}), \qquad x_t \in X_{\lambda_t},\ x_{t+1} \in X_{\lambda_{t+1}},\ X_{\lambda_t} \neq X_{\lambda_{t+1}},
$$

maps between different spaces. A fixed enlarged $X \times \Lambda$ can still contain such transitions if $X$ is taken large enough to hold every $X_{\lambda}$ at once, at the price of a state space specified in advance to contain possibilities that the model treats as produced during the dynamics. The nearest prior term, the meta-dynamical adaptive system, was introduced for the case in which a higher level modifies lower-level dynamics and the state-space dimension can change (Moulay & Baguelin, 2005). Nomopoiesis names the process and adds the causal and typed reading that prevents its collapse into a flat system.

The cases can be ordered by what is rewritten. Parametric nomopoiesis (depth one) leaves the form of $F$ fixed and moves its parameters, as when organisms shift a temperature or a resource density. Structural nomopoiesis (depth two) keeps the state space and changes the geometry, boundary conditions, constraints or interaction graph that define $F$, as a trail changes a cost metric or a dam changes a boundary. Generative nomopoiesis (depth three) changes the state space or the action alphabet, as a new symbiosis, signalling channel or technology adds a variable that did not previously exist. The three depths are progressively harder to flatten and to formalize. At depth three, evolution changes the set of problems a lineage faces in addition to solving problems within a fixed set; recent work on functional information attempts to quantify this expansion of possibility under selection for function (Wong et al., 2023).

## 4. Niche construction as ecological nomopoiesis

Niche construction is the instance around which the formalism was built. Let the population be a distribution $\mu_t$ over states advancing under a transition operator, and let the population edit the operator through a heritable constructor policy $\pi_\theta$,

$$
\mu_{t+1} = \mu_t P_t, \qquad P_{t+1} = \mathcal{N}(P_t, \mu_t, \pi_\theta).
$$

The population changes both which states are common and the operator that will determine which states are common next. Selection acts on constructor policies through their long-run invasion fitness in the environment a resident policy generates, and the adaptive-dynamics gradient of that fitness gives the direction of evolution (Geritz, Kisdi, Meszéna, & Metz, 1998). That a constructed environment feeds back into selection, fixing otherwise deleterious alleles and creating or removing polymorphisms, is the founding formal result of niche-construction theory (Laland, Odling-Smee, & Feldman, 1999), and the reach of a constructor's effect beyond its own body is the extended phenotype (Dawkins, 1982).

The niche can be defined through viability, which avoids assuming that organisms maximize anything. Let $z = (x,e)$ be the joint organism-environment state and $K$ the set of viable states. The viability kernel is the set of initial conditions from which some admissible policy keeps the trajectory in $K$ for all future time (Aubin, 1991),

$$
\operatorname{Viab}(K) = \{\, z_0 : \exists\, u(\cdot)\ \text{with}\ z_t \in K\ \text{for all}\ t \geq 0 \,\}.
$$

Construction is then the organism-induced enlargement, displacement or stabilization of this kernel, and the usual descriptors become geometric: niche breadth is the size of the kernel, resilience is the distance from the current state to its boundary, and construction efficiency is kernel gain per unit work. No utility function is posited, and selection can install mechanistic policies that keep a lineage viable without foresight. When the edited object is an interaction graph, the same picture applies to adaptive networks, in which node states and topology coevolve and adding or cutting an edge creates or destroys a feasible transition (Gross & Blasius, 2008).

## 5. Direct and niche-mediated selection

The central decomposition states how much of selection runs through the constructed environment. Suppose the environment built by a resident trait $\theta$ settles to an equilibrium $e^*(\theta)$ defined by $G(e^*, \theta) = 0$, and let fitness be $w(\theta, e)$. Differentiating the realized fitness $w(\theta, e^*(\theta))$ and applying the implicit-function theorem to the equilibrium condition gives

$$
\frac{dw}{d\theta} = \underbrace{\frac{\partial w}{\partial \theta}}_{\text{direct}} \; \underbrace{- \frac{\partial w}{\partial e}\left(\frac{\partial G}{\partial e}\right)^{-1}\frac{\partial G}{\partial \theta}}_{\text{niche-mediated}}.
$$

The first term is the trait's direct effect on reproduction. The second is its effect through the equilibrium environment; it records the sign and strength of the feedback and is amplified when the environment is persistent and sensitive. For fluctuating or spatial environments the inverse becomes a resolvent or adjoint-sensitivity operator, and the split still holds.

Ecological inheritance is the part of this effect that crosses generations, and it has an impulse-response form. Let the environment propagate construction actions linearly, $e_{t+1} = R e_t + B a_t$, so that a unit action propagates as $R^{k-1} B$ after $k$ steps, and let fitness read the environment through a sensitivity $q$. The delayed effect of an action on later fitness is the niche-response kernel

$$
\mathcal{K}_k = q^\top R^{k-1} B,
$$

which records the strength, sign, delay and generational reach of a construction (Lehmann, 2008). A costly constructor is favoured when the discounted, recipient-weighted benefit exceeds the cost,

$$
-c + \sum_{k=1}^{\infty} \beta^k\, r_k\, \mathcal{K}_k > 0,
$$

with $c$ the present cost, $\beta$ a generational discount, and $r_k$ the association between the constructor and whoever holds the altered environment $k$ generations later. Future benefit counts only when the environment persists to hold it ($R$) and remains with descendants or relatives ($r_k$). Whether such a trait constitutes a distinct evolutionary force or a special case of standard theory is debated, and the decomposition is neutral on the question: it separates the channels so that either reading can be stated precisely.

## 6. Four minimal models

Four small deterministic models instantiate the definitions above with named values. None is fit to data, and every number reported is a key in the accompanying `results.json`. The models test the consistency of the definitions and show what the corresponding measurements would look like; they establish no biological fact.

The selection decomposition can reverse the sign of selection. In a coupled trait-environment model in which the trait is directly costly and builds an environment that pays, the direct gradient is $dw/d\theta = -0.6$, so reasoning at a fixed environment classifies the trait as deleterious. The niche-mediated term is $+6.0$ and the total gradient $+5.4$: once the environment tracks the trait, the trait is favoured. The analytic total agrees with a finite difference of the numerically solved equilibrium fitness to six figures. Ecological inheritance sets a threshold (Figure 1). As the environmental persistence, the spectral radius of $R$, is varied, net selection on a costly constructor crosses zero at a critical persistence of $0.68$, located by bisection on the closed form ($0.677365$). Below it the environment forgets the construction before the benefit returns and the trait is selected against ($-0.47$ at persistence $0.3$); above it ecological inheritance delivers the benefit to descendants and the trait invades ($+0.60$ at persistence $0.9$). The closed-form geometric sum $\beta r\, q^\top (I - \beta r R)^{-1} B$ agrees with an explicit four-hundred-generation lineage sum.

![Components of selection and the persistence threshold. Left: the selection gradient $dw/d\theta$ split into a direct term ($-0.6$), a niche-mediated term ($+6.0$) and their total ($+5.4$); the analytic total equals a finite difference of the constructed-equilibrium fitness. Right: net selection on a costly constructor against environmental persistence (spectral radius of $R$), crossing zero at $0.68$.](../simulation/output/figures/selection.png){width=100%}

A nomopoietic gain separates law editing from external forcing. Define $G_N(k)$ as the ratio of a late to an early separation between a lineage that takes a one-off construction action and a counterfactual lineage that does not. When the state edits the law, the perturbation propagates through the law and the separation grows to $4.5$ times its initial value by forty steps (Figure 2). In an externally forced twin, with the identical law time-course and no path from state to law, the same action decays, and its separation falls below $10^{-11}$ over the same span. The two systems agree at every instant on how the rule varies and differ in whether a present action affects the future, which is the causal-path criterion of Section 2 in quantitative form.

![Trajectory separation from a counterfactual after a single construction action, on a log scale. When the state edits the law the separation grows to $G_N(40) = 4.5$ times its initial value; in the forced twin, with the same law time-course set by an external clock, it decays toward zero.](../simulation/output/figures/gain.png){width=72%}

Play can rewrite the game in which it takes place. Consider replicator dynamics for a cooperation frequency $p$ on a payoff matrix that an environment $n$ interpolates between a defection-dominant dilemma and a cooperation-favouring game, with the environment driven by the play. The cooperator's payoff advantage in this construction is $2(n - 0.5)$, independent of $p$. At any frozen environment the game is an ordinary one: play fixates at all-defect when $n < 0.5$ and at all-cooperate when $n > 0.5$, and at $n = 0.5$ exactly the advantage vanishes and play stays where it starts. With the feedback closed, the coupled system neither fixates nor comes to rest. Cooperation and environment cycle with an amplitude of $0.95$ around a mean cooperation of $0.50$ (Figure 3), a sustained oscillation of the kind first shown for game-environment feedback (Weitz, Eksin, Paarporn, Brown, & Ratcliff, 2016) and extended by models in which the current play and the current game jointly select the next game (Su, McAvoy, Wang, & Nowak, 2019). In logit coordinates the coupled system conserves a quantity along its orbits (numerical drift $3 \times 10^{-11}$ relative), so the cycles are neutral and their amplitude is set by the initial condition: starting from $(p, n) = (0.5, 0.85)$ gives $0.95$, and starting from $(0.5, 0.65)$ gives $0.52$. The population does not settle on a strategy within a fixed game, because the play keeps changing which game is played.

![Cooperation frequency $p$ and environment $n$ under replicator dynamics whose payoff matrix is interpolated by the environment, with the environment driven by the play. Frozen games with $n \neq 0.5$ fixate at a corner (dashed lines at $0$ and $1$); the coupled system follows a neutral cycle of amplitude $0.95$ from the initial condition used here.](../simulation/output/figures/game.png){width=90%}

## 7. Cost, composition and scale

Construction requires work, because a constructed state relaxes toward the environment's passive dynamics unless it is maintained. If $P_0$ is the passive path distribution and $P_\pi$ the distribution under a construction policy, a stochastic-control reading prices the policy by a path-space divergence, $\mathcal{C}(\pi) \propto D_{\mathrm{KL}}(P_\pi \,\|\, P_0)$, the cost of holding trajectories away from where they would drift on their own (Todorov, 2009). A variational free-energy account of the same organism-environment loop has been developed within active inference; it is useful for perception-action coupling and is one available formulation among several (Constant, Ramstead, Veissière, Campbell, & Friston, 2018).

Organisms are open systems that exchange matter, energy and information, so the framework needs a way to nest constructors without treating a cell, a tissue, an organism and an ecosystem as one monolith. The compositional tools of open games supply one. A constructor is a lens, a forward map that acts on the environment paired with a backward map that returns altered constraints and selection pressures, and lenses compose along shared interfaces in a symmetric monoidal category (Ghani, Hedges, Winschel, & Zahn, 2018). Composition guarantees that a model built at one scale connects to a model at the next; it does not by itself predict the biology.

At large scales most construction consists of many small local actions, and the question is which of them survive coarse-graining to become macroscopic niche variables such as trails, fields, conventions and regimes. This is a renormalization question. Under coarse-graining the organism-environment couplings transform, and a given constructor effect is irrelevant if it washes out, marginal if it persists without amplification, and relevant if it grows to dominate the large-scale description (Wilson, 1975). A niche is then an organism-produced causal memory that survives coarse-graining. Three dimensionless quantities organize the regimes: the persistence ratio $\Pi = \tau_E/\tau_G$ of environmental memory to generation time, the feedback gain $\Gamma$ of the closed loop, and the capture $Q$ of delayed benefit that returns to the constructor's lineage. Large $\Pi$ with small $Q$ describes public infrastructure open to exploitation; large $\Pi$ with large $Q$ an inherited niche; high positive $\Gamma$ runaway feedback or a tipping point; and high negative $\Gamma$ homeostatic regulation. The persistence threshold computed in Section 6 is the point on the $\Pi$ axis at which a costly constructor begins to pay.

## 8. Related concepts

Two terminological neighbours should be distinguished. An autopoietic system produces its own components and thereby its own boundary (Maturana & Varela, 1980), whereas a nomopoietic system produces its own laws, and a system can do either without the other. Metadynamics in molecular simulation is an enhanced-sampling method for escaping free-energy minima (Laio & Parrinello, 2002); it shares a stem with the present term and is otherwise unrelated.

## 9. Limitations

The four models are illustrative. Each has a handful of stipulated parameters, the environments are deterministic and, in two cases, linear, and none is calibrated against a population or an ecosystem. The sign reversal and the persistence threshold follow from the chosen functional forms, and their magnitudes carry no empirical weight. The game oscillation is a neutral cycle whose amplitude depends on the initial condition, and it is structurally fragile: noise or dissipation that breaks the conserved quantity can turn it into a spiral or a limit cycle. The measurement proposed in Section 2, a path-specific causal effect through the constructed environment estimated under intervention, has not been carried out here. Depth-three nomopoiesis, in which the state space itself changes, is defined but not simulated.

## 10. Conclusion

Treating evolution as motion across a fixed landscape asks which point a lineage reaches. Treating it as nomopoiesis asks how a lineage rewrites the landscape's metric, boundaries, transition rules and set of possibilities, and which of those rewrites persist and return to the lineage. The models show checkable consequences of the second view: a selection gradient that reverses sign when the constructed environment is counted, a persistence threshold that determines whether a costly constructor pays, a gain that separates a law a system edits from a law driven by a clock, and cycles that only the coupled game admits. Organisms rarely alter physical law, but they repeatedly alter the local laws under which they and their descendants act.

## Reproducibility

The simulation (`analyses.py`, `figures.py`, `run_all.py`) is deterministic, uses closed forms or numerical solutions to tolerance, samples nothing, and reproduces every number and figure reported here. It checks the analytic selection gradient against a finite difference, the closed-form kernel sum against a truncated lineage sum, the refined critical persistence against the grid crossing, and conservation of the game's orbit invariant.

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
