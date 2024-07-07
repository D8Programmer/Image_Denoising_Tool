import cv2
from pathlib import Path
import matplotlib.pyplot as plt

def denoise_image(image_path, gaussian_ksize=(5, 5), median_ksize=5, bilateral_d=9, bilateral_sigma_color=75, bilateral_sigma_space=75):
    """Denoise an image using Gaussian Blur, Median Blur, and Bilateral Filter."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image '{image_path}'")
        return
    
    # Denoising operations
    denoised_images = [
        cv2.GaussianBlur(image, gaussian_ksize, sigmaX=0),
        cv2.medianBlur(image, median_ksize),
        cv2.bilateralFilter(image, bilateral_d, bilateral_sigma_color, bilateral_sigma_space)
    ]
    
    # Plotting
    titles = ['Gaussian Blur', 'Median Blur', 'Bilateral Filter']
    fig, axs = plt.subplots(1, 3, figsize=(10, 4))
    for ax, denoised_image, title in zip(axs, denoised_images, titles):
        ax.imshow(cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB))
        ax.set_title(title)
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()

def get_image_files(directory):
    """Retrieve image files from the specified directory."""
    valid_extensions = {'.png', '.jpg', '.jpeg', '.jfif'}
    return [str(f) for f in Path(directory).iterdir() if f.suffix.lower() in valid_extensions]

def main(image_directory):
    """Main function to process images in the given directory."""
    image_files = get_image_files(image_directory)
    if not image_files:
        print(f"No valid image files found in '{image_directory}'.")
        return

    for image_file in image_files:
        denoise_image(image_file)

if __name__ == "__main__":
    main('Noisy_Images')
