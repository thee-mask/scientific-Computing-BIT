# Task E: Solution of Systems of Linear Equations (`Task_06_linear_systems.py`)

## B. Input Values and Mathematical Operations
* **Inputs:**
  * Coefficient matrix $A = \begin{bmatrix} 4.0 & 2.0 \\ 8.0 & 12.0 \end{bmatrix}$ representing per-server resource consumption (Row 1: CPU units; Row 2: Memory in GB for Type A and Type B servers).
  * Constant vector $b = \begin{bmatrix} 20.0 \\ 72.0 \end{bmatrix}$ representing total observed CPU units and memory usage.
* **Mathematical Operations:**
  * Solves the linear system $Ax = b$ via LU factorization with partial pivoting using `np.linalg.solve(A, b)` to find the unknown server count vector $x = [x_1, x_2]^T$.
  * Computes the residual vector $r = b - Ax$ and its Euclidean ($L_2$) norm $\|r\|_2 = \sqrt{r_1^2 + r_2^2}$ using `np.linalg.norm(residual)` to verify numerical accuracy.

## C. Parameter Modification and Impact
* **Change Made:** Increased total observed CPU usage in vector $b$ from `20.0` to `28.0` while keeping total memory usage at `72.0` GB ($b_{\text{new}} = [28.0, 72.0]^T$).
* **Result Change:** The solution shifts from `[3, 4]` (3 Type A, 4 Type B) to `[6, 2]` (6 Type A, 2 Type B).
* **Explanation:** Type A servers are CPU-intensive (4 CPU, 8 GB RAM), whereas Type B servers are memory-intensive (2 CPU, 12 GB RAM). Raising total CPU demand without increasing memory forces the linear system to reallocate capacity toward more Type A servers and fewer Type B servers so both equations remain satisfied simultaneously.

## D. Output Interpretation
* **Numerical Output:** `Type A servers: 3`, `Type B servers: 4`, `Verification A @ solution: [20. 72.]`, `Residual norm: 0.0`.
* **Meaning:** Exactly 3 active Type A servers and 4 active Type B servers account for the entire 20 CPU units and 72 GB of memory in use. A residual norm of `0.0` confirms an exact solution with zero floating-point discrepancy. (No graph is generated for this task.)

## E. Modified Real-World Case: DC Electrical Circuit Mesh Analysis
* **Problem Statement:** Determine the steady-state loop currents ($I_1, I_2, I_3$ in Amperes) in a three-loop resistive DC circuit powered by two voltage sources ($24\text{ V}$ in Loop 1 and $12\text{ V}$ in Loop 3) using Kirchhoff's Voltage Law (KVL).
* **Assumptions:**
  1. All resistors are linear and ohmic with constant resistance values at room temperature.
  2. Voltage sources are ideal (zero internal resistance).
  3. Mesh currents $I_1, I_2, I_3$ are defined clockwise in each loop.
* **Input Data:**
  * Mesh equations:
    $$10I_1 - 2I_2 - 3I_3 = 24$$
    $$-2I_1 + 12I_2 - 4I_3 = 0$$
    $$-3I_1 - 4I_2 + 15I_3 = 12$$
* **Output & Interpretation:**
  * Solving yields $I_1 \approx 3.1348\text{ A}$, $I_2 \approx 1.0955\text{ A}$, and $I_3 \approx 1.7191\text{ A}$, with a residual norm on the order of $10^{-15}$.
  * Loop 1 carries the highest current ($3.13\text{ A}$) because it is directly driven by the $24\text{ V}$ supply, while Loop 2 carries a positive current ($1.10\text{ A}$) induced purely through shared resistors ($2\ \Omega$ and $4\ \Omega$) despite having no independent voltage source.