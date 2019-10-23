from matplotlib import pyplot as plt
from skimage.io import imshow
from skimage.color import *

from python.src.common.ImageManagement import *
from python.src.patchwork.PatchworkUtils import *


image = loadImageAndConvertToYUV()
imshow(yuv2rgb(image))
plt.show()

image = changeLuminanceOfPixel(image, 25, 25, 1)

imshow(yuv2rgb(image))
plt.show()



