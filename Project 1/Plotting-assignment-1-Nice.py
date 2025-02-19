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

# Compute statistics
datasets = {
    "Manual": manual_filtered_heights,
    "Python1": python_filtered_heights_1,
    "Python2": python_filtered_heights_2
}

for name, data in datasets.items():
    mean = np.mean(data)
    std = np.std(data, ddof=1)  # Sample standard deviation
    print(f"{name} - Mean: {mean:.2f}, Std Dev: {std:.2f}")

# Set y-axis limits for consistency
y_min, y_max = 310, 400

# Create 3x2 subplots (restored original size)
fig, axes = plt.subplots(3, 2, figsize=(10, 8), dpi=100)

# Define plot labels
titles = ["Manual", "Python1", "Python2"]
colors = ["royalblue", "darkorange", "forestgreen"]

# Loop through datasets and plot
for i, (name, color, time, heights) in enumerate(zip(titles, colors, 
                                                     [manual_filtered_time, python_filtered_time_1, python_filtered_time_2], 
                                                     [manual_filtered_heights, python_filtered_heights_1, python_filtered_heights_2])):

    # Time series plot
    axes[i, 0].plot(time, heights, color=color, linewidth=1.5)
    axes[i, 0].set_title(f"{name}: Height Over Time", fontsize=12, fontweight='bold')
    axes[i, 0].set_xlabel("Time (s)", fontsize=10)
    axes[i, 0].set_ylabel("Height (cm)", fontsize=10)
    axes[i, 0].axhline(y=350, color='red', linestyle='--', linewidth=1, label="Setpoint")
    axes[i, 0].set_ylim(y_min, y_max)
    axes[i, 0].grid(True, linestyle="--", alpha=0.5)
    axes[i, 0].legend()

    # Keep script upper/lower bounds
    if i == 1:  # Python1
        axes[i, 0].axhline(y=325, color='r', linestyle='--', alpha=0.5)
        axes[i, 0].axhline(y=375, color='r', linestyle='--', alpha=0.5)
    elif i == 2:  # Python2
        axes[i, 0].axhline(y=340, color='r', linestyle='--', alpha=0.5)
        axes[i, 0].axhline(y=360, color='r', linestyle='--', alpha=0.5)

    # Violin plot
    violin = axes[i, 1].violinplot(heights, showmeans=True, showmedians=True)
    axes[i, 1].set_title(f"{name}: Height Distribution", fontsize=12, fontweight='bold')
    axes[i, 1].set_xlabel(name, fontsize=10)
    axes[i, 1].set_ylabel("Height (cm)", fontsize=10)
    axes[i, 1].set_ylim(y_min, y_max)
    axes[i, 1].grid(True, linestyle="--", alpha=0.5)

    # Style violin plots
    for part in ["cbars", "cmins", "cmaxes", "cmedians", "cmeans"]:
        violin[part].set_edgecolor("black")
        violin[part].set_linewidth(1)

    for pc in violin["bodies"]:
        pc.set_facecolor(color)
        pc.set_edgecolor("black")
        pc.set_alpha(0.6)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
