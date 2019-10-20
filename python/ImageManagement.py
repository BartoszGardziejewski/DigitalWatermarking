from skimage import io

image = io.imread("./sources/python.bmp")

print(image.shape)

imageR = image[..., 0]
imageG = image[..., 1]
imageB = image[..., 2]

io.imsave("./sources/pythonR.bmp", imageR)
io.imsave("./sources/pythonG.bmp", imageG)
io.imsave("./sources/pythonB.bmp", imageB)
