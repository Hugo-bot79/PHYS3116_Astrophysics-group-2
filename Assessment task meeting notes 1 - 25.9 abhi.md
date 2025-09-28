Assessment task meeting notes for the first meeting
# Date: tutorial on Thursday, 25/09/2025, additional meeting on Sunday, 28/09/2025.
Note: We have to fixed the problems on VS code and Github, so we will have an additional meeting on Sunday to finish the markdown note.
# Group meeting 1 
# Attendee: Hugo Chen, XingKun Feng, Abhinaya Jeyandran

Agenda:
- Github

Note:
# Choice
XingKun Feng:Option 1
Abhinaya Jeyandran:Option 1
Hugo Chen: Option 1

# What will be included in our assessment task.
XingKun Feng:


Abhinaya Jeyandran:


Hugo Chen:


# First three lines of codes
XingKun Feng:


Abhinaya Jeyandran:
#import csv file to python 
file_handle = open(r"Krause21.csv", "r", encoding="utf-8") #opens Krause21 file and reads
csv_reader= DictReader(file_handle, delimiter = ",")
for row in csv_reader:
  print(row)

file_handle1 = open(r"HarrisPartIII.csv", "r", encoding="utf-8") #opens Harris Part III file
csv_reader1=  DictReader(file_handle1, deliminter = "'")
for row in csv_reader1:
  print(row)


Hugo Chen:
