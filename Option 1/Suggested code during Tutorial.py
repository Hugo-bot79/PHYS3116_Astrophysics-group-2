# Lines of code that are discussed in the tutorial on Thursday, 25/09/2025
# The code has been discussed and recorded by Hugo Chen, XingKun Feng and Abhinaya Jeyandran

#first step, define and install all package that we need.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Import csv file to python (testing whether it works)
from csv import DictReader
file_handle = open(r"Krause21.csv", "r", encoding="utf-8")
csv_reader = DictReader(file_handle, delimiter = ",")
for row in csv_reader:
    print(row)

file_handle.close()

#import csv file to pandas (real)
Galaxydata_1 = pd.read_csv(r"Krause21.csv")
print(Galaxydata_1)