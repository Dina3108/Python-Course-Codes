#to create and do operations in json file import json library
import json

employee={'name':'Harini','age':20,'job':'IT Professional'}

file_path='C:\\Users\\user1\\Music\\Python\\Python Course Tutorial\\Lesson-20-(File-Detection)\\Lectures\\output.json'

try:
    with open(file_path,'w') as k:
        #using dump function we can overwrite the data into the file
        #using the indent keyword it will store the data from 4 indentation spaces from start line
        json.dump(employee,k,indent=4)
except FileExistsError:
    print('File Already Exists')

#to create and do operations in Csv file we have to import the csv library
import csv

employees=[['Name','Age','Job'],['Dinakar',20,'Student'],['Harini',30,'Student'],['Spongebob',30,'Cook']]


file_path2='C:\\Users\\user1\\Music\\Python\\Python Course Tutorial\\Lesson-20-(File-Detection)\\Lectures\\output.csv'
try:
 with open(file_path2,'x') as k:
    print('CSV File Created')
except FileExistsError:
   print('File Already Exists')


try:
   #using the newline keyword we can append the data as per our convenience
   # IN newline keyword if you give \n means it will go to next line for every newline
   #by using \r it will moves the cursor to the beginning of the line and prints the value
   with open(file_path2,'w',newline='\r') as fi:
      #first decalre the data in csv format using writer function from CSV
      writer=csv.writer(fi)
      for row in employees:
         #using for loop we have to write the data as row using the writerow function
         writer.writerow(row)
except FileExistsError:
   print('File Already Exists')