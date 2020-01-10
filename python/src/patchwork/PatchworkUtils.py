from skimage import io


def changeLuminanceOfPixel(image, x, y, value):
    image[x, y, 0] += value
    return image
