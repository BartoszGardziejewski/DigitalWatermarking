import os

from python.src.common import ImageManagement
from python.src.lsb import Algorithm as LsbAlgorithm


def startInterface():
    imagePath = input('please specify image or directory with images that will be watermarked: ')

    if os.path.isfile("../resources/" + imagePath):
        image = ImageManagement.loadImage(imagePath)
        watermarkAndSaveImage(image, imagePath)

    elif os.path.isdir("../resources/" + imagePath):
        images = ImageManagement.loadImages(imagePath)
        for image, file in zip(images, images.files):
            watermarkAndSaveImage(image, file.replace("\\", "/"))

    else:
        print("given path is not valid")


def watermarkAndSaveImage(image, imagePath):
    watermarkedImage = LsbAlgorithm.embedRandomNoiseInImage(image)
    splitName = imagePath.split("/")
    splitName[-1] = "watermarked_" + splitName[-1]
    outPath = "/".join(splitName)
    ImageManagement.saveImage(watermarkedImage, outPath)
