"""Deterministic demonstrations for *Nomopoiesis: Dynamics That Rewrite Their
Own Dynamics*.

A nomopoietic system carries an ordinary state ``x`` and a law parameter
``lambda`` that its own trajectory edits: ``x_{t+1} = F_lambda(x_t)`` and
``lambda_{t+1} = N(lambda_t, x_t)``. The paper's worked instance is niche
construction, where an organism trait writes a persistent change into its
environment and thereby edits the selection its lineage later meets. Four facts
about small, explicit models are computed here, each a claim the paper makes
precise.

  1. Direct versus niche-mediated selection. In a coupled trait-environment
     model the derivative of long-run fitness splits into a direct term and an
     environment-mediated term (implicit-function theorem on the constructed
     equilibrium). The two can carry opposite signs: a trait that within-a-fixed-
     environment reasoning calls deleterious is favoured once the environment it
     builds is counted. The analytic split is validated against a direct
     finite-difference of the numerically solved equilibrium fitness.

  2. The niche-response kernel and the persistence threshold. Ecological
     inheritance is the impulse response K_k = q' R^{k-1} B of fitness to a past
     construction action. A costly constructor is favoured when
     -c + sum_k beta^k r^k K_k > 0. Sweeping environmental persistence (the
     spectral radius of R) locates the critical persistence at which the trait
     flips from selected against to selected for. The geometric-series value is
     validated against an explicit truncated-lineage sum.

  3. Nomopoietic gain and the genuineness criterion. G_N(k) is the ratio of a
     late to an early trajectory separation between a constructing lineage and a
     non-constructing counterfactual. In a genuinely nomopoietic system (the law
     is edited by the state) the gain grows and persists; in an externally forced
     system with the same instantaneous variation but no state-to-law path, it
     decays. The contrast operationalizes the paper's causal-path criterion.

  4. A game whose matrix is rewritten by play. Replicator dynamics on an
     environment-dependent payoff matrix, with the environment driven by the play,
     produce persistent cooperation-defection oscillation that neither the fixed
     game (which fixates on defection) nor the passive environment predicts.

Everything is deterministic and closed-form or solved to tolerance; nothing is
sampled. The models are illustrative and instantiate the paper's definitions;
they are not fit to data. Every reported number is a key in results.json.
"""
from __future__ import annotations

import numpy as np

# ----------------------------------------------------------------------------
# 1. Direct versus niche-mediated selection
# ----------------------------------------------------------------------------
# Trait theta drives a construction action that shifts the environmental
# equilibrium e*(theta). Fitness w(theta, e) rewards the environment but the
# trait is directly costly. The environment equilibrates at G(e*, theta) = 0.

def _env_equilibrium(theta: float, rho: float, kappa: float) -> float:
    """e* solves e = rho*e + kappa*theta  ->  e* = kappa*theta/(1-rho)."""
    return kappa * theta / (1.0 - rho)


def _fitness(theta: float, e: float, cost: float, benefit: float) -> float:
    """Direct quadratic cost of the trait, linear benefit from the environment."""
    return benefit * e - cost * theta * theta


def analysis_selection_decomposition() -> dict:
    rho = 0.8          # environmental persistence
    kappa = 1.0        # how strongly the trait writes the environment
    cost = 0.5         # direct cost coefficient
    benefit = 1.2      # fitness value of the constructed environment
    theta0 = 0.6       # resident trait

    # G(e, theta) = rho*e + kappa*theta - e = 0
    # de*/dtheta by implicit-function theorem: -(dG/de)^{-1} dG/dtheta
    dG_de = rho - 1.0
    dG_dtheta = kappa
    de_dtheta = -(1.0 / dG_de) * dG_dtheta        # = kappa/(1-rho)

    e_star = _env_equilibrium(theta0, rho, kappa)
    dw_dtheta_direct = -2.0 * cost * theta0        # partial w / partial theta at fixed e
    dw_de = benefit
    dw_dtheta_total = dw_dtheta_direct + dw_de * de_dtheta
    niche_mediated = dw_de * de_dtheta

    # validate the total gradient against a finite difference of w(theta, e*(theta))
    h = 1e-6
    def realized(t):
        return _fitness(t, _env_equilibrium(t, rho, kappa), cost, benefit)
    fd_total = (realized(theta0 + h) - realized(theta0 - h)) / (2 * h)

    return {
        "rho": rho, "kappa": kappa, "cost": cost, "benefit": benefit,
        "theta": theta0,
        "e_star": round(e_star, 6),
        "de_star_dtheta": round(de_dtheta, 6),
        "direct_gradient": round(dw_dtheta_direct, 6),
        "niche_mediated_gradient": round(niche_mediated, 6),
        "total_gradient": round(dw_dtheta_total, 6),
        "finite_difference_total": round(fd_total, 6),
        "analytic_matches_numeric": bool(abs(dw_dtheta_total - fd_total) < 1e-4),
        "sign_reversal": bool(np.sign(dw_dtheta_direct) != np.sign(dw_dtheta_total)),
        "_direct": dw_dtheta_direct, "_total": dw_dtheta_total,
        "_niche": niche_mediated,
    }


