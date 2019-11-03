import itertools

from math import floor

from python.src.common.ImageManagement import *
from python.src.common.ImageGeneration import *


def embedRandomNoiseInImage(baseImage):
    embedImage = generateRandomImageWithParametersLike(baseImage)
    embedImageInAnotherImage(image, embedImage)


def embedImageInAnotherImage(baseImage, embeddedImage):

    for currentColor in range(baseImage.shape[2]):
        for pixelRowNumber, pixelColumnNumber in createIteratorOverPixels(baseImage[..., currentColor]):
            currentBasePixel = baseImage[..., currentColor][pixelRowNumber][pixelColumnNumber]
            currentEmbeddedPixel = embeddedImage[..., currentColor][pixelRowNumber][pixelColumnNumber]
            embeddedMSB = (currentEmbeddedPixel / 128) == 1
            baseImage[..., currentColor][pixelRowNumber][pixelColumnNumber] = \
                calculateValueWithNewLSB(currentBasePixel, embeddedMSB)
            embeddedImage[..., currentColor][pixelRowNumber][pixelColumnNumber] = 128 * embeddedMSB

    saveImage(baseImage, "python_random.bmp")
    saveImage(embeddedImage, "embedded_image.bmp")


def calculateValueWithNewLSB(baseLSB, embeddedMSB):
    return (baseLSB & ~1) | embeddedMSB


def createIteratorOverPixels(greyImage):
    imageRows = range(greyImage.shape[0])
    imageColumns = range(greyImage.shape[1])
    return itertools.product(imageRows, imageColumns)


image = loadImage("python.bmp")
embedRandomNoiseInImage(image)
