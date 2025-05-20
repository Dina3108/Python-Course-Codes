import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QRadioButton,QVBoxLayout,QButtonGroup

'''
Difference between checkbox and radio button is -

* In check box you can select multiple options
* In radio button you can able to select only one button

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.radio1=QRadioButton('Do you like me Hariniii...?',self)
        self.radio2=QRadioButton('Dont you like me Hariniii...?',self)
        self.radio3=QRadioButton('Am I spoiling your life Hariniii...?',self)
        self.radio4=QRadioButton('Iam Missing you very much Hariniii...?',self)
        self.radio5=QRadioButton('Do you miss me Even Once Hariniii...?',self)
        #Inside a bunch of 5 buttons, while making it as Button group as 2 button groups, you are supposed to click only one button, and you can click another button in an another button group
        self.Button_group1=QButtonGroup(self)
        self.Button_group2=QButtonGroup(self)
        self.init_UI()        
    
    def init_UI(self):
        self.radio1.setGeometry(0,0,600,100)
        self.radio2.setGeometry(0,50,600,100)
        self.radio3.setGeometry(0,100,600,100)
        self.radio4.setGeometry(0,150,600,100)
        self.radio5.setGeometry(0,200,600,100)
        self.Button_group1.addButton(self.radio1)
        self.Button_group1.addButton(self.radio2)
        self.Button_group1.addButton(self.radio3)
        self.Button_group2.addButton(self.radio4)
        self.Button_group2.addButton(self.radio5)
        self.setStyleSheet('QRadioButton{font-size:30px}')
        self.radio1.toggled.connect(self.button_toggled)
        self.radio2.toggled.connect(self.button_toggled)
        self.radio3.toggled.connect(self.button_toggled)
        self.radio4.toggled.connect(self.button_toggled)
        self.radio5.toggled.connect(self.button_toggled)

    def button_toggled(self):
        print('You have toggled the radio button')
        #print(self.sender())
        #from the calling radio-button-object it will send you a object of details of toogled operation
        radio_button_details=self.sender()
        if radio_button_details.isChecked():
            print(f'You clicked {radio_button_details.text()}')
    
def main():
    app1=QApplication(sys.argv)
    radio_button_window=MainWindow()
    radio_button_window.show()
    sys.exit(app1.exec())

if __name__=='__main__':
    main()