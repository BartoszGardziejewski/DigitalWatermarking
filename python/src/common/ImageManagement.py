from skimage import io
from skimage import color

resourcesDir = '../resources/'


# Loads from resource folder
def loadImageAndConvertToYUV(imagePath=resourcesDir + "python.bmp"):
    image = io.imread(imagePath)
    return color.rgb2yuv(image)


# Loads from resources folder
def loadImage(imagePath=resourcesDir + "python.bmp"):
    return io.imread(imagePath)


def loadImages(imagesPath=resourcesDir + "test", postfix="/*.bmp"):
    return io.ImageCollection(imagesPath + postfix)


def saveImage(image, imagePath=resourcesDir + "python.bmp"):
    io.imsave(imagePath, image)
