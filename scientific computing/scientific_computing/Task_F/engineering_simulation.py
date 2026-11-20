
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Conductance matrix for a simplified three-node circuit
# Conductance is measured in millisiemens (mS)
G = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])

# Current inputs for two operating conditions, in milliamperes (mA)
current_conditions = [
    np.array([15.0, 10.0, 10.0]),
    np.array([20.0, 10.0, 10.0])
]

# Perform LU factorization once
lu, piv = lu_factor(G)

print("Engineering Simulation: Three-Node Electrical Circuit")
print("----------------------------------------------------")

for i, current in enumerate(current_conditions, start=1):
    # Solve G V = I to calculate node voltages
    voltage = lu_solve((lu, piv), current)

    # Calculate the residual
    residual = G @ voltage - current
    residual_norm = np.linalg.norm(residual)

    print(f"\nOperating condition {i}")
    print("Current inputs (mA):", current)
    print("Calculated node voltages (V):", np.round(voltage, 4))
    print(f"Residual norm: {residual_norm:.6f}")
