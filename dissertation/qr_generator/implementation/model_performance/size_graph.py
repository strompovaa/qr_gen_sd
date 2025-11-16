import json
import matplotlib.pyplot as plt
import numpy as np

# Load the JSON file
with open('image_v2_scan_data.json') as file:
    data = json.load(file)

# Initialize a dictionary to hold the results
conditioning_scale_groups = {}

# Iterate through each entry in the data dictionary
for key, value in data.items():
    # Extract the conditioning_scale and scan_test values
    cond_scale = value["size"]
    scan_test = value["scan_test"]
    
    # Check if this conditioning_scale already has an entry in the results dictionary
    if cond_scale not in conditioning_scale_groups:
        # If not, initialize it with an empty list
        conditioning_scale_groups[cond_scale] = []
    
    # Append the scan_test value to the list for this conditioning_scale
    conditioning_scale_groups[cond_scale].append(scan_test)

# Calculate percentages
percentages = {scale: {"SCAN": group.count('SCAN') / len(group) * 100, "FAIL": group.count('FAIL') / len(group) * 100}
               for scale, group in conditioning_scale_groups.items()}

# Sort scales for ordered x-axis
scales = sorted(list(percentages.keys()))
scan_percentages = [percentages[scale]["SCAN"] for scale in scales]
fail_percentages = [percentages[scale]["FAIL"] for scale in scales]

# Plot configuration
bar_width = 0.35
index = np.arange(len(scales))

fig, ax = plt.subplots()
bar1 = ax.bar(index, scan_percentages, bar_width, label='SCAN', color='lightgreen')
bar2 = ax.bar(index + bar_width, fail_percentages, bar_width, label='FAIL', color='lightcoral')

# Labeling and layout adjustments
ax.set_xlabel('Size')
ax.set_ylabel('Percentage')
ax.set_title('Scannability by Size')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(scales)

ax.legend()

plt.show()