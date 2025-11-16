import json
import os

json_dir = "/Users/admin/Library/CloudStorage/OneDrive-UniversityofGlasgow/_L5_project/qr_gen_sd/qr_gen_sd/experiment_monster-labs/images_v3/images/json" 
combined_data = {}

for file_name in os.listdir(json_dir):
    if file_name.endswith('.json'):
        with open(os.path.join(json_dir, file_name), 'r') as f:
            data = json.load(f)
            key = os.path.splitext(file_name)[0]
            combined_data[key] = data

# Save the combined data to a new JSON file
combined_json_path = "/Users/admin/Library/CloudStorage/OneDrive-UniversityofGlasgow/_L5_project/qr_gen_sd/qr_gen_sd/experiment_monster-labs/images_v3/images/images_v3_data.json" 
with open(combined_json_path, 'w') as f:
    json.dump(combined_data, f, indent=4)
