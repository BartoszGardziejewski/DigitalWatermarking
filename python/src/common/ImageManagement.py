from skimage import io
from skimage import color
from skimage.util import *
from skimage import exposure


# Loads from resource folder
def loadImageAndConvertToYUV(fileName = "python.bmp"):
    image = io.imread("../../resources/" + fileName)
    return color.rgb2yuv(image)

def convertToRGBAndSave(image, fileName = "output.bmp"):
    image = color.yuv2rgb(image)
    io.imsave("../../resources/" + fileName, image)

#Loads from resource folder
def saveImage(image, fileName = "python.bmp"):
    io.imsave("../../resources/" + fileName, image)

# Loads from resources folder
def loadImage(fileName = "python.bmp"):
    return io.imread("../../resources/" + fileName)


# Save image to resources folder
def saveImage(image, fileName = "python.bmp"):
    io.imsave("../../resources/" + fileName, image)

