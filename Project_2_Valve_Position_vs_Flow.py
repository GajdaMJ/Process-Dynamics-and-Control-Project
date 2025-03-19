import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravity constant in m/s^2
d_1 = 1.40  # Diameter in dm
Q_1 = 0.05
# Loading Data
valve_0_3 = np.genfromtxt('Flow_0.05_valve_0.3.csv', delimiter=',')
valve_0_5 = np.genfromtxt('Flow_0.05_valve_0.5.csv', delimiter=',')
valve_0_2 = np.genfromtxt('Project 2\Data-Michal-Experiments\\0.05__0.2.csv', delimiter=',', skip_header=29, skip_footer=170)
valve_0_4 = np.genfromtxt('Project 2\Data-Michal-Experiments\\0.05__0.4.csv', delimiter=',', skip_header=29, skip_footer=200)
valve_0_6 = np.genfromtxt('Project 2\Data-Michal-Experiments\\0.05__0.6.csv', delimiter=',', skip_header=29, skip_footer=170)
valve_0_25 = np.genfromtxt('Project 2\Data-Michal-Experiments\\0.05__0.25.csv', delimiter=',', skip_header=29, skip_footer=170)
valve_0_45 = np.genfromtxt('Project 2\Data-Michal-Experiments\\0.05__0.45.csv', delimiter=',', skip_header=29, skip_footer=170)
valve_0_55 = np.genfromtxt('Project 2\Data-Michal-Experiments\\0.05__0.55.csv', delimiter=',', skip_header=29, skip_footer=170)

# Steady State Heights (calculated from the last 100 rows)
valve_0_3_steady_state = np.average(valve_0_3[-100:, 2])
valve_0_5_steady_state = np.average(valve_0_5[-100:, 1])
valve_0_2_steady_state = np.average(valve_0_2[-100:, 2])
valve_0_4_steady_state = np.average(valve_0_4[-100:, 2])
valve_0_6_steady_state = np.average(valve_0_6[-100:, 2])
valve_0_25_steady_state = np.average(valve_0_25[-100:, 2])
valve_0_45_steady_state = np.average(valve_0_45[-100:, 2])
valve_0_55_steady_state = np.average(valve_0_55[-100:, 2])

# # Visual Confirmation: Plotting all valve combinations with their steady state heights
# plt.plot(valve_0_3[:, 1], valve_0_3[:, 2], label='Valve 0.3')
# plt.axhline(y=valve_0_3_steady_state, color='r', linestyle='--', label=f'Valve 0.3 Steady State: {valve_0_3_steady_state:.2f}')
# plt.plot(valve_0_5[:, 1], valve_0_5[:, 2], label='Valve 0.5')
# plt.axhline(y=valve_0_5_steady_state, color='g', linestyle='--', label=f'Valve 0.5 Steady State: {valve_0_5_steady_state:.2f}')
# plt.plot(valve_0_2[:, 1], valve_0_2[:, 2], label='Valve 0.2')
# plt.axhline(y=valve_0_2_steady_state, color='b', linestyle='--', label=f'Valve 0.2 Steady State: {valve_0_2_steady_state:.2f}')
# plt.plot(valve_0_4[:, 1], valve_0_4[:, 2], label='Valve 0.4')
# plt.axhline(y=valve_0_4_steady_state, color='purple', linestyle='--', label=f'Valve 0.4 Steady State: {valve_0_4_steady_state:.2f}')
# plt.plot(valve_0_6[:, 1], valve_0_6[:, 2], label='Valve 0.6')
# plt.axhline(y=valve_0_6_steady_state, color='orange', linestyle='--', label=f'Valve 0.6 Steady State: {valve_0_6_steady_state:.2f}')
# plt.plot(valve_0_25[:, 1], valve_0_25[:, 2], label='Valve 0.25')
# plt.axhline(y=valve_0_25_steady_state, color='brown', linestyle='--', label=f'Valve 0.25 Steady State: {valve_0_25_steady_state:.2f}')
# plt.plot(valve_0_45[:, 1], valve_0_45[:, 2], label='Valve 0.45')
# plt.axhline(y=valve_0_45_steady_state, color='pink', linestyle='--', label=f'Valve 0.45 Steady State: {valve_0_45_steady_state:.2f}')
# plt.plot(valve_0_55[:, 1], valve_0_55[:, 2], label='Valve 0.55')
# plt.axhline(y=valve_0_55_steady_state, color='yellow', linestyle='--', label=f'Valve 0.55 Steady State: {valve_0_55_steady_state:.2f}')

# # Adding labels, title, and legend
# plt.xlabel('Flow')
# plt.ylabel('Height')
# plt.title('Valve Data Comparison with Steady State Heights')
# plt.legend()

# # Show the plot
# plt.show()

