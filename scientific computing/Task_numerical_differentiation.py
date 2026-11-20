import numpy as np
import matplotlib.pyplot as plt


# REQUIREMENT B: Baseline GPS Speed Estimation



time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0], dtype=float)

speed = np.zeros_like(position)


speed[0] = (position[1] - position[0]) / (time[1] - time[0])


for i in range(1, len(time) - 1):
    speed[i] = (position[i + 1] - position[i - 1]) / (time[i + 1] - time[i - 1])


speed[-1] = (position[-1] - position[-2]) / (time[-1] - time[-2])


#  REQUIREMENT D: Output Printing & Plot Generation 

print("--- Baseline GPS Speed Estimation ---")
for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed = {v:.2f} m/s")


plt.plot(time, speed, marker="o", color="tab:blue", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Estimated Speed (m/s)")
plt.title("Speed estimated from GPS position data")
plt.grid(True)
plt.savefig("images/speed_plot.png", dpi=300, bbox_inches='tight')
plt.show()


# REQUIREMENT C: Parameter Modification Analysis


def analyze_step_size(h_val):

    t_test = np.arange(0, 5 + h_val, h_val)
    pos_test = t_test**2 + 0.5 * t_test
    
   
    vel_test = np.gradient(pos_test, h_val)
    return t_test, vel_test


t_coarse, v_coarse = analyze_step_size(1.0)
t_fine, v_fine = analyze_step_size(0.1)

print("\n--- Step-Size Parameter Analysis ---")
print(f"Coarse points evaluated: {len(t_coarse)} | Values: {v_coarse}")
print(f"Fine points evaluated: {len(t_fine)} | First 5 Values: {v_fine[:5]}")