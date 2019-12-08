import itertools

import math


def watermarkImage(baseImage, embeddedImage):
    watermarkedImage = baseImage[:]
    if baseImage.shape[2] > embeddedImage.shape[2]:
        colorsRange = range(embeddedImage.shape[2])
    else:
        colorsRange = range(baseImage.shape[2])

    for currentColor in colorsRange:
        for pixelRowNumber, pixelColumnNumber in createIteratorOverPixels(baseImage[..., currentColor]):
            currentBasePixel = baseImage[..., currentColor][pixelRowNumber][pixelColumnNumber]
            currentEmbeddedPixel = embeddedImage[..., currentColor][pixelRowNumber % (len(embeddedImage)-1)][pixelColumnNumber % (len(embeddedImage)-1)]
            embeddedMSB = (math.floor((currentEmbeddedPixel / 128))) == 1
            watermarkedImage[..., currentColor][pixelRowNumber][pixelColumnNumber] = \
                calculateValueWithNewLSB(currentBasePixel, embeddedMSB)

    return watermarkedImage
# ./test/python.bmp
# watermark.bmp
def calculateValueWithNewLSB(baseLSB, embeddedMSB):
    bitShift = 0
    return (baseLSB & ~(1 << bitShift)) | (embeddedMSB << bitShift)


def createIteratorOverPixels(greyImage):
    imageRows = range(greyImage.shape[0])
    imageColumns = range(greyImage.shape[1])
    return itertools.product(imageRows, imageColumns)
