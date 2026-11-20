import numpy as np
import matplotlib.pyplot as plt

# Adjacency matrix for a small undirected network (Nodes: A, B, C, D)
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Dominant eigenvalue/eigenvector
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]
print("--- Task H: Base Network Centrality ---")
print(f"All Eigenvalues: {np.round(np.real(eigenvalues), 4)}")
print(f"Dominant Eigenvalue: {dominant_value:.4f}")
print("Eigenvector-based importance (Normalized Centrality):")
for node, score in zip(nodes, centrality):
    print(f"  Node {node}: {score:.4f} ({score*100:.2f}%)")

# Verify Av = lambda*v
v = np.real(eigenvectors[:, index])
print(f"Verification error ||Av - lambda*v||: {np.linalg.norm(A @ v - dominant_value * v):.2e}")

# Visualization
plt.figure(figsize=(7, 4))
bars = plt.bar(nodes, centrality, color=['#4C72B0', '#DD8452', '#DD8452', '#4C72B0'])
plt.title("Task H (Base): Eigenvector Centrality of Network Nodes")
plt.xlabel("Network Node")
plt.ylabel("Normalized Importance Score")
plt.ylim(0, 0.4)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f"{yval:.4f}", ha='center', va='bottom')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("task_h_base_plot.png", dpi=150)
plt.close()
