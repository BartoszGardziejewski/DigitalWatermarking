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
        watermarkAndSaveImage(algorithm, image, watermark, file.replace("\\", "/"))


def getImagesToWatermark():
    resourcesPath = ImageManagement.resourcesDir
    while True:
        imagePath = input('Please specify image or directory with images to watermark (press Enter to use example '
                          'collection): ')
        imagePath = resourcesPath + imagePath
        if os.path.isfile(imagePath):
            return ImageManagement.loadImages(imagePath, "")
        elif os.path.isdir(imagePath):
            return ImageManagement.loadImages(imagePath)
        else:
            print(f'ERROR: Given path <{imagePath}> is not valid, please try again.')


def selectImageToUseAsWaterMark(image, file):
    while True:
        imagePath = input(
            f'Please specify image to be used as watermark for {file} (press Enter to use random image from example '
            f'collection): ')
        if not imagePath:
            return generateRandomImageWithParametersLike(image)
        imagePath = ImageManagement.resourcesDir + imagePath
        if os.path.isfile(imagePath):
            break
        else:
            print(f'ERROR: Given file <{imagePath}> is not valid, please try again.')
    return ImageManagement.loadImage(imagePath)


def selectAlgorithmToUse():
    while True:
        algorithm = input('Please specify algorithm to use to watermark the image (LSB | PAT): ')
        if algorithm == "LSB":
            return LsbAlgorithm
        elif algorithm == "PAT":
            return PatAlgorithm
        else:
            print(f'ERROR: Unknown algorithm {algorithm}. Please try again.')


def watermarkAndSaveImage(algorithm, image, watermark, imagePath):
    watermarkedImage = algorithm.watermarkImage(image, watermark)
    splitName = imagePath.split("/")
    splitName[-1] = "watermarked_" + splitName[-1]
    outPath = "/".join(splitName)
    ImageManagement.saveImage(watermarkedImage, outPath)
