# Image Denoising Tool

This repository contains two versions of a Python script for denoising images using various techniques.

## Simple Version

### Features

- **Denoising Techniques:** Applies Gaussian Blur, Median Blur, and Bilateral Filter to remove noise from images.
- **Plotting:** Visualizes denoised images using Matplotlib.
- **Ease of Use:** Simple to use, processes all images in a specified directory.

### Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/D8Programmer/Image_Denoising_Tool.git
   cd Image_Denoising_Tool
   ```

2. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**

   ```bash
   python simple_version.py Noisy_Images
   ```

4. **Results:**

   - The denoised images will be displayed using Matplotlib.
   - Optionally, modify the script parameters for different denoising effects.

## Professional Version

### Features

- **Advanced Techniques:** Utilizes asyncio for concurrent image processing, logging for detailed execution tracking, and robust error handling.
- **Multiple Denoising Methods:** Includes Gaussian Blur, Median Blur, and Bilateral Filter.
- **Efficiency:** Handles large sets of images efficiently using asyncio.
- **Visualization:** Uses Matplotlib for visualizing denoised images and provides options for saving them.

### Usage

1. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script:**

   ```bash
   python professional_version/professional_version.py
   ```

3. **Results:**

   - Denoised images will be displayed (if `show_images=True`) and saved to the `Denoised_Images` directory.
   - Modify the script parameters or add additional functionality as needed.