import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QWidget,QPushButton,QLineEdit,QVBoxLayout,QHBoxLayout
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QFontDatabase

class Weather_App_Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel('Enter City Name: 🏙',self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton('Get Weather',self)
        self.tempearture_label= QLabel('Welcome to Vaanam 🌈',self)
        self.emoji_label=QLabel('Your personal Weather guide 🌥',self)
        self.description_label=QLabel('That brings you real-time climate updates for any City 🌡',self)
        self.setWindowTitle('Vaanam 🌈 ')
        self.setStyleSheet('font-size:25px;background-color:#FFECA1;color:#F411DB;font-family:PoetsenOne')
        font_id_number=QFontDatabase.addApplicationFont(r'C:\Users\user1\Music\Python\Python Course Tutorial\Lesson-23-(PyQt5-GUI)\Exercises\PoetsenOne-Regular.ttf')
        if font_id_number!=-1:
         font_family=QFontDatabase.applicationFontFamilies(font_id_number)[0]
         self.setFont(QFont(font_family,30))
        else:
            print('font not found')
        
        self.UI()
        
    def UI(self):
        #while making a window from QWidget you can't make any central widget
        c=QWidget()
        self.setCentralWidget(c)
        VB=QVBoxLayout()
        VB.addWidget(self.city_label)
        VB.addWidget(self.city_input)
        VB.addWidget(self.get_weather_button)
        VB.addWidget(self.tempearture_label)
        VB.addWidget(self.emoji_label)
        VB.addWidget(self.description_label)
        c.setLayout(VB)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.tempearture_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        #pushbutton don't have set Alignment option like below
        #self.get_weather_button.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName('city_label')
        self.city_input.setObjectName('city_input')
        self.emoji_label.setObjectName('emoji_label')
        self.get_weather_button.setObjectName('get_weather_button')
        self.tempearture_label.setObjectName('tempearture_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')
        self.get_weather_button.clicked.connect(self.get_weather)


    def get_weather(self):
        self.setStyleSheet('''
                           QLabel,QPushButton,QLineEdit
                           {
                           font-weight:bold;
                           }
                           QLabel#city_label
                           {
                           font-size:40px;
                           }
                           QLineEdit#city_input
                           {
                           font-size:40px;
                           background-color:#FFECA1;
                           color:#F411DB;
                           border:none;
                           border-radius:20px;
                           padding:20px;
                           }
                           QLineEdit#city_input:hover
                           {
                           color:#FFECA1;
                           background-color:#F411DB;
                           border:1.5px solid #FFECA1;
                           border-color:#FFECA1;
                           }
                           QPushButton#get_weather_button
                           {
                           font-size:35px;
                           font-weight:bold;
                           background-color:#FFECA1;
                           color:#F411DB;
                           border:1.5px solid #FFECA1;
                           padding:25px;
                           border-radius:20px;
                           }
                           QPushButton#get_weather_button:hover
                           {
                           color:#FFECA1;
                           background-color:#F411DB;
                           border:1.5px solid #FFECA1;
                           border-color:#FFECA1;
                           }
                           QLabel#tempearture_label
                           {
                           font-size:75px;
                           }
                           QLabel#emoji_label
                           {
                           font-size:100px;
                           font-family:Segoe UI emoji;
                           }
                           QLabel#description_label
                           {
                           font-size:50px;
                           }
                           QWidget
                           {
                           color:#FFECA1;
                           background-color:#F411DB
                           }
                           
         ''')    
        api_key='6ca118f683134085a978f6809bec7342'
        city_name=self.city_input.text()
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

        try:
            response=requests.get(url)
            #by using the method raise_for_status() from response object which get the data from the URL will raise error based on the status
            response.raise_for_status()
            data=response.json()
            #cod key gives the HTTP Code from the server if the code is 200 it has successfully retrieved data from the API Server 
            if data['cod']==200:
                self.display_weather(data)

#from the exceptions module from the HTTP Error we can raise an exception for HTTP Error
        except requests.exceptions.HTTPError:
            #based on the HTTP Status code error we can raise different error exceptions
            match response.status_code:
                case 400:
                    self.display_error('Bad request\nPlease check your request')
                case 401:
                    self.display_error('Unauthorised\nInvalid API Key')
                case 403:
                    self.display_error('Forbidden\nAccess is denied')
                case 404:
                    self.display_error('Not Found\nCity not Found')
                case 500:
                    self.display_error('Internal Servor Error\nPlease try again later')
                case 502:
                    self.display_error('Bad Gateway\nInvalid response from the Server')
                case 503:
                    self.display_error('Service Unavailable\nServer is down')
                case 504:
                    self.display_error('Gateway Timeout\nNo response from the server')
                case _:
                    self.display_error(f'HTTP Error occured')

        except requests.exceptions.ConnectionError:
            self.display_error('Connection Error:\nCheck your Internet Connection')
        except requests.exceptions.Timeout:
            self.display_error('Timeout Error:\nThe request timed out')
        except requests.exceptions.TooManyRedirects:
            self.display_error('Too many Redirects:\nCheck the URl')
        except requests.exceptions.RequestException as req_error:
            self.display_error(f'Request Error:\n{req_error}')            


    def display_error(self,message):
        self.tempearture_label.setStyleSheet('font-size:30px;')
        self.tempearture_label.setText(message)
        #using clear function we can make it as empty
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self,data):
        
        self.tempearture_label.setStyleSheet('font-size:75px;')
        #in the data of json dictionary in the main key in the value of another dictionary there is a key known as temp that will give us the value of temperature of that particular city
        self.tempearture_label.setText(f'{data['main']['temp']-273.15:.2f}°C')
        #in the key of weather there is a list of element in that first elemnent first element holds a dictionary in that dictionary using discription key it will give us is it is a clear sky/cloudy or something
        self.description_label.setText(f'{data['weather'][0]['description']}')
        weather_id=data['weather'][0]['id']
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200<= weather_id <=232:
            return '⛈'
        elif 300<= weather_id<=321:
            return '🌦'
        elif 500 <= weather_id <=531:
            return '🌧'
        elif 600 <= weather_id <=622:
            return '❄'
        elif 701 <= weather_id <=741:
            return '🌫️'
        elif weather_id == 762:
            return '🌋'
        elif weather_id== 771:
            return '💨'
        elif weather_id == 781:
            return '🌪'
        elif weather_id ==800:
            return '☀'
        elif 801 <= weather_id <=804:
            return '☁️'
        else:
            return'🤔'

def main():
    app2=QApplication(sys.argv)
    ww=Weather_App_Widget()
    ww.show()
    sys.exit(app2.exec())

if __name__=='__main__':
    main()