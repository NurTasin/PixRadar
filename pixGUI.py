from graphics import *
import serial as ser
import random as rand

#This project is tested on python 2.7
def initPort():
	port=str(raw_input("Enter the port to connect: "))
	board=ser.Serial(port,115200,timeout=0.2)
	return board
def drawRad():
	win=GraphWin("PixRadar",520,150)
	mainRect=Rectangle(Point(0,0), Point(520,150))
	mainRect.setFill(color_rgb(33,33,33))
	mainRect.setOutline(color_rgb(33,33,33))
	mainRect.draw(win)

	line0=Line(Point(0,0), Point(0,100))
	line0.setOutline(color_rgb(0,0,0))
	line0.draw(win)

	line1=Line(Point(100,0), Point(100,100))
	line1.setOutline(color_rgb(0,0,0))
	line1.draw(win)

	line2=Line(Point(200,0), Point(200,100))
	line2.setOutline(color_rgb(0,0,0))
	line2.draw(win)

	line3=Line(Point(300,0), Point(300,100))
	line3.setOutline(color_rgb(0,0,0))
	line3.draw(win)

	line4=Line(Point(400,0), Point(400,100))
	line4.setOutline(color_rgb(0,0,0))
	line4.draw(win)

	line5=Line(Point(500,0), Point(500,100))
	line5.setOutline(color_rgb(0,0,0))
	line5.draw(win)

	separatorLine=Line(Point(0,100), Point(500,100))
	separatorLine.setOutline(color_rgb(0,0,0))
	separatorLine.setWidth(2)
	separatorLine.draw(win)

	zeroCmText=Text(Point(20,120), "0cm")
	zeroCmText.setOutline(color_rgb(255,255,255))
	zeroCmText.setSize(15)
	zeroCmText.draw(win)

	tenCmText=Text(Point(95,120),"10cm")
	tenCmText.setTextColor(color_rgb(255,255,255))
	tenCmText.setSize(15)
	tenCmText.draw(win)

	twentyCmText=Text(Point(195,120), "20cm")
	twentyCmText.setTextColor(color_rgb(255,255,255))
	twentyCmText.setSize(15)
	twentyCmText.draw(win)

	thirtyCmText=Text(Point(295,120), "30cm")
	thirtyCmText.setTextColor(color_rgb(255,255,255))
	thirtyCmText.setSize(15)
	thirtyCmText.draw(win)

	fourtyCmText=Text(Point(395,120), "40cm")
	fourtyCmText.setTextColor(color_rgb(255,255,255))
	fourtyCmText.setSize(15)
	fourtyCmText.draw(win)

	fiftyCmText=Text(Point(495,120), "50cm")
	fiftyCmText.setTextColor(color_rgb(255,255,255))
	fiftyCmText.setSize(15)
	fiftyCmText.draw(win)
	try:
		__board=initPort()
	except ser.serialutil.SerialException:
		print("Can't open the port that you have entered")
		win.close()
		quit()
	global subRectangle
	subRectangle=Rectangle(Point(0,0), Point(0,0))
	subRectangle.draw(win)
	while True:
		subRectangle.undraw()
		finalStr=""
		while True:
			output=__board.read()
			output=str(output)
			output=output.decode()
			if output!="\n":
				finalStr=finalStr+output
			elif output=="\n":
				break
		distance=int(finalStr)
		print(distance)
		subRectangle=Rectangle(Point(0,0),Point(distance*10 , 100))
		subRectangle.setFill(color_rgb(0,250,15))
		subRectangle.setOutline(color_rgb(0,250,25))
		subRectangle.draw(win)
		time.sleep(0.1)
	win.close()

if __name__=="__main__":
	try:
		drawRad()
	except GraphicsError:
		pass