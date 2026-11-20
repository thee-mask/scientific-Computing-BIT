import numpy as np
import matplotlib.pyplot as plt

# Original vs Modified Adjacency Matrix
# Modification: Add direct connection between Node A and Node D (A[0,3]=1, A[3,0]=1)
# This turns the graph into a complete K4 graph where every node connects to every other node.
A_mod = np.array([
    [0., 1., 1., 1.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [1., 1., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A_mod)
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]
print("--- Task H: Parameter Modification (Added A-D Link) ---")
print(f"All Eigenvalues: {np.round(np.real(eigenvalues), 4)}")
print(f"New Dominant Eigenvalue: {dominant_value:.4f} (Increased from 2.5616)")
print("New Eigenvector-based importance:")
for node, score in zip(nodes, centrality):
    print(f"  Node {node}: {score:.4f} ({score*100:.2f}%)")

# Comparison Plot
base_centrality = [0.2192, 0.2808, 0.2808, 0.2192]
x = np.arange(len(nodes))
width = 0.35

plt.figure(figsize=(8, 4.5))
plt.bar(x - width/2, base_centrality, width, label='Base Network (No A-D link)', color='#4C72B0')
plt.bar(x + width/2, centrality, width, label='Modified Network (With A-D link)', color='#55A868')
plt.xticks(x, nodes)
plt.ylabel("Normalized Centrality Score")
plt.title("Task H (Param Change): Impact of Adding Link A-D on Node Importance")
plt.ylim(0, 0.35)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("task_h_param_plot.png", dpi=150)
plt.close()
