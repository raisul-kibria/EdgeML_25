import numpy as np
from PIL import Image
import os

# Configuration
# Provide the image width and height according to camera resolution
image_width = None
image_height = None

color_mode = 'RGB'
hex_file_path = './hex_data.txt'
output_folder = 'output_images'
output_filename = 'test_image.png'


def read_image_from_hex_file(file_path, width, height, mode):
    # Read hex data from file and clean it up
    with open(file_path, 'r') as file:
        hex_data = file.read().replace(' ', '').replace('\n', '')

    print("Image data received. Decoding...")

    # Read into a bytes array the hex data
    # You can use for example bytes.fromhex and np.frombuffer function
    raw_data = None
    rgb565 = None

    r = ((rgb565 >> 11) & 0x1F)  # 5 bits red

    # Do the shift for green and blue channels
    g = None                     # 6 bits green
    b = None                     # 5 bits blue


    # Rescale the values in [0,255] range
    r = None
    g = None
    b = None

    # Combine into RGB888 format
    rgb888 = np.stack((r, g, b), axis=-1).astype(np.uint8)

    # Reshape to image dimensions
    return Image.fromarray(rgb888.reshape((height, width, 3)), mode)


def save_image(image, folder, filename):
    os.makedirs(folder, exist_ok=True)
    save_path = os.path.join(folder, filename)

    # save the image in the path: folder/filename    
    image = None

    assert os.path.isfile(save_path)
    print(f"Image saved to: {save_path}")

# Main execution
image = read_image_from_hex_file(hex_file_path, image_width, image_height, color_mode)
save_image(image, output_folder, output_filename)

# Display the image
image.show()
