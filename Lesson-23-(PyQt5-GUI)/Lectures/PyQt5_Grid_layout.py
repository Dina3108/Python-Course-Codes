from PyQt5.QtWidgets import (QMainWindow,QApplication,QLabel,QVBoxLayout,QHBoxLayout,QGridLayout,QWidget)
from PyQt5.QtGui import(QFont,QIcon)
import sys
'''
Steps to make Vertical / Horizontal layout of widgets in a central widget :
1. Initialising the method (UI) in the INIT Constructor
2. Inside that method create an empty widget and set that widget as central_widget of a window
[central widget - will act like a platform for other child widgets]
3. Inside that method create 5 labels
4. Create another empty object of vertical_layout/Horizontal_layout box
5. Add 5 labels of widgets into that vertical_layout/Horizontal_layout box individually
6. Using set_layout method make layout of Vertical_layout/Horizontal_layout box in the central widget
7. You will get the desired Vertical/Horizontal layout
'''
class layout_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layout Lecture Window')
        self.setGeometry(300,300,500,500)
        self.UI()

    def UI(self):
        central_widget= QWidget()
        #setCentralWidget will arranges the other child widgets in it
        self.setCentralWidget(central_widget)

        label1=QLabel('#1',self)
        label2=QLabel('#2',self)
        label3=QLabel('#3',self)
        label4=QLabel('#4',self)
        label5=QLabel('#5',self)
        
        label1.setStyleSheet('background-color:blue')
        label2.setStyleSheet('background-color:red')
        label3.setStyleSheet('background-color:green')
        label4.setStyleSheet('background-color:purple')
        label5.setStyleSheet('background-color:pink')
        #for above without using layout it will be like overlapping all the labels and only the last label will be visible

        Grid_layout_box=QGridLayout()
      
        #Grid_layout_object.addWidget(label_name,row_number,column_number)
        #row and coulumn number always starts with zero
        Grid_layout_box.addWidget(label1,0,0)
        Grid_layout_box.addWidget(label2,0,1)
        Grid_layout_box.addWidget(label3,1,0)
        Grid_layout_box.addWidget(label4,1,1)
        Grid_layout_box.addWidget(label5,2,2)

        central_widget.setLayout(Grid_layout_box)        


def main():
    layout_app=QApplication(sys.argv)
    window1=layout_window()
    window1.show()
    sys.exit(layout_app.exec())


if __name__=='__main__':
    main()
    