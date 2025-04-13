import numpy as np
from PIL import Image
import os

# Configuration 
# Please fix based on your configuration
image_width = 0
image_height = 0
assert image_height != 0 and image_width !=0, "Please configure image height and width based on your camera configuration."

color_mode = 'L'
hex_file_path = './hex_data.txt'
output_folder = 'output_images'
output_filename = 'test_image.png'


def read_image_from_hex_file(file_path, width, height, mode='L'):
    """
    converts the hex string into an numpy array, converts from 2 bytes to standard 1 byte per pixel and reshapes to target size.
    returns: PIL image
    """
    with open(file_path, 'r') as file:
        hex_data = file.read().replace(' ', '').replace('\n', '')

    print("Image data received. Decoding...")


    raw_data = bytes.fromhex(hex_data)
    grayscale_16bit = np.frombuffer(raw_data, dtype=np.uint16)

    if grayscale_16bit.size != width * height:
        raise ValueError(f"Expected {width * height} pixels, got {grayscale_16bit.size}")

    # Normalize to 8-bit (0–255) for 'L' mode
    grayscale_8bit = (grayscale_16bit / 256).astype(np.uint8)

    image_array = grayscale_8bit.reshape((height, width))

    return Image.fromarray(image_array, mode)


def save_image(image, folder, filename):
    """makes a folder if doesn't exist and save the image."""
    os.makedirs(folder, exist_ok=True)
    save_path = os.path.join(folder, filename)

    image.save(save_path)

    assert os.path.isfile(save_path)
    print(f"Image saved to: {save_path}")


# Main execution
image = read_image_from_hex_file(hex_file_path, image_width, image_height, color_mode)
save_image(image, output_folder, output_filename)

# Display the image
image.show()
