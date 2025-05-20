import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QCheckBox,QLabel
from PyQt5.QtCore import Qt

class Check_Box_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.setWindowTitle('Check Box Window')
        self.checkbox_obj1=QCheckBox('Do you Love Me.....Hariniii....?',self)
        self.initGUI()
    
    def initGUI(self):
        self.checkbox_obj1.setGeometry(0,0,600,100)
        self.checkbox_obj1.setStyleSheet('font-size:40px')
        #using the below setChecked method we can disable the checkbox to not get clicked
        self.checkbox_obj1.setChecked(False)
        #using the connect method we can do unclick function
        self.checkbox_obj1.stateChanged.connect(self.check_box_state_changed)

    def check_box_state_changed(self,state):
        #using the below state attribute from Qt module we can know the current state of checkbox if state is 2 it is checked or 0 means it is not checked
        if state == Qt.Checked:
         #print(Qt.Checked) - Qt.checked will defaultly give the checked state as 2
         print('you Clicked the Check Box')
        else:
            print('You have not clicked the check box')

def main():
    cb_app=QApplication(sys.argv)
    cw=Check_Box_Window()
    cw.show()
    sys.exit(cb_app.exec())

if __name__=='__main__':
    main()