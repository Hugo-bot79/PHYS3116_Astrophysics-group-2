
# import necessary libraries for data analysis

# handling numerical data (things such as convert data to numeric type, calculate threshold)
import numpy as np
# Manipulating spreadsheet(read and merge data)
import pandas as pd
# enable us to visualize the graph (Age and metalicity graph)
import matplotlib.pyplot as plt
# special library for astronomy-could be used
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


# We need to first change object and #NGC columns of data from Krause21 and vandenBerg_table2. 
# They should have a common format.
krau["NGC"] = krau["Object"].str.extract(r'(\d+)', expand=False) 
# the r'(\d+)' can be used to extract the number part, while expand=False returns a Series.
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
# ensure all numerical values are stored as floating point numbers (some may showed as text instead of numbers after merging the data)
merged_data['HBtype'] = to_float_series(merged_data['HBtype'])
merged_data['R_G'] = to_float_series(merged_data['R_G'])
merged_data['M_V'] = to_float_series(merged_data['M_V'])
print(merged_data)

# Seventh step, plot the graph of age vs metallicity to identify the possible accreted clusters
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
# I use feh_cutoff=-1.5 to isolate those clusters. Values lower than feh_cutoff shows a metal-poor cluster. Then I applied 75th percentile to isolate the oldest 25% of the clusters. This forms a subset of clusters. 
# Then I plot the filtered subsets by using some marker-*' marker to highlight the special clusters; color = 'blue' colour use to distinguish them clearly; edgecolor = 'k' to make the stars stands out visually; legend box will place where it best fits(no overlapping).
# Afterthat I build a column list to prevent some possible errors. By doing this we have a smallest analyzable scenario-> Only export fields that are valuable for diagnosing the accreted clusters.
# The CSV I generated now is the filtered set (“old cluster + low metal abundance”). Hugo and Abhi can directly use my candidate samples without rerunning the entire process->Png created


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

# Summary (Clearly display the filtering standard; Quantitatively show the suitability of the filtering conditions; Directly output the list of star clusters meeting the accretion criteria, without needing to open files for inspection)
print(f"Age threshold (Q3): {age_threshold:.2f} Gyr | FeH cutoff: {feh_cutoff}")
print(f"Candidates flagged: {len(candis)}")
print(candis[cols].to_string(index=False))



# Eightth step, plot M_V vs R_G to identify the possible accreted clusters
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
# for the clusters that are located at larger R_G, they are most likely originated from the outer halo or have been accreted from the dwarf galaxies.
# This is beacuse the clusters that are originated from the thin disk or inner halo are most likely loctae at the smaller R_G, referring to Belokurov & Kravtsov (2023).
# The absolute magnitude M_V  provide information about the luminosity of the clusters, where less M_V indicates a more luminous cluster.
# Accreted clusters are generally less luminous than those clusters originated in-situ. Referring to Marsakov et al. (2019).
# Therefore, the clusters with higher R_G and higher M_V are more likely to be accreted clusters in the graph.
# This suggested that NGC1621, NGC1851, NGC5024, NGC6715 in the graph might be accreted from dwarf galaxies.

# Apply the filter 'HBtype > 0.85' to the graph M_V vs R_G to identify accreted clusters.
# Referring to Marsakov et al. (2019).
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

# What can this graph tell us?
# Clusters with HBtype > 0.85 means that they may have blue horizontal branches. These clusters are older, metal-poor stellar populations.
# Therefore, these clusters are more likely to be accreted from dwarf galaxies, referring to McGill et al. (2025).
# Therefore, apply the filter allow us to analyse the old clusters in Milkey Way, and plot the graph of M_V and R_G to analyze these clusters. 
# However, the limitations of this filter is that some accreted clusters may have red horizontal branches.
# And clusters with large R_G and large M_V are not necessarily accreted since they can originate from the outer halo with large dark matter content.
# Therefore, further information like data from kinematic is required to comfirm the accreted clusters.

# Reference
# Belokurov V., Kravtsov A., 2023, MNRAS, 525, 4456.
# Marsakov V. A., Koval’ V. V., Gozha M. L., 2019, AstBu, 74, 403. 
# McGill G., Ferguson A. M. N., Mackey D., Huxor A. P., Lewis G. F., Martin N. F., McConnachie A. W., et al., 2025, MNRAS, 542, L60.


