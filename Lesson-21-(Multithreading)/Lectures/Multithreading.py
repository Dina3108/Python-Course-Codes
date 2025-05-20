'''
Multithreading - Used to perform multiple tasks concurrenlty (multitasking) Good for I/O bound tasks like reading files or fetching data from APIs 
Ex: threading.Thread(target=my_function)
'''
import threading
import time

def walk_dog(first,last):
    time.sleep(8)
    print(f'You finish walking the {first} {last}')

def take_out_trash():
    time.sleep(2)
    print('You take out the trash')

def get_mail():
    time.sleep(4)
    print('You get the mail')

#Without using thread function first after 8 sec walk_dog function will get execute followed by take_out_trash after 2 sec will execute and after 4 sec get_mail function will execute

#But using threading functions we can able to make these 3 functions concurrenlty at the same time

chore1=threading.Thread(target=walk_dog,args=('scooby','lover'))
# as above is tupple if you give that argument without comma means it will show you an error
chore1.start()

chore2=threading.Thread(target=take_out_trash)
chore2.start()

chore3=threading.Thread(target=get_mail)
chore3.start()
#by using the above thread functions first takeuttrash function after 2sec will get executed and followed by 4 sec and 8 sec fucntions will get executed


#print('All chores are complete')
#when you gave the print statement above first print statement will execute because of without any sleep function
chore1.join()
chore2.join()
chore3.join()
print('All chordes are completed')
#by using the above join function after completing all the above thread functions only below that code will get execute