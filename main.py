from PIL import Image
import os

def crop_and_save(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file_name in files:
        # Check if the file is an image (you may want to add more checks)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            # Open the image
            img = Image.open(input_path)

            # Get the original dimensions
            width, height = img.size

            # Calculate the crop dimensions for a 3:4 aspect ratio
            new_width = min(width, height * 3 // 4)
            new_height = new_width * 4 // 3

            # Calculate the crop box
            left = (width - new_width) // 2
            top = (height - new_height) // 2
            right = left + new_width
            bottom = top + new_height

            # Crop the image
            cropped_img = img.crop((left, top, right, bottom))

            # Save the cropped image
            cropped_img.save(output_path)

            # Close the image
            img.close()

if __name__ == "__main__":
    input_folder = r'F:\Lessons\Sem 7\Research\dataset\all Dataset\cropped error\20_1'
    output_folder = r"F:\Lessons\Sem 7\Research\Operations\cropping_specific_ratio\images\20_1"

    crop_and_save(input_folder, output_folder)
