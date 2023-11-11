
# HomeWork 1

## 1 - Gaussian Filter Creation
The values of σ can be chosen based on the filter size to ensure a proper Gaussian distribution
Write the custom function to create Gaussian filters

```bash
   G(x,y) = 1/2πσ^2 exp(- x^2 + y^2 / 2σ^2)
```

## 2- image loading 
We will use libraries like Pillow 

## 3 - apply Gaussian filter for convolution
We will loop over the picture and apply the Gaussian filter to each pixel

## 4- Compute PSNR
  
 Write the custom function to create PSNR
```bash
PSNR = 10.log(10) * (MAX^6/MSE)
```
Max: possible pixel value of the image
MSE: is calculated between the original and the filtered image




## Homework 2
## 1- Gaussian Filter Creation
The values of σ can be chosen based on the filter size to ensure a proper Gaussian distribution
Write the custom function to create Gaussian filters

```bash
   G(x,y) = 1/2πσ^2 exp(- x^2 + y^2 / 2σ^2)
```

## 2. Image loading 
The pillow will be used to load the image, which will then be converted to a grayscale Numpy array 


## 3- Apply Gaussian Filter
I
 will reuse the convolution function that was previously implemented 

## 4- Compute PSNR
  
 Write the custom function to create PSNR
```bash
PSNR = 10.log(10) * (MAX^6/MSE)
```
Max: possible pixel value of the image
MSE: is calculated between the original and the filtered image

## Note:  
Gaussian Filter with sigma values of 1, 10, and 30, all of size 3*3 
- Each filter is normalized, ensuring that its value sums up to 1
- Load the image using pillow and convert it to a Numpy array 
- Apply the Gaussian Filters using the convolution function and compute the PSNR
- Each filtered image compared to the original image

## HomeWork 3

### Comparison Results : 

- 3x3 Gaussian Filter: PSNR = 36.10
- 7x7 Gaussian Filter: PSNR = 34.99
- 11x11 Gaussian Filter: PSNR = 34.99

The filter size increases, and the PSNR slightly decreases. A larger filter size means more blurring
Each pixel's new value is the avg of a large number of surrounding pixels
The slight reduction in PSNR with larger filters indicates that the image losing some of its original quality due to an increase in the blurring

- Sigma 1 Gaussian Filter: PSNR = 36.10
- Sigma 10 Gaussian Filter: PSNR = 35.34
- Sigma 30 Gaussian Filter: PSNR = 35.34

The PSNR decreases as the Sigma value increases 
The sigma in a Gaussian filter determines how spread out and how intense the blur is
A higher sigma results in a more spread out and intense blur
A decrease in PSNR with higher sigma values indicates a loss in fidelity to the original image due to increased blurring

### Meaning of PSNR Values

- PSNR is a measure used to assess the quality of a reconstructed or processed image compared to its original version
- Higher PSNR values typically indicate better quality, meaning the processed image is closer to the original
- The PSNR values you have obtained are all above 30 d, which generally indicates good quality for image processing tasks
- Removing noise or unwanted details (higher blurring) and keeping the original quality and details of the image

### Conclusion :
Filters with smaller sizes or lower sigma values maintain image quality
Filters with larger sizes or higher sigma values blur the image more, lowering the PSNR
Each choice of filter size and sigma value serves different purposes 

## Homework 4

##  Unsharp mask

### 1 - Load Image 
   We will use Pillow to load the image
### 2 - unsharp Mask App
We going to create a blurred version of the image. We can use a simple average filter for this purpose and then subtract it from the original image to create the Unsharp mask 

### 3 - Edge Detection  Mask App
We will apply the provided Edge detection mask using the custom convolution function

### 4 - Display Results 
We will use matplotlib.pyplot to display the results
