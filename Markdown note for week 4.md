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
# Based on our investigation, there are more clusters of stars in Krause 21 compared to the number of clusters of stars in vandeBerg_table2.
# Therefore, we will use the age and FeH in the this dataset to fist define the obvious candidates for accreted cluster (The codeing graph will be written by Hugo, Abhi and XingKun).
# Create the figure and axis
fig, axis1 = plt.subplots(figsize=(10, 5))

# Plot Age on the left y-axis
# label the age in y axis and FeH in the x axis.
plt.xlabel('FeH')
plt.ylabel('Age')

# Plot the scatter plot and set up the colour as blue
plt.scatter(Galaxydata_1_selected['FeH'], Galaxydata_1_selected['Age'], color = "blue", marker='o')



# Fix mistakes from the last meeting note about meeting data.
# Because there are more clusters in Krause21 compared to vandeBerg_table2. And almost all cluters in vandeBerg_table2 is covered in Krause21. Therefore, I need to remove some rows before merging data, and we have to first identify the obvious candidate from the Krause21.

# Remove the rows from Krause21 and vandeBerg_table2 so that they have the same rows. 
# From the Krause21
removed_objects = ['Ruprecht106', 'Terzan7', 'Palomar12', 'NGC1904', 'NGC2298', 'NGC5897', 'NGC6093', 'NGC6139', 'NGC6388', 'NGC6441', ]  # example objects to remove
krau_1 = krau_1[~krau_1['Object'].isin(removed_objects)].copy()
print(krau_1)

# From the vandeBerg_table2.
removed_ngc = ['4147', 'XXXX']          # example NGC I want to remove
vdb_2 = vdb_2[~vdb_2['#NGC'].isin(removed_ngc)].copy()
print(vdb_2)

# rename '#NGC' to 'object' for vendenberg table so that these two set of data can be merged
vdb_2.rename(columns={'#NGC': 'Object'}, inplace=True)
print(vdb_2)

# Add 'NGC' to the front of each entry in the 'Object' column
vdb_2['Object'] = 'NGC' + vdb_2['Object'].astype(str).str.strip()
print(vdb_2)

# select the data that we need from both csv file. Note that rh and log_sigma_0 will be chosen to identify the rotational kinematic.
Galaxydata_1_selected = krau_1[['Object', 'Mstar', 'rh', 'FeH', 'Age']]
Galaxydata_2_selected = vdb[['Object', 'HBtype', 'R_G', 'log_sigma_0']]