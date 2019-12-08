from skimage import io
from skimage import color


# Loads from resource folder
def loadImageAndConvertToYUV(fileName="python.bmp"):
    image = io.imread("../resources/" + fileName)
    return color.rgb2yuv(image)


# Loads from resources folder
def loadImage(fileName="python.bmp"):
    return io.imread("../resources/" + fileName)


def loadImages(imagesPath="./test", postfix="/*.bmp"):
    return io.ImageCollection("../resources/" + imagesPath + postfix)


# Save image to resources folder
def saveImage(image, imagePath="python.bmp"):
    io.imsave("../resources/" + imagePath, image)

