import numpy as np


A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

b = np.array([100., 0., 0., 0., 20.])

def gauss_seidel_solver(A, b, tol, max_iter=500):
    """Gauss-Seidel solver tracking iterations for a specific tolerance."""
    x = np.zeros_like(b)
    for iteration in range(1, max_iter + 1):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        if error < tol:
            return x, iteration
    return x, max_iter

def jacobi_solver(A, b, tol, max_iter=500):
    """Jacobi solver tracking iterations for a specific tolerance."""
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


x_gs_strict, iter_gs_strict = gauss_seidel_solver(A, b, tol=1e-8)
x_gs_relaxed, iter_gs_relaxed = gauss_seidel_solver(A, b, tol=1e-3)

x_j_strict, iter_j_strict = jacobi_solver(A, b, tol=1e-8)
x_j_relaxed, iter_j_relaxed = jacobi_solver(A, b, tol=1e-3)


print("=" * 65)
print("     REQUIREMENT C: PARAMETER EXPERIMENTATION RESULTS")
print("=" * 65)
print(f"Strict Tolerance (1e-8):")
print(f"  - Gauss-Seidel Iterations : {iter_gs_strict}")
print(f"  - Jacobi Iterations       : {iter_j_strict}")
print(f"  - Computed Temperatures   : {x_gs_strict}\n")

print(f"Relaxed Tolerance (1e-3):")
print(f"  - Gauss-Seidel Iterations : {iter_gs_relaxed}")
print(f"  - Jacobi Iterations       : {iter_j_relaxed}")
print(f"  - Computed Temperatures   : {x_gs_relaxed}")
print("=" * 65)