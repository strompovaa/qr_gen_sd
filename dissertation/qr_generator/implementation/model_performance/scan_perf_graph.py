import json
import matplotlib.pyplot as plt
import numpy as np

# Function to process JSON data
def process_json_data(file_path):
    with open(file_path) as file:
        data = json.load(file)
        
    print(f"Number of entries in {file_path}: {len(data.keys())}")
    conditioning_scales = {}
    for k, entry in data.items():
        cs = entry["conditioning_scale"]
        if not "scan_test" in entry:
            print(k)
            continue
        scan_test = 1 if entry["scan_test"] == "SCAN" else 0
        if cs not in conditioning_scales:
            conditioning_scales[cs] = [scan_test]
        else:
            conditioning_scales[cs].append(scan_test)

    return conditioning_scales

# Process data from both files
conditioning_scales1 = process_json_data('image_v2_scan_data.json')
conditioning_scales2 = process_json_data('image_v2_scan2.json')

# Function to calculate percentages and standard deviations
def calculate_stats(conditioning_scales):
    cs_values, scan_percentages, scan_std_devs = [], [], []
    for cs, scans in conditioning_scales.items():
        cs_values.append(cs)
        scan_percentage = np.mean(scans) * 100
        scan_std_dev = np.std(scans) * 100
        scan_percentages.append(scan_percentage)
        scan_std_devs.append(scan_std_dev)
    return cs_values, scan_percentages, scan_std_devs

cs_values1, scan_percentages1, scan_std_devs1 = calculate_stats(conditioning_scales1)
cs_values2, scan_percentages2, scan_std_devs2 = calculate_stats(conditioning_scales2)

# Combine and sort data
all_cs_values = list(set(cs_values1 + cs_values2))
all_cs_values.sort()
index_map = {cs: i for i, cs in enumerate(all_cs_values)}

# Prepare plot data
plot_data1 = np.zeros(len(all_cs_values))
plot_data2 = np.zeros(len(all_cs_values))
std_devs1 = np.zeros(len(all_cs_values))
std_devs2 = np.zeros(len(all_cs_values))

for i, cs in enumerate(all_cs_values):
    if cs in cs_values1:
        idx = cs_values1.index(cs)
        plot_data1[i] = scan_percentages1[idx]
        std_devs1[i] = scan_std_devs1[idx]
    if cs in cs_values2:
        idx = cs_values2.index(cs)
        plot_data2[i] = scan_percentages2[idx]
        std_devs2[i] = scan_std_devs2[idx]

# Plot
plt.figure(figsize=(12, 6))
bar_width = 0.35
indices = np.arange(len(all_cs_values))

plt.bar(indices - bar_width/2, plot_data1, bar_width, yerr=std_devs1, capsize=5, label='Dataset 1', color='skyblue')
plt.bar(indices + bar_width/2, plot_data2, bar_width, yerr=std_devs2, capsize=5, label='Dataset 2', color='orange')

plt.xticks(indices, labels=[f"{cs:.2f}" for cs in all_cs_values], rotation=45)
plt.xlabel('Conditioning Scale', fontsize=14)
plt.ylabel('Successful Scanning Attempts (%)', fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()