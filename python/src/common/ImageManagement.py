from skimage import io

resourcesDirPath = '../resources/'
resultsDirName = 'results'
resultsDirPath = f'../{resultsDirName}/'


# Loads from resources folder
def loadImage(imagePath=resourcesDirPath + "python.bmp"):
    return io.imread(imagePath)


def loadImages(imagesPath=resourcesDirPath + "test", postfix="/*.bmp"):
    return io.ImageCollection(imagesPath + postfix)


def saveImage(image, imagePath=resultsDirPath + "python.bmp"):
    io.imsave(imagePath, image)
