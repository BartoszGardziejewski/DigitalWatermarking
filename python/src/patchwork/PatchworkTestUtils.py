from skimage import exposure


def changeGamma(image, change):
    return exposure.adjust_gamma(image, change)

def cropImage(image, x, y, width, heigth):
    return image[y:(y+heigth), x:(x+width)]