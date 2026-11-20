# Task Q: Numerical Solution of ODEs Using SciPy (`Task_18_scipy_ode.py`)

## B. Input Values and Mathematical Operations
* **Inputs:**
  * Supply voltage $V_s = 5.0\text{ V}$, resistance $R = 1000.0\ \Omega$, capacitance $C = 0.001\text{ F}$, and initial capacitor voltage $V_0 = 0.0\text{ V}$.
  * Integration interval $t \in [0, 5]\text{ s}$ evaluated at 200 evenly spaced points (`t_eval`), with solver tolerances `rtol=1e-9` and `atol=1e-11`.
* **Mathematical Operations:**
  * Numerically integrates the first-order linear ODE $\frac{dV}{dt} = \frac{V_s - V}{RC}$ using `scipy.integrate.solve_ivp` (default adaptive Runge-Kutta RK45 method).
  * Validates the numerical trajectory against the analytical closed-form solution $V(t) = V_s\left(1 - e^{-t/(RC)}\right)$ by computing the maximum absolute error across all time points.

## C. Parameter Modification and Impact
* **Change Made:** Increased series resistance $R$ from `1000.0` $\Omega$ to `2500.0` $\Omega$ while keeping $C = 0.001\text{ F}$ and $V_s = 5.0\text{ V}$.
* **Result Change:** The capacitor voltage at $t = 5.0\text{ s}$ drops from `4.9663 V` (99.33% of $V_s$) to `4.3233 V` (86.47% of $V_s$).
* **Explanation:** Increasing resistance restricts charging current ($I = (V_s - V)/R$), raising the circuit time constant $\tau = RC$ from $1.0\text{ s}$ to $2.5\text{ s}$. Consequently, $t = 5.0\text{ s}$ represents only $2\tau$ instead of $5\tau$, leaving the capacitor noticeably further from full charge.

## D. Output and Graph Interpretation
* **Numerical Output:** At $t = 5\text{ s}$, `solve_ivp` reports `4.9663 V` with a maximum error of $\approx 1.18 \times 10^{-11}\text{ V}$ against the exact formula.
* **Graph Interpretation:** The curve starts at $(0, 0)$ with its steepest slope—because the voltage difference $V_s - V$ driving current is largest initially—and gradually flattens as $V(t)$ approaches the horizontal asymptote of $5.0\text{ V}$. The solid `solve_ivp` curve and dashed exact analytical curve overlap completely, confirming solver accuracy.

## E. Modified Real-World Case: SIR Infectious Disease Transmission Model
* **Problem Statement:** Simulate the spread of an acute viral infection through a closed population of $N = 10,000$ individuals over 100 days using a coupled system of three nonlinear ODEs (Susceptible $S$, Infected $I$, Recovered $R$).
* **Assumptions:**
  1. Total population $N = S(t) + I(t) + R(t) = 10,000$ remains constant (no births, migration, or disease-induced mortality).
  2. Homogeneous mixing: every susceptible person has an equal probability of contacting an infected person.
  3. Recovered individuals gain permanent immunity over the 100-day simulation window.
* **Input Data:**
  * Initial state at $t = 0$: $S_0 = 9,990$, $I_0 = 10$, $R_0 = 0$.
  * Transmission rate $\beta = 0.35\text{ day}^{-1}$ and recovery rate $\gamma = 0.10\text{ day}^{-1}$ (basic reproduction number $R_0 = \beta/\gamma = 3.5$).
* **Output & Graph Interpretation:**
  * Active infections peak around Day 29 at approximately $3,558$ simultaneous cases ($35.6\%$ of the population), and by Day 100 roughly $9,658$ people have recovered while only $\approx 335$ remain susceptible.
  * On the plot, the susceptible curve ($S$) drops steeply during the exponential growth phase, the infected curve ($I$) forms a classic bell-shaped epidemic wave peaking when $S/N = \gamma/\beta$, and the recovered curve ($R$) rises monotonically to level off near $96.6\%$ of the population.