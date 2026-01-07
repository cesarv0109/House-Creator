def clampValueToRange(value, low, high):
    if value < low:
        return int(low)
    elif value > high:
        return int(high)
    else:
        return int(value)

# returnColor("130 -77 -68 -82 -13") should return [130, -77, 68]
# use split

def returnColor(line):
    intlst = []
    newlst = line.split(" ")
    for i in range(0, 3):
        intlst.append(int(newlst[i])) 
        
    return intlst

# test case
# returnLocation("1 2 3 4 5")
# should evaluate to
# [4, 5]

def returnLocation(line):
    intlst2 = []
    newlst2 = line.split(" ")
    for i in range(3, 5):
        intlst2.append(int(newlst2[i]))
    
    return intlst2

# It should return a Boolean, True if x and y are both greater than or equal to
# zero and x is less than width and y is less than height and False otherwise


def locationValid(x, width, y, height):
    if x >= 0 and y >= 0 and x < width and y < height :
        return True
    else:
        return False

# parameter color is a list with three #s
# The function should return a dictionary with three keys, r, g, and b.
# The values for these from respectively in the first, second, and third
# positions of the input list. Each value from the input list must be processed using
# clampValueToRange from milestone 1 to ensure values are
# integers in the range of 0 to 255 in order to get full credit.

# Test Cases:
# convertPixel([-10, 100.5, 300])
# should evaluate to
# {'r': 0, 'g': 100, 'b': 255}
# convertPixel([500, -5, 25.5])
# should evaluate to
# {'r': 255, 'g': 0, 'b': 25}


def convertPixel(color):
    colorDict = {}
    red = clampValueToRange((color[0]),0, 255)
    green = clampValueToRange((color[1]),0, 255)
    blue = clampValueToRange((color[2]),0, 255)
    
    colorDict['r'] = red
    colorDict['g'] = green
    colorDict['b'] = blue
    return colorDict


# The 1st parameter, called x is an integer representing the x location of the pixel
# The 2nd parameter, called y is an integer representing the y location of the pixel
# The 3rd parameter, called color is a dictionary of the type created by convertPixel
# The function should return a dictionary with the following key/value pairs:
# 'x': the x coordinate
# 'y': the y coordinate
# 'pixel': the color dictionary

# Test Cases:
# positionPixel(2,3,{'r': 0, 'g': 100, 'b': 255})
# should evaluate to
# {'pixel': {'r': 0, 'g': 100, 'b': 255}, 'x': 2, 'y': 3}

def positionPixel(x, y, color):
    pixelDict = {}
    pixelDict['pixel'] = color
    pixelDict['x'] = x
    pixelDict['y'] = y
    return pixelDict
    

# The 1st parameter, called pixel is a dictionary of the type created by positionPixel
# The 2nd parameter, called pixelList is a list of dictionaries of the type created
# by positionPixel
# The purpose of this function is to add new pixels to the pixel list.
# Test Cases:
# updateChangeList({'pixel': {'r': 0, 'g': 100, 'b': 255},
# 'x': 2, 'y': 3},[{'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': 4, 'y': 5}])
# should update pixelList to
# [{'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': 4, 'y': 5},
# {'pixel': {'r': 0, 'g': 100, 'b': 255}, 'x': 2, 'y': 3}] and return None


def updateChangeList(pixel, pixelList):
    pixelList.append(pixel)
    
# Test cases:
# file: example.txt
# 1 2 3 4 5
# 6 7 8 9 10
# pixels = []
# readPixelFile(pixels,'example.txt')
# should not return anything and update pixels to be
# [{'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': 4, 'y': 5}, {'pixel':
# {'r': 6, 'g': 7, 'b': 8}, 'x': 9, 'y': 10}]
# Test case 2:
# file: example.txt
# -75 200 100 800 -20
# 6 7 8 9 10
# pixels = []
# readPixelFile(pixels,'example.txt')
# should not return anything and update pixels to be
# [{'pixel': {'r': 0, 'g': 200, 'b': 100}, 'x': 800, 'y': -20}, {'pixel':
# {'r': 6, 'g': 7, 'b': 8}, 'x': 9, 'y': 10}]


def readPixelFile(pixels, filename):
    with open(filename) as fp:
        for line in fp:
            line = line.rstrip("\n")
            color = returnColor(line) # [r, g, b]
            location = returnLocation(line) # [x, y] 
            converted = convertPixel(color) #{r, g, b}
            colorD = positionPixel(location[0], location[1], converted)
            updateChangeList(colorD, pixels)
        print(pixels)
                 
# test case:
# generateEmptyPicture(2,3)
# should evaluate to
# [[{'r': 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}],
# [{'r': 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}],
# [{'r': 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}]]

def generateEmptyPicture(width, height):
    picture = []
    for i in range(height):
        row = []
        for n in range(width):
            Dict = {'r': 0, 'g': 0, 'b': 0}
            row.append(Dict)
        picture.append(row)
    return picture

