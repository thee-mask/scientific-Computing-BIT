import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Real-World Case: Agricultural Fertilizer Blend Cost Minimization (Kiambu County Farm)
# Mix three commercial fertilizers (kg) to meet minimum soil nutrient requirements per hectare:
#   x1 = Urea (46% Nitrogen, 0% Phosphorus, 0% Potassium)      - Cost: KES 75/kg
#   x2 = DAP  (18% Nitrogen, 46% Phosphorus, 0% Potassium)     - Cost: KES 95/kg
#   x3 = NPK 17:17:17 (17% N, 17% P, 17% K)                    - Cost: KES 88/kg
#
# Minimum Nutrient Requirements per Hectare:
#   Nitrogen (N)   >= 90 kg
#   Phosphorus (P) >= 60 kg
#   Potassium (K)  >= 30 kg
# Additional operational constraint: Total fertilizer weight <= 450 kg/ha

def total_cost(x):
    return 75 * x[0] + 95 * x[1] + 88 * x[2]

constraints = [
    {"type": "ineq", "fun": lambda x: 0.46*x[0] + 0.18*x[1] + 0.17*x[2] - 90.0},  # Nitrogen >= 90
    {"type": "ineq", "fun": lambda x: 0.00*x[0] + 0.46*x[1] + 0.17*x[2] - 60.0},  # Phosphorus >= 60
    {"type": "ineq", "fun": lambda x: 0.00*x[0] + 0.00*x[1] + 0.17*x[2] - 30.0},  # Potassium >= 30
    {"type": "ineq", "fun": lambda x: 450.0 - (x[0] + x[1] + x[2])}               # Max weight <= 450
]

bounds = [(0, None), (0, None), (0, None)]
x0 = [100.0, 100.0, 200.0]

res = minimize(total_cost, x0=x0, method="SLSQP", bounds=bounds, constraints=constraints)
x1, x2, x3 = res.x

N_supplied = 0.46*x1 + 0.18*x2 + 0.17*x3
P_supplied = 0.46*x2 + 0.17*x3
K_supplied = 0.17*x3

print("--- Task R: Real-World Case (Agricultural Fertilizer Blend Optimization) ---")
print("Optimization success:", res.success)
print(f"Optimal Urea (x1):         {x1:.2f} kg (Cost: KES {75*x1:,.2f})")
print(f"Optimal DAP (x2):          {x2:.2f} kg (Cost: KES {95*x2:,.2f})")
print(f"Optimal NPK 17:17:17 (x3): {x3:.2f} kg (Cost: KES {88*x3:,.2f})")
print(f"Total Fertilizer Weight:   {x1+x2+x3:.2f} kg")
print(f"Minimum Total Cost:        KES {res.fun:,.2f} per hectare")
print(f"Nutrients Supplied -> N: {N_supplied:.2f} kg (min 90), P: {P_supplied:.2f} kg (min 60), K: {K_supplied:.2f} kg (min 30)")

# Visualization: Optimal Blend & Nutrient Verification
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

labels = ['Urea (46-0-0)', 'DAP (18-46-0)', 'NPK (17-17-17)']
weights = [x1, x2, x3]
colors = ['#4C72B0', '#DD8452', '#55A868']
bars1 = ax1.bar(labels, weights, color=colors)
ax1.set_title("Optimal Fertilizer Mix (kg/hectare)")
ax1.set_ylabel("Quantity (kg)")
ax1.set_ylim(0, max(weights)*1.25)
for b in bars1:
    ax1.text(b.get_x() + b.get_width()/2, b.get_height() + 3, f"{b.get_height():.2f} kg", ha='center')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

nutrients = ['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)']
required = [90, 60, 30]
supplied = [N_supplied, P_supplied, K_supplied]
x_idx = np.arange(len(nutrients))
w = 0.35
ax2.bar(x_idx - w/2, required, w, label='Minimum Required (kg)', color='#C44E52')
ax2.bar(x_idx + w/2, supplied, w, label='Supplied by Blend (kg)', color='#8172B3')
ax2.set_xticks(x_idx)
ax2.set_xticklabels(nutrients)
ax2.set_title("Soil Nutrient Requirement vs. Supplied")
ax2.set_ylabel("Nutrient Mass (kg)")
ax2.set_ylim(0, 115)
ax2.legend()
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("task_r_realworld_plot.png", dpi=150)
plt.close()
