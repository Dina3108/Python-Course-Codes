import sys
#The above sys library is directly associated with python interpretor and also get access the variables and functions maintained by the python intrepretor

#In below from PyQt5 library in Qtwidgets module import classes named QApplication and QMainwindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
#QApplication class is used to App Object
#QMain window class will be useful to get interact do functios or create window in python VS Code

#creating a class from the parent QMainwindow
class Dinakars_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #using setWindowTitle function we can set the title of window screen that was Appearing
        self.setWindowTitle('Shri Harini')
        #we can able to set the Geometry of the window screen Appearing
        #self.setGeometry(x-axis-coordinates,y-axis-coordinates,height,width)
        self.setGeometry(400,400,500,500)
        #using the setWindowIcon method in window object and Imported QIcon function sets the Icon image for the newly appearing window
        #QIcon will create an Icon object with suitable uploaded file suitable for displaying it as Icon and the setWindowIcon will set the Icon object into icon of the Appearing Window
        self.setWindowIcon(QIcon('Python Course Tutorial\\Lesson-23-(PyQt5-GUI)\\Lectures\\call-center.png'))
        #using the QLabel class we can create an object that content in the argument of the class inside that object will get appear in the window
        first_font=QLabel('Hi Harini Epdi Irukka',self)
        #using the setWordWrap method we can wrap the text into next line also if given width is filled
        first_font.setWordWrap(True)
        #from that object using setFont method and QFont function we can able to set its Font-Family and font-size
        first_font.setFont(QFont('Roboto',40))
        #using setGeometry method we can able to modify its position in the window
        first_font.setGeometry(10,10,1000,150)
        #using setStyleSheet method we can insert css functions inside that object to modify
        first_font.setStyleSheet('color:white;background-color:red;font-weight:bold;font-style:italic;text-decoration:underline')
        #using setAlignment method and using AlignBottom from Qt we can align text in the bottom region of the in its place of region

        #Below are different alignment options

        #first_font.setAlignment(Qt.AlignBottom) - Verically Bottom
        #first_font.setAlignment(Qt.AlignTop)- vertically Top
        #first_font.setAlignment(Qt.AlignVCenter)- vertically center
        #first_font.setAlignment(Qt.AlignHCenter) - Horizontally center
        #first_font.setAlignment(Qt.AlignLeft)-Horizontally Left
         # first_font.setAlignment(Qt.AlignRight)- Horizontally Right
  
        #we can do 2 Align Options at a time also
        first_font.setAlignment(Qt.AlignVCenter | Qt.AlignTop)
        #The Above denotes both center and top alignment
def main():
    #creating the App Object from the QApplication class
    app=QApplication(sys.argv)
    #creating window object from the created Dinakars_window class
    window=Dinakars_Window()
    #print(type(window))
    # by using the show function window object only the created screen will display otherwise not
    window.show()
    #exec function in app object displays a window screen in VS Code , it gets close when the VS Code window get closed
    #using exit function from sys library and app exexcution means only it closes the displayed new screen with proper return code
    sys.exit(app.exec())
if __name__=='__main__':
    main()

