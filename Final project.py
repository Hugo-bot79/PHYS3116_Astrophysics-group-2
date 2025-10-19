
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

# Fourth step: Data cleaning and preparation
# Normalize IDs for merging
def ngc_number(id):
# Ensures that only NGC on common are processed.
    if pd.isna(id):
        return None
# Filters only those entries that are labeled with "NGC"
    if "NGC" in id:
        return id.replace("NGC", "").strip()
    return None

# Before we merge the data, we need to change object and #NGC columns of data from Krause21 and vandenBerg_table2 to a common format.
krau["NGC"] = krau["Object"].str.extract(r'(\d+)', expand=False)
vdb["NGC"] = vdb["#NGC"].astype(str)

# select only relevant columns for diagnostics
krau_selected = krau[["NGC", "Age", "FeH"]]
vdb_selected = vdb[["NGC", 'HBtype', 'R_G', 'M_V']]

# Fifth step: Merge datasets on the normalized NGC column
# Note that we only investigate the common clusters (NGC...) in all datasets
merged_data = pd.merge(krau_selected, vdb_selected, on="NGC")
print(merged_data)

#Sixth step: Convert each column to floating numbers
# Helper function to convert a pandas Series to float, handling errors
def to_float_series(series):
    return pd.to_numeric(series, errors='coerce')

# Convert relevant columns to float
merged_data['Age'] = to_float_series(merged_data['Age'])
merged_data['FeH'] = to_float_series(merged_data['FeH'])
merged_data['HBtype'] = to_float_series(merged_data['HBtype'])
merged_data['R_G'] = to_float_series(merged_data['R_G'])
merged_data['M_V'] = to_float_series(merged_data['M_V'])
print(merged_data)

plt.title("Age vs [Fe/H] for Milky Way Globular Clusters")

for row in merged_data.iterrows():
    plt.annotate(
        str(row[1]['NGC']),
        xy=(row[1]['FeH'], row[1]['Age']),
        xytext=(3, 3),
        textcoords="offset points",
        fontsize=8,
        alpha=0.9
    )

plt.grid(True)
plt.show()