# Test case:
# insertPixelList([{'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': 0,
# 'y': 0}, {'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': 1, 'y':
# 1}],[[{'r': 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}],
# [{'r': 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}],[{'r':
# 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}]])
# should evaluate to
# [[{'r': 1, 'g': 2, 'b': 3}, {'r': 0, 'g': 0, 'b': 0}], [{'r':
# 0, 'g': 0, 'b': 0}, {'r': 1, 'g': 2, 'b': 3}], [{'r': 0, 'g': 0
# 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}]]
# insertPixelList([{'pixel': {'r': 1, 'g': 2, 'b': 3}, 'x': -1,
# 'y': 0}, {'pixel': {'r': 4, 'g': 5, 'b': 6}, 'x': 1, 'y':
# 0}],[[{'r': 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}],
# [{'r': 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}],[{'r':
# 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}]])
# should evaluate to
# [[{'r': 0, 'g': 0, 'b': 0}, {'r': 4, 'g': 5, 'b': 6}], [{'r':
# 0, 'g': 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}], [{'r': 0, 'g':
# 0, 'b': 0}, {'r': 0, 'g': 0, 'b': 0}]]

def insertPixelList(pixels, image):
    for d in range(len(pixels)):
        if locationValid((pixels[d]["x"]), len(image[0]), (pixels[d]["y"]), len(image)) == True:
            x = pixels[d]["x"]
            y = pixels[d]["y"]
            image[y][x]['r'] = pixels[d]['pixel']['r']
            image[y][x]['g'] = pixels[d]['pixel']['g']
            image[y][x]['b'] = pixels[d]['pixel']['b']
            
# should create a PPM file using details created in generateEmptyImage function

def writePPM(image, inputName, filename):
    import os
    from PIL import Image
    import easygui as eg
    import sys

    returnInfo = [inputName, False]


    def get_output_path(fname):
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        return os.path.join(desktop, fname)

    try :
        #write ppm                          
        ppm_path = get_output_path(filename)

        height = len(image)
        width = len(image[0])
        
        with open(ppm_path, "w") as f:
            f.write("P3\n")
            f.write(str(width) + " " + str(height) + "\n" )
            f.write("255\n")
            for y in range(height):
                for x in range(width):
                    f.write(str(image[y][x]['r']) + " ")
                    f.write(str(image[y][x]['g']) + " ")
                    f.write(str(image[y][x]['b']) + " ")
                f.write("\n")


        # convert to JPG
        
        jpg_path = get_output_path(inputName + '.jpg')

        # Open the PPM image file
        with Image.open(ppm_path) as im:
            im.save(jpg_path)

        if os.path.exists(ppm_path):
            os.remove(ppm_path)

        return returnInfo


    
    except FileNotFoundError:
        fnfmsg = "An error occurred: {input_file}\n\nWould you like to try again?"
        fnftitle = "Error: File Not Found!"
        fnfoptions = ["Try again", "Exit"]
        fnf_choice = eg.buttonbox(fnfmsg, fnftitle, fnfoptions)
        if fnf_choice == "Try again" :
            returnInfo[1] = True
            return returnInfo
        sys.exit(0) 
            
    except Exception as e:
        excmsg = "An error occurred: {e}\n\nWould you like to try again?"
        exctitle = "Error: Exception!"
        excoptions = ["Try again", "Exit"]
        exc_choice = eg.buttonbox(excmsg, exctitle, excoptions)
        if exc_choice == "Try again" :
            returnInfo[1] = True
            return returnInfo
        sys.exit(0)


# addCircleToList(0,0,2,{'r': 1, 'g': 1, 'b': 1},[])
# should evaluate to
# [{'x': 0, 'y': -2, 'pixel': {'r': 1, 'g': 1, 'b': 1}},
# {'x': -1, 'y': -1, 'pixel': {'r': 1, 'g': 1, 'b': 1}},
# {'x': 0,'y': -1, 'pixel': {'r': 1, 'g': 1, 'b': 1}},
# {'x': 1, 'y': -1, 'pixel': {'r': 1, 'g': 1, 'b': 1}},

# defaultDict = {'x': 0, 'y': 0, 'pixel': {'r': 0, 'g': 0, 'b': 0}}

def addCircleToList(x, y, r, color, pixels):
    for yT in range(y-r, (y + r) + 1):
        for xT in range(x-r, (x + r) + 1):
            if (xT - x)**2 + (yT - y)**2 <= r**2:
                Dict = {"x": xT, "y": yT, "pixel" : color}
                pixels.append(Dict)

# Test Cases:
# addRectangleToList(0,2,1,2,{'r': 1, 'g': 1, 'b': 1},[])
# should evaluate to
# [{'x': 0, 'y': 1, 'pixel': {'r': 1, 'g': 1, 'b': 1}}, {'x':
# 0, 'y': 2, 'pixel': {'r': 1, 'g': 1, 'b': 1}}, {'x': 1, 'y':
# 1, 'pixel': {'r': 1, 'g': 1, 'b': 1}}, {'x': 1, 'y': 2, 'pixel':
# {'r': 1, 'g': 1, 'b': 1}}, {'x': 2, 'y': 1, 'pixel': {'r':
# 1, 'g': 1, 'b': 1}}, {'x': 2, 'y': 2, 'pixel': {'r': 1, 'g': 1, 'b': 1}}]

