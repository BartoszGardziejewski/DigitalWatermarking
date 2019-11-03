import numpy


def generateRandomImageWithParametersLike(baseImage):
    embedImage = numpy.random.random(baseImage.shape) * 255
    embedImage = embedImage.astype('uint8')
    return embedImage
