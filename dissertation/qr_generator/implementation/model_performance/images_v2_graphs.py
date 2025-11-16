import matplotlib.pyplot as plt
import numpy as np
import json
import matplotlib.pyplot as plt
import os

combined_dict={}

# Load the JSON data
with open("image_v2_data.json", "r") as f:
    data = json.load(f)

# Load the txt file content
with open("qr-verify_3003204.txt", "r") as f:
    scannability_file = f.readlines()

    for line in scannability_file:
            if 'SCAN' in line or 'FAIL' in line:
                scan_test = line.split()[0]
                key = line.split()[1].replace('.png', '')
                combined_dict[key] = data[key]
                combined_dict[key]['scan_test']=scan_test

# Save data into .json
with open("image_v2_scan_data.json", "w") as f:
    json.dump(combined_dict, f, indent=5)