def addRectangleToList(x1, x2, y1, y2, pixel, pixels):
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            Dict = {"x": x, "y": y, "pixel" : pixel}
            pixels.append(Dict)

def addTriangleToList(x, y, h, color, pixels):

    import math
    
    half_width = h / math.sqrt(3)

    y_start = int(y- (h / 2))
    y_end = int(y + (h / 2))
    x_start = int(x - half_width)
    x_end = int(x + half_width)

    for yT in range(y_start, y_end + 1):
        for xT in range(x_start, x_end +1):
            relative_y = (yT - y_start) / h
            current_half_width = relative_y * half_width

            if x - current_half_width <= xT <= x + current_half_width:
                if y_start <= yT <= y_end :
                    pixel_data = {"x": xT, "y": yT, "pixel": color}
                    pixels.append(pixel_data)


def yourPictureFunction():
    image = generateEmptyPicture(userimagewidth,userimageheight)
    rectangle = []
    addRectangleToList(1, 2400, 1, 2400, {'r': 255, 'g': 255, 'b': 255}, rectangle)
    insertPixelList(rectangle, image)
    circleb1 = []
    circleb2 = []
    circle = []
    circle2 = []
    circle3 = []
    circle4 = []
    circle5 = []
    circle6 = []
    circle7 = []
    circle8 = []
    circle9 = []
    circle10 = []
    circle11 = []
    circle12 = []
    addCircleToList(600, 600, 700, {'r': 0, 'g': 5, 'b': 0}, circleb1)
    insertPixelList(circleb1, image)
    addCircleToList(600, 600, 650, {'r': 0, 'g': 15, 'b': 0}, circleb2)
    insertPixelList(circleb2, image)
    addCircleToList(600, 600, 600, {'r': 0, 'g': 25, 'b': 0}, circle)
    insertPixelList(circle, image)
    addCircleToList(600, 600, 550, {'r': 0, 'g': 35, 'b': 0}, circle2)
    insertPixelList(circle2, image)
    addCircleToList(600, 600, 500, {'r': 0, 'g': 55, 'b': 0}, circle3)
    insertPixelList(circle3, image)
    addCircleToList(600, 600, 450, {'r': 0, 'g': 75, 'b': 0}, circle4)
    insertPixelList(circle4, image)
    addCircleToList(600, 600, 400, {'r': 0, 'g': 100, 'b': 0}, circle5)
    insertPixelList(circle5, image)
    addCircleToList(600, 600, 350, {'r': 0, 'g': 115, 'b': 0}, circle6)
    insertPixelList(circle6, image)
    addCircleToList(600, 600, 300, {'r': 0, 'g': 130, 'b': 0}, circle7)
    insertPixelList(circle7, image)
    addCircleToList(600, 600, 250, {'r': 0, 'g': 155, 'b': 0}, circle8)
    insertPixelList(circle8, image)
    addCircleToList(600, 600, 150, {'r': 0, 'g': 175, 'b': 0}, circle9)
    insertPixelList(circle9, image)
    addCircleToList(600, 600, 100, {'r': 0, 'g': 200, 'b': 0}, circle10)
    insertPixelList(circle10, image)
    addCircleToList(600, 600, 50, {'r': 0, 'g': 225, 'b': 0}, circle11)
    insertPixelList(circle11, image)
    addCircleToList(600, 600, 25, {'r': 0, 'g': 250, 'b': 0}, circle12)
    insertPixelList(circle12, image)
    filename = "Myimage.ppm"
    writePPM(image, filename)

