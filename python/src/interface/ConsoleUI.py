import os
import functools

from python.src.common import ImageManagement
from python.src.common.ImageGeneration import generateRandomImageWithParametersLike
from python.src.lsb import Algorithm as LsbAlgorithm
from python.src.patchwork import Algorithm as PatAlgorithm


def startInterface():
    switch = {
        'E': _encodeImages,
        'D': _decodeImages,
    }

    while True:
        choice = input(f'Do you wish to Encode or Decode images? {[key for key in switch.keys()]}: ')
        func = switch.get(choice, None)
        if func:
            func()
            break
        else:
            print(f'ERROR: Unknown choice - {choice}. Please try again.')

    print('Exit')


def _encodeImages():
    images = _getImages()
    for image, file in zip(images, images.files):
        algorithm, kwargs = _getAlgorithmWithArguments(image, file)
        watermarkedImage = _watermarkImage(image, algorithm, kwargs)
        _saveImage(watermarkedImage, file.replace("\\", "/"))
        print(f"Encoded file: {file}")


def _decodeImages():
    images = _getImages(ImageManagement.resultsDirPath)
    for image, file in zip(images, images.files):
        algorithm, kwargs = _getAlgorithmWithArguments(image, file)
        result = _decodeImage(image, algorithm, kwargs)


def _getImages(exampleCollection=ImageManagement.resourcesDirPath):
    while True:
        imagePath = input('Please specify image or directory with images (press Enter to use example collection): ')
        imagePath = exampleCollection + imagePath
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
    while True:
        key = input(f'Please specify the secret key [0 .. 4,294,967,295] to watermark the {file} with: ')
        try:
            key = int(key)
            if not 0 <= key <= 4294967295:
                print(f'ERROR: Key {key} not in range [0 .. 4,294,967,295]. Please try again.')
                continue
            return key
        except ValueError as e:
            print(f'ERROR: {e}. Please try again.')
            continue


def _getAlgorithmWithArguments(image, file):
    switch = {
        'LSB': (LsbAlgorithm, {'embeddedImage': functools.partial(_selectImageToUseAsWaterMark, image, file)}),
        'PAT': (PatAlgorithm, {'key': functools.partial(_getPatchworkSecretKey, file)}),
    }

    while True:
        choice = input(f'Please specify algorithm to use to watermark the image {[key for key in switch.keys()]}: ')
        algorithmWithArguments = switch.get(choice, None)

        if algorithmWithArguments:
            algorithm, kwargs = algorithmWithArguments
            for key, value in kwargs.items():
                kwargs[key] = value()
            return algorithm, kwargs

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


def _watermarkImage(image, algorithm, kwargs):
    if kwargs:
        return algorithm.watermarkImage(image, **kwargs)
    else:
        return algorithm.watermarkImage(image)


def _decodeImage(image, algorithm, kwargs):
    if kwargs:
        return algorithm.decodeImage(image, **kwargs)
    else:
        return algorithm.decodeImage(image)
