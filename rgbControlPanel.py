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
        self.channels = [self.footwellChannel, self.shifterChannel, self.underglowChannel]
        self.activeChannel = self.channels[0]
        self.window = Tk()
        self.window.title = "RGB Control"
        #self.window.attributes('-zoomed', True)
        self.window.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.window.columnconfigure(0, weight=1)
        topBtnFrame = Frame(self.window)
        topBtnFrame.rowconfigure(0, weight=1)
        topBtnFrame.columnconfigure((0,1,2), weight=1)
        topBtnFrame.grid(row=0, column=0, sticky='nesw')
        self.footwellChannel.button = Button(topBtnFrame, text="FOOTWELL", font=("Conduit ITC",32), command=lambda: self.channelButtonPress(self.footwellChannel.button), highlightcolor="blue")
        self.footwellChannel.button.config(activebackground=self.footwellChannel.button.cget('background'), activeforeground=self.footwellChannel.button.cget('foreground'))
        self.footwellChannel.button.config(bg="#363636", bd=10, fg="white")
        self.footwellChannel.button.grid(row=0, column=0, sticky='nesw')
        self.shifterChannel.button = Button(topBtnFrame, text="SHIFTER", font=("Conduit ITC",32), command=lambda: self.channelButtonPress(self.shifterChannel.button))
        self.shifterChannel.button.config(activebackground=self.shifterChannel.button.cget('background'), activeforeground=self.shifterChannel.button.cget('foreground'))
        self.shifterChannel.button.config(bg="#363636", bd=10, fg="white")
        self.shifterChannel.button.grid(row=0,column=1, sticky='nesw')
        self.underglowChannel.button = Button(topBtnFrame, text="UNDERGLOW", font=("Conduit ITC",32), command=lambda: self.channelButtonPress(self.underglowChannel.button))
        self.underglowChannel.button.config(activebackground=self.underglowChannel.button.cget('background'), activeforeground=self.underglowChannel.button.cget('foreground'))
        self.underglowChannel.button.config(bg="#363636", bd=10, fg="white")
        self.underglowChannel.button.grid(row=0,column=2, sticky='nesw')

        self.redSlider = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, width=50,
            bg="#363636", fg="white", troughcolor="red", repeatdelay=100, repeatinterval=35,
            command=lambda pos: self.sliderCB("red", pos))
        self.redSlider.grid(row=1, column=0, sticky='news')

        self.greenSlider = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, width=50,
            bg="#363636", fg="white", troughcolor="green", repeatdelay=100, repeatinterval=35,
            command=lambda pos: self.sliderCB("green", pos))
        self.greenSlider.grid(row=2, column=0, sticky='nesw')

        self.blueSlider = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, width=50,
            bg="#363636", fg="white", troughcolor="blue", repeatdelay=100, repeatinterval=35,
            command=lambda pos: self.sliderCB("blue", pos))
        self.blueSlider.grid(row=3, column=0, sticky='nesw')

        self.speedLabel = Label(self.window, text="Animation Speed", fg="white", bg="#363636", font=("Conduit ITC",24))
        self.speedLabel.grid(row=4, column=0, sticky='nesw')

        self.speedSlider = Scale(self.window, from_=1, to=100, orient=HORIZONTAL, width=50,
            bg="#363636", fg="white", troughcolor="black", repeatdelay=100, repeatinterval=35,
            command=lambda pos: self.sliderCB("speed", pos))
        self.speedSlider.grid(row=5, column=0, sticky='nesw')

        self.brightLabel = Label(self.window, text="Brightness", fg="white", bg="#363636", font=("Conduit ITC",24))
        self.brightLabel.grid(row=6, column=0, sticky='nesw')

        self.brightnessSlider = Scale(self.window, from_=1, to=100, orient=HORIZONTAL, width=50,
            bg="#363636", fg="white",  troughcolor="black", repeatdelay=100, repeatinterval=35,
            command=lambda pos: self.sliderCB("brightness", pos))
        self.brightnessSlider.grid(row=7, column=0, sticky='nesw')

        self.botBtnFrame = Frame(self.window)
        self.botBtnFrame.rowconfigure(0, weight=1)
        self.botBtnFrame.columnconfigure((0,1,2,3,4), weight=1)
        self.botBtnFrame.grid(row=8, column=0, sticky='nesw')

        self.sqsBtn = Button(self.botBtnFrame, text="Solid Quick \nSelect", font=("Conduit ITC",32), command=self.qsButtonPress)
        self.sqsBtn.config(bg="#363636", bd=10, fg="white")
        self.sqsBtn.grid(row=0, column=0, sticky='nesw')

        self.solidBtn = Button(self.botBtnFrame, text="Solid", font=("Conduit ITC",32))
        self.solidBtn.config(bg="#363636", bd=10, fg="white")
        self.solidBtn.grid(row=0, column=1, sticky='nesw')

        self.breathBtn = Button(self.botBtnFrame, text="Breathing", font=("Conduit ITC",32))
        self.breathBtn.config(bg="#363636", bd=10, fg="white")
        self.breathBtn.grid(row=0, column=2, sticky='nesw')

        self.flashBtn = Button(self.botBtnFrame, text="Flashing Multicolor", font=("Conduit ITC",32))
        self.flashBtn.config(bg="#363636", bd=10, fg="white")
        self.flashBtn.grid(row=0, column=3, sticky='nesw')

        self.spectrumBtn = Button(self.botBtnFrame, text="Color Shift", font=("Conduit ITC",32))
        self.spectrumBtn.config(bg="#363636", bd=10, fg="white")
        self.spectrumBtn.grid(row=0, column=4, sticky='nesw')

        for chan in self.channels:
            chan.readValues()
            if (chan.enabled):
                chan.button.config(fg="white", relief=SUNKEN, activeforeground="white", bg='#363636')

        self.channelButtonPress(self.footwellChannel.button)

        self.window.mainloop()

