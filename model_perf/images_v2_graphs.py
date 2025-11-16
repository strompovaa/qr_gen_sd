
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

import numpy as np
# %matplotlib inline

import json
import matplotlib.pyplot as plt
import os

# Load the JSON data
with open("/Users/admin/Library/CloudStorage/OneDrive-UniversityofGlasgow/_L5_project/images_v2/json/combined_data.json", "r") as f:
    data = json.load(f)

# Load the txt file content
with open("/Users/admin/Library/CloudStorage/OneDrive-UniversityofGlasgow/_L5_project/images_v2/qr-verify_3003204.txt", "r") as f:
    scannability_file = f.readlines()
    scannability_results=[]
    for line in scannability_file:
        print(line)
        if 'FAIL' in line or 'SCAN' in line:
            scannability_results.append(line)

print(scannability_results)

# Parse the scannability results
scannability_dict = {}
for line in scannability_results:
    parts = line.split()
    status, filename = parts[0], parts[1]
    scannability_dict[filename] = 1 if status == "SCAN" else 0

print(scannability_dict)

# Group data by prompt, guidance_scale, size, and position
grouped_data = {}
for filename, params in data.items():
    key = (params["prompt"], params["guidance_scale"], params["size"], params["position"])
    scannability = scannability_dict.get(filename + ".png", -1)  # -1 if not found
    if scannability == -1:
        continue  # Skip if scannability result is not available
    if key not in grouped_data:
        grouped_data[key] = []
    grouped_data[key].append((params["conditioning_scale"], scannability))


# Plotting
for key, values in grouped_data.items():
    prompt, guidance_scale, size, position = key
    conditioning_scales, scannabilities = zip(*values)
    plt.figure(figsize=(10, 6))
    plt.scatter(conditioning_scales, scannabilities, alpha=0.7)
    plt.title(f"Scannability by Conditioning Scale\nPrompt: {prompt[:50]}...\nGuidance Scale: {guidance_scale}, Size: {size}, Position: {position}")
    plt.xlabel("Conditioning Scale")
    plt.ylabel("Scannability (1=SCAN, 0=FAIL)")
    plt.grid(True)
    plt.savefig(str(key)+str(values)+'.pdf')

# def f(x, a, b):
#     return 1 / (1 + np.exp(-a*x + b))

# scannability = [int(b) for b in scan_checks]
# x = cond_scales
# y = scannability

# # Fit the curve
# params, covariance = curve_fit(f, x, y)
# a, b = params

# # Generate the fitted curve
# x_fit = np.linspace(-1, 4, 100)
# y_fit = f(x_fit, a, b)

# # Plot the data and the fitted curve
# plt.scatter(x, y, label='Data', alpha=0.5)
# plt.plot(x_fit, y_fit, label=f'Fitted curve: a={a:.2f}, b={b:.2f}', linewidth=2)
# plt.legend()
# plt.xlabel('Conditioning scale')
# plt.ylabel('Scannability')
# plt.title('Scannability of QR Codes')
# plt.show()