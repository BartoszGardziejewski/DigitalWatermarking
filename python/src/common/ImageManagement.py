from skimage import io

resourcesDirPath = '../resources/'
resultsDirName = 'results'
resultsDirPath = f'../{resultsDirName}/'


# Loads from resources folder
def loadImage(imagePath=resourcesDirPath + "python.bmp"):
    return io.imread(imagePath)


def loadImages(imagesPath=resourcesDirPath + "test", postfix="/*.*"):
    return io.ImageCollection(imagesPath + postfix)


def saveImage(image, imagePath=resultsDirPath + "python.bmp"):
    postfix = imagePath.split('.')[-1]
    if any(p in postfix for p in ['jpg', 'jpeg']):
        print(
            f"WARNING: {postfix.capitalize()} format may be problematic due to format's compression / optimalization.")
    io.imsave(imagePath, image)
