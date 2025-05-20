import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QPushButton,QWidget,QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.button1=QPushButton('#1',self)
        self.button2=QPushButton('#2',self)
        self.button3=QPushButton('#3',self)
        self.initGUI() 

    def initGUI(self):
        #like setting class for individual HTML Element we can set here individually as object name
        self.button1.setObjectName('button1')
        self.button2.setObjectName('button2')
        self.button3.setObjectName('button3')
        cw=QWidget()
        self.setCentralWidget(cw)
        hb=QHBoxLayout()
        hb.addWidget(self.button1)
        hb.addWidget(self.button2)
        hb.addWidget(self.button3)
        cw.setLayout(hb)
        #by using the 3 double quotes inside setStyleSheet method you can style for multiple objects 
        #In CSS instead of dot we are using # in python.setStyleSheet
        self.setStyleSheet("""
                   QPushButton
                           {
                           font-size:30px;
                           font-family:Arial;
                           padding: 15px 75px;
                           margin:25px;
                           border: 3px solid;
                           border-radius:15px
                           }
                    
                    QPushButton#button1
                           {
                           background-color:red;
                           color:white;
                           }       
                    QPushButton#button2
                           {
                           background-color:green;
                           color:white;
                           }
                    QPushButton#button3
                           {
                           background-color:purple;
                           color:white;
                           }
""")

def main():
    app=QApplication(sys.argv)
    Line_Edit_window=MainWindow()
    Line_Edit_window.show()
    sys.exit(app.exec())

if __name__=='__main__':
    main()