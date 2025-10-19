
# import necessary libraries for data analysis

#use numpy for numerical calculation-> arrays
import numpy as np
#use pandas for spreadsheet data
import pandas as pd

import matplotlib.pyplot as plt
from astropy.io import fits

# Second step: import the dataset to the python
from csv import DictReader
file_handle = open(r"Krause21.csv", "r", encoding="utf-8")
csv_reader = DictReader(file_handle, delimiter=",")
for row in csv_reader:
    print(row) 

file_handle.close()

file_handle1 = open(r"vandenBerg_table2.csv", "r", encoding="utf-8")
csv_reader = DictReader(file_handle1, delimiter=",")
for row in csv_reader:
    print(row)  

file_handle.close()

# Third step: import csv file to pandas
krau = pd.read_csv(r"Krause21.csv")
vdb = pd.read_csv(r"vandenBerg_table2.csv")
print(krau)
print(vdb)


