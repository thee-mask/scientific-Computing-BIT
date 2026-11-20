import numpy as np

def run_circuit_simulation():
    """
    Requirement E: Nodal Voltage Analysis for an Electrical Resistor Circuit
    """

    A_circuit = np.array([
        [ 2., -1.,  0.,  0.,  0.],
        [-1.,  2., -1.,  0.,  0.],
        [ 0., -1.,  2., -1.,  0.],
        [ 0.,  0., -1.,  2., -1.],
        [ 0.,  0.,  0., -1.,  2.]
    ])


    b_circuit = np.array([12.0, 0.0, 0.0, 0.0, 0.0])

   
    def gauss_seidel_circuit(A, b, tol=1e-8, max_iter=500):
        x = np.zeros_like(b)
        for iteration in range(1, max_iter + 1):
            old = x.copy()
            for i in range(len(b)):
                x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
            
            error = np.linalg.norm(x - old, ord=np.inf)
            if error < tol:
                return x, iteration
        return x, max_iter


    def jacobi_circuit(A, b, tol=1e-8, max_iter=500):
        D = np.diag(A)
        R = A - np.diagflat(D)
        x = np.zeros_like(b)
        for iteration in range(1, max_iter + 1):
            x_new = (b - R @ x) / D
            error = np.linalg.norm(x_new - x, ord=np.inf)
            if error < tol:
                return x_new, iteration
            x = x_new
        return x, max_iter


    v_gs, iters_gs = gauss_seidel_circuit(A_circuit, b_circuit)
    v_j, iters_j   = jacobi_circuit(A_circuit, b_circuit)
    v_exact        = np.linalg.solve(A_circuit, b_circuit)

   
    print("=" * 60)
    print("     REQUIREMENT E: ELECTRICAL RESISTOR CIRCUIT SIMULATION")
    print("=" * 60)
    print("Node Potentials (Gauss-Seidel Method):")
    for idx, v in enumerate(v_gs, start=1):
        print(f"  Node V{idx} : {v:8.4f} V")
    
    print("\nSolver Performance Summary:")
    print(f"  - Gauss-Seidel Iterations : {iters_gs}")
    print(f"  - Jacobi Iterations       : {iters_j}")
    print("  - Direct Solution Check   :", np.round(v_exact, 4))
    print("=" * 60)

if __name__ == "__main__":
    run_circuit_simulation()