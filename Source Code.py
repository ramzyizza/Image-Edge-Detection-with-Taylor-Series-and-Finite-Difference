import numpy as np #for mathematical operation purposes
import cv2 as cv #for basic image processing

# We first import the image from local with .imread()
img = cv.imread('pen_image.png')

# Create the function that will convert the image from RGB to Greyscale
def rgbToGreyscale(image):
    # take the dot product of the image first three channels (Red, Green, Blue)
    grey_img = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]) # Coefficients
    return grey_img

# Create the function that calculate the first derivative of taylor series
def firstDerivative(img):
    #convert the gray image to array
    fx = np.zeros_like(img)

    for x in range(1, img.shape[0]-1):
        for y in range(1, img.shape[1]-1): #with respect to both x and y axis
            h = 1 #smaller h value gives better accuracy
            fx[x,y] = (img[x,y+h] - img[x,y-h])/ 2*h
            # Original Formula = F'(x) = (F(x+h) - F(x-h)) / 2h
    return fx

# Create the function that calculate the second derivative of taylor series
def secondDerivatives(img):
    #convert the gray image to array
    fxx = np.zeros_like(img)

    # Compute the second-order derivatives using central differences
    for x in range(1, img.shape[0]-1):
        for y in range(1, img.shape[1]-1): #with respect to both x and y axis
            h = 1 
            fxx[x,y] = (img[x,y+h] - 2*img[x,y] + img[x,y-h]) / h*h
                        # Original Formula = F"(x) = (F(x+h) - 2F(x) + f(x-h)) / h^^2
    return fxx

# Convert the image to grayscale
grey_img = rgbToGreyscale(img)

# Calculate the first derivative using the function
fx = firstDerivative(grey_img)

# Calculate the second derivative using the function
fxx = secondDerivatives(grey_img)

# Output the result
cv.imwrite("grey_image.jpg", grey_img)
cv.imwrite("first_derivative.jpg", fx)
cv.imwrite("second_derivative.jpg", fxx)