# ----------------------------------------------------------------------------
# 2. Niche-response kernel and the persistence threshold
# ----------------------------------------------------------------------------
# e_{t+1} = R e_t + B a_t. A unit construction action a_0 propagates as
# e_k = R^{k-1} B, and fitness sensitivity q reads it off: K_k = q' R^{k-1} B.
# A costly trait invades when -c + sum_k beta^k r^k K_k > 0.

def _kernel_value(R: np.ndarray, B: np.ndarray, q: np.ndarray,
                  beta: float, r: float, kmax: int) -> float:
    """sum_{k>=1} beta^k r^k q' R^{k-1} B, truncated at kmax (explicit lineage sum)."""
    total = 0.0
    Rp = np.eye(R.shape[0])            # R^{0}
    for k in range(1, kmax + 1):
        Kk = float(q @ Rp @ B)         # q' R^{k-1} B
        total += (beta * r) ** k * Kk
        Rp = Rp @ R
    return total


def _kernel_value_closed(R: np.ndarray, B: np.ndarray, q: np.ndarray,
                         beta: float, r: float) -> float:
    """Closed form sum_{k>=1}(beta r)^k q' R^{k-1} B = beta r q' (I - beta r R)^{-1} B."""
    n = R.shape[0]
    M = np.linalg.inv(np.eye(n) - beta * r * R)
    return float(beta * r * (q @ M @ B))


def analysis_persistence_threshold() -> dict:
    n = 3
    # a fixed interaction shape for R, scaled to a target spectral radius
    base = np.array([[0.6, 0.3, 0.0],
                     [0.0, 0.5, 0.2],
                     [0.1, 0.0, 0.4]])
    base_sr = max(abs(np.linalg.eigvals(base)))
    B = np.array([1.0, 0.3, 0.0])
    q = np.array([0.9, 0.4, 0.2])
    beta = 0.9        # generational discount
    r = 0.8           # association between constructor and later recipients
    cost = 1.4        # present construction cost
    kmax = 400

    def R_of(sr):
        return base * (sr / base_sr)

    persistences = np.linspace(0.05, 0.95, 181)
    net = []
    closed_ok = True
    for sr in persistences:
        R = R_of(sr)
        val = _kernel_value(R, B, q, beta, r, kmax)
        val_closed = _kernel_value_closed(R, B, q, beta, r)
        if abs(val - val_closed) > 1e-6 * max(1.0, abs(val_closed)):
            closed_ok = False
        net.append(-cost + val)
    net = np.array(net)

    # critical persistence where net selection crosses zero
    crossings = np.where(np.diff(np.sign(net)) != 0)[0]
    if len(crossings):
        i = crossings[0]
        x0, x1 = persistences[i], persistences[i + 1]
        y0, y1 = net[i], net[i + 1]
        sr_crit = float(x0 - y0 * (x1 - x0) / (y1 - y0))
    else:
        sr_crit = float("nan")

    # The value above is a linear interpolation between two points of a 181-point
    # grid. Refine it by bisection on the closed-form net selection (prose audit,
    # 2026-09-23); the closed form is monotone in the spectral radius here.
    def net_closed(sr):
        return -cost + _kernel_value_closed(R_of(sr), B, q, beta, r)
    lo, hi = float(persistences[crossings[0]]), float(persistences[crossings[0] + 1])
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if np.sign(net_closed(mid)) == np.sign(net_closed(lo)):
            lo = mid
        else:
            hi = mid
    sr_crit_exact = 0.5 * (lo + hi)
    assert abs(net_closed(sr_crit_exact)) < 1e-9
    assert abs(sr_crit_exact - sr_crit) < (persistences[1] - persistences[0])

    R_lo, R_hi = R_of(0.3), R_of(0.9)
    return {
        "beta": beta, "association_r": r, "cost": cost,
        "kmax_truncation": kmax,
        "closed_form_matches_truncated_sum": bool(closed_ok),
        "critical_persistence": round(sr_crit, 6),
        "critical_persistence_exact": round(sr_crit_exact, 9),
        "net_selection_at_sr_0.3": round(-cost + _kernel_value_closed(R_lo, B, q, beta, r), 6),
        "net_selection_at_sr_0.9": round(-cost + _kernel_value_closed(R_hi, B, q, beta, r), 6),
        "_persistences": persistences.tolist(),
        "_net": net.tolist(),
    }


