from matplotlib import pyplot as plt
from skimage.io import imshow
from skimage.color import *


from python.src.common.ImageManagement import *
from python.src.patchwork.PatchworkUtils import *



image = loadImageAndConvertToYUV("python.bmp")

imshow(color.yuv2rgb(image))
plt.show()


image = encode(image, "VeryLongPassword", 10)
convertToRGBAndSave(image, "output.bmp")


imshow(yuv2rgb(image))
plt.show()








