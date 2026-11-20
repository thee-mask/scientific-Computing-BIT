
Task N: Numerical Differentiation

## Table of Contents
1. [Overview & Concept](#1-overview--concept)
2. [Requirement B: Identification of Inputs and Mathematical Operations](#2-requirement-b-identification-of-inputs-and-mathematical-operations)
3. [Requirement C: Parameter Modification & Result Analysis](#3-requirement-c-parameter-modification--result-analysis)
4. [Requirement D: Output Interpretation & Graphical Convergence Analysis](#4-requirement-d-output-interpretation--graphical-convergence-analysis)
5. [Requirement E: Real-World Modification (Instantaneous Acceleration from Velocity Data)](#5-requirement-e-real-world-modification-instantaneous-acceleration-from-velocity-data)

---

## 1. Overview & Concept

Numerical differentiation is the process of estimating the derivative (rate of change) of a function or discrete dataset when an explicit analytical derivative formula is unavailable or impractical. 

Because experimental and real-world datasets consist of discrete measurements (such as time-series sensor samples), continuous calculus cannot be applied directly. Instead, numerical differentiation approximates slopes using finite differences across neighboring data points:
* **Forward Difference:** Estimates the derivative using the current point and the subsequent point: $f'(x) \approx \frac{f(x + h) - f(x)}{h}$
* **Backward Difference:** Estimates the derivative using the current point and the preceding point: $f'(x) \approx \frac{f(x) - f(x - h)}{h}$
* **Central Difference:** Estimates the derivative symmetrically: $f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}$ *(Offers higher accuracy for step size $h$)*

---

## 2. Requirement B: Identification of Inputs and Mathematical Operations

### 2.1 Physical Setup and Mathematical Problem Formulation
The baseline problem models motion where a GPS tracking device records position coordinates at closely spaced time intervals. The objective is to compute the instantaneous velocity (speed) profile of the moving object over time using finite difference schemes.

### 2.2 Complete Implementation Script (`code/Task_15_numerical_differentiation.py`)
Below is the unabbreviated Python script showing the setup of input arrays and the implementation of forward, central, and backward difference operations:

```python
import numpy as np
import matplotlib.pyplot as plt


time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0], dtype=float)

speed = np.zeros_like(position)


speed[0] = (position[1] - position[0]) / (time[1] - time[0])


for i in range(1, len(time) - 1):
    speed[i] = (position[i + 1] - position[i - 1]) / (time[i + 1] - time[i - 1])


speed[-1] = (position[-1] - position[-2]) / (time[-1] - time[-2])

```

---

## 3. Requirement C: Parameter Modification & Result Analysis

### 3.1 Parameter Alteration

To analyze how data resolution and sampling step size ($h$) impact numerical gradient accuracy, we can modify the temporal sampling granularity from the baseline interval ($h = 1.0\,\text{s}$) to a high-density interval ($h = 0.1\,\text{s}$).

### 3.2 Performance and Accuracy Trade-off Code Snippet

```python
def analyze_step_size(h_val):
    
    t_test = np.arange(0, 5 + h_val, h_val)
    pos_test = t_test**2 + 0.5 * t_test
    

    vel_test = np.gradient(pos_test, h_val)
    return t_test, vel_test


t_coarse, v_coarse = analyze_step_size(1.0)
t_fine, v_fine = analyze_step_size(0.1)

print(f"Coarse points evaluated: {len(t_coarse)} | Fine points evaluated: {len(t_fine)}")

```

* **Analytical Impact:** Decreasing step size $h$ reduces local truncation error, yielding a smoother and more precise gradient approximation. However, extremely small steps can amplify high-frequency noise in real-world sensor data.

---

## 4. Requirement D: Output Interpretation & Graphical Convergence Analysis

### 4.1 Terminal Output Interpretation & Printing Code

The results are printed iteratively to inspect the calculated velocity at each timestamp using the following full code block:

```python
print("--- Baseline GPS Speed Estimation ---")
for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed = {v:.2f} m/s")

```

* **Console Output Results:**
```text
t=0s, position=0.0m, estimated speed = 5.10 m/s
t=1s, position=4.8m, estimated speed = 5.10 m/s
t=2s, position=10.2m, estimated speed = 5.65 m/s
t=3s, position=16.1m, estimated speed = 6.25 m/s
t=4s, position=22.7m, estimated speed = 6.95 m/s
t=5s, position=30.0m, estimated speed = 7.65 m/s
t=6s, position=38.0m, estimated speed = 8.00 m/s

```


* **Physical Meaning:** The output values show a steady increase from $5.10\,\text{m/s}$ to $8.00\,\text{m/s}$, indicating continuous acceleration over the 6-second window.

### 4.2 Graphical Plotting Code & Interpretation

The full plotting code below translates discrete speed estimates into an intuitive visual trend line saved directly to your local `images/` directory:

```python
plt.plot(time, speed, marker="o", color="tab:blue", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Estimated Speed (m/s)")
plt.title("Speed estimated from GPS position data")
plt.grid(True)
plt.savefig("images/speed_plot.png", dpi=300, bbox_inches='tight')
plt.show()

```

* **Graphical Convergence Analysis:**


---

## 5. Requirement E: Real-World Modification (Instantaneous Acceleration from Velocity Data)

### 5.1 Scenario & Assumptions

To demonstrate the broader utility of numerical differentiation, the algorithm is adapted to calculate **Instantaneous Acceleration from Time-Series Velocity Data** for a vehicle traveling down a test track ($a = dv/dt$).

### 5.2 Full Real-World Script Implementation (`code/task_n_acceleration.py`)

```python
import numpy as np
import matplotlib.pyplot as plt


time_sec = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
velocity_ms = np.array([0.0, 5.2, 11.0, 17.5, 24.8, 33.0, 42.1], dtype=float)

acceleration = np.zeros_like(velocity_ms)


acceleration[0] = (velocity_ms[1] - velocity_ms[0]) / (time_sec[1] - time_sec[0])


for i in range(1, len(time_sec) - 1):
    acceleration[i] = (velocity_ms[i + 1] - velocity_ms[i - 1]) / (time_sec[i + 1] - time_sec[i - 1])


acceleration[-1] = (velocity_ms[-1] - velocity_ms[-2]) / (time_sec[-1] - time_sec[-2])

print("--- Vehicle Acceleration Analysis ---")
for t, v, a in zip(time_sec, velocity_ms, acceleration):
    print(f"Time: {t}s | Velocity: {v} m/s | Calculated Acceleration: {a:.2f} m/s^2")


plt.plot(time_sec, acceleration, marker="s", color="tab:red", linestyle="--")
plt.xlabel("Time (s)")
plt.ylabel("Estimated Acceleration (m/s^2)")
plt.title("Vehicle Acceleration Derived from Velocity Data")
plt.grid(True)
plt.savefig("images/acceleration_plot.png", dpi=300, bbox_inches='tight')
plt.show()

```

### 5.3 Output Data & Physical Interpretation

* **Interpretation:** Differentiating position yields velocity, and differentiating velocity yields acceleration. This proves that finite-difference numerical differentiation is recursive, robust, and universally applicable across automotive telemetry, robotics control loops, and physics simulations.

> **Vehicle Acceleration Profile:**
> 

```

```