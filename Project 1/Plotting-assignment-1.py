import numpy as np
import matplotlib.pyplot as plt

# Load data
manual_data_1 = np.genfromtxt('Project 1/Results/Assignment-1-PDC-Manual.csv', delimiter=',')
python_data_1 = np.genfromtxt('Project 1/Results/Assignment-1-PDC-Python.csv', delimiter=',')


# Create figure and axes
fig, axes = plt.subplots(1, 2)

# Define consistent styling
plot_styles = {
    "linewidth": 2,
    "alpha": 0.8
}
# Manual Data Plot
axes[0].plot(manual_data_1[:, 0], manual_data_1[:, 1], label='Manual', color='royalblue', **plot_styles)
axes[0].axhline(y=350, color='r', linestyle='--', label='Setpoint')
axes[0].set_xlabel('Time (s)', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Height (cm)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Time (s)', fontsize=14, fontweight='bold')
axes[0].set_title('Manual Data', fontsize=16, fontweight='bold')
axes[0].set_xlim(100, 800)
axes[0].set_ylim(300, 400)
axes[0].tick_params(axis='both', which='major', labelsize=12)
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend(fontsize=12, loc='best')

# Python Data Plot
axes[1].plot(python_data_1[:, 0], python_data_1[:, 1], label='Python', color='darkorange', **plot_styles)
axes[1].set_xlabel('Time (s)', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Height (cm)', fontsize=14, fontweight='bold')
axes[1].axhline(y=350, color='r', linestyle='--', label='Setpoint')
axes[1].axhline(y=325, color='r', linestyle='--', label='Lower Bound', alpha=0.5)
axes[1].axhline(y=375, color='r', linestyle='--', label='Upper Bound', alpha=0.5)

axes[1].set_title('Python Data', fontsize=16, fontweight='bold')
axes[1].set_xlim(100, 800)
axes[1].tick_params(axis='both', which='major', labelsize=12)
axes[1].grid(True, linestyle='--', alpha=0.6)
axes[1].legend(fontsize=12, loc='best')
axes[1].set_xlabel('Time (s)', fontsize=14, fontweight='bold')
axes[1].set_ylim(300, 400)

# Adjust layout
plt.tight_layout()
plt.show()
