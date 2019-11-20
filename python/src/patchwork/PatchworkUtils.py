import random


luminanceDifference = 1.0


def changeLuminanceOfPixel(image, x, y, value):

    luminance = image[x, y, 0]

    if (luminance + value > 1.0):
        newLuminance = 1.0
    elif (luminance + value < 0.0):
        newLuminance = 0.0
    else:
        newLuminance = luminance + value

    image[x, y, 0] = newLuminance

    return image



def calculateDifferenceWithinPair(image, px1, px2):
    difference = image[px1[0], px1[1], 0] - image[px2[0], px2[1], 0]
    return difference



def encode(image, password, numOfPairs):
    """
    Size of pairs[][][] is as follows: pairs[numOfPairs][2][2]. Though pairs[x][0][1] == pairs[x][1][1] as they are neighbours at y axis.
    For first pair (pairs[x][0][...]) luminance is change with +luminanceDifference. Second pair (pairs[x][1][...]) with -luminanceDifference
    """
    pairs = []


    #
    # Populate pairs based on pseudo-random generation based on password
    #
    if( image.shape[0] > image.shape[1]):
        generatedRangeLimit = image.shape[1] - 1
    else:
        generatedRangeLimit = image.shape[0] - 1

    random.seed(password)
    coordinates = random.sample(range(1, generatedRangeLimit), numOfPairs * 2)

    for i in range(numOfPairs):
        y = coordinates.pop()
        x1 = coordinates.pop()
        x2 = x1+1
        pairs.append([[x1, y], [x2, y]])


    #
    # Change luminance for each pair
    #
    for pair in pairs:
        image = changeLuminanceOfPixel(image, pair[0][0], pair[0][1], luminanceDifference)
        image = changeLuminanceOfPixel(image, pair[1][0], pair[1][1], -luminanceDifference)


    #
    # Verify that watermark is mathematically correct.
    # S = 2*n*luminanceDifference, where S = E(fm(xi, yj)) - (fm(xi+1, yj)) and n = numOfPairs
    #
    controlSum = 0
    expectedSum = 2 * numOfPairs * luminanceDifference

    for pair in pairs:
        controlSum += calculateDifferenceWithinPair(image, pair[0], pair[1])

    #Adjust verification to IEEE computation error
    if(not (controlSum < expectedSum + 0.5 and controlSum > expectedSum - 0.5)):
        #ToDo
        print(controlSum, "is very different from ", expectedSum, ". Something went wrong. An exception should be raised here")

    return image





# CAUTION! OBSOLETE
def getLuminanceFromRGB(image, x, y):
    return R_LUM_FACTOR * image[x, y, 0] + G_LUM_FACTOR * image[x, y, 1] + B_LUM_FACTOR * image[x, y, 2]

# CAUTION! OBSOLETE Does not work as expected!!
def changeLuminanceOfPixelRGB(image, x, y, value):
    print("Old value:", getLuminanceFromRGB(image, x, y))
    luminance = getLuminanceFromRGB(image, x, y)

    if(luminance + value > 1.0):
        newLuminance = 1.0
    elif(luminance + value < 0.3):
        newLuminance = 0.3
    else:
        newLuminance = luminance + value

    r = R_LUM_FACTOR * newLuminance
    g = G_LUM_FACTOR * newLuminance
    b = B_LUM_FACTOR * newLuminance

    image[x, y, 0] = r
    image[x, y, 1] = g
    image[x, y, 2] = b

    print("New value: ", getLuminanceFromRGB(image, x, y), "\n")
    return image