#    def switchActiveChannel(self, channel):
#        # pull last values from file
#        self.channel.readValues()
#
    def sliderCB(self, slider, pos):
        if (slider == "red"):
            prop = "color"
            val = str(pos) + "," + str(self.activeChannel.green) + "," + str(self.activeChannel.blue)
            self.activeChannel.red = pos
        elif (slider == "green"):
            prop = "color"
            val = str(self.activeChannel.red) + "," + str(pos) + "," + str(self.activeChannel.blue)
            self.activeChannel.green = pos
        elif (slider == "blue"):
            prop = "color"
            val = str(self.activeChannel.red) + "," + str(self.activeChannel.green) + "," + str(pos)
            self.activeChannel.blue = pos
        elif (slider == "speed"):
            prop = slider
            val = pos
            self.activeChannel.speed = pos
        elif (slider == "brightness"):
            prop = slider
            val = pos
            self.activeChannel.brightness = pos
        self.activeChannel.writeProperty(prop, val)

    def channelButtonPress(self, inbutton):
        # save values
        for chan in self.channels:
            if (inbutton == chan.button):
                # Do work on the button we just pushed
                if (chan.buttonState == "inactiveOff"):
                    # Button was not previously pressed, we've pressed it once to display the channel
                    chan.buttonState = "activeOff"
                    chan.button.config(fg="red", relief=GROOVE, activeforeground="red", bg='#363636')
                    self.activeChannel.writeAll()
                    self.activeChannel = chan
                elif (chan.buttonState == "inactiveOn"):
                    # we're coming back to an already turned on channel
                    chan.buttonState = "activeOn"
                    self.activeChannel.writeAll()
                    self.activeChannel = chan
                    chan.button.config(fg="red", relief=SUNKEN, activeforeground="red", bg='#363636')
                elif (chan.buttonState == "activeOff"):
                    # we just pressed the button to turn on the channel
                    chan.buttonState = "activeOn"
                    chan.button.config(fg="red", relief=SUNKEN, activeforeground="red", bg='#363636')
                    chan.enableChannel()
                elif (chan.buttonState == "activeOn"):
                    # We just pressed the button to turn off the channel
                    chan.buttonState = "activeOff"
                    self.activeChannel = chan
                    chan.button.config(fg="red", relief=GROOVE,activeforeground="red", bg='#363636')
                    chan.disableChannel()
                else:
                    # I don't think we should ever get to this point
                    chan.buttonState = "inactiveOff"
                    chan.button.config(fg="white", relief=RAISED,activeforeground="green", bg='#363636')
            else:
                # Do work on the buttons we didn't press
                if (chan.buttonState == "activeOn"):
                    chan.buttonState = "inactiveOn"
                    chan.button.config(fg="white", relief=SUNKEN, activeforeground="white", bg='#363636')
                elif (chan.buttonState == "activeOff"):
                    chan.buttonState = "inactiveOff"
                    chan.button.config(fg="white", relief=RAISED,activeforeground="white", bg='#363636')
                else: # inactives, state=state, no changes
                    continue
        # set slider values
        self.redSlider.set(self.activeChannel.red)
        self.greenSlider.set(self.activeChannel.green)
        self.blueSlider.set(self.activeChannel.blue)
        self.speedSlider.set(self.activeChannel.speed)
        self.brightnessSlider.set(self.activeChannel.brightness)
        self.window.focus_set()

    def qsButtonPress(self):
        self.activeChannel.cycleQSColors()
        self.sqsBtn.config(fg="white", relief=SUNKEN, activeforeground="white", bg='#363636')
        self.solidBtn.config(fg="white", relief=RAISED, activeforeground="white", bg='#363636')
        self.breathBtn.config(fg="white", relief=RAISED, activeforeground="white", bg='#363636')
        self.flashBtn.config(fg="white", relief=RAISED, activeforeground="white", bg='#363636')
        self.spectrumBtn.config(fg="white", relief=RAISED, activeforeground="white", bg='#363636')
        self.redSlider.set(self.activeChannel.red)
        self.greenSlider.set(self.activeChannel.green)
        self.blueSlider.set(self.activeChannel.blue)
        print(str(self.activeChannel.red) + "," + str(self.activeChannel.green) + "," + str(self.activeChannel.blue))

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
