from tkinter import *
import os.path


fileLoc = "/home/pi/"

defaults = ["disabled", "off", "100,0,0", "1", "1", "0"]

def createFile(filename, startDisabled):
    if (os.path.isfile(filename)):
        print("creating file " + filename)
        if (startDisabled):
            f = open(filename, 'r')
            lines = f.readlines()
            lines[0] = "disabled\n"
            f.close()
            f = open(filename, 'w')
            f.writelines("%s" % line for line in lines)
            f.close()
    else:
        f = open(filename,'w')
        f.writelines("%s\n" % line for line in defaults)
        f.close()

class RGBColor:
    def __init__(self, name, rv, gv, bv):
        self.name = name
        self.red = rv
        self.green = gv
        self.blue = bv
class RGBChannel:
    def __init__(self, name, startDisabled, colorList): # more to come I'm sure
        self.name = name
        self.stateFile = str(fileLoc + name + "_state.txt")
        writelines = defaults;
        createFile(self.stateFile, startDisabled)
        f = open(self.stateFile, 'r')
        lines = f.readlines()
        f.close()
        self.enabled = lines[0]
        self.state = lines[1]
        currentColors = list(lines[2].split(","))
        self.red = int(currentColors[0])
        self.green = int(currentColors[1])
        self.blue = int(currentColors[2])
        self.speed = int(lines[3])
        self.brightness = int(lines[4])
        self.qsIndex = int(lines[5])
        self.button = None
        self.colorList=colorList
        self.colorIndex=0
        if (self.enabled == "enabled" and not startDisabled):
            self.buttonState = "inactiveOn"
        else:
            self.buttonState = "inactiveOff"

    def writeProperty(self, prop, value):
        f = open(self.stateFile, 'r')
        lines = f.readlines()
        f.close()
        index = 0
        if (prop == "enable"):
            index = 0
        elif (prop == "state"):
            index = 1
        elif (prop == "color"):
            index = 2
        elif (prop == "speed"):
            index = 3
        elif (prop == "brightness"):
            index = 4
        elif (prop == "qscolor"):
            index = 5
        else:
            printf("error! invalid property change requested")
            return
        lines[index] = value
        f = open(filename,'w')
        f.writelines("%s\n" % line for line in lines)
        f.close()
            
    def enableChannel(self):
        self.enabled = True
        self.writeProperty("enable", "enabled")
        
    def disableChannel(self):
        self.enabled = False
        self.writeProperty("enable", "disabled")
     
    def setState(self, value):
        self.state = value
        self.writeProperty("state", value)
        
    def setColos(self, red, green, blue):
         self.red = red
         self.green = green
         self.blue = blue
         self.writeProperty(color, str(str(red) + "," + str(green) + "," + str(blue)))
     
    def cycleQSColors(self):
        self.colorIndex = self.colorIndex + 1
        if (self.colorIndex >= len(self.colorList)):
            self.colorIndex=0
        self.writeProperty("qscolor", str(self.colorIndex))

    def setSpeed(self, value):
        self.speed = value
        self.writeProperty("speed", str(value))
    
    def setBrightness(self, value):
        self.brightness = value
        self.writeProperty(self, str(value))
        
        
        
        
        
        
