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
XingKun Feng: globular cluster


Abhinaya Jeyandran: enclose mass and angular momentum


Hugo Chen: metallicity.


# First three lines of codes
# XingKun Feng: 
#import numpy as np (manipulation of arrays)
#import pandas as pd (essential for merging process)
#import matplotlib.pyplot as plt (create labelled figures of results)
#from astropy.io import fits (has range of tools for astronomical computations, and also FITS contain multi-dimensional arrays)


# Abhinaya Jeyandran:
#import csv file to python 
#open file on read mode with UTF-8 encoding
file_handle = open(r"Krause21.csv", "r", encoding="utf-8") 
#create a DictReader object to parse through the file
#Dictreader reads each row into a dictionary
#keys are taken from the first line (header row) and values are the corresponding fields in each row
csv_reader= DictReader(file_handle, delimiter = ",")
#loop through each row and print the dictionary
for row in csv_reader:
  print(row)
#close the reader - needs to be done always
file_handle.close()

#open and read HarrisPartIII csv file
file_handle1 = open(r"HarrisPartIII.csv", "r", encoding="utf-8") 
#create a new Dictreader similar to above
csv_reader1=  DictReader(file_handle1, deliminter = ",")
#loop through and print rows from the file
for row in csv_reader1:
  print(row)
#close the second file
file_handle1.close()

# Hugo Chen:
#import csv file to pandas (real)
#import HarrisPartIII.csv file to pandas. This step ensure pandas can read and manipulate the data. 
Galaxydata_1 = pd.read_csv("HarrisPartIII.csv")
#import Krause21.csv file to pandas. This step ensure pandas can read and manipulate the data. 
Galaxydata_2 = pd.read_csv("Krause21.csv") 
#test whether pandas can read the data from HarrisPartIII.csv
print(Galaxydata_1)
#test whether pandas can read the data from Krause21.csv
print(Galaxydata_2) 

Finish meeting
