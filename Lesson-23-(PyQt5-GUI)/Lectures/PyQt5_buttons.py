from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton
from PyQt5.QtGui import QFont,QIcon
import sys

class button_window(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.setGeometry(300,300,300,300)
        self.but=QPushButton('Click Me Mapla...!',self)
        self.but_UI()
        self.l=QLabel('Button Click Pannu da',self)
        self.l.setGeometry(0,0,300,100)
        self.l.setStyleSheet('font-size:20px')

    def but_UI(self):
        self.but.setGeometry(100,100,400,100)
        self.but.setStyleSheet('font-size:30px;background-color:pink;color:white;border:solid 2px blue;border-radius:20px;font-weight:800;')
        #using the clicked method by calling the connect we can do onclick function in a button also
        self.but.clicked.connect(self.onclick_function)

    def onclick_function(self):
        print('Button Clicked...!')
        self.but.setText('Varatta...Durrr...!!!')
        self.but.setStyleSheet('background-color:green')
        self.l.setText('Button Click Pannitaan')

def main():
    a=QApplication(sys.argv)
    w=button_window()
    w.show()
    sys.exit(a.exec())

if __name__=='__main__':
    main()