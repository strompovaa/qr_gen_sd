import json

# Load the JSON data
json_file_path = '/Users/admin/Library/CloudStorage/OneDrive-UniversityofGlasgow/_L5_project/qr_gen_sd/qr_gen_sd/model_perf/image_v3_data.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Read the text file and update the JSON data
text_file_path = '/Users/admin/Library/CloudStorage/OneDrive-UniversityofGlasgow/_L5_project/qr_gen_sd/qr_gen_sd/model_perf/qr_verify3.txt'
with open(text_file_path, 'r') as text_file:
    for line in text_file.readlines():
        if 'SCAN' in line or 'FAIL' in line:
            parts = line.strip().split()
            scan_result = parts[0]  # 'TRUE' or 'FAIL'
            image_name = parts[1][:-4]  # Removing '.png'
            if image_name in data:
                data[image_name]['scan'] = scan_result

# Save the updated JSON data
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)