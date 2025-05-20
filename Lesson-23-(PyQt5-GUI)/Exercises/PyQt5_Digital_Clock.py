import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont,QFontDatabase

class alarm_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DIGITAL CLOCK')
        self.setGeometry(700,300,900,200)
        self.timer_label=QLabel(self)
        self.timer1=QTimer(self)
        self.UI()
    
    def UI(self):
        self.timer_label.setGeometry(0,0,900,200)
        V_box=QVBoxLayout()
        V_box.addWidget(self.timer_label)
        self.setLayout(V_box)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet('''
                font-size:150px;
                color:#F60BE9;
                background-color:black;
                font-weight:800;
                           
''')
        import os 
        file_path=r'C:\Users\user1\Music\Python\Python Course Tutorial\Lesson-23-(PyQt5-GUI)\Exercises\DS-DIGIT.TTF'
        print(os.path.exists(file_path))
        font_id_number=QFontDatabase.addApplicationFont(r'C:\Users\user1\Music\Python\Python Course Tutorial\Lesson-23-(PyQt5-GUI)\Exercises\DS-DIGIT.TTF')
        if font_id_number!=-1:
         print('Found')
         font_family=QFontDatabase.applicationFontFamilies(font_id_number)[0]
         self.timer_label.setFont(QFont(font_family,150))
        else:
            print('font not found')
        #from timer object creating using timeout method we can connect with the update_time method
        #using the start function it will work for every second (1sec-1000millsec)
        self.timer1.timeout.connect(self.update_time)
        #using the timer object it will call the function repeatedly after an interval of time
        self.timer1.start(1000)

    def update_time(self):
            #hh mm ss are format specifiers to specify time and AP denotes for Anti-meridian and post-meridian
            current_time=QTime.currentTime().toString('hh:mm:ss AP')
            self.timer_label.setText(current_time)

def main():
    app=QApplication(sys.argv)
    A_W=alarm_window()
    A_W.show()
    sys.exit(app.exec())

if __name__=='__main__':
    main()