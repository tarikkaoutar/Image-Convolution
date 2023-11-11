import numpy as np
from PIL import Image

# Function to create a Gaussian filter
def create_gaussian_filter(size, sigma=1.0):
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

# Function to compute PSNR
def compute_psnr(original_image, filtered_image):
    mse = np.mean((original_image - filtered_image) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

# Function to load an image using Pillow
def load_image(file_path):
    with Image.open(file_path) as img:
        img_gray = img.convert('L')  # Convert to grayscale
        return np.array(img_gray)

# Creating Gaussian filters
gaussian_filter_3x3 = create_gaussian_filter(3)
gaussian_filter_7x7 = create_gaussian_filter(7)
gaussian_filter_11x11 = create_gaussian_filter(11)

# Load the image
image = load_image('/content/柴犬飛飛.jpg')

# Apply the convolution with each filter
filtered_image_3x3 = convolve(image, gaussian_filter_3x3)
filtered_image_7x7 = convolve(image, gaussian_filter_7x7)
filtered_image_11x11 = convolve(image, gaussian_filter_11x11)

# Compute PSNR for each filtered image
psnr_3x3 = compute_psnr(image, filtered_image_3x3)
psnr_7x7 = compute_psnr(image, filtered_image_7x7)
psnr_11x11 = compute_psnr(image, filtered_image_11x11)

print("PSNR for 3x3 Gaussian filter:", psnr_3x3)
print("PSNR for 7x7 Gaussian filter:", psnr_7x7)
print("PSNR for 11x11 Gaussian filter:", psnr_11x11)