# Valve positions and corresponding steady state heights
valve_positions = [0.2, 0.25, 0.3, 0.4, 0.45, 0.5, 0.55, 0.6]
steady_state_heights = [
    valve_0_2_steady_state,
    valve_0_25_steady_state,
    valve_0_3_steady_state,
    valve_0_4_steady_state,
    valve_0_45_steady_state,
    valve_0_5_steady_state,
    valve_0_55_steady_state,
    valve_0_6_steady_state
]
valve_positions = np.array(valve_positions)
print(valve_positions[-2], steady_state_heights[-2])


steady_state_heights = np.array(steady_state_heights) / Q_1**2
inverse_squared_positions = 1 / (np.array(valve_positions)**2)

# Plotting 1 / (Valve Position^3) vs steady state heights
plt.scatter(inverse_squared_positions, steady_state_heights, color='r', marker='x', label='Data')

# Fit a linear function to the transformed data (y = mx + b)
slope, intercept = np.polyfit(inverse_squared_positions, steady_state_heights, 1)

# Calculate the fitted line
fitted_line = np.polyval([slope, intercept], inverse_squared_positions)

# Calculate R^2 value
residuals = steady_state_heights - fitted_line
ss_residual = np.sum(residuals**2)
ss_total = np.sum((steady_state_heights - np.mean(steady_state_heights))**2)
r_squared = 1 - (ss_residual / ss_total)

# Plot the fitted line
plt.plot(inverse_squared_positions, fitted_line, color='b', label=f'Linear Fit: y = {slope:.2f}x + {intercept:.2f}')

# Adding labels and title
plt.xlabel(r'$1 / (Valve Position^2)$', fontsize=12)
plt.ylabel(r'$\frac{Steady State Height}{Q_1}$', fontsize=12)
plt.title(r'$\frac{1}{Valve Position^2}$ vs Steady State Height', fontsize=14)

# Display slope, intercept, and R^2 in the bottom right corner
plt.legend()
plt.text(25, 25000, f"Slope: {slope:.2f}\nIntercept: {intercept:.2f}\nR^2: {r_squared:.6f}", fontsize=10, bbox=dict(facecolor='white', alpha=0.5), verticalalignment='top', horizontalalignment='right')

plt.tight_layout()

plt.savefig('valve_position_vs_height_fit.png', bbox_inches='tight')
# Show the plot
plt.show()

# Save the figure


# Output the slope, intercept, and R^2 value to the console
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"R^2: {r_squared:.6f}")
print("Sum of squared residuals (SS_residual):", ss_residual)
print("Total sum of squares (SS_total):", ss_total)

# # Compute sqrt(2gh) for each valve position
# sqrt_heights = np.sqrt(2 * g * np.array(steady_state_heights)) / Q_1

# # Plotting Valve Position vs sqrt(2gh)
# plt.scatter(valve_positions, sqrt_heights, color='r', marker='x', label='sqrt(2gh)')

# ## Fit a quadratic function (y = ax^2 + bx + c) to the data
# coefficients = np.polyfit(valve_positions, sqrt_heights, 2)  # 2 for quadratic

# # Calculate the fitted quadratic curve
# fitted_curve = np.polyval(coefficients, valve_positions)

# # Calculate R^2 value for the quadratic fit
# # Residuals (difference between the observed and predicted values)
# residuals = sqrt_heights - fitted_curve
# ss_residual = np.sum(residuals**2)
# ss_total = np.sum((sqrt_heights - np.mean(sqrt_heights))**2)
# r_squared = 1 - (ss_residual / ss_total)

# # Plot the fitted quadratic curve
# plt.plot(valve_positions, fitted_curve, color='b', label=f'Quadratic Fit: y = {coefficients[0]:.2f}x^2 + {coefficients[1]:.2f}x + {coefficients[2]:.2f}')

# # Adding labels and title
# plt.xlabel('Valve Position')
# plt.ylabel('sqrt(2gh)')
# plt.title('Valve Position vs sqrt(2gh)')

# # Display the coefficients, R^2 value
# plt.legend()
# plt.text(0.35, np.max(sqrt_heights), f"a: {coefficients[0]:.2f}\nb: {coefficients[1]:.2f}\nc: {coefficients[2]:.2f}\nR^2: {r_squared:.2f}",
#          fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

# # Show the plot
# plt.show()

# # Output the coefficients and R^2 value
# print(f"Quadratic Coefficients: a = {coefficients[0]:.2f}, b = {coefficients[1]:.2f}, c = {coefficients[2]:.2f}")
# print(f"R^2: {r_squared:.2f}")



# # print(valve_0_3_steady_state, valve_0_5_steady_state)
# # # sqrt 2gh

# # sqrt_2gh = [np.sqrt(valve_0_3_steady_state*2*9.81), np.sqrt(valve_0_5_steady_state*2*9.81)]

# # # plt.plot(valve_positions, sqrt_2gh, '.')









plt.show()