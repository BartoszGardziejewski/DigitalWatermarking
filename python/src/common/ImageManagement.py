from skimage import io

#Does its work in resources folder
def convertImageToMasksAndSave(fileName = "python.bmp"):
    image = io.imread("./resources/" + fileName)

    print(image.shape)

    imageR = image[..., 0]
    imageG = image[..., 1]
    imageB = image[..., 2]

    io.imsave("./resources/" + fileName.replace(".","R."), imageR)
    io.imsave("./resources/" + fileName.replace(".","G."), imageG)
    io.imsave("./resources/" + fileName.replace(".","B."), imageB)