# ----------------------------------------------------------------------------
# 3. Nomopoietic gain and the genuineness criterion
# ----------------------------------------------------------------------------
# Genuine: the law parameter lambda is edited by the state (x -> lambda -> x).
# Forced: lambda follows the same time course but by an external clock, with no
# path from the state. Both share the instantaneous law variation; only the
# genuine one lets a present nudge compound into the future.

def _run_genuine(x0, lam0, nudge, T, alpha, g):
    x, lam = x0, lam0
    xs = [x]
    for t in range(T):
        u = nudge if t == 0 else 0.0           # a one-off construction action at t=0
        x = alpha * x + lam * 1.0 + u          # state moves under the current law
        lam = lam + g * x                      # STATE edits the law (nomopoietic path)
        xs.append(x)
    return np.array(xs)


def _run_forced(x0, lam_series, nudge, T, alpha):
    x = x0
    xs = [x]
    for t in range(T):
        u = nudge if t == 0 else 0.0
        x = alpha * x + lam_series[t] * 1.0 + u   # same law time course, external clock
        xs.append(x)
    return np.array(xs)


def analysis_nomopoietic_gain() -> dict:
    T = 40
    alpha = 0.5
    g = 0.05
    lam0 = 0.2
    x0 = 1.0
    nudge = 0.5

    # genuine system: reference and nudged trajectories; the law is state-edited
    ref = _run_genuine(x0, lam0, 0.0, T, alpha, g)
    per = _run_genuine(x0, lam0, nudge, T, alpha, g)
    sep_genuine = np.abs(per - ref)

    # forced twin: replay the reference system's own law series as an external clock
    lam_series = []
    x, lam = x0, lam0
    for t in range(T):
        x = alpha * x + lam * 1.0
        lam_series.append(lam)
        lam = lam + g * x
    lam_series = np.array(lam_series)
    ref_f = _run_forced(x0, lam_series, 0.0, T, alpha)
    per_f = _run_forced(x0, lam_series, nudge, T, alpha)
    sep_forced = np.abs(per_f - ref_f)

    def gain(sep, k):
        return float(sep[k] / sep[1]) if sep[1] > 0 else float("nan")

    return {
        "horizon": T, "alpha": alpha, "law_coupling_g": g, "nudge": nudge,
        "gain_genuine_k10": round(gain(sep_genuine, 10), 6),
        "gain_genuine_k40": round(gain(sep_genuine, 40), 6),
        "gain_forced_k10": round(gain(sep_forced, 10), 6),
        "gain_forced_k40": round(gain(sep_forced, 40), 6),
        "genuine_grows": bool(sep_genuine[40] > sep_genuine[1]),
        "forced_decays": bool(sep_forced[40] < sep_forced[1]),
        "_sep_genuine": sep_genuine.tolist(),
        "_sep_forced": sep_forced.tolist(),
    }


# ----------------------------------------------------------------------------
# 4. A game whose payoff matrix is rewritten by play
# ----------------------------------------------------------------------------
# Replicator dynamics for cooperation frequency p on a payoff matrix A(e); the
# environment e in [0,1] is driven by the current level of cooperation and feeds
# back into the payoffs. At e=0 the game is a defection-dominant dilemma; at e=1
# cooperation is favoured. The coupled system oscillates.

def _payoff_matrix(n: float) -> np.ndarray:
    """Payoff matrix interpolated by the environment n in [0,1]. Rows/cols are
    [cooperate, defect]. At n=0 defection dominates (T>R, P>S); at n=1 cooperation
    dominates. The cooperator's payoff advantage works out to exactly 2(n-0.5),
    independent of the population mix, so the environment sets which game is played."""
    A0 = np.array([[2.0, 0.0], [3.0, 1.0]])       # defect-dominant dilemma
    A1 = np.array([[3.0, 1.0], [2.0, 0.0]])       # cooperation-dominant game
    return (1 - n) * A0 + n * A1


