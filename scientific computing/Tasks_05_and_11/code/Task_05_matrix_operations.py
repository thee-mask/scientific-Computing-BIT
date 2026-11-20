"""Task 5: apply a planar transformation to floor-plan coordinates.

Inputs: four floor-plan corners in metres, scale 1.2 and rotation 30 degrees.
Operation: matrix multiplication rotates and scales every point; determinant gives area scale.
Parameter change: rotate by 60 degrees and compare coordinates.
Run: python code/Task_05_matrix_operations.py
"""
import numpy as np

points = np.array([[0., 0.], [4., 0.], [4., 3.], [0., 3.]])
scale = 1.2

def transform(angle_degrees):
    angle = np.deg2rad(angle_degrees)
    rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    return rotation @ (scale * np.eye(2))

for angle in (30, 60):
    matrix = transform(angle)
    moved = points @ matrix.T
    print(f"\nRotation: {angle} degrees")
    print("Transformed corners (m):\n", np.round(moved, 3))
    print(f"Area scale (determinant): {np.linalg.det(matrix):.3f}")
