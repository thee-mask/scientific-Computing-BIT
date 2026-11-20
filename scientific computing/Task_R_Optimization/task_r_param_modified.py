import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Parameter Modifications:
# 1. Cost of Type A server reduced from $12 to $9 (bulk vendor discount)
# 2. Required minimum total capacity increased from 1000 to 1500 units

def cost_mod(z):
    x, y = z
    return 9 * x + 18 * y

def capacity_constraint_mod(z):
    x, y = z
    return 100 * x + 170 * y - 1500

constraints = {"type": "ineq", "fun": capacity_constraint_mod}
bounds = [(0, None), (0, None)]

solution = minimize(cost_mod, x0=[5, 5], method="SLSQP", bounds=bounds, constraints=constraints)
x_opt, y_opt = solution.x

print("--- Task R: Parameter Modification (Type A Cost=$9, Min Capacity=1500) ---")
print("Optimization success:", solution.success)
print(f"Continuous Type A allocation: {x_opt:.3f}")
print(f"Continuous Type B allocation: {y_opt:.3f}")
print(f"Total capacity achieved: {100*x_opt + 170*y_opt:.2f}")
print(f"Minimum continuous planning cost: ${solution.fun:.2f}")

best_integer = None
for a in range(0, 25):
    for b in range(0, 25):
        cap = 100 * a + 170 * b
        if cap >= 1500:
            c = 9 * a + 18 * b
            if best_integer is None or c < best_integer[0]:
                best_integer = (c, a, b, cap)

print(f"Best integer solution: Cost=${best_integer[0]}, Type A={best_integer[1]}, Type B={best_integer[2]}, Capacity={best_integer[3]}")

x_vals = np.linspace(0, 18, 200)
y_boundary = np.maximum(0, (1500 - 100 * x_vals) / 170)

plt.figure(figsize=(8, 5))
plt.fill_between(x_vals, y_boundary, 12, color='#55A868', alpha=0.2, label='New Feasible Region (Cap >= 1500)')
plt.plot(x_vals, y_boundary, 'g-', linewidth=2, label='New Boundary: 100x + 170y = 1500')
plt.scatter([x_opt], [y_opt], color='red', s=100, zorder=5, label=f'New Continuous Optimum ({x_opt:.1f}, {y_opt:.1f}) -> ${solution.fun:.2f}')
plt.scatter([best_integer[1]], [best_integer[2]], color='purple', marker='s', s=100, zorder=5, label=f'Best Integer ({best_integer[1]}, {best_integer[2]}) -> ${best_integer[0]}')
plt.xlim(0, 18)
plt.ylim(0, 11)
plt.xlabel("Type A Servers (x)")
plt.ylabel("Type B Servers (y)")
plt.title("Task R (Param Change): Shift from Type B to Type A After Price Drop")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("task_r_param_plot.png", dpi=150)
plt.close()
