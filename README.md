# Image-Edge-Detection-with-Taylor-Series-and-Finite-Difference
This Python project implements Taylor series derivatives and finite difference methods to detect edges in images, efficiently highlighting the boundaries between objects. The approach converts RGB images to grayscale, then computes both first and second derivatives to pinpoint edges.

# I. INTRODUCTION
In computer science, image processing has risen in significance as a result of the increasing popularity of digital image processing in a variety of applications. One of the basic operations in image processing is edge detection, which is used to identify the boundaries between objects in an image. Edge detection in digital image processing is usually done using numerical techniques such as Taylor series derivatives and finite differences. 

The Taylor series is a mathematical tool that can approximate a function by a series of polynomial terms. By computing the derivatives of the Taylor series, it is possible to estimate the slope of a function at any point. Additionally, we are able to calculate the derivatives of the function using numerical approximations using finite difference methods. Both of these techniques can be used to calculate an image's gradient and locate the boundaries between objects, making them useful for image edge detection. In this report, we will go over how Python programs that use Taylor series derivatives and finite difference techniques for image edge detection were implemented.

# II. METHODOLOGY
Our initial step starts with importing the essential libraries for basic image processing and mathematical calculations. The `cv2.imread()` method is then used to import the image that has to be processed. This function imports the picture from our local directory. 

The RGB picture is then turned into grayscale using the method `rgbToGreyscale()`, which we define next. This is accomplished by taking the dot product of the red, green, and blue channels' first three coefficients, as indicated by the expression `grey_img = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])`. The method returns a grayscale picture as a result.

We then define two more functions: `firstDerivative()` and `secondDerivatives()`. These functions calculate the first and second derivatives of the grayscale image using the Taylor series and finite difference methods.

Using central differences, the first derivative is calculated using the previously generated grayscale picture using the `firstDerivative()` function. This is achieved by using the formula `fx[x,y] = (img[x,y+h] - img[x,y-h])/ 2*h`, where h is a small constant that sets the size of the neighborhood over which the derivative is computed. The border pixels are excluded from this calculation. The function returns the generated first derivative picture.

Similar to the previous one, the `secondDerivatives()` method uses central differences to compute the second derivative from the converted grayscale picture. In order to compute the second derivative at each pixel position, the formula `fxx[x,y] = (img[x,y+h] - 2*img[x,y] + img[x,y-h]) / h*h` is calculated for all pixels to obtain the edge. The function returns the second derivative picture that results.

Finally, after defining all the functions above, we can convert the input image to grayscale using the `rgbToGreyscale()` function. We then apply the `firstDerivative()` and `secondDerivatives()` functions to the grayscale image to obtain the first and second derivative images, respectively. In order to save the result, we will utilize the `cv2.imwrite()` function to store the generated image locally.


# III. Formulas Used

1. **Grayscale Conversion**: 
![equation](https://latex.codecogs.com/svg.latex?\large&space;\text{grey\_img}=\text{image}[...,:3]*[0.2989,%200.5870,%200.1140])

2. **First Derivative using Central Differences**:
![equation](https://latex.codecogs.com/svg.latex?f'_x(x,y)%20=%20\frac{\text{img}[x,y+h]%20-%20\text{img}[x,y-h]}{2h})
Where \( h \) is a small constant defining the neighborhood for the derivative.

3. **Second Derivative using Central Differences**:
![equation](https://latex.codecogs.com/svg.latex?f''_x(x,y)%20=%20\frac{\text{img}[x,y+h]%20-%202%20\times%20\text{img}[x,y]%20+%20\text{img}[x,y-h]}{h^2})


# IV. Results
<img src="https://github.com/ramzyizza/Image-Edge-Detection-with-Taylor-Series-and-Finite-Difference/assets/89899122/f073bba5-4c20-4f13-ae0c-b57b92eb457c" width="45%"></img> <img src="https://github.com/ramzyizza/Image-Edge-Detection-with-Taylor-Series-and-Finite-Difference/assets/89899122/7efd4062-530d-4280-8e5f-a88ec5165baa" width="45%"></img> <img src="https://github.com/ramzyizza/Image-Edge-Detection-with-Taylor-Series-and-Finite-Difference/assets/89899122/815f2139-f356-465c-987e-9e307e281bab" width="45%"></img> <img src="https://github.com/ramzyizza/Image-Edge-Detection-with-Taylor-Series-and-Finite-Difference/assets/89899122/70259420-b871-4f66-be14-50afa95a20ec" width="45%"></img> 

 # V. Evaluation
 We have successfully implemented Taylor series derivatives and finite difference methods for image edge detection in Python. The implementation was done by converting the RGB image into grayscale and then calculating the first and second derivatives of the grayscale image using the Taylor series and finite difference methods. The implementation was then evaluated by visually analyzing the resulting images. The grayscale image showed the original image in grayscale, while the first and second derivative images showed the edges of the image. 

Observing the result of both derivative images, we can clearly see that the first derivative successfully separates the subject and the background with white lines, indicating the edge of the subject. Meanwhile, the second derivative also results almost similar to the first derivative, but with the exception of capturing more noises and textures on the upper pen area and some proportion of the background, implying that it is very sensitive to the noise. This can be further improved with some pre-image processing processes, in the beginning, such as denoise in order to achieve higher accuracy in detecting edges and prevent false edge detection on noises parts of the image.





