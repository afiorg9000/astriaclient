import os
from PIL import Image
import pyheif

def convert_heic_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_filename)
            
            # Read the HEIC file
            heif_file = pyheif.read(input_path)
            
            # Convert HEIC to a PIL Image
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            
            # Save the image as JPG
            image.save(output_path, "JPEG")
            print(f"Converted {input_path} to {output_path}")

# Example usage
input_folder = "images"  # Replace with your input folder containing HEIC files
output_folder = "converted_images"  # Replace with your desired output folder

convert_heic_folder(input_folder, output_folder)
