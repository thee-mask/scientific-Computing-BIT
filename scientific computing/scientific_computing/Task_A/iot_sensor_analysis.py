
import numpy as np

# Simulated temperature readings from an IoT sensor
# Readings are collected every hour in degrees Celsius
sensor_readings = np.array([
    22.4, 23.1, 22.8, 24.0, 25.2, 26.1, 27.3,
    28.0, 27.6, 26.8, 25.9, 24.7
])

# Calculate sensor reading statistics
mean_reading = np.mean(sensor_readings)
minimum_reading = np.min(sensor_readings)
maximum_reading = np.max(sensor_readings)

# Convert Celsius readings to Fahrenheit
fahrenheit_readings = (1.8 * sensor_readings) + 32

# Display results
print("IoT Sensor Reading Analysis")
print("---------------------------")
print("Sensor readings (Celsius):", sensor_readings)
print(f"Mean temperature: {mean_reading:.2f} C")
print(f"Minimum temperature: {minimum_reading:.2f} C")
print(f"Maximum temperature: {maximum_reading:.2f} C")
print("First six Fahrenheit readings:",
      fahrenheit_readings[:6])