def createImage(housecolor, doorcolor, treeselection, roofShape, rooftype):
    import easygui as eg
    image = generateEmptyPicture(2400, 2400)
    rectangle = []
    addRectangleToList(1, 2400, 1, 2400, {'r': 255, 'g': 255, 'b': 255}, rectangle)
    insertPixelList(rectangle, image)
    house = []
    windowframe = []
    windowframe2 = []
    windowframe3 = []
    windowframe4 = []
    windowframe5 = []
    windowbackground = []
    windowframemid = []
    windowframe2mid = []
    windowframe3mid = []
    windowframe4mid = []
    windowframe5mid = []
    windowbackgroundmid = []
    windowframer = []
    windowframe2r = []
    windowframe3r = []
    windowframe4r = []
    windowframe5r = []
    windowbackgroundr = []
    windowframes = []
    windowframe2s = []
    windowframe3s = []
    windowframe4s = []
    windowframe5s = []
    windowbackgrounds = []
    windowframemids = []
    windowframe2mids = []
    windowframe3mids = []
    windowframe4mids = []
    windowframe5mids = []
    windowbackgroundmids = []
    windowframers = []
    windowframe2rs = []
    windowframe3rs = []
    windowframe4rs = []
    windowframe5rs = []
    windowbackgroundrs = []
    door = []
    doorknob = []
    doorknob2 = []
    roof = []

    #background
    sky = []
    grass = []
    cloudbase = []
    cloudleft = []
    cloudright = []
    cloudtop = []
    cloud2base = []
    cloud2left = []
    cloud2right = []
    cloud2top = []
    cloudlight = {'r': 245, 'g': 245, 'b': 245}
    cloud_mid = {'r': 230, 'g': 230, 'b': 230}

    #sky
    addRectangleToList(1, 2400, 1, 1800, {'r': 135, 'g': 206, 'b': 235}, sky)
    insertPixelList(sky, image)

    #clouds
    addRectangleToList(350,650,380, 430, cloud_mid, cloudbase)
    insertPixelList(cloudbase, image)
    addRectangleToList(300,520,350, 410, cloudlight, cloudleft)
    insertPixelList(cloudleft, image)
    addRectangleToList(500,720,360, 420, cloudlight, cloudright)
    insertPixelList(cloudright, image)
    addRectangleToList(420,620,320, 370, cloudlight, cloudtop)
    insertPixelList(cloudtop, image)

    addRectangleToList(1550,1900,320, 370, cloud_mid, cloud2base)
    insertPixelList(cloud2base, image)
    addRectangleToList(1480,1700,290, 350, cloudlight, cloud2left)
    insertPixelList(cloud2left, image)
    addRectangleToList(1650,1850,260, 330, cloudlight, cloud2right)
    insertPixelList(cloud2right, image)
    addRectangleToList(1780,2000,300, 360, cloudlight, cloud2top)
    insertPixelList(cloud2top, image)
                    

    #grass
    addRectangleToList(1, 2400, 1801, 2400, {'r': 17, 'g': 124, 'b': 19}, grass)
    insertPixelList(grass, image)

    if housecolor == 'Red' :
        addRectangleToList(850, 1550, 1200, 1800, {'r': 203, 'g': 65, 'b': 84}, house)
    elif housecolor == 'Blue' :
        addRectangleToList(850, 1550, 1200, 1800, {'r': 128, 'g': 156, 'b': 167}, house)
    elif housecolor == 'Green' :
        addRectangleToList(850, 1550, 1200, 1800, {'r': 122, 'g': 135, 'b': 104}, house)
    elif housecolor == 'Pink' :
        addRectangleToList(850, 1550, 1200, 1800, {'r': 255, 'g': 105, 'b': 180}, house)
    elif housecolor == 'Yellow' :
        addRectangleToList(850, 1550, 1200, 1800, {'r': 255, 'g': 220, 'b': 133}, house)
    elif housecolor == 'Purple' :
        addRectangleToList(850, 1550, 1200, 1800, {'r': 141, 'g': 56, 'b': 201}, house)
    elif housecolor == 'Orange' :
        addRectangleToList(850, 1550, 1200, 1800, {'r': 193, 'g': 74, 'b': 9}, house)
    elif housecolor == 'Black' :
        addRectangleToList(850, 1550, 1200, 1800, {'r': 63, 'g': 62, 'b': 62}, house)
    elif housecolor == 'White' :
        addRectangleToList(850, 1550, 1200, 1800, {'r': 248, 'g': 249, 'b': 243}, house)
    insertPixelList(house, image)

    #2nd story windows
    addRectangleToList(1000, 1050, 1300, 1400, {'r': 135, 'g': 206, 'b': 235}, windowbackground)
    insertPixelList(windowbackground, image)
    addRectangleToList(1000, 1010, 1300, 1400, {'r': 255, 'g': 255, 'b': 255}, windowframe)
    insertPixelList(windowframe, image)
    addRectangleToList(1050, 1060, 1300, 1400, {'r': 255, 'g': 255, 'b': 255}, windowframe2)
    insertPixelList(windowframe2, image)
    addRectangleToList(1010, 1050, 1300, 1310, {'r': 255, 'g': 255, 'b': 255}, windowframe3)
    insertPixelList(windowframe3, image)
    addRectangleToList(1010, 1050, 1390, 1400, {'r': 255, 'g': 255, 'b': 255}, windowframe4)
    insertPixelList(windowframe4, image)
    addRectangleToList(1010, 1050, 1345, 1355, {'r': 255, 'g': 255, 'b': 255}, windowframe5)
    insertPixelList(windowframe5, image)
    addRectangleToList(1180, 1230, 1300, 1400, {'r': 135, 'g': 206, 'b': 235}, windowbackgroundmid)
    insertPixelList(windowbackgroundmid, image)
    addRectangleToList(1180, 1190, 1300, 1400, {'r': 255, 'g': 255, 'b': 255}, windowframemid)
    insertPixelList(windowframemid, image)
    addRectangleToList(1230, 1240, 1300, 1400, {'r': 255, 'g': 255, 'b': 255}, windowframe2mid)
    insertPixelList(windowframe2mid, image)
    addRectangleToList(1190, 1230, 1300, 1310, {'r': 255, 'g': 255, 'b': 255}, windowframe3mid)
    insertPixelList(windowframe3mid, image)
    addRectangleToList(1190, 1230, 1390, 1400, {'r': 255, 'g': 255, 'b': 255}, windowframe4mid)
    insertPixelList(windowframe4mid, image)
    addRectangleToList(1190, 1230, 1345, 1355, {'r': 255, 'g': 255, 'b': 255}, windowframe5mid)
    insertPixelList(windowframe5mid, image)
    addRectangleToList(1350, 1400, 1300, 1400, {'r': 135, 'g': 206, 'b': 235}, windowbackgroundr)
    insertPixelList(windowbackgroundr, image)
    addRectangleToList(1350, 1360, 1300, 1400, {'r': 255, 'g': 255, 'b': 255}, windowframer)
    insertPixelList(windowframer, image)
    addRectangleToList(1400, 1410, 1300, 1400, {'r': 255, 'g': 255, 'b': 255}, windowframe2r)
    insertPixelList(windowframe2r, image)
    addRectangleToList(1360, 1400, 1300, 1310, {'r': 255, 'g': 255, 'b': 255}, windowframe3r)
    insertPixelList(windowframe3r, image)
    addRectangleToList(1360, 1400, 1390, 1400, {'r': 255, 'g': 255, 'b': 255}, windowframe4r)
    insertPixelList(windowframe4r, image)
    addRectangleToList(1360, 1400, 1345, 1355, {'r': 255, 'g': 255, 'b': 255}, windowframe5r)
    insertPixelList(windowframe5r, image)

    #1st story windows 
    addRectangleToList(1000, 1050, 1550, 1650, {'r': 135, 'g': 206, 'b': 235}, windowbackgrounds)
    insertPixelList(windowbackgrounds, image)
    addRectangleToList(1000, 1010, 1550, 1650, {'r': 255, 'g': 255, 'b': 255}, windowframes)
    insertPixelList(windowframes, image)
    addRectangleToList(1050, 1060, 1550, 1650, {'r': 255, 'g': 255, 'b': 255}, windowframe2s)
    insertPixelList(windowframe2s, image)
    addRectangleToList(1010, 1050, 1550, 1560, {'r': 255, 'g': 255, 'b': 255}, windowframe3s)
    insertPixelList(windowframe3s, image)
    addRectangleToList(1010, 1050, 1640, 1650, {'r': 255, 'g': 255, 'b': 255}, windowframe4s)
    insertPixelList(windowframe4s, image)
    addRectangleToList(1010, 1050, 1595, 1605, {'r': 255, 'g': 255, 'b': 255}, windowframe5s)
    insertPixelList(windowframe5s, image)
    addRectangleToList(1180, 1230, 1550, 1650, {'r': 135, 'g': 206, 'b': 235}, windowbackgroundmids)
    insertPixelList(windowbackgroundmids, image)
    addRectangleToList(1180, 1190, 1550, 1650, {'r': 255, 'g': 255, 'b': 255}, windowframemids)
    insertPixelList(windowframemids, image)
    addRectangleToList(1230, 1240, 1550, 1650, {'r': 255, 'g': 255, 'b': 255}, windowframe2mids)
    insertPixelList(windowframe2mids, image)
    addRectangleToList(1190, 1230, 1550, 1560, {'r': 255, 'g': 255, 'b': 255}, windowframe3mids)
    insertPixelList(windowframe3mids, image)
    addRectangleToList(1190, 1230, 1640, 1650, {'r': 255, 'g': 255, 'b': 255}, windowframe4mids)
    insertPixelList(windowframe4mids, image)
    addRectangleToList(1190, 1230, 1595, 1605, {'r': 255, 'g': 255, 'b': 255}, windowframe5mids)
    insertPixelList(windowframe5mids, image)
    addRectangleToList(1350, 1400, 1550, 1650, {'r': 135, 'g': 206, 'b': 235}, windowbackgroundrs)
    insertPixelList(windowbackgroundrs, image)
    addRectangleToList(1350, 1360, 1550, 1650, {'r': 255, 'g': 255, 'b': 255}, windowframers)
    insertPixelList(windowframers, image)
    addRectangleToList(1400, 1410, 1550, 1650, {'r': 255, 'g': 255, 'b': 255}, windowframe2rs)
    insertPixelList(windowframe2rs, image)
    addRectangleToList(1360, 1400, 1550, 1560, {'r': 255, 'g': 255, 'b': 255}, windowframe3rs)
    insertPixelList(windowframe3rs, image)
    addRectangleToList(1360, 1400, 1640, 1650, {'r': 255, 'g': 255, 'b': 255}, windowframe4rs)
    insertPixelList(windowframe4rs, image)
    addRectangleToList(1360, 1400, 1595, 1605, {'r': 255, 'g': 255, 'b': 255}, windowframe5rs)
    insertPixelList(windowframe5rs, image)

    #door selector
    if doorcolor == 'Natural Wood' :
        addRectangleToList(1135, 1265, 1675, 1800, {'r': 196, 'g': 164, 'b': 132}, door)
        insertPixelList(door, image)
        addCircleToList(1175, 1731, 5, {'r': 101, 'g': 67, 'b': 33}, doorknob)
        insertPixelList(doorknob, image)
        addCircleToList(1225, 1731, 5, {'r': 101, 'g': 67, 'b': 33}, doorknob2)
        insertPixelList(doorknob2, image)
    elif doorcolor == 'Yellow' :
        addRectangleToList(1135, 1265, 1675, 1800, {'r': 255, 'g': 192, 'b': 0}, door)
        insertPixelList(door, image)
        addCircleToList(1175, 1731, 5, {'r': 101, 'g': 67, 'b': 33}, doorknob)
        insertPixelList(doorknob, image)
        addCircleToList(1225, 1731, 5, {'r': 101, 'g': 67, 'b': 33}, doorknob2)
        insertPixelList(doorknob2, image)
    elif doorcolor == 'Blue' :
        addRectangleToList(1135, 1265, 1675, 1800, {'r': 63, 'g': 0, 'b': 255}, door)
        insertPixelList(door, image)
        addCircleToList(1175, 1731, 5, {'r': 196, 'g': 194, 'b': 205}, doorknob)
        insertPixelList(doorknob, image)
        addCircleToList(1225, 1731, 5, {'r': 196, 'g': 194, 'b': 205}, doorknob2)
        insertPixelList(doorknob2, image)
    elif doorcolor == 'Red' :
        addRectangleToList(1135, 1265, 1675, 1800, {'r': 255, 'g': 44, 'b': 44}, door)
        insertPixelList(door, image)
        addCircleToList(1175, 1731, 5, {'r': 188, 'g': 198, 'b': 204}, doorknob)
        insertPixelList(doorknob, image)
        addCircleToList(1225, 1731, 5, {'r': 188, 'g': 198, 'b': 204}, doorknob2)
        insertPixelList(doorknob2, image)
    elif doorcolor == 'Black' :
        addRectangleToList(1135, 1265, 1675, 1800, {'r': 31, 'g': 33, 'b': 34}, door)
        insertPixelList(door, image)
        addCircleToList(1175, 1731, 5, {'r': 181, 'g': 166, 'b': 66}, doorknob)
        insertPixelList(doorknob, image)
        addCircleToList(1225, 1731, 5, {'r': 181, 'g': 166, 'b': 66}, doorknob2)
        insertPixelList(doorknob2, image)
    elif doorcolor == 'White' :
        addRectangleToList(1135, 1265, 1675, 1800, {'r': 237, 'g': 234, 'b': 222}, door)
        insertPixelList(door, image)
        addCircleToList(1175, 1731, 5, {'r': 181, 'g': 166, 'b': 66}, doorknob)
        insertPixelList(doorknob, image)
        addCircleToList(1225, 1731, 5, {'r': 181, 'g': 166, 'b': 66}, doorknob2)
        insertPixelList(doorknob2, image)
    elif doorcolor == 'Green' :
        addRectangleToList(1135, 1265, 1675, 1800, {'r': 76, 'g': 187, 'b': 23}, door)
        insertPixelList(door, image)
        addCircleToList(1175, 1731, 5, {'r': 181, 'g': 166, 'b': 66}, doorknob)
        insertPixelList(doorknob, image)
        addCircleToList(1225, 1731, 5, {'r': 181, 'g': 166, 'b': 66}, doorknob2)
        insertPixelList(doorknob2, image)
    elif doorcolor == 'Purple' :
        addRectangleToList(1135, 1265, 1675, 1800, {'r': 147, 'g': 83, 'b': 127}, door)
        insertPixelList(door, image)
        addCircleToList(1175, 1731, 5, {'r': 181, 'g': 166, 'b': 66}, doorknob)
        insertPixelList(doorknob, image)
        addCircleToList(1225, 1731, 5, {'r': 181, 'g': 166, 'b': 66}, doorknob2)
        insertPixelList(doorknob2, image)
    elif doorcolor == 'Pink' :
        addRectangleToList(1135, 1265, 1675, 1800, {'r': 243, 'g': 207, 'b': 198}, door)
        insertPixelList(door, image)
        addCircleToList(1175, 1731, 5, {'r': 188, 'g': 198, 'b': 204}, doorknob)
        insertPixelList(doorknob, image)
        addCircleToList(1225, 1731, 5, {'r': 188, 'g': 198, 'b': 204}, doorknob2)
        insertPixelList(doorknob2, image)

    #roof creation
    if roofShape == 'Flat' :
        if rooftype == 'Clay' :
            addRectangleToList(800, 1600, 1160, 1200, {'r': 186, 'g': 86, 'b': 37}, roof)
            insertPixelList(roof, image)
        elif rooftype == 'Dark Asphalt' :
            addRectangleToList(800, 1600, 1160, 1200, {'r': 42, 'g': 41, 'b': 34}, roof)
            insertPixelList(roof, image)
        elif rooftype == 'Gray Asphalt' :
            addRectangleToList(800, 1600, 1160, 1200, {'r': 87, 'g': 87, 'b': 86}, roof)
            insertPixelList(roof, image)
        elif rooftype == 'Yellow Asphalt' :
            addRectangleToList(800, 1600, 1160, 1200, {'r': 255, 'g': 219, 'b': 88}, roof)
            insertPixelList(roof, image)
        elif rooftype == 'Green Asphalt' :
            addRectangleToList(800, 1600, 1160, 1200, {'r': 0, 'g': 66, 'b': 37}, roof)
            insertPixelList(roof, image)
        elif rooftype == 'Metal' :
            addRectangleToList(800, 1600, 1160, 1200, {'r': 79, 'g': 71, 'b': 67}, roof)
            insertPixelList(roof, image)
        elif rooftype == 'Red Metal' :
            addRectangleToList(800, 1600, 1160, 1200, {'r': 118, 'g': 46, 'b': 33}, roof)
            insertPixelList(roof, image)
    elif roofShape == 'Gable' :
        if rooftype == 'Clay' :
            addTriangleToList(1200, 850, 700, {'r': 186, 'g': 86, 'b': 37}, roof)
            insertPixelList(roof, image)
        elif rooftype == 'Dark Asphalt' :
            addTriangleToList(1200, 850, 700, {'r': 42, 'g': 41, 'b': 34}, roof)
            insertPixelList(roof, image)
        elif rooftype == 'Gray Asphalt' :
            addTriangleToList(1200, 850, 700, {'r': 87, 'g': 87, 'b': 86}, roof)
            insertPixelList(roof, image)            
        elif rooftype == 'Yellow Asphalt' :
            addTriangleToList(1200, 850, 700, {'r': 255, 'g': 219, 'b': 88}, roof)
            insertPixelList(roof, image)            
        elif rooftype == 'Green Asphalt' :
            addTriangleToList(1200, 850, 700, {'r': 0, 'g': 66, 'b': 37}, roof)
            insertPixelList(roof, image)            
        elif rooftype == 'Metal' :
            addTriangleToList(1200, 850, 700, {'r': 79, 'g': 71, 'b': 67}, roof)
            insertPixelList(roof, image)            
        elif rooftype == 'Red Metal' :
            addTriangleToList(1200, 850, 700, {'r': 118, 'g': 46, 'b': 33}, roof)
            insertPixelList(roof, image)            


    #tree
    if treeselection == 'Yes' :
        treeTrunk = []
        trunkHighlight = []
        leafBtm = []
        leafMid = []
        leafTop = []
        leaflpuff = []
        leafrpuff = []
        trunk_dark = {'r': 101, 'g': 67, 'b': 33}
        trunk_light = {'r': 130, 'g': 90, 'b': 50}
        leaf_dark = {'r': 34, 'g': 139, 'b': 34}
        leaf_mid = {'r': 50, 'g': 160, 'b': 60}
        leaf_light = {'r': 80, 'g': 180, 'b': 90}

        #tree trunk
        addRectangleToList(520, 580, 1540, 1800, trunk_dark, treeTrunk)
        insertPixelList(treeTrunk, image)
        addRectangleToList(535, 560, 1540, 1800, trunk_light, trunkHighlight)
        insertPixelList(trunkHighlight, image)

        #leaves
        addRectangleToList(390, 710, 1380, 1540, leaf_mid, leafBtm)
        insertPixelList(leafBtm, image)
        addRectangleToList(420, 680, 1280, 1380, leaf_light, leafMid)
        insertPixelList(leafMid, image)
        addRectangleToList(460, 640, 1200, 1280, leaf_dark, leafTop)
        insertPixelList(leafTop, image)
        addRectangleToList(350, 430, 1300, 1450, leaf_dark, leaflpuff)
        insertPixelList(leaflpuff, image)
        addRectangleToList(670, 750, 1320, 1460, leaf_dark, leafrpuff)
        insertPixelList(leafrpuff, image)

    nameEntry = False
    while nameEntry == False : 
        inputName = eg.enterbox("Please type a name for the image file: ", "Filename Entry")
        if inputName:
            eg.msgbox(f"Great! Your home image will be saved to your computer as: {inputName}", "Filename Entry Confirmed", ok_button = "Finish")
            nameEntry = True
        else:
            msg = "Are you sure you'd like to exit the program?"
            title = "Please confirm"
            options = ["Back", "Exit"]
            user_choice = eg.buttonbox(msg, title, options)
            if user_choice == "Back" :
                nameEntry = False
            else:
                import sys
                sys.exit(0) 
                    
        
    filename = inputName + '.ppm'
    returnInfo = writePPM(image, inputName, filename)

    return returnInfo


