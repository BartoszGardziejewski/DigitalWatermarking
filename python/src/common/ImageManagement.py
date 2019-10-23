from skimage import io
from skimage import color

#Does its work in resources folder
def convertImageToMasksAndSave(fileName = "python.bmp"):
    baseDir = "../../resources"
    image = io.imread(baseDir + fileName)

    imageR = image[..., 0]
    imageG = image[..., 1]
    imageB = image[..., 2]

    io.imsave(baseDir + fileName.replace(".","R."), imageR)
    io.imsave(baseDir + fileName.replace(".","G."), imageG)
    io.imsave(baseDir + fileName.replace(".","B."), imageB)

#Loads from resource folder
def loadImageAndConvertToYUV(fileName = "python.bmp"):
    image = io.imread("../../resources/" + fileName)
    return color.rgb2yuv(image)

#Loads from resources folder
def loadImage(fileName = "python.bmp"):
    return io.imread("../../resources/" + fileName)



