Assessment task meeting notes for the second meeting
# Date: Thursday, 02/10/2025 and Friday, 03/10/2025
# Group meeting 2 
# Attendee: Hugo Chen, XingKun Feng, Abhinaya Jeyandran

Agenda:
- Github

# Fix the error from the first meeting about the contents of the assessment task.
The purpose for this assessment task:  
Use stellar population (metallicities [Fe/H] and ages) and dynamical information to identify potentially accreted globular clusters. Consider if there are some globular clusters that stand out in the age metallicity relation or that do not rotate with the bulk of other globular clusters. 
Consider what the above findings might mean for how the Milky Way formed and how many of its globular clusters could be accreted and how many may have formed within the Milky Way. Consider what further tests could be performed to delineate various possible formation scenarios.
Our group has decided to use data vandenBerg_table2 insteand of HarrisPart III. This is because we want to analyse age-FeH relations and magnitude-Galactic radius to determine accreted globular cluster, and we are going to use mass of the star and HB type to conduct further analysis.  



#Note:
Hugo Chen: 
Defined the parameter on the table and sent the link of the article to other group members, so that we can find out the mistake that we made and make a proper choice and determine what we will talk about in the project.

And we have decided our tasks for this group meeting, I will choose the parameter that we need, Abhinaya and XingKun will change the data to floating numbers.



# First three lines of codes
#Hugo Chen:
# fix the problem from the last meeting
#import csv file to pandas (real)
#import Krause21.csv file to pandas. This step ensure pandas can read and manipulate the data. 
krau = pd.read_csv(r"Krause21.csv")
#import VandenBerg.csv file to pandas. This step ensure pandas can read and manipulate the data.
vdb = pd.read_csv(r"vandenBerg_table2.csv")
#test whether pandas can read the data from Krause21.csv
print(krau)
#test whether pandas can read the data from VandenBerg.csv
print(vdb)

#Select the required data from the Krause 21.csv.
Galaxydata_1_selected = krau[['Object', 'Mstar']]
#Select the required data from the VandeBerg.
Galaxydata_2_selected = vdb[['object', 'FeH', 'Age', 'HBtype' 'R_G' 'M_V', 'v_e0']]
#Merge the data that we need to a single datset.
merge_data = pd.merge(Galaxydata_1_selected, Galaxydata_2_selected, on = 'object')
#Print the resultant table in the terminal
print(merge_data)

#Abhinaya Jeyandran:

#import pandas for table loading, selction and merging
import pandas as pd
#import regex to parse numbers in needed
import re

#load the files that we are selecting from
krau = pd.read_csv('Kruase21.csv') 
vdb = pd.read_csv('vandenBerg_table,csv')

#Strip coloumn names from that spaces to not have any whitepspaces
krau.columns = [c.strp() for c in krau.columns]
vdb.columns = [c.strip() for c in vdb.columns]

#from Hugos code, we can now float the numeric columns
#in Krause: Mstar is numeric; keep 'object' as a string identifier
Galaxy_1_selected['Mstar'] = to_float_series(Galaxydata_1_selected['Mstar'])  #Convert Mstar to float

#In vandenberg, all numeric fields can be converted to float
#[Fe/H] metallicity → float
Galaxydata_2_selected['FeH'] = to_float_series(Galaxydata_2_selected['FeH']) 
#Age (Gyr) → float
Galaxydata_2_selected['Age'] = to_float_series(Galaxydata_2_selected['Age'])   
#HB type (B-R)/(B+V+R) - float
Galaxydata_2_selected['HBtype'] = to_float_series(Galaxydata_2_selected['HBtype'])

#XingKun Feng
#Convert R_G, M_V and v_e0 columns in merge data to float

#Convert R_G
#Unify as string which ensure all values have same type
merge_data['R_G'] = merge_data['R_G'].astype(str)
#Remove spaces
merge_data['R_G'] = merge_data['R_G'].str.strip()
#Convert into float finally
merge_data['R_G'] = merge_data['R_G'].astype(float)

#Convert M_V
merge_data['M_V'] = merge_data['M_V'].astype(str)
merge_data['M_V'] = merge_data['M_V'].str.strip()
merge_data['M_V'] = merge_data['M_V'].astype(float)

#Convert v_e0
merge_data['v_e0'] = merge_data['v_e0'].astype(str)
merge_data['v_e0'] = merge_data['v_e0'].str.strip()
merge_data['v_e0'] = merge_data['v_e0'].astype(float)

#Verification process
#Check Datatypes
print(merge_data[['R_G','M-V','v_e0']].dtypes)

#Confirm values
print(merge_data[['R_G','M-V','v_e0']].head())
