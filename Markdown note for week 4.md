Assessment task meeting notes for the third meeting
# Date: Thursday, 09/10/2025 and Friday, 10/10/2025
# Group meeting 3
# Attendee: Hugo Chen, XingKun Feng, Abhinaya Jeyandran

Agenda:
- Github
- Code will be contributed before Friday by each member.

What have we said in the meeting?
# Hugo Chen:
"We have to fix some errors from the last lesson. For example, we need to include "rh" from the Krause 21 and vandeberg."
"I need to rename object in the krause 21 before merging the data."
"we decided to plot the age and metallicity graph this week to get rid of some obvious candidates this week."


# Abhinaya Jeyandran:
- We have decided which data sets to plot and will confer again at the end of the week to regroup.
- We need to decide next couple of plots and have decided to aim to plot by next week
- We have decided to proofread the existing code ASAP to make sure that we are flush out any errors that are existing.
- we decided to plot age and metallicity


# XingKun Feng:
-put previous code(week3 md) in python/vs code and assess. need to finish this and correct any possible errors for floating numbers before proceed to plot age & metaliciity graph in week 4 md.

# Three lines of codes and documentation
# Hugo Chen
#Based on our investigation, there are more clusters of stars in Krause 21 compared to the number of clusters of stars in vandeBerg_table2.
# Therefore, we will use the age and FeH in the this dataset to fist define the obvious candidates for accreted cluster (The codeing graph will be written by Hugo, Abhi and XingKun).
# Create the figure and axis
fig, axis1 = plt.subplots(figsize=(10, 5))


# label the age in y axis and FeH in the x axis.
plt.xlabel('FeH')
plt.ylabel('Age')

# Plot the scatter plot and set up the colour as blue
plt.scatter(Galaxydata_1_selected['FeH'], Galaxydata_1_selected['Age'], color = "blue", marker='o')



# Fix mistakes from the last meeting note about meeting data.
# Because there are more clusters in Krause21 compared to vandeBerg_table2. And almost all cluters in vandeBerg_table2 is covered in Krause21. Therefore, I need to remove some rows before merging data, and we have to first identify the obvious candidate from the Krause21.

# I have gone through the test, this codes didn't work well
# I would rather try this way:
# Select all the NGC cluster on common for the datasets
# Normalize names of the clusters for merging
# define the function to contain only clusters on common before merging data
def extract_ngc_number(id):
# Ensures that only NGC on common are processed.
    if pd.isna(id):
        return None
 # Filters only entries that are labeled with "NGC"
    if "NGC" in id:
        return id.replace("NGC", "").strip()
    return None

# Before we merge the data, we need to change  object and #NGC columns of data from Krause21 and vandenBerg_table2 to a common format
krau["NGC"] = krau["Object"].str.extract(r'(\d+)', expand=False) # The extract ensure that only number exist
vdb["NGC"] = vdb["#NGC"].astype(str)

# select only relevant columns for diagnostics
krau_selected = krau[["NGC", "rh", "FeH", "Age"]]
vdb_selected = vdb[["NGC", "HBtype", "R_G", "v_e0", "M_V"]]

# Note that we only investigate the common clusters (NGC...) in all datasets
merged_data = pd.merge(krau_selected, vdb_selected, on="NGC")
print(merged_data)


# abhi
- i have continued with the code from Hugo to add titles and labels
#title for the plot from above
axis1.set_title(
    "Age vs [Fe/H] for Milky Way Globular Clusters (Krause21 subset)",
    fontsize=14, pad=12
)
#this is for the labels for each of the plots, and the labels are slightly offset to make sure that it does not overlap
for row in Galaxydata_1_selected.iterrows():
    axis1.annotate(
        row["Object"],
        xy=(row["FeH"], row["Age"]),
        xytext=(3, 3),
        textcoords="offset points",
        fontsize=8,
        alpha=0.9
    )
- I also made a few errors in the code from last week that needed to be re-written
#this code was fixed from last week to define the function to convert it to a floating 
def to_float_series(s: pd.Series) -> pd.Series:
    out = pd.to_numeric(s, errors='coerce')
    
# Xingkun Feng
# Finalisation: flag obvious 'candidates', highlight them, save outputs

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Threshold use 
feh_cutoff = -1.5

# CreateMerge table
merge_data = pd.merge(Galaxydata_1_selected, Galaxydata_2_selected, on='Object', how='inner').copy()

# Select obvious candidates
age_threshold = merge_data['Age'].quantile(0.75)
# Keep only rows that are both very metal-poor and very old
candis = merge_data[(merge_data['FeH'] <= feh_cutoff) & (merge_data['Age'] >=age_threshold)].copy()

# Highlight candidates
ax = axis1
ax.scatter(..., s=80, marker='*', colors='blue', edgecolours='k', linewidths=0.5,label='Candidates')
ax.legend(loc='best')

# Save outputs
cols = [c for c in ['Object', 'FeH', 'Age', 'rh', 'R_G'] if c in candis.columns]
candis[cols].to_csv('week4_candidates.csv', index=False)
ax.get_figured().savefig('week4_age_feh_candidates.png', dpi=200)

# Summary
print(f"Age threshold (Q3): {age_threshold:.2f} Gyr | FeH cutoff: {feh_cutoff}")
print(f"Candidates flagged: {len(candis)}")
print(candis[cols].to_string(index=Flase))
