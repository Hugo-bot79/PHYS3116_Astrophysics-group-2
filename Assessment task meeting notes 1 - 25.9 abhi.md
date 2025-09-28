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


Hugo Chen: From the data for FeH to determine the metallicity.


# First three lines of codes
XingKun Feng: 
Option 1 Accreted Milky Way Globular Clusters
Xingkun: Globular Clusters,Elliptical 
Graph analysis based on clusters
# first step, define and install all package that we need.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Abhinaya Jeyandran:
# import csv file to python 
file_handle = open(r"Krause21.csv", "r", encoding="utf-8") #opens Krause21 file and reads
csv_reader= DictReader(file_handle, delimiter = ",")
for row in csv_reader:
  print(row)

file_handle1 = open(r"HarrisPartIII.csv", "r", encoding="utf-8") #opens Harris Part III file
csv_reader1=  DictReader(file_handle1, deliminter = "'")
for row in csv_reader1:
  print(row)


Hugo Chen:
# import csv file to pandas (real)
Galaxydata_1 = pd.read_csv("HarrisPartIII.csv") #import HarrisPartIII.csv file to pandas. This step ensure pandas can read and manipulate the data. 
Galaxydata_2 = pd.read_csv("Krause21.csv") #import Krause21.csv file to pandas. This step ensure pandas can read and manipulate the data. 
print(Galaxydata_1) #test whether pandas can read the data from HarrisPartIII.csv
print(Galaxydata_2) #test whether pandas can read the data from Krause21.csv

Finish meeting