#user prompts
hcolors = ['Red','Blue','Green','Yellow','Pink','Purple','Orange']
colors = ['Red','Blue','Green','Pink', 'red','blue','green','pink','RED','BLUE','GREEN','PINK','yellow','YELLOW','Yellow','Purple','PURPLE','purple','Orange','ORANGE','orange']
def HCSelector():

    import easygui as eg
    
    msg = "What color would you like your home to be?\n\nPlease choose from the options below: "
    title = "House Color"
    choices = ['Red','Blue','Green','Yellow','Pink','Purple','Orange', 'White', 'Black']

    housecolor = eg.buttonbox(msg, title, choices)

    if housecolor:
        eg.msgbox(f"You chose: {housecolor}\n\nThank you for selecting your house color!\n", "House Color Confirmed", "Next")
        return housecolor


dcolors = ['Wood','Yellow','Blue','Red','Black','White','wood','WOOD','YELLOW','yellow','blue','BLUE','red','RED','black','BLACK','white','WHITE']
hdcolors = ['Wood','Yellow','Blue','Red','Black','White']
def DCSelector():

    import easygui as eg
    
    msg = "What color would you like your front door to be?\n\nPlease choose from the options below: "
    title = "Door Color"
    choices = ['Natural Wood','Yellow','Blue','Red','Black','White', 'Green', 'Purple', 'Pink']

    doorcolor = eg.buttonbox(msg, title, choices)

    if doorcolor:
        eg.msgbox(f"You chose: {doorcolor}\n\nThank you for selecting your door color!", "Door Color Confirmed", "Next")
        return doorcolor

    
