import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# x = units of Type A server (Cost = 12, Capacity = 100)
# y = units of Type B server (Cost = 18, Capacity = 170)
# Constraint: 100*x + 170*y >= 1000, x >= 0, y >= 0

def cost(z):
    x, y = z
    return 12 * x + 18 * y

def capacity_constraint(z):
    x, y = z
    return 100 * x + 170 * y - 1000

constraints = {"type": "ineq", "fun": capacity_constraint}
bounds = [(0, None), (0, None)]

solution = minimize(cost, x0=[5, 3], method="SLSQP", bounds=bounds, constraints=constraints)
x_opt, y_opt = solution.x

print("--- Task R: Base Cloud Server Optimization ---")
print("Optimization success:", solution.success)
print(f"Continuous Type A allocation: {x_opt:.3f}")
print(f"Continuous Type B allocation: {y_opt:.3f}")
print(f"Total capacity achieved: {100*x_opt + 170*y_opt:.2f}")
print(f"Minimum continuous planning cost: ${solution.fun:.2f}")

# Integer search for whole servers
best_integer = None
for a in range(0, 20):
    for b in range(0, 20):
        cap = 100 * a + 170 * b
        if cap >= 1000:
            c = 12 * a + 18 * b
            if best_integer is None or c < best_integer[0]:
                best_integer = (c, a, b, cap)

print(f"Best integer solution: Cost=${best_integer[0]}, Type A={best_integer[1]}, Type B={best_integer[2]}, Capacity={best_integer[3]}")

# Feasible region visualization
x_vals = np.linspace(0, 12, 200)
y_boundary = np.maximum(0, (1000 - 100 * x_vals) / 170)

plt.figure(figsize=(8, 5))
plt.fill_between(x_vals, y_boundary, 10, color='#4C72B0', alpha=0.2, label='Feasible Region (Cap >= 1000)')
plt.plot(x_vals, y_boundary, 'b-', linewidth=2, label='Capacity Boundary: 100x + 170y = 1000')
plt.scatter([x_opt], [y_opt], color='red', s=100, zorder=5, label=f'Continuous Optimum ({x_opt:.2f}, {y_opt:.2f}) -> ${solution.fun:.2f}')
plt.scatter([best_integer[1]], [best_integer[2]], color='green', marker='s', s=100, zorder=5, label=f'Best Integer ({best_integer[1]}, {best_integer[2]}) -> ${best_integer[0]}')
plt.xlim(0, 12)
plt.ylim(0, 8)
plt.xlabel("Type A Servers (x)")
plt.ylabel("Type B Servers (y)")
plt.title("Task R (Base): Feasible Region and Optimal Cloud Server Allocation")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("task_r_base_plot.png", dpi=150)
plt.close()
