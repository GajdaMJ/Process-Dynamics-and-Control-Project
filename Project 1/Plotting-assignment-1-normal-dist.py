import numpy as np
import matplotlib.pyplot as plt

# Load data
manual_data_1 = np.genfromtxt('Project 1/Results/Assignment-1-PDC-Manual.csv', delimiter=',')
python_data_1 = np.genfromtxt('Project 1/Results/Assignment-1-PDC-Python.csv', delimiter=',')

# Filter data where the first column (time) is between 100 and 800
manual_mask = (manual_data_1[:, 0] >= 100) & (manual_data_1[:, 0] <= 800)
python_mask = (python_data_1[:, 0] >= 100) & (python_data_1[:, 0] <= 800)

manual_filtered_heights = manual_data_1[manual_mask][:, 1]  # Heights
python_filtered_heights = python_data_1[python_mask][:, 1]  # Heights

# Create violin plot
fig, ax = plt.subplots(figsize=(6, 4), dpi=200)

# Violin plot for height values
data = [manual_filtered_heights, python_filtered_heights]
labels = ['Manual', 'Python']

violin_parts = ax.violinplot(data, showmeans=True, showmedians=True, widths=0.8)

# Styling
colors = ['royalblue', 'darkorange']
for i, pc in enumerate(violin_parts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.75)

for part in ['cbars', 'cmins', 'cmaxes', 'cmedians', 'cmeans']:
    violin_parts[part].set_edgecolor('black')
    violin_parts[part].set_linewidth(1.2)

# Labels and title
ax.set_xticks([1, 2])
ax.set_xticklabels(labels, fontsize=12, fontweight='bold')
ax.set_ylabel('Height (cm)', fontsize=13, fontweight='bold')
ax.set_title('Distribution of Heights Over Time', fontsize=14, fontweight='bold')

# Adjust y-axis limits for better readability
ax.set_ylim(min(np.min(manual_filtered_heights), np.min(python_filtered_heights)) - 5, 
            max(np.max(manual_filtered_heights), np.max(python_filtered_heights)) + 5)

ax.grid(True, linestyle='--', alpha=0.5)

# Show plot
plt.tight_layout()
plt.show()


import numpy as np

# Compute statistics
manual_mean = np.mean(manual_filtered_heights)
manual_std = np.std(manual_filtered_heights, ddof=1)  # ddof=1 for sample standard deviation

python_mean = np.mean(python_filtered_heights)
python_std = np.std(python_filtered_heights, ddof=1)

# Print results
print(f"Manual Data - Mean: {manual_mean:.2f}, Std Dev: {manual_std:.2f}")
print(f"Python Data - Mean: {python_mean:.2f}, Std Dev: {python_std:.2f}")
