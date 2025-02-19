import numpy as np
import matplotlib.pyplot as plt

# Load data
manual_data_1 = np.genfromtxt('Project 1/Results/Assignment-1-PDC-Manual.csv', delimiter=',')
python_data_1 = np.genfromtxt('Project 1/Results/Assignment-1-PDC-Python.csv', delimiter=',')
python_data_2 = np.genfromtxt('Project 1/Results/Assignment-1-PDC-Python2.csv', delimiter=',')

# Filter data where the first column (time) is between 100 and 800
manual_mask = (manual_data_1[:, 0] >= 100) & (manual_data_1[:, 0] <= 800)
python_mask_1 = (python_data_1[:, 0] >= 100) & (python_data_1[:, 0] <= 800)
python_mask_2 = (python_data_2[:, 0] >= 100) & (python_data_2[:, 0] <= 800)

manual_filtered_time = manual_data_1[manual_mask][:, 0]
manual_filtered_heights = manual_data_1[manual_mask][:, 1]

python_filtered_time_1 = python_data_1[python_mask_1][:, 0]
python_filtered_heights_1 = python_data_1[python_mask_1][:, 1]

python_filtered_time_2 = python_data_2[python_mask_2][:, 0]
python_filtered_heights_2 = python_data_2[python_mask_2][:, 1]

# Create 3x2 subplots
fig, axes = plt.subplots(3, 2, figsize=(10, 12))

# Plot (a) - Manual: Height over Time
axes[0, 0].plot(manual_filtered_time, manual_filtered_heights)
axes[0, 0].set_title("Manual: Height Over Time")
axes[0, 0].set_xlabel("Time (s)")
axes[0, 0].set_ylabel("Height (cm)")
axes[0, 0].axhline(y=350, color='r', linestyle='--', label='Setpoint')

# Plot (b) - Manual: Violin Plot
axes[0, 1].violinplot(manual_filtered_heights, showmeans=True, showmedians=True)
axes[0, 1].set_title("Manual: Height Distribution")
axes[0, 1].set_xlabel("Manual Data")
axes[0, 1].set_ylabel("Height (cm)")

# Plot (c) - Python1: Height over Time
axes[1, 0].plot(python_filtered_time_1, python_filtered_heights_1)
axes[1, 0].set_title("Python1: Height Over Time")
axes[1, 0].set_xlabel("Time (s)")
axes[1, 0].set_ylabel("Height (cm)")
axes[1, 0].axhline(y=350, color='r', linestyle='--')
axes[1, 0].axhline(y=325, color='r', linestyle='--', alpha=0.5)
axes[1, 0].axhline(y=375, color='r', linestyle='--', alpha=0.5)


# Plot (d) - Python1: Violin Plot
axes[1, 1].violinplot(python_filtered_heights_1, showmeans=True, showmedians=True)
axes[1, 1].set_title("Python1: Height Distribution")
axes[1, 1].set_xlabel("Python1 Data")
axes[1, 1].set_ylabel("Height (cm)")

# Plot (e) - Python2: Height over Time
axes[2, 0].plot(python_filtered_time_2, python_filtered_heights_2)
axes[2, 0].set_title("Python2: Height Over Time")
axes[2, 0].set_xlabel("Time (s)")
axes[2, 0].set_ylabel("Height (cm)")
axes[2, 0].axhline(y=350, color='r', linestyle='--')
axes[2, 0].axhline(y=340, color='r', linestyle='--', alpha=0.5)
axes[2, 0].axhline(y=360, color='r', linestyle='--', alpha=0.5)

# Plot (f) - Python2: Violin Plot
axes[2, 1].violinplot(python_filtered_heights_2, showmeans=True, showmedians=True)
axes[2, 1].set_title("Python2: Height Distribution")
axes[2, 1].set_xlabel("Python2 Data")
axes[2, 1].set_ylabel("Height (cm)")

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