selection = ['Yes','YES','yes','no','NO','No']
def TSelector():

    import easygui as eg
    
    msg = "Would you like a tree at your home?\n\nPlease select your choice below: "
    title = "Tree Selection"
    choices = ['Yes', 'No']

    treeselection = eg.buttonbox(msg, title, choices)

    if treeselection == 'Yes':
        eg.msgbox(f"You chose: {treeselection}\n\nWonderful! You will have a beautiful tree in no time!\n", "Tree Choice Confirmed", "Next" )
        return treeselection
    if treeselection == 'No':
        eg.msgbox(f"You chose: {treeselection}\n\nMaybe next time! We will pass on the tree for now.\n", "Tree Choice Confirmed", "Next" )
        return treeselection

def roofShapeSelector():

    import easygui as eg
    
    msg = "Which roof shape would you like?\n\nPlease select your choice below: "
    title = "Roof Shape Selection"
    choices = ['Flat', 'Gable']

    roofshapeselection = eg.buttonbox(msg, title, choices)

    if roofshapeselection :
        eg.msgbox(f"You chose: {roofshapeselection}\n\nThank you for selecting a roof shape!\n", "Roof Shape Confirmed", "Next" )
        return roofshapeselection

def roofTypeSelector():

    import easygui as eg
    
    msg = "What type of roof would you like?\n\nPlease select your choice below: "
    title = "Roof Type Selection"
    choices = ['Clay', 'Dark Asphalt', 'Gray Asphalt', 'Yellow Asphalt', 'Green Asphalt', 'Metal', 'Red Metal']

    roofselection = eg.buttonbox(msg, title, choices)

    if roofselection :
        eg.msgbox(f"You chose: {roofselection}\n\nThank you for selecting a roof type!\n", "Roof Type Confirmed", "Next" )
        return roofselection


