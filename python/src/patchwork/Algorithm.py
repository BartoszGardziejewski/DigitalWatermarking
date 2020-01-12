import random


def watermarkImage(image, key, percentage):
    rows = image.shape[0]
    columns = image.shape[1]
    valueChange = 1

    for dimension in range(image.ndim):
        rows_to_change, columns_to_change = _getPixelsToChange(rows, columns, percentage, key, valueChange)
        for row in rows_to_change:
            for column in columns_to_change:
                if image[row][column][dimension] < 256 - valueChange:
                    image[row][column][dimension] += valueChange
                if image[row - 1][column - 1][dimension] > 0 + valueChange:
                    image[row - 1][column - 1][dimension] -= valueChange
    return image


def _getPixelsToChange(rows, columns, percentage, key, valueChange):
    random.seed(key)
    rows = _getIndexesToChange(rows, percentage, valueChange)
    columns = _getIndexesToChange(columns, percentage, valueChange)
    return rows, columns


def _getIndexesToChange(size, percentage, valueChange):
    return random.sample(range(valueChange, size - valueChange), int(percentage * size))
