import numpy as np
import matplotlib.pyplot as plt

# Real-World Case: Web Page Authority / Academic Citation Influence Ranking (Directed Weighted Network)
# Five research papers (P1 to P5) citing one another.
# Entry M[i, j] = weight of citation influence passed from Paper j to Paper i.
# Using Google PageRank transition matrix with damping factor d = 0.85 to handle directed links.

papers = ["P1 (AI Survey)", "P2 (Core Algo)", "P3 (Dataset)", "P4 (App Study)", "P5 (Hardware)"]
N = len(papers)

# Raw citation matrix C[i, j] = 1 if Paper j cites Paper i
C = np.array([
    [0., 1., 1., 1., 0.],  # P1 is cited by P2, P3, P4
    [1., 0., 1., 1., 1.],  # P2 is cited by P1, P3, P4, P5
    [0., 1., 0., 1., 0.],  # P3 is cited by P2, P4
    [0., 0., 1., 0., 1.],  # P4 is cited by P3, P5
    [1., 0., 0., 0., 0.]   # P5 is cited by P1
])

# Column-normalize C to form stochastic transition matrix H
col_sums = C.sum(axis=0)
H = C / col_sums

# Apply PageRank damping factor d = 0.85: G = d*H + (1-d)/N * J
d = 0.85
G = d * H + ((1 - d) / N) * np.ones((N, N))

eigenvalues, eigenvectors = np.linalg.eig(G)
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
pagerank_scores = dominant_vector / dominant_vector.sum()

print("--- Task H: Real-World Case (Research Paper Citation Authority / PageRank) ---")
print(f"Dominant Eigenvalue of Google Matrix G: {dominant_value:.4f}")
print("Paper Influence Scores (PageRank):")
ranked = sorted(zip(papers, pagerank_scores), key=lambda x: x[1], reverse=True)
for rank, (paper, score) in enumerate(ranked, 1):
    print(f"  #{rank} {paper}: {score:.4f} ({score*100:.2f}%)")

v = np.real(eigenvectors[:, index])
print(f"Verification error ||Gv - lambda*v||: {np.linalg.norm(G @ v - dominant_value * v):.2e}")

plt.figure(figsize=(8.5, 4.5))
bars = plt.barh([r[0] for r in reversed(ranked)], [r[1] for r in reversed(ranked)], color='#8172B3')
plt.xlabel("Authority / PageRank Score")
plt.title("Task H (Real-World): Research Paper Citation Authority via Dominant Eigenvector")
plt.xlim(0, 0.40)
for bar in bars:
    w = bar.get_width()
    plt.text(w + 0.005, bar.get_y() + bar.get_height()/2, f"{w:.4f}", va='center')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("task_h_realworld_plot.png", dpi=150)
plt.close()