def appProcess():
    #print('Welcome to the home creator where you can customize your home and we will transform it into an image for you!\nWe will begin by selecting a house color from the following list: \n')
    import easygui as eg
    eg.msgbox(f'Welcome to the home creator where you can customize your home and\n\nwe will transform it into an image for you!', "Start Menu", "Begin")
    housecolor = HCSelector()
    doorcolor = DCSelector()
    roofShape = roofShapeSelector()
    rooftype = roofTypeSelector()
    treeselection = TSelector()
    eg.msgbox(f'We are ready to develop your home!\n\nWhen you are ready, please click the Develop button below to start the process.\nIt may take a minute or two.', "Developing Image", 'Develop')
    imgInfo = ['', True]
    while imgInfo[1] == True :
        imgInfo = createImage(housecolor, doorcolor, treeselection, roofShape, rooftype)
    imageName = imgInfo[0]
    eg.msgbox(f'Your home has been developed! The image can be found in your files as {imageName}.jpg', "Image Created!", "Next")

restartopt = ['Restart','restart','RESTART','Close','close','CLOSE']
def endOptions():

    import easygui as eg
    import sys

    msg = "Would you like to continue creating homes or exit the creator?"
    title = "Please confirm"
    options = ["Continue Creating!", "Exit"]
    user_choice = eg.buttonbox(msg, title, options)
    if user_choice == "Continue Creating!" :
        return True
    else:
        sys.exit(0) 
    
exitApp = True
while exitApp != False :
    appProcess()
    exitApp = endOptions()
sys.exit(0)




              
    
    
