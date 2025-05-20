import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        #lineEdit is like input tag in HTML
        self.lineEdit1=QLineEdit(self)
        self.button1=QPushButton('Submit',self)
        self.initGUI() 

    def initGUI(self):
        self.lineEdit1.setGeometry(10,10,400,40)
        self.button1.setGeometry(410,10,100,40)
        self.lineEdit1.setStyleSheet('font-size:25px;font-family:Arial')
        self.button1.setStyleSheet('font-size:25px;font-family:Arial')
        self.lineEdit1.setPlaceholderText('Enter your Message to Shri Harini')
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        print(self.lineEdit1.text())

def main():
    app=QApplication(sys.argv)
    Line_Edit_window=MainWindow()
    Line_Edit_window.show()
    sys.exit(app.exec())

if __name__=='__main__':
    main()