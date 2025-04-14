# EdgeML_25
The repository includes the template code and isntructions for the second project of the course Edge Computing for ML, 2025 at ÅA. Each file serves as follows:
- ConvertImage.py (needs path corrections; might need target size): Takes as input an RGB image and converts it to grayscale of the target size. The outcome is a C-header with an uint8 array called image_data.
- DisplayRawImage_grayscale.py (needs image width and height): Transforms 2-bytes grayscale image to 1-byte grayscale, saves, and displays it. Reads data from hex_data.txt.
- DisplayRawImage.py (incomplete): Converts RGB565 images to RGB888 (standard) format, displays and saves the result. Reads data from hex_data.txt.
- EdgeML25.ipynb (incomplete): Includes data loading, processing and model architecture. Should be used for compression experiments.
- requirements.txt: Requirements for running the experiments locally (instead of Colab).
