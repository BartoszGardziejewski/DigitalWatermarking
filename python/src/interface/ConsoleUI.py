import os

from python.src.common import ImageManagement
from python.src.common.ImageGeneration import generateRandomImageWithParametersLike
from python.src.lsb import Algorithm as LsbAlgorithm
from python.src.patchwork import Algorithm as PatAlgorithm


def startInterface():
    images = _getImagesToWatermark()

    for image, file in zip(images, images.files):
        algorithm, arguments = _getAlgorithmWithArguments(image, file)
        watermarkedImage = _watermarkImage(image, algorithm, arguments)
        _saveImage(watermarkedImage, file.replace("\\", "/"))


def _getImagesToWatermark():
    resourcesPath = ImageManagement.resourcesDirPath
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


def _selectImageToUseAsWaterMark(image, file):
    while True:
        imagePath = input(
            f'Please specify image to be used as watermark for {file} (press Enter to use random image from example '
            f'collection): ')
        if not imagePath:
            return generateRandomImageWithParametersLike(image)
        imagePath = ImageManagement.resourcesDirPath + imagePath
        if os.path.isfile(imagePath):
            break
        else:
            print(f'ERROR: Given file <{imagePath}> is not valid, please try again.')
    return ImageManagement.loadImage(imagePath)


def _getPatchworkSecretKey(file):
    return input(f'Please specify the secret key used to watermark the {file}: ')


def _getPercentageOfPixelsToWatermark(file):
    while True:
        percentage = input(f'Please specify the percentage (0..1] of pixels to watermark the {file}: ')
        if 0 < float(percentage) <= 1:
            return percentage
        else:
            print(f'ERROR: Given percentage {percentage} not in range (0..1]. Please try again.')


def _getAlgorithmWithArguments(image, file):
    switch = {
        'LSB': (LsbAlgorithm, {'embeddedImage': _selectImageToUseAsWaterMark(image, file)}),
        'PAT': (PatAlgorithm, {'key': _getPatchworkSecretKey(file),
                               'percentage': _getPercentageOfPixelsToWatermark(file)}),
    }

    while True:
        choice = input(f'Please specify algorithm to use to watermark the image {[key for key in switch.keys()]}: ')
        algorithmWithArguments = switch.get(choice, None)
        if algorithmWithArguments:
            return algorithmWithArguments
        else:
            print(f'ERROR: Unknown algorithm - {choice}. Please try again.')


def _saveImage(watermarkedImage, imagePath):
    if watermarkedImage is not None:
        splitName = imagePath.split("/")
        splitName[-2] = ImageManagement.resultsDirName
        resultsDir = "/".join(splitName[:-1])
        os.makedirs(resultsDir, exist_ok=True)
        outPath = "/".join(splitName)
        ImageManagement.saveImage(watermarkedImage, outPath)
    else:
        print(f'ERROR: Could not save watermarked image: <{imagePath}>')


def _watermarkImage(image, algorithm, arguments):
    if arguments:
        return algorithm.watermarkImage(image, **arguments)
    else:
        return algorithm.watermarkImage(image)
