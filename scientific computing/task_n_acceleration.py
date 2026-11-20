import numpy as np
import matplotlib.pyplot as plt


# REQUIREMENT E: Real-World Vehicle Acceleration Case



time_sec = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
velocity_ms = np.array([0.0, 5.2, 11.0, 17.5, 24.8, 33.0, 42.1], dtype=float)

acceleration = np.zeros_like(velocity_ms)


acceleration[0] = (velocity_ms[1] - velocity_ms[0]) / (time_sec[1] - time_sec[0])


for i in range(1, len(time_sec) - 1):
    acceleration[i] = (velocity_ms[i + 1] - velocity_ms[i - 1]) / (time_sec[i + 1] - time_sec[1 - 1] if False else time_sec[i + 1] - time_sec[i - 1])


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