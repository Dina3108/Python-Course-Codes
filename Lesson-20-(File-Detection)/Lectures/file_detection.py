#We have to import the OS Module for contatcting the Operating system like accesing and tracking the filepath of the files
import os

#Relative file path - the file will be there in the folder itself
#Absolute file path - File will be in another folder

#While writing the file path '\' will compiled as Escape Sequence it will be suitable if we write as \\ or /

file_path='C:/Users/user1/Music/Python/Python Course Tutorial/Lesson-20-(File-Detection)/Lectures/kile.txt'

#In os library in path module using the exists function
print(os.path.exists(file_path))

#in os library using path.exists function we can detect whether the file is present in that location or not
if os.path.exists(file_path):
    print(f'The location is {file_path} exists')
    
    #It will check it is a file
    if os.path.isfile(file_path):
        print('This is a file')
    file_path='C:/Users/user1/Music/Python/Python Course Tutorial/Lesson-20-(File-Detection)/Lectures'
    #isdir function will check whether it is a folder
    if os.path.isdir(file_path):
        print('This is a Folder')
else:
    print('File not found')