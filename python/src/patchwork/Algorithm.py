from skimage import img_as_ubyte
from skimage.color import rgb2hsv, hsv2rgb
import numpy as np
from math import sqrt


def _getColorFormatConversionAlgorithms():
    luminanceChannel = 2
    return rgb2hsv, hsv2rgb, luminanceChannel


def _getLuminanceValueChange():
    return 0.005


# W. Bender, D. Gruhl, N. Morimoto, A. Lu,
# "Techniques for Data Hiding" IBM Systems Journal, Vol. 35 Nos 3&4, 1996
def _getNumberOfPixelPairsToChange(image):
    rows = image.shape[0]
    columns = image.shape[1]
    numberOfPixels = rows * columns

    typicalNumber = 30000
    limitingMultiplier = 2  # we don't want to alter too many pixels in a single image

    if numberOfPixels >= limitingMultiplier * typicalNumber:
        return typicalNumber
    else:
        percentageOfPixels = 1 / limitingMultiplier
        return int(percentageOfPixels * numberOfPixels)


def watermarkImage(image, key):
    convert, convertBack, luminanceChannel = _getColorFormatConversionAlgorithms()
    image = convert(image)

    mask = _getMaskOfDeltas(image, key)

    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            if image[row, col, luminanceChannel] + mask[row, col] < 1:
                image[row, col, luminanceChannel] += mask[row, col]
            elif image[row, col, luminanceChannel] - mask[row, col] > 0:
                image[row, col, luminanceChannel] -= mask[row, col]

    image = convertBack(image)

    image[image < -1] = -1
    image[image > 1] = 1

    image = img_as_ubyte(image)

    return image


def decodeImage(image, key):
    convert, _, luminanceChannel = _getColorFormatConversionAlgorithms()
    image = convert(image)
    mask = _getMaskOfDeltas(image, key)

    expectedControlSum = 280 * _getLuminanceValueChange() * sqrt(_getNumberOfPixelPairsToChange(image))
    controlSumOfModifiedImage = _calculateControlSum(image, luminanceChannel, mask)

    certaintyTheImageIsEncoded = (100 * controlSumOfModifiedImage) / expectedControlSum
    certaintyTheImageIsEncoded = max(min(100., certaintyTheImageIsEncoded), 0.)

    print(f"There's {certaintyTheImageIsEncoded}% probability that the image is encoded using key: {key}")
    return certaintyTheImageIsEncoded


def _getMaskOfDeltas(image, key):
    rows = image.shape[0]
    columns = image.shape[1]

    mask = np.zeros(rows * columns, dtype=np.float)
    n = _getNumberOfPixelPairsToChange(image)

    mask[:n] = _getLuminanceValueChange()
    mask[n:2 * n] = -1 * _getLuminanceValueChange()

    np.random.seed(key)
    np.random.shuffle(mask)

    return mask.reshape((rows, columns))


def _calculateControlSum(image, luminanceChannel, mask):
    rows = mask.shape[0]
    columns = mask.shape[1]

    controlSum = 0
    for row in range(rows):
        for column in range(columns):
            if mask[row, column] > 0:
                controlSum += image[row, column, luminanceChannel]
            elif mask[row, column] < 0:
                controlSum -= image[row, column, luminanceChannel]
    return controlSum
