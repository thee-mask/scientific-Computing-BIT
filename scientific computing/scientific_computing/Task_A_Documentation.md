# Task A: NumPy Arrays and Numerical Computation

## 1. Purpose of the Program

The purpose of this program is to demonstrate how NumPy can be used to perform numerical computations on an array of temperature readings. The program calculates the mean, minimum and maximum temperatures and converts the temperatures from Celsius to Fahrenheit.

## 2. Input Values

The program uses an array containing 24 hourly temperature readings in degrees Celsius. The readings are stored using a NumPy array.

## 3. Mathematical Operations

The program performs the following operations:

- Calculates the mean temperature.
- Identifies the minimum temperature.
- Identifies the maximum temperature.
- Converts Celsius temperatures to Fahrenheit using the formula:

  F = (1.8 × C) + 32

  where C represents temperature in Celsius and F represents temperature in Fahrenheit.

## 4. Modification of an Input Value

In the original program, the seventh temperature reading was 21.5°C. We changed this value to 31.5°C while keeping the other readings unchanged.

## 5. Results and Observations

After running the modified program, I observed the following changes:

- The mean temperature increased because one of the readings increased by 10°C.
- The minimum temperature remained unchanged because another reading was still lower.
- The maximum temperature changed to 31.5°C because the modified reading became the highest value.
- The first six Fahrenheit readings remained unchanged because the modified reading was the seventh value, which was not included in the first-six output.

## 6. Interpretation

The experiment demonstrates that changing an input value affects the results of numerical computations. The mean, minimum and maximum functions respond to the values contained in the array. The Fahrenheit conversion also demonstrates how mathematical formulas can be applied to array data using NumPy.

The experiment further shows that the program can display selected elements of an array without displaying all the readings.

## 7. Conclusion

The program successfully demonstrates the use of NumPy arrays for storing temperature readings and performing basic numerical calculations. Changing one temperature value helped me understand how input data affects the program's output.
## 8. Related Real-World Application: IoT Sensor Reading Analysis

### Problem Description
The original program was modified to analyse temperature readings collected by an Internet of Things (IoT) temperature sensor. Such sensors can be used in smart homes to monitor indoor environmental conditions.

### Assumptions
- The program uses 12 simulated temperature readings.
- Each reading represents a measurement collected at hourly intervals.
- Temperatures are measured in degrees Celsius.
- The readings are sample data and are not collected from a physical IoT device.

### Input Data
The program receives an array containing 12 temperature readings: 22.4, 23.1, 22.8, 24.0, 25.2, 26.1, 27.3, 28.0, 27.6, 26.8, 25.9 and 24.7 degrees Celsius.

### Operations Performed
NumPy is used to calculate the mean, minimum and maximum sensor readings. The Celsius readings are also converted to Fahrenheit using the formula F = (1.8 × C) + 32. The program displays the first six converted readings.

### Output and Interpretation
The program calculates an average temperature of approximately 25.33°C when rounded to two decimal places but in the terminal it shows 25.32°C  a minimum temperature of 22.40°C and a maximum temperature of 28.00°C. These results show how temperatures varied during the simulated monitoring period. The mean represents the average temperature, while the minimum and maximum indicate the lowest and highest recorded temperatures during the simulated monitoring period.

The Fahrenheit conversion demonstrates how mathematical operations can be applied to sensor data using NumPy arrays.

### Conclusion
This modification demonstrates how NumPy can be applied to IoT sensor data analysis. The same numerical operations used in the original temperature program can help interpret readings from smart home monitoring devices. The current version analyses simulated data and does not connect to a physical sensor or retrieve live readings.