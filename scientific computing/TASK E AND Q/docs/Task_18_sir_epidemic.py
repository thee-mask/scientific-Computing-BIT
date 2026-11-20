import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# SIR Epidemic Model parameters
N = 10_000.0        # Total closed population
beta = 0.35         # Transmission rate (per day)
gamma = 0.10        # Recovery rate (per day -> 10-day average infectious period)

# Initial counts: [Susceptible, Infected, Recovered]
y0 = [9990.0, 10.0, 0.0]

def sir_model(t, y):
    S, I, R = y
    dS_dt = -beta * S * I / N
    dI_dt = (beta * S * I / N) - gamma * I
    dR_dt = gamma * I
    return [dS_dt, dI_dt, dR_dt]

t_eval = np.linspace(0, 100, 400)
solution = solve_ivp(
    sir_model,
    (0, 100),
    y0,
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

S, I, R = solution.y
peak_idx = np.argmax(I)

print("Solver success:", solution.success)
print(f"Peak infections: {I[peak_idx]:.0f} people on Day {solution.t[peak_idx]:.1f}")
print(f"Day 100 totals -> Susceptible: {S[-1]:.0f}, Infected: {I[-1]:.0f}, Recovered: {R[-1]:.0f}")

plt.figure(figsize=(8, 5))
plt.plot(solution.t, S, label="Susceptible (S)")
plt.plot(solution.t, I, label="Infected (I)")
plt.plot(solution.t, R, label="Recovered (R)")
plt.xlabel("Time (days)")
plt.ylabel("Number of individuals")
plt.title("SIR Epidemic Dynamics (N = 10,000, R0 = 3.5)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/Task_18_sir_epidemic.png", dpi=150)
plt.show()