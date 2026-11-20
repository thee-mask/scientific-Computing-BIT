# Task 5: Matrix Algebra and Matrix Operations (`Task_05_matrix_operations.py`)

## B. Input Values and Mathematical Operations

- **Inputs:** Four rectangular floor-plan corners in metres: (0,0), (4,0), (4,3), and (0,3). The plan is uniformly scaled by 1.2 and rotated counterclockwise by 30 degrees.
- **Mathematical operations:** The program forms a 2-by-2 rotation matrix, multiplies it by the scale matrix, then applies the combined transformation to every point using matrix multiplication. The determinant gives the area scale.

## C. Parameter Modification and Impact

- **Change made:** The rotation is increased from 30 degrees to 60 degrees.
- **Result change:** Coordinates change orientation, while the determinant remains 1.44.
- **Explanation:** Rotation moves the corners around the origin but does not change area. Scaling both coordinate directions by 1.2 multiplies area by 1.2 x 1.2 = 1.44.

## D. Output Interpretation

- **Numerical output:** At 30 degrees the transformed non-origin corners are approximately (4.157, 2.400), (2.357, 5.518), and (-1.800, 3.118) metres. At 60 degrees they are approximately (2.400, 4.157), (-0.718, 5.957), and (-3.118, 1.800) metres. The determinant is 1.440 in both cases.
- **Meaning:** The transformed coordinates describe the revised floor-plan position. Its area is 1.44 times its original area. The negative x values simply mean some corners now lie to the left of the coordinate origin.
- **Graph:** No graph is generated for this task.

## E. Modified Real-World Case: Rotating and Scaling a Room Plan

- **Problem statement:** Transform a rectangular room plan to represent a scaled drawing rotated to a new orientation.
- **Assumptions:** Coordinates are measured in metres; the plan is flat and two-dimensional; all points receive the same scale and rotation; measurements and transformation parameters are treated as exact.
- **Input data:** Corners (0,0), (4,0), (4,3), (0,3); scale 1.2; rotations 30 and 60 degrees.
- **Output:** The script prints transformed corner coordinates and the determinant for each rotation.
- **Interpretation:** Rotation changes the direction of the room in the coordinate plane. The scale increases lengths by 20 percent and area by 44 percent. The model does not include perspective, translation, or measurement uncertainty.

## F. Individual Repository Note

Keep the Python file and this documentation in your own repository. Run the script from the repository root with `python code/Task_05_matrix_operations.py`, then include your observed output in your submission.
