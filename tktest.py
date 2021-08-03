from tkinter import *
import os.path

aniTypeFile = "/home/pi/animationType.txt"
solidQSStateFile = "/home/pi/solidQSState.txt"


def readFirstLine(filename):
	if (os.path.isfile(filename)):
		f = open(filename,'r')
		retval = f.read()
		f.close()
		return retval
	else:
		pass

def createFile(filename, instring):
	if (os.path.isfile(filename)):
		pass
	else:
		f = open(filename,'w')
		f.write(instring)
		f.close()

def changeToSolidQS():
	# open animation type file
	if (os.path.isfile(aniTypeFile)):
		f = open(aniTypeFile,'r')
		state = f.read()
		f.close()
	else:
		f = open(aniTypeFile,'w')
		f.write("Solid QS")
		state = "Solid QS"
		f.close()
	# check and see if the state is solid quick select
	if (state == "Solid QS"):
		# increment color
	else:
		f = open(aniTypeFile,'w')
		f.write("Solid QS")
		state = "Solid QS"
		f.close()


	if (os.path.isfile(aniTypeFile)):
		f = open(aniTypeFile,'r')
		currentColor = int(f.read()) + 1
		f.close()
		if (currentColor >= len(colors)):
			currentColor=0

		f = open(fname,'w')
		f.write(str(currentColor))
		f.close()
		solidBtn.config(text=str("Solid " + colors[currentColor].name))
		

	else:
		f = open(fname,'w')
		f.write("0")
		f.close()


class RGBColor:
	def __init__(self, name, rv, gv, bv):
		self.name = name
		self.red = rv
		self.green = gv
		self.blue = bv





red = RGBColor("red", 255, 0, 0)
green = RGBColor("green", 0, 255, 0)
blue = RGBColor("blue", 0, 0, 255)
yellow = RGBColor("yellow", 255, 255, 0)
pink = RGBColor("pink", 255, 0, 255)
purple = RGBColor("purple", 128, 0, 255)
teal = RGBColor("teal", 0, 255, 255)
orange = RGBColor("orange", 255, 128, 0)


colors = [red, green, blue, yellow, pink, purple, teal, orange]

window = Tk()

window.title = "RGB TEST APP"
window.attributes('-zoomed', True)
frame = Frame(window)
Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)
frame.grid(row=0, column=0)
lbl = Label(window, text="TEST")
lbl.grid(column=4, row=7)

# get starting solid quick select color selection
if createFile()
qsSolidColor = 
# get saved color selection
# get current selected speed
# get current selected brightness
# get current selected mode




	

solidBtn = Button(window, text=str("Solid " + colors[currentColor].name), command=changeToSolidQS)
solidBtn.grid(column=0, row=7, sticky='nesw')
window.mainloop()