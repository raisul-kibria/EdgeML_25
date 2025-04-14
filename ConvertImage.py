import cv2
import numpy as np

def preprocess_image(image_path: str, target_size=(32, 32)) -> np.ndarray:
    """Reads and preprocesses the image by resizing and converting to grayscale."""
    image = cv2.imread(image_path)
    image = cv2.resize(image, target_size)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image.astype(np.uint8)

def save_to_header(data: np.ndarray, output_file: str):
    """Flattens the image array and writes it as a C header file in uint8_t array format."""
    with open(output_file, 'w') as f:
        f.write('#ifndef IMAGE_DATA_H\n')
        f.write('#define IMAGE_DATA_H\n\n')
        f.write('#include <stdint.h>\n\n')
        f.write('const uint8_t image_data[] = {\n')

        flat_data = data.flatten()
        for i, value in enumerate(flat_data):
            f.write(f'{value}')
            if i != len(flat_data) - 1:
                f.write(', ')
            if (i + 1) % 16 == 0:  # Wrap lines every 16 values for readability
                f.write('\n')

        f.write('\n};\n\n')
        f.write('#endif // IMAGE_DATA_H\n')

if __name__ == "__main__":
    # Todo: Add path for image and the output file name with .h extension (e.g., image_data.h)
    image_path = ""
    output_file = ""

    processed_image = preprocess_image(image_path)
    save_to_header(processed_image, output_file)