def _coop_advantage(n: float, p: float) -> float:
    A = _payoff_matrix(n)
    x = np.array([p, 1 - p])
    f = A @ x
    return float(f[0] - f[1])                     # = 2(n - 0.5)


def analysis_game_rewritten() -> dict:
    dt = 0.02
    T = 60000
    eps = 0.6            # environmental feedback rate
    p0, n0 = 0.5, 0.85   # start off the interior fixed point (0.5, 0.5)

    def deriv(p, n):
        dp = p * (1 - p) * _coop_advantage(n, p)          # replicator on the current game
        dn = eps * n * (1 - n) * (0.5 - p)                # play writes the environment
        return dp, dn

    def rk4(p, n):
        k1p, k1n = deriv(p, n)
        k2p, k2n = deriv(p + 0.5 * dt * k1p, n + 0.5 * dt * k1n)
        k3p, k3n = deriv(p + 0.5 * dt * k2p, n + 0.5 * dt * k2n)
        k4p, k4n = deriv(p + dt * k3p, n + dt * k3n)
        p2 = p + dt / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        n2 = n + dt / 6 * (k1n + 2 * k2n + 2 * k3n + k4n)
        return min(1.0, max(0.0, p2)), min(1.0, max(0.0, n2))

    p, n = p0, n0
    ps, ns = [], []
    for _ in range(T):
        p, n = rk4(p, n)
        ps.append(p)
        ns.append(n)
    ps, ns = np.array(ps), np.array(ns)

    # fixed-environment baselines: freeze the game and evolve play alone -> fixation
    def fixate(n_fixed):
        pf = 0.5
        for _ in range(T):
            pf = min(1.0, max(0.0, pf + dt * pf * (1 - pf) * _coop_advantage(n_fixed, pf)))
        return float(pf)

    tail = slice(T // 2, T)
    amp = float(ps[tail].max() - ps[tail].min())

    # The coupled system has a conserved quantity. In logit coordinates
    # u = logit p, v = logit n: du/dt = 2n - 1 and
    # dv/dt = eps (0.5 - p), so H = eps*(ln(1+e^u) - u/2) + (2 ln(1+e^v) - v) is
    # constant along orbits. The oscillation is therefore a neutral cycle whose
    # amplitude is set by the initial condition (prose audit, 2026-09-23).
    def H(pp, nn):
        u = np.log(pp / (1 - pp)); v = np.log(nn / (1 - nn))
        return eps * (np.log1p(np.exp(u)) - u / 2) + (2 * np.log1p(np.exp(v)) - v)
    H0 = H(p0, n0)
    Hs = H(ps, ns)
    H_drift = float(np.max(np.abs(Hs - H0)) / abs(H0))
    assert H_drift < 1e-3, "the coupled game must conserve H to integration accuracy"
    # a second initial condition closer to the centre gives a smaller cycle
    p, n = 0.5, 0.65
    ps2 = []
    for _ in range(T):
        p, n = rk4(p, n)
        ps2.append(p)
    ps2 = np.array(ps2)
    amp2 = float(ps2[tail].max() - ps2[tail].min())
    # At the frozen environment n = 0.5 the cooperator's advantage 2(n - 0.5) is
    # zero, so play is neutral there and does not fixate.
    return {
        "dt": dt, "steps": T, "env_feedback_eps": eps,
        "coupled_coop_mean": round(float(ps[tail].mean()), 6),
        "coupled_coop_amplitude": round(amp, 6),
        "coupled_persistent_oscillation": bool(amp > 0.1),
        "fixed_game_low_env_fixation": round(fixate(0.2), 6),
        "fixed_game_high_env_fixation": round(fixate(0.8), 6),
        "fixed_game_neutral_env_0.5_final_p": round(fixate(0.5), 6),
        "conserved_quantity_H_max_relative_drift": float(f"{H_drift:.3g}"),
        "coupled_coop_amplitude_from_n0_0.65": round(amp2, 6),
        "_p": ps[::40].tolist(), "_n": ns[::40].tolist(),
    }


def run() -> dict:
    return {
        "note": "Illustrative closed models instantiating the paper's definitions; not fit to data. Deterministic.",
        "selection_decomposition": analysis_selection_decomposition(),
        "persistence_threshold": analysis_persistence_threshold(),
        "nomopoietic_gain": analysis_nomopoietic_gain(),
        "game_rewritten": analysis_game_rewritten(),
    }
