import os

from python.src.common import ImageManagement
from python.src.common.ImageGeneration import generateRandomImageWithParametersLike
from python.src.lsb import Algorithm as LsbAlgorithm
from python.src.patchwork import Algorithm as PatAlgorithm


def startInterface():
    images = getImagesToWatermark()
    algorithm = selectAlgorithmToUse()

    for image, file in zip(images, images.files):
        watermark = selectImageToUseAsWaterMark(image, file)
        wtrImage = watermarkAndSaveImage(algorithm, image, watermark, file.replace("\\", "/"))
        extractWatermarkAndSaveIt(algorithm, wtrImage, file.replace("\\", "/"))

def getImagesToWatermark():
    imagePath = 'test/python.bmp'
    # imagePath = input('please specify image or directory with images that will be watermarked: ')
    if os.path.isfile("../resources/" + imagePath):
        return ImageManagement.loadImages(imagePath, "")
    elif os.path.isdir("../resources/" + imagePath):
        return ImageManagement.loadImages(imagePath)
    else:
        print("given path is not valid")


def selectImageToUseAsWaterMark(image, file):
    imagePath = "watermark.bmp"
    # imagePath = input('please specify image to be used as watermark for '+file+' (empty means use random image): ')
    if not imagePath:
        return generateRandomImageWithParametersLike(image)
    else:
        if os.path.isfile("../resources/" + imagePath):
            return ImageManagement.loadImage(imagePath)
        else:
            print("given path is not valid")


def selectAlgorithmToUse():
    algorithmName = 'LSB'
    # algorithmName = input('please specify algorithm to use to watermark image (LSB , PAT): ')
    if algorithmName == "LSB":
        return LsbAlgorithm
    if algorithmName == "PAT":
        return PatAlgorithm
    else:
        print("unknown algorithm")

def watermarkAndSaveImage(algorithm, image, watermark, imagePath):
    watermarkedImage = algorithm.watermarkImage(image, watermark)
    splitName = imagePath.split("/")
    splitName[-1] = "watermarked_" + splitName[-1]
    outPath = "/".join(splitName)
    ImageManagement.saveImage(watermarkedImage, outPath)
    return watermarkedImage

def extractWatermarkAndSaveIt(algorithm, watermarkedImage, imagePath):
    extractedWatermark = algorithm.extractWatermarkFromImage(watermarkedImage)
    splitName = imagePath.split("/")
    splitName[-1] = "watermark_" + splitName[-1]
    outPath = "/".join(splitName)
    ImageManagement.saveImage(extractedWatermark, outPath)
    return extractedWatermark