from tkinter import *
import os.path
from rgbClasses import RGBColor, RGBChannel

# state file layout:
# enabled/disabled
# state (solid, breathing, flashing, multiFlash, spectrum)
# RGB color multiplier(0-100, 0-100, 0-100)
# selected speed multiplier (1-100)
# selected brightness multiplier (1-100)
# quick select color index (0- # of colors)
# ex:
# enabled
# solid
# 50,35,65
# 50
# 100
# 3


#fileLoc = "/home/pi/rgbfiles/"

class RGBControlPanel:



    def __init__(self, name, colorList):
        self.name=name
        self.colorList = colorList
        self.footwellChannel = RGBChannel(name="Footwell", startDisabled=False, colorList=colorList)
        self.shifterChannel = RGBChannel(name="Shifter", startDisabled=False, colorList=colorList)
        self.underglowChannel = RGBChannel(name="Underglow", startDisabled=True, colorList=colorList)
        self.window = Tk()
        self.window.title = "RGB Control"
        self.window.attributes('-zoomed', True)
        self.window.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.window.columnconfigure(0, weight=1)
        topBtnFrame = Frame(self.window)
        topBtnFrame.rowconfigure(0, weight=1)
        topBtnFrame.columnconfigure((0,1,2), weight=1)
        topBtnFrame.grid(row=0, column=0, sticky='nesw')
        self.footwellChannel.button = Button(topBtnFrame, text="FOOTWELL", font=("Conduit ITC",32), command=lambda: self.channelButtonPress(self.footwellChannel.button), highlightcolor="blue")
        self.footwellChannel.button.config(activebackground=self.footwellChannel.button.cget('background'), activeforeground=self.footwellChannel.button.cget('foreground'))
        self.footwellChannel.button.grid(row=0, column=0, sticky='nesw')
        self.shifterChannel.button = Button(topBtnFrame, text="SHIFTER", font=("Conduit ITC",32), command=lambda: self.channelButtonPress(self.shifterChannel.button))
        self.shifterChannel.button.config(activebackground=self.shifterChannel.button.cget('background'), activeforeground=self.shifterChannel.button.cget('foreground'))
        self.shifterChannel.button.grid(row=0,column=1, sticky='nesw')
        self.underglowChannel.button = Button(topBtnFrame, text="UNDERGLOW", font=("Conduit ITC",32), command=lambda: self.channelButtonPress(self.underglowChannel.button))
        self.underglowChannel.button.config(activebackground=self.underglowChannel.button.cget('background'), activeforeground=self.underglowChannel.button.cget('foreground'))
        self.underglowChannel.button.grid(row=0,column=2, sticky='nesw')
        self.activechannel = self.footwellChannel
        self.channels = [self.footwellChannel, self.shifterChannel, self.underglowChannel]

        self.redSlider = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, width=50, troughcolor="red", repeatdelay=100, repeatinterval=35, command=lambda: self.updateSlider(self.redSlider))
        self.redSlider.grid(row=1, column=0, sticky='news')

        self.greenSlider = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, width=50, troughcolor="green")
        self.greenSlider.grid(row=2, column=0, sticky='nesw')

        self.blueSlider = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, width=50, troughcolor="blue")
        self.blueSlider.grid(row=3, column=0, sticky='nesw')
        
        self.speedLabel = Label(self.window, text="Animation Speed", font=("Conduit ITC",24))
        self.speedLabel.grid(row=4, column=0, sticky='nesw')

        self.speedSlider = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, width=50)
        self.speedSlider.grid(row=5, column=0, sticky='nesw')

        self.brightLabel = Label(self.window, text="Brightness", font=("Conduit ITC",24))
        self.brightLabel.grid(row=6, column=0, sticky='nesw')

        self.brightnessSlider = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, width=50)
        self.brightnessSlider.grid(row=7, column=0, sticky='nesw')

        self.botBtnFrame = Frame(self.window)
        self.botBtnFrame.rowconfigure(0, weight=1)
        self.botBtnFrame.columnconfigure((0,1,2,3,4), weight=1)
        self.botBtnFrame.grid(row=8, column=0, sticky='nesw')

        self.sqsBtn = Button(self.botBtnFrame, text="Solid Quick \nSelect", font=("Conduit ITC",32))
        self.sqsBtn.grid(row=0, column=0, sticky='nesw')

        self.solidBtn = Button(self.botBtnFrame, text="Solid", font=("Conduit ITC",32))
        self.solidBtn.grid(row=0, column=1, sticky='nesw')

        self.breathBtn = Button(self.botBtnFrame, text="Breathing", font=("Conduit ITC",32))
        self.breathBtn.grid(row=0, column=2, sticky='nesw')

        self.flashBtn = Button(self.botBtnFrame, text="Flashing Multicolor", font=("Conduit ITC",32))
        self.flashBtn.grid(row=0, column=3, sticky='nesw')

        self.spectrumBtn = Button(self.botBtnFrame, text="Color Shift", font=("Conduit ITC",32))
        self.spectrumBtn.grid(row=0, column=4, sticky='nesw')
        self.window.mainloop()

#    def switchActiveChannel(self, channel):
        # read channel file
        
#    def updateSlider(self, slider):
        
    def channelButtonPress(self, inbutton):
        for chan in self.channels:
            if (inbutton == chan.button):
                if (chan.buttonState == "inactiveOff"):
                    chan.buttonState = "activeOff"
                    chan.button.config(fg="blue", relief=GROOVE, activeforeground="blue")
                elif (chan.buttonState == "inactiveOn" or chan.buttonState == "activeOff"):
                    chan.buttonState = "activeOn"
                    self.activeChannel = chan
                    chan.button.config(fg="blue", relief=SUNKEN, activeforeground="blue")
                elif (chan.buttonState == "activeOn"):
                    chan.buttonState = "activeOff"
                    self.activeButton = inbutton
                    self.activeChannel = chan
                    chan.button.config(fg="blue", relief=GROOVE,activeforeground="blue")
                else:
                    chan.buttonState = "inactiveOff"
                    chan.button.config(fg="black", relief=RAISED,activeforeground="black")
            else: # button was not pressed
                if (chan.buttonState == "activeOn"):
                    chan.buttonState = "inactiveOn"
                    chan.button.config(fg="black", relief=SUNKEN, activeforeground="black")
                elif (chan.buttonState == "activeOff"):
                    chan.buttonState = "inactiveOff"
                    chan.button.config(fg="black", relief=RAISED,activeforeground="black")
                else: # inactives, state=state, no changes
                    continue
        self.window.focus_set()

if __name__ == "__main__":
    red = RGBColor("red", 255, 0, 0)
    green = RGBColor("green", 0, 255, 0)
    blue = RGBColor("blue", 0, 0, 255)
    yellow = RGBColor("yellow", 255, 255, 0)
    pink = RGBColor("pink", 255, 0, 255)
    purple = RGBColor("purple", 128, 0, 255)
    teal = RGBColor("teal", 0, 255, 255)
    orange = RGBColor("orange", 255, 128, 0)

    newColors = [red, green, blue, yellow, pink, purple, teal, orange]

    controlPanel = RGBControlPanel(name="controls", colorList=newColors)
