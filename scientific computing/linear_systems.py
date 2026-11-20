import os
import numpy as np
import matplotlib.pyplot as plt


A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])


b = np.array([100., 0., 0., 0., 20.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (
                b[i] 
                - A[i, :i] @ x[:i] 
                - A[i, i+1:] @ old[i+1:]
            ) / A[i, i]
            
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
            
    return x, errors

 
x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)


print("--- TASK G RESULTS ---")
print("Jacobi temperatures:", x_j)
print("Gauss-Seidel temperatures:", x_gs)
print("Direct solution:", x_exact)


os.makedirs("images", exist_ok=True)


plt.figure(figsize=(8, 5), dpi=300)
plt.semilogy(err_j, label="Jacobi Method", color="#e74c3c", linewidth=2.0, linestyle="--")
plt.semilogy(err_gs, label="Gauss-Seidel Method", color="#2980b9", linewidth=2.0, linestyle="-")
plt.xlabel("Iteration Count ($k$)", fontsize=11, fontweight='bold', labelpad=8)
plt.ylabel(r"Maximum Absolute Change ($\log$ scale)", fontsize=11, fontweight='bold', labelpad=8)
plt.title("Convergence Rate Comparison: Jacobi vs. Gauss-Seidel", fontsize=12, fontweight='bold', pad=15)
plt.legend(fontsize=10, loc='upper right', frameon=True, facecolor='#f8f9fa', edgecolor='#bdc3c7')
plt.grid(True, which="both", linestyle=":", linewidth=0.8, color="#bdc3c7")


plt.tight_layout()


plt.savefig("images/convergence_plot.png", dpi=300, bbox_inches='tight')
print("\n[SUCCESS] Graph plot automatically saved to images/convergence_plot.png")

plt.show()