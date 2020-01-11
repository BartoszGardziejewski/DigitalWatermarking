import random
from skimage.color import rgb2yuv, yuv2rgb
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize, suppress=True)


def _getLuminanceValueChange():
    return 0.001


def _getPercentageOfPixelsToChange():
    return 0.25


def watermarkImage(image, key):
    image = rgb2yuv(image)

    rows = image.shape[0]
    columns = image.shape[1]
    valueChange = _getLuminanceValueChange()

    rows_to_change, columns_to_change = _getPixelsBasedOnKey(rows, columns, key)
    for row in rows_to_change:
        for column in columns_to_change:

            if image[row][column][0] + valueChange < 1:
                image[row][column][0] += valueChange
            else:
                image[row][column][0] = 1

            if image[row - 1][column - 1][0] - valueChange > 0:
                image[row - 1][column - 1][0] -= valueChange
            else:
                image[row - 1][column - 1][0] = 0

    return yuv2rgb(image)


def decodeImage(image, key):
    image = rgb2yuv(image)

    rows = image.shape[0]
    columns = image.shape[1]
    valueChange = _getLuminanceValueChange()
    luminanceChangeSum = 0

    rows_to_change, columns_to_change = _getPixelsBasedOnKey(rows, columns, key)
    for row in rows_to_change:
        for column in columns_to_change:
            luminanceChangeSum += image[row][column][0] - image[row - 1][column - 1][0]
    print(luminanceChangeSum, 2 * valueChange * len(rows_to_change))


def _getPixelsBasedOnKey(rows, columns, key):
    random.seed(key)
    rows = _getIndexesToChange(rows)
    columns = _getIndexesToChange(columns)
    return rows, columns


def _getIndexesToChange(size):
    return random.sample(range(1, size - 1), int(size * _getPercentageOfPixelsToChange()))
