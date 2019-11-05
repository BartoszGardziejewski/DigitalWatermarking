from skimage import io
from skimage import color


# Loads from resource folder
def loadImageAndConvertToYUV(fileName="python.bmp"):
    image = io.imread("../resources/" + fileName)
    return color.rgb2yuv(image)


# Loads from resources folder
def loadImage(fileName="python.bmp"):
    return io.imread("../resources/" + fileName)


# Save image to resources folder
def saveImage(image, fileName="python.bmp"):
    io.imsave("../resources/" + fileName, image)

