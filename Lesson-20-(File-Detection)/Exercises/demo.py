import pygame
import time
import datetime
print(datetime.datetime.now().strftime('%H:%M:%S'))
t=input('Enter Time:')
file_path='Python Course Tutorial/Lesson-20-(File-Detection)/Exercises/Naa-Ready-MassTamilan.dev.mp3'
if t== datetime.datetime.now().strftime('%H:%M:%S'):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.get_busy:
        time.sleep(1)
else:
    print('Not Found')