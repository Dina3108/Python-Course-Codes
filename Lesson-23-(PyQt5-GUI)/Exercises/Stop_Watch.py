import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont,QFontDatabase

class Stop_Watch_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        #we have to create QTime object with format of hours,minutes,seconds,milliseconds
        self.time=QTime(0,0,0,0)
        self.stop_time_label=QLabel('00:00:00:00',self)
        self.stop_watch_timer=QTimer(self)
        self.start_button=QPushButton('🏃 Start',self)
        self.stop_button=QPushButton('🛑 Stop',self)
        self.Reset_button=QPushButton('⏱ Reset',self)
        self.UI()

    def UI(self):
        self.setWindowTitle('STOP WATCH')
        cen=QWidget()
        self.setCentralWidget(cen)
        vb=QVBoxLayout()
        vb.addWidget(self.stop_time_label)
        self.stop_time_label.setAlignment(Qt.AlignCenter)
        hb=QHBoxLayout()
        hb.addWidget(self.start_button)
        hb.addWidget(self.stop_button)
        hb.addWidget(self.Reset_button)
        #using the addLayout method to an VBox object we can add multiple add multiple VBox or HBox
        vb.addLayout(hb)
        cen.setLayout(vb)
        self.setStyleSheet('''
                           QPushButton,QLabel
                           {
                           padding:20px;
                           font-weight:bold;
                           font-family:Times New Roman
                           }
QPushButton
                           {
                           font-size:50px;
                           color:white;
                           border-radius:20px;
                           }
                           QLabel 
                           {
                           font-size:120px;
                           background-color:purple;
                           color:white;
                           border-radius:20px;
                           }
                           QPushButton#Startbut
                           {
                           background-color:green
                           }
                           QPushButton#Stopbut
                           {
                           background-color:red
                           }
                           QPushButton#Resetbut
                           {
                           background-color:blue
                           }
                           QWidget
                           {
                           font-family:Jersey 10;
                           font-weight:900;
                           }
                           
''')
        self.start_button.setObjectName('Startbut')
        self.stop_button.setObjectName('Stopbut')
        self.Reset_button.setObjectName('Resetbut')
        font_id_number=QFontDatabase.addApplicationFont(r'C:\Users\user1\Music\Python\Python Course Tutorial\Lesson-23-(PyQt5-GUI)\Exercises\Jersey10-Regular.ttf')
        if font_id_number!=-1:
         font_family=QFontDatabase.applicationFontFamilies(font_id_number)[0]
         self.setFont(QFont(font_family,30))

        self.start_button.clicked.connect(self.start_method)
        self.stop_button.clicked.connect(self.stop_method)
        self.Reset_button.clicked.connect(self.reset_method)
        self.stop_watch_timer.timeout.connect(self.time_display)

    def start_method(self):
        self.stop_watch_timer.start(10)
        self.stop_time_label.setStyleSheet('background-color:green')

    def stop_method(self):
        self.stop_watch_timer.stop()
        self.stop_time_label.setStyleSheet('background-color:red')

    def reset_method(self):
        self.stop_watch_timer.stop()
        self.stop_time_label.setStyleSheet('background-color:blue')
        self.time=QTime(0,0,0,0)
        self.stop_time_label.setText(self.format_time(self.time))

    def format_time(self,time):
        return f'{time.hour():02}:{time.minute():02}:{time.second():02}:{time.msec()//10:02}'

    def time_display(self):
        #we are updating the time object for every 10 Milli seconds
        self.time=self.time.addMSecs(10)
        self.stop_time_label.setText(self.format_time(self.time))
        

def main():
    app=QApplication(sys.argv)
    S_W=Stop_Watch_window()
    S_W.show()
    #sys.exit(app.exec())
    app.exec()

if __name__=='__main__':
    main()