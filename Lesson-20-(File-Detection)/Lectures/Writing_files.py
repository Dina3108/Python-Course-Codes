#python writing files (.txt , .json, .csv)

import os 
txt_data='I love you... Where are you..?  Please Come to me'
file_path='C:\\Users\\user1\\Music\\Python\\Python Course Tutorial\\Lesson-20-(File-Detection)\\Lectures\\output.txt'
print(os.path.exists(file_path))

#after opening the file with writing mode as file or (otherword)
with open(file_path,'w') as file:
    #using the write function with argument of data, the file will get overwrited
    file.write(txt_data)
    print(f'txt file {file_path} was created')

#using the x - mode we can create a new file
file_path2='C:\\Users\\user1\\Music\\Python\\Python Course Tutorial\\Lesson-20-(File-Detection)\\Lectures\\output2.txt'
try :
 with open(file_path2,'x') as fi:
    print('File was created')
except FileExistsError:
   print('File Already Exists')

#using the a - append mode it will add data to already exists dat but using the write mode it will overwrite the existing data in the file

with open(file_path,'a') as k:
   k.write(txt_data)
   print('Data Appended')

   