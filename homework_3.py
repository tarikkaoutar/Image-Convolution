from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# Function to load an image using Pillow
def load_image(file_path):
    with Image.open(file_path) as img:
        img_gray = img.convert('L')  # Convert to grayscale
        return np.array(img_gray)

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

# Function to create a simple averaging filter
def create_averaging_filter(size):
    return np.ones((size, size)) / (size ** 2)

# Load the image (replace 'test.jpg' with the actual path to your image)
image_path = '/content/柴犬飛飛.jpg'  # Assuming the image is in the same directory
image = load_image(image_path)

# Creating a simple averaging filter for blurring (for Unsharp Mask)
averaging_filter = create_averaging_filter(5)

# Applying Unsharp Mask
blurred_image = convolve(image, averaging_filter)
unsharp_masked_image = image - blurred_image

# Applying Edge Detection
edge_detection_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
edge_detected_image = convolve(image, edge_detection_kernel)

# Displaying the results
plt.figure(figsize=(10, 8))

plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(132), plt.imshow(unsharp_masked_image, cmap='gray'), plt.title('Unsharp Mask')
plt.subplot(133), plt.imshow(edge_detected_image, cmap='gray'), plt.title('Edge Detection')

plt.tight_layout()
plt.show()