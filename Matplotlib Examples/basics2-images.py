import matplotlib.pyplot
import matplotlib.image
import numpy

# Reading an image with Matplotlib
# Image Reference: https://www.pexels.com/photo/rocky-cliff-under-cloudy-sky-6930991/
input_image = matplotlib.image.imread('Matplotlib Examples\scenery.jpg')
print(input_image)

# Displaying images with Matplotlib
matplotlib.pyplot.imshow(input_image)
matplotlib.pyplot.show()

# Displaying image histogram with Matplotlib
matplotlib.pyplot.hist(input_image.ravel(), bins=256,
                       range=(0.0, 255.0), fc='k', ec='k')
matplotlib.pyplot.ylabel('Number of Pixels')
matplotlib.pyplot.xlabel('Pixel Value')
matplotlib.pyplot.show()
