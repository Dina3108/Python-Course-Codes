import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import Qt
#for doing image operaions import QPixmap class from QtGui Module
#Qpixmap means image composed of pixels displayed on the screen
from PyQt5.QtGui import QPixmap

class image_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,2000,1200)
        self.setWindowTitle('Missing Letter')
        self.setWindowIcon(QIcon('Python Course Tutorial\\Lesson-23-(PyQt5-GUI)\\Lectures\\AlbumArtSmall.jpg'))
        #ensure that Qlabel consits of self that every object which was created
        image_label=QLabel('Missing you very Much...!!!',self)
        image_label.setGeometry(0,0,self.width()//2,self.height()//2 )
        image_label.setFont(QFont('Alkarta',50))
        image_label.setStyleSheet('color:pink')
        image_label.setAlignment(Qt.AlignVCenter)

        first_image=QPixmap('Python Course Tutorial\\Lesson-23-(PyQt5-GUI)\\Lectures\\AlbumArtSmall.jpg')
        image_label.setPixmap(first_image)
        #setScaledcontents method will set the image fit into the size of the label where it is as into parameters of setGeometry
        image_label.setScaledContents(True)
        #using the width and height function from the label it will automatically get aligned with the window
        #using the below calculation of height and width parameters we can set the image into center
        image_label.setGeometry((self.width()-image_label.width())//2,(self.height()-image_label.height())//2,image_label.width(),image_label.height())
def main():
    #before creating window object first have to create an Application Object to initialise the event loop then to initialise widgets in that app like window creation
    image_app=QApplication(sys.argv)
    This_window=image_window()
    This_window.show()
    sys.exit(image_app.exec())
    


if __name__=='__main__':
    main()