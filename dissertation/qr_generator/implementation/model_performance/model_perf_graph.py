import json
import matplotlib.pyplot as plt
import numpy as np

# Load the JSON file
with open('image_v2_scan_data.json') as file:
    data = json.load(file)

# Process data
conditioning_scales = {}
for entry in data.values():
    cs = entry["conditioning_scale"]
    scan_test = 1 if entry["scan_test"] == "SCAN" else 0
    if cs not in conditioning_scales:
        conditioning_scales[cs] = [scan_test]
    else:
        conditioning_scales[cs].append(scan_test)

# Calculate SCAN percentages and standard deviations for each conditioning scale
cs_values = []
scan_percentages = []
scan_std_devs = []
for cs, scans in conditioning_scales.items():
    cs_values.append(cs)
    scan_percentage = np.mean(scans) * 100
    scan_std_dev = np.std(scans) * 100
    scan_percentages.append(scan_percentage)
    scan_std_devs.append(scan_std_dev)

# Sort data by conditioning scale for plotting
sorted_indices = np.argsort(cs_values)
sorted_cs_values = np.array(cs_values)[sorted_indices]
sorted_scan_percentages = np.array(scan_percentages)[sorted_indices]
sorted_scan_std_devs = np.array(scan_std_devs)[sorted_indices]

# Plot
plt.figure(figsize=(10, 6))
plt.bar(range(len(sorted_cs_values)), sorted_scan_percentages, width=0.4, yerr=sorted_scan_std_devs, capsize=5, color='skyblue')
plt.xticks(range(len(sorted_cs_values)), labels=[f"{cs:.2f}" for cs in sorted_cs_values], rotation=45)
plt.xlabel('Conditioning Scale', fontsize=14)
plt.ylabel('Successful scanning attempts (%)',fontsize=14)
plt.ylim(0, 120)  # Set the y-axis to range from 0 to 100
plt.tight_layout()
plt.show()