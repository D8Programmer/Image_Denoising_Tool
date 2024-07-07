import cv2
import asyncio
import logging
from pathlib import Path
import matplotlib.pyplot as plt
from typing import List, Dict, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def read_image(image_path: str) -> cv2.Mat:
    """Read an image and convert it to RGB format."""
    image = await asyncio.to_thread(cv2.imread, image_path)
    if image is None:
        raise FileNotFoundError(f"Unable to load image '{image_path}'")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def apply_denoising(image: cv2.Mat) -> Dict[str, cv2.Mat]:
    """Apply denoising methods to an image."""
    return {
        'Noisy': image,
        'Median Blur': cv2.medianBlur(image, 5),
        'Bilateral Filter': cv2.bilateralFilter(image, 9, 75, 75),
        'Gaussian Blur': cv2.GaussianBlur(image, (5, 5), 0),
    }

def plot_images(images: Dict[str, cv2.Mat]) -> None:
    """Plot multiple images."""
    plt.figure(figsize=(10, 5))
    for i, (title, img) in enumerate(images.items(), start=1):
        plt.subplot(2, 2, i)
        plt.title(title)
        plt.imshow(img)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

async def save_images(images: Dict[str, cv2.Mat], save_path: Path) -> None:
    """Save images to the specified path."""
    save_path.mkdir(parents=True, exist_ok=True)
    tasks = [
        asyncio.to_thread(cv2.imwrite, str(save_path / f"{title.replace(' ', '_')}.png"), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        for title, img in images.items()
    ]
    await asyncio.gather(*tasks)
    logging.info(f"Saved images to {save_path}")

async def process_image(image_path: str, save_path: Optional[Path], show: bool) -> None:
    """Process and denoise a single image."""
    try:
        image = await read_image(image_path)
        denoised_images = apply_denoising(image)
        if show:
            plot_images(denoised_images)
        if save_path:
            await save_images(denoised_images, save_path)
    except FileNotFoundError as e:
        logging.error(e)

async def process_images(image_files: List[str], save_path: Optional[Path], show: bool) -> None:
    """Process multiple images concurrently."""
    await asyncio.gather(*[process_image(img, save_path, show) for img in image_files])

def get_image_files(directory: str) -> List[str]:
    """Retrieve image files from the specified directory."""
    valid_extensions = {'.png', '.jpg', '.jpeg', '.jfif'}
    return [str(f) for f in Path(directory).iterdir() if f.suffix.lower() in valid_extensions]

def main(image_directory: str, save_directory: Optional[str] = None, show_images: bool = False) -> None:
    """Main function to process images in the given directory."""
    image_files = get_image_files(image_directory)
    if not image_files:
        logging.info(f"No valid image files found in '{image_directory}'.")
        return

    save_path = Path(save_directory) if save_directory else None
    asyncio.run(process_images(image_files, save_path, show_images))

if __name__ == "__main__":
    main('Noisy_Images', 'Denoised_Images', show_images=False)
