from tkinter import *
import os.path


# states: inactiveOff, inactiveOn, activeOff, activeOn
# inactiveOff: black text, Raised
# inactiveOn: black text, SUNKEN
# activeOff: blue text, grooved
# activeOn: blue text, Sunken


def btnTest(inbtn, channelButtons):
    for btn,state in channelButtons:
        if (btn == inbtn):
            if (state == "inactiveOff"):
                state = "activeOff"
                btn.config(fg="blue", relief=GROOVE)
                print(state)
            elif (state == "inactiveOn" or state == "activeOff"):
                state = "activeOn"
                btn.config(fg="blue", relief=SUNKEN)
                print(state)
            elif (state == "activeOn"):
                state = "activeOff"
                btn.config(fg="blue", relief=GROOVE)
                print(state)
            else:
                state = "inactiveOff"
                btn.config(fg="black", relief=RAISED)
                print(state + " should not happen")
        else: # button was not pressed
            if (state == "activeOn"):
                state = "inactiveOn"
                btn.config(fg="black", relief=SUNKEN)
                print("not btn: " + state)
            elif (state == "activeOff"):
                state = "inactiveOff"
                btn.config(fg="black", relief=RAISED)
                print("not btn: " + state)
            else: # inactives, state=state, no changes
                print("not btn: " + state)
                continue


window = Tk()
window.title = "TK SCRATCHPAD"
window.attributes('-zoomed', True)
window.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
window.columnconfigure(0, weight=1)
topBtnFrame = Frame(window)
topBtnFrame.rowconfigure(0, weight=1)
topBtnFrame.columnconfigure((0,1,2), weight=1)
topBtnFrame.grid(row=0, column=0, sticky='nesw')
btn1 = Button(topBtnFrame, text="FOOTWELL", font=("Conduit ITC",32), command=lambda: btnTest(btn1,channelButtons))
btn1.grid(row=0, column=0, sticky='nesw')
btn2 = Button(topBtnFrame, text="SHIFTER", font=("Conduit ITC",32), command=lambda: btnTest(btn2,channelButtons))
btn2.grid(row=0,column=1, sticky='nesw')
btn3 = Button(topBtnFrame, text="UNDERGLOW", font=("Conduit ITC",32), command=lambda: btnTest(btn3,channelButtons))
btn3.grid(row=0,column=2, sticky='nesw')

redSlider = Scale(window, from_=0, to=100, orient=HORIZONTAL, width=50, troughcolor="red")
redSlider.grid(row=1, column=0, sticky='news')

greenSlider = Scale(window, from_=0, to=100, orient=HORIZONTAL, width=50, troughcolor="green")
greenSlider.grid(row=2, column=0, sticky='nesw')

blueSlider = Scale(window, from_=0, to=100, orient=HORIZONTAL, width=50, troughcolor="blue")
blueSlider.grid(row=3, column=0, sticky='nesw')

speedLabel = Label(window, text="Animation Speed", font=("Conduit ITC",24))
speedLabel.grid(row=4, column=0, sticky='nesw')

speedSlider = Scale(window, from_=0, to=100, orient=HORIZONTAL, width=50)
speedSlider.grid(row=5, column=0, sticky='nesw')

brightLabel = Label(window, text="Brightness", font=("Conduit ITC",24))
brightLabel.grid(row=6, column=0, sticky='nesw')

brightnessSlider = Scale(window, from_=0, to=100, orient=HORIZONTAL, width=50)
brightnessSlider.grid(row=7, column=0, sticky='nesw')

botBtnFrame = Frame(window)
botBtnFrame.rowconfigure(0, weight=1)
botBtnFrame.columnconfigure((0,1,2,3,4), weight=1)
botBtnFrame.grid(row=8, column=0, sticky='nesw')

sqsBtn = Button(botBtnFrame, text="Solid Quick \nSelect", font=("Conduit ITC",32))
sqsBtn.grid(row=0, column=0, sticky='nesw')

solidBtn = Button(botBtnFrame, text="Solid", font=("Conduit ITC",32))
solidBtn.grid(row=0, column=1, sticky='nesw')

breathBtn = Button(botBtnFrame, text="Breathing", font=("Conduit ITC",32))
breathBtn.grid(row=0, column=2, sticky='nesw')

flashBtn = Button(botBtnFrame, text="Flashing Multicolor", font=("Conduit ITC",32))
flashBtn.grid(row=0, column=3, sticky='nesw')

spectrumBtn = Button(botBtnFrame, text="Color Shift", font=("Conduit ITC",32))
spectrumBtn.grid(row=0, column=4, sticky='nesw')

#channelButtons=[footwellBtn, shifterBtn, underglowBtn]

channelButtons=[btn1:"inactiveOff"], [btn2: "inactiveOff"], [btn3: "incativeOff"]]

window.mainloop()

#1024x768
