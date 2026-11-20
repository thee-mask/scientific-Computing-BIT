import numpy as np

# Three-loop DC circuit mesh analysis using Kirchhoff's Voltage Law (R * I = V)
# Unknowns: I1, I2, I3 (mesh currents in Amperes)
R = np.array([
    [10.0, -2.0, -3.0],
    [-2.0, 12.0, -4.0],
    [-3.0, -4.0, 15.0]
])

# Independent voltage sources in each loop (Volts)
V = np.array([24.0, 0.0, 12.0])

currents = np.linalg.solve(R, V)
residual = V - R @ currents

for idx, current in enumerate(currents, start=1):
    print(f"Loop {idx} current (I{idx}): {current:.4f} A")

print("Verification R @ I:", np.round(R @ currents, 6))
print(f"Residual norm: {np.linalg.norm(residual):.3e}")