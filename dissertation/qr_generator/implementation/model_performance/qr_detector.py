import cv2
import os

# Directory containing the images
image_dir = "/Users/admin/Library/CloudStorage/OneDrive-UniversityofGlasgow/_L5_project/qr_gen_sd/experiment_monster-labs/images_v2/"
output_file = "qr_detect.txt"

# Initialize the QRCode detector
detector = cv2.QRCodeDetector()

# Prepare to write results to the output file
with open(output_file, "w") as f_out:
    # Iterate through each image in the directory
    for image_name in os.listdir(image_dir):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Construct the full path to the image
            image_path = os.path.join(image_dir, image_name)
            
            # Load the image
            image = cv2.imread(image_path)
            
            # Detect and decode the QR Code
            data, bbox, _ = detector.detectAndDecode(image)
            
            # Check if a QR Code was detected and decoded
            if bbox is not None and data:
                # QR Code was successfully decoded
                result_line = f"TRUE {image_name} {data}\n"
            else:
                # QR Code detection failed
                result_line = f"FAIL {image_name}\n"
            
            # Write the result to the output file
            f_out.write(result_line)

print(f"Results written to {output_file}.")
