import numpy as np
import matplotlib.pyplot as plt

# Load all the necessary data files
valve_0_3_exp12_P = np.genfromtxt('Project 3\\Data\\exp12_valve0.3_P.csv', delimiter=',', skip_header=29)
valve_0_3_exp13_P = np.genfromtxt('Project 3\\Data\\exp13_valve0.3_P.csv', delimiter=',', skip_header=29)
valve_0_3_exp10_PI = np.genfromtxt('Project 3\\Data\\exp10_valve0.3_PI_v4.csv', delimiter=',', skip_header=29)
valve_0_3_exp14_PI = np.genfromtxt('Project 3\\Data\\exp14_valve0.3_PI_noerrorline.csv', delimiter=',', skip_header=29)
valve_0_3_exp15_PI = np.genfromtxt('Project 3\\Data\\exp15_valve0.3_PI_noerrorline.csv', delimiter=',', skip_header=29)
valve_0_1_exp2_PI = np.genfromtxt('Project 3\\Data\\exp2_valve0.1_PI_witthouterrorline.csv', delimiter=',', skip_header=29)
valve_0_1_exp5_PI = np.genfromtxt('Project 3\\Data\\exp5_valve0.1_PI_v4.csv', delimiter=',', skip_header=29)
valve_0_1_goed_PI = np.genfromtxt('Project 3\\Data\\exp_0.1_goed.csv', delimiter=',', skip_header=29)
valve_0_5_exp9_PI = np.genfromtxt('Project 3\\Data\\exp9_valve0.5_PI_noerrorline.csv', delimiter=',', skip_header=29)
valve_0_5_exp11_PI = np.genfromtxt('Project 3\\Data\\exp11_valve0.5_PI_v4.csv', delimiter=',', skip_header=29)

# Set constants for violin plot y-axis
Alpha = 350 * 0.9  # Lower bound for y-axis
Beta = 350 * 1.1   # Upper bound for y-axis

# Set time thresholds
settling_time_threshold = 300
drain_time_threshold = 500

# Estimate constant error from PI experiment (to align steady state)
contant_error_0_3 = np.mean(valve_0_3_exp10_PI[1000:4000, 2] - 350)
contant_error_0_1 = np.mean(valve_0_1_exp2_PI[1000:4000, 2] - 350)
contant_error_0_5 = np.mean(valve_0_5_exp9_PI[3500:4000, 2] - 350)
print(contant_error_0_5)
valve_0_1_goed_PI[:,2] = valve_0_1_goed_PI[:,2] + contant_error_0_1
# Plot metadata
plot_data = [
    ("Valve 0.3 P Control", [valve_0_3_exp12_P, valve_0_3_exp13_P], ['Exp 1', 'Exp 2'], 0),
    ("Valve 0.3 PI Control", [valve_0_3_exp10_PI, valve_0_3_exp14_PI, valve_0_3_exp15_PI], ['Exp 3', 'Exp 4', 'Exp 5'], -contant_error_0_3),
    ("Valve 0.1 PI Control", [valve_0_1_exp2_PI, valve_0_1_exp5_PI, valve_0_1_goed_PI], ['Exp 6', 'Exp 7', 'Exp 8'], -contant_error_0_1),
    ("Valve 0.5 PI Control", [valve_0_5_exp9_PI, valve_0_5_exp11_PI], ['Exp 9', 'Exp 10'], -contant_error_0_5)
]

fig, axes = plt.subplots(nrows=len(plot_data), ncols=2, figsize=(14, 4 * len(plot_data)+10))
mean_list = []
stdev_list = []
for i, (name, datasets, labels, offset) in enumerate(plot_data):
    ax_time = axes[i, 0]
    ax_violin = axes[i, 1]
    ax_violin.axhline(350, color='g', linestyle='--', alpha=0.5, label='Steady State Value')
    ax_violin.axhline(350 * 1.05, color='b', linestyle='--', alpha=0.3, label='SSV + 5%')
    ax_violin.axhline(350 * 0.95, color='b', linestyle='--', alpha=0.3, label='SSV - 5%')
    # Plot time series
    for data, label in zip(datasets, labels):
        ax_time.plot(data[:, 1], data[:, 2] + offset, label=label)
    ax_time.axvline(settling_time_threshold, color='r', linestyle='--', alpha=0.3)
    ax_time.axhline(350, color='g', linestyle='--', alpha=0.5)
    ax_time.axhline(350 * 1.05, color='b', linestyle='--', alpha=0.3)
    ax_time.axhline(350 * 0.95, color='b', linestyle='--', alpha=0.3)
    ax_time.set_title(name, fontsize=18, fontweight='bold')
    ax_time.set_xlabel("Time [s]", fontsize=14, fontweight='bold')
    ax_time.set_ylabel("Water Level [mm]", fontsize=14, fontweight='bold')
    ax_time.legend()
    ax_time.set_xlim(0, 500)
    ax_time.grid(True, linestyle="--", alpha=0.5)

    # Build violin data: filter out empty slices
    violin_data = []
    for data in datasets:
        mask = (data[:, 1] > settling_time_threshold) & (data[:, 1] < drain_time_threshold)
        steady_vals = data[mask, 2] + offset
        if steady_vals.size > 0:
            violin_data.append(steady_vals)

    # Only plot if data is valid
    if len(violin_data) > 0:
        mean_list.append(np.mean(violin_data))
        stdev_list.append(np.std(violin_data))
        violin = ax_violin.violinplot(violin_data, showmeans=True, showmedians=True)
        ax_violin.set_title(name, fontsize=18, fontweight='bold')
        ax_violin.set_ylabel("Height (mm)", fontsize=14, fontweight='bold')
        ax_violin.set_ylim(Alpha, Beta)
        ax_violin.grid(True, linestyle="--", alpha=0.5)

        # Style violin plots
        for part in ["cbars", "cmins", "cmaxes", "cmedians", "cmeans"]:
            violin[part].set_edgecolor("black")
            violin[part].set_linewidth(1)
        for pc in violin["bodies"]:
            pc.set_facecolor("orange")
            pc.set_edgecolor("black")
            pc.set_alpha(0.6)
    else:
        ax_violin.text(0.5, 0.5, "No valid data", ha='center', va='center', fontsize=10, fontweight='bold')
        ax_violin.set_axis_off()

for mean, stdev in zip(mean_list, stdev_list):
    print(f"P & 0.3&{mean:.2f} & {stdev:.2f} \\\ \hline")
plt.tight_layout() 
# rect=[0, 0.03, 1, 1]
plt.savefig("Project 3\\Figures\\Full_Comparison_with_Violin_Plots.png", dpi=500)
plt.show()
