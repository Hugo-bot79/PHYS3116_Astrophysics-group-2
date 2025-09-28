# Three lines of code that are discussed in the tutorial on Thursday, 25/09/2025
# The code has been discussed and recorded by Hugo Chen, XingKun Feng and Abhinaya Jeyandran

#first step, define and install all package that we need.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from csv import DictReader

#Import csv fle to python (testing whether it works)
#open file on read mode with UTF-8 encoding
file_handle = open(r"Krause21.csv", "r", encoding="utf-8")
# create a DictReader object to parse through the file
# Dictreader reads each row into a dictionary
# keys are taken from the first line - header row
# values are the corresponding fields in each row
csv_reader = DictReader(file_handle, delimiter = ",")
#loop through each row and print the dictionary
for row in csv_reader:
    print(row)
#close the reader - needs to be done always
file_handle.close()
# open and read HarrisPartIII csv file 
file_handle1 = open(r"HarrisPartIII.csv", "r", encoding="utf-8") 
# create a new Dictreader similar to above
csv_reader1= DictReader(file_handle1, delimiter = ",") 
#loop through and print rows from this file
for row in csv_reader1: 
    print(row)
#Close the second file
file_handle1.close()

#import csv file to pandas (real)
Galaxydata_1 = pd.read_csv(r"Krause21.csv")
print(Galaxydata_1)

9/28 Sunday Meeting
Option 1 Accreted Milky Way Globular Clusters
Xingkun: Globular Clusters,Elliptical 
Graph analysis based on clusters
