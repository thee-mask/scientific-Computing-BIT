# Task F: Gaussian Elimination and LU Decomposition

## 1. Purpose of the Program

The purpose of the program is to demonstrate how Gaussian elimination and LU decomposition can be used to solve systems of linear equations. The program uses NumPy and SciPy to calculate solutions for different measurement sets and evaluates the accuracy of the solutions using the residual norm.

## 2. Input Values

The program uses a coefficient matrix representing a system of linear equations and three measurement vectors. The coefficient matrix describes the relationships between the unknown variables, while each measurement vector provides the values on the right-hand side of the equations.

## 3. Operations Performed

The program performs the following operations:

- Defines the coefficient matrix and measurement vectors.
- Uses LU decomposition to factor the coefficient matrix.
- Solves the systems of equations for the different measurement sets.
- Calculates the residual norm to assess how closely the calculated solutions satisfy the equations.
- Compares the LU-based solution with the direct solution.

## 4. Modification of an Input Parameter

In the original program, the first coefficient of the matrix was 4.0. I changed this value to 10.0 while keeping the other matrix coefficients unchanged.

## 5. Results and Observations

After running the modified program, I observed that the calculated solution values changed. The residual norm remained 0.0 at the displayed numerical precision.

## 6. Interpretation

Changing a coefficient in the matrix changes the system of linear equations being solved. As a result, the calculated values of the unknown variables may change for the different measurement sets.

The residual norm remaining at 0.0 indicates that the computed solutions satisfy the modified system to the displayed numerical precision.

## 7. Conclusion

The experiment demonstrates that LU decomposition can be used to solve systems of linear equations efficiently. It also shows that changing the coefficient matrix affects the calculated solutions, while the residual norm can be used to assess the accuracy of the computed results.
## 8. Related Real-World Application: Engineering Simulation

### Problem Description
The original program was adapted to simulate a simplified three-node electrical circuit. The purpose is to calculate the voltage at each node under different current-input conditions using a system of linear equations.

### Assumptions
- The circuit is represented by a linear conductance matrix.
- The conductance matrix and current inputs are assumed values for an educational simulation.
- The circuit conditions remain constant during each calculation.
- The model does not include nonlinear components or time-dependent behaviour.

### Input Data
The program uses a three-by-three conductance matrix and two current-input vectors: [15.0, 10.0, 10.0] mA and [20.0, 10.0, 10.0] mA.

### Operations Performed
The program uses SciPy to perform LU factorization of the conductance matrix. It then solves the system of linear equations for each current-input condition to calculate the node voltages. The residual norm is calculated to assess how closely the computed solution satisfies the equations.

### Output and Interpretation
The program displays the calculated node voltages for both operating conditions. Changing the current input changes the calculated voltages. A residual norm close to zero indicates that the computed voltages satisfy the mathematical model to numerical precision.

### Conclusion
The engineering simulation demonstrates how LU decomposition can be applied to solve systems of linear equations in electrical engineering. It shows how a mathematical model can be used to estimate circuit behaviour under different input conditions.
## 9. Engineering Simulation Results and Interpretation

### Results

The engineering simulation ran successfully and produced calculated node voltages for two operating conditions.

- **Operating condition 1:** The current inputs were [15.0, 10.0, 10.0] mA. The calculated node voltages were approximately [5.0, 5.0, 5.0] V, and the residual norm was 0.0.
- **Operating condition 2:** The current inputs were [20.0, 10.0, 10.0] mA. The calculated node voltages changed in response to the modified current input, and the residual norm was 0.0.

### Interpretation

The results demonstrate that changing the current input affects the calculated node voltages in the simulated electrical circuit. The residual norm of 0.0 indicates that the computed solutions satisfy the mathematical model to the displayed numerical precision.

The simulation illustrates how LU decomposition can be used to solve systems of linear equations in engineering applications. By factoring the conductance matrix once, the program can efficiently solve the system for multiple operating conditions.

### Conclusion

The engineering simulation successfully demonstrates the application of numerical methods to a simplified electrical circuit. It shows how scientific computing can be used to calculate unknown values and analyse the effect of changing input conditions.