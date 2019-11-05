from python.src.common import ImageManagement
from python.src.lsb import Algorithm as LsbAlgorithm


def startInterface():
    baseImageName = input('please specify image that will be watermarked: ')
    baseImage = ImageManagement.loadImage(baseImageName)
    watermarkedImage = LsbAlgorithm.embedRandomNoiseInImage(baseImage)
    ImageManagement.saveImage(watermarkedImage, "watermarked_" + baseImageName)
