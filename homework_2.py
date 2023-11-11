import numpy as np
from PIL import Image

# Gaussian filter creation function
def create_gaussian_filter(size, sigma):
    kernel = np.fromfunction(lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2) / (2*sigma**2)), (size, size))
    return kernel / np.sum(kernel)

# Convolution function
def convolve(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape

    # Padding
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='edge')

    # Convolution
    new_image = np.zeros_like(image)
    for y in range(image_height):
        for x in range(image_width):
            new_image[y, x] = np.sum(kernel * padded_image[y:y+kernel_height, x:x+kernel_width])
    return new_image

# PSNR calculation function
def compute_psnr(original_image, filtered_image):
    mse = np.mean((original_image - filtered_image) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

# Image loading function using Pillow
def load_image(file_path):
    with Image.open(file_path) as img:
        img_gray = img.convert('L')  # Convert to grayscale
        return np.array(img_gray)

# Gaussian filters creation
gaussian_filter_sigma1 = create_gaussian_filter(3, 1)
gaussian_filter_sigma10 = create_gaussian_filter(3, 10)
gaussian_filter_sigma30 = create_gaussian_filter(3, 30)

# Load the image
image = load_image('/content/柴犬飛飛.jpg')

# Apply convolution with each filter
filtered_image_sigma1 = convolve(image, gaussian_filter_sigma1)
filtered_image_sigma10 = convolve(image, gaussian_filter_sigma10)
filtered_image_sigma30 = convolve(image, gaussian_filter_sigma30)

# Compute PSNR for each filtered image
psnr_sigma1 = compute_psnr(image, filtered_image_sigma1)
psnr_sigma10 = compute_psnr(image, filtered_image_sigma10)
psnr_sigma30 = compute_psnr(image, filtered_image_sigma30)

print("PSNR for sigma 1 Gaussian filter:", psnr_sigma1)
print("PSNR for sigma 10 Gaussian filter:", psnr_sigma10)
print("PSNR for sigma 30 Gaussian filter:", psnr_sigma30)