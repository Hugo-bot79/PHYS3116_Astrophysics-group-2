
# import necessary libraries for data analysis

#use numpy for numerical calculation-> arrays
import numpy as np
#use pandas for spreadsheet data
import pandas as pd

import matplotlib.pyplot as plt
from astropy.io import fits

# Second step: import the dataset to the python
from csv import DictReader
file_handle = open(r"Option 1\Krause21.csv", "r", encoding="utf-8")
csv_reader = DictReader(file_handle, delimiter=",")
for row in csv_reader:
    print(row) 

file_handle.close()

file_handle1 = open(r"Option 1\vandenBerg_table2.csv", "r", encoding="utf-8")
csv_reader = DictReader(file_handle1, delimiter=",")
for row in csv_reader:
    print(row)  

file_handle.close()

# Third step: import csv file to pandas
krau = pd.read_csv(r"Option 1\Krause21.csv")
vdb = pd.read_csv(r"Option 1\vandenBerg_table2.csv")
# Print out the data in the terminal to check if the data is imported correctly
print(krau)
print(vdb)

# Fourth step: Data cleaning and preparation
# Normalize IDs for merging, extract the NGC number 
def ngc_number(id):
# checks whether the id is missing value
    if pd.isna(id):
        return None
# Check whether 'NGC' is present.
    if "NGC" in id:
        return id.replace("NGC", "").strip()
    return None # If no NGC, then return empty set


# Before we merge the data, we need to change object and #NGC columns of data from Krause21 and vandenBerg_table2 to a common format.
krau["NGC"] = krau["Object"].str.extract(r'(\d+)', expand=False) # the r'(\d+)' can be used to extract the number part, while expand=False returns a Series.
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

# Seventh step, plot the graph of age against metallicity to identify the possible accreted clusters from the merged data
plt.figure(figsize=(10, 6))

# Put the age in y axis and FeH in the x axis
plt.xlabel('FeH')
plt.ylabel('Age (Gyr)')
plt.scatter( merged_data['FeH'], merged_data['Age'], color = "blue", marker='o')

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

# KK: Apply the filter

# We can also apply a filter for age and FeH to identify the possible accreted clusters.
# Threshold use 
feh_cutoff = -1.5


# Select obvious candidates
age_threshold = merged_data['Age'].quantile(0.75)
# Keep only rows that are both very metal-poor and very old
candis = merged_data[(merged_data['FeH'] <= feh_cutoff) & (merged_data['Age'] >= age_threshold)].copy()

# Highlight candidates
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(candis['FeH'], candis['Age'], s=80, marker='*', color='blue', edgecolors='k', linewidths=0.5, label='Candidates')
ax.legend(loc='best')

# Save outputs
cols = [c for c in ['NGC', 'FeH', 'Age', 'R_G', 'M_V'] if c in candis.columns]

candis[cols].to_csv('week4_candidates.csv', index=False)
fig.savefig('week4_age_feh_candidates.png', dpi=200)

# Summary
print(f"Age threshold (Q3): {age_threshold:.2f} Gyr | FeH cutoff: {feh_cutoff}")
print(f"Candidates flagged: {len(candis)}")
print(candis[cols].to_string(index=False))



# Eightth step, plot M_V vs R_G in the filter of HBtype to identify the possible accreted clusters from the merged data
# Set up the figure size and axis
plt.figure(figsize=(10, 6))
# label the M_V in y axis and R_G in the x axis.
# label the M_V in y axis and R_G in the x axis.
plt.xlabel('R_G(kpc)')
plt.ylabel('M_V(mag)')

# Plot the scatter plot and set up the colour as blue
plt.scatter(merged_data['R_G'], merged_data['M_V'], color="green", marker='o')
plt.title("M_V vs R_G for Milky Way Globular Clusters")

for _, row in merged_data.iterrows():
    plt.annotate(
        str(row['NGC']),
        xy=(row['R_G'], row['M_V']),  
        xytext=(3, 3),
        textcoords="offset points",
        fontsize=8,
        alpha=0.9
    )

plt.grid(True)
plt.show()

# What can this graph tell us?
# For the clusters that are located at larger R_G, they are most likely originated from the outer halo or have been accreted from the dwarf galaxies.
# This is beacuse the clusters that are originated from the thin disk or inner halo are most likely loctae at the smaller R_G, referring to Belokurov & Kravtsov (2023).


# If we apply the filter
# We will keep all rows with HBtype > 0.85
HB_merged_data = merged_data[merged_data['HBtype'] > 0.85].copy()
print(HB_merged_data)

# Create the figure and axis
plt.figure(figsize=(10, 6))

# label the M_V in y axis and R_G in the x axis.
plt.xlabel('R_G(kpc)')
plt.ylabel('M_V(mag)')

# Plot the scatter plot and set up the colour as blue
plt.scatter(HB_merged_data['R_G'], HB_merged_data['M_V'], color="green", marker='o')
plt.title("M_V vs R_G for Milky Way Globular Clusters with HBtype > 0.85")

# From the codes that are contributed from Abhi, I label the clusters on my graph
for _, row in HB_merged_data.iterrows():
    plt.annotate(
        str(row['NGC']),
        xy=(row['R_G'], row['M_V']),  
        xytext=(3, 3),
        textcoords="offset points",
        fontsize=8,
        alpha=0.9
    )

plt.grid(True)
plt.show()



# Reference
# Belokurov V., Kravtsov A., 2023, MNRAS, 525, 4456.

