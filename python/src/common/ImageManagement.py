from skimage import io
from skimage import color

resourcesDirPath = '../resources/'
resultsDirName = 'results'
resultsDirPath = f'../{resultsDirName}/'


# Loads from resource folder
def loadImageAndConvertToYUV(imagePath=resourcesDirPath + "python.bmp"):
    image = io.imread(imagePath)
    return color.rgb2yuv(image)


# Loads from resources folder
def loadImage(imagePath=resourcesDirPath + "python.bmp"):
    return io.imread(imagePath)


def loadImages(imagesPath=resourcesDirPath + "test", postfix="/*.bmp"):
    return io.ImageCollection(imagesPath + postfix)


def saveImage(image, imagePath=resultsDirPath + "python.bmp"):
    io.imsave(imagePath, image)
