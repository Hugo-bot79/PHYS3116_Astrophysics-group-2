Assessment task meeting notes for the third meeting
# Date: Thursday, 16/10/2025
# Group meeting 4
# Attendee: Hugo Chen, Abhinaya Jeyandran

Agenda:
- Github
- Code will be contributed before Friday by each member.

What have we said in the meeting?

We will plot: 
HB type vs FE 

Abhi - will mess around with more the code and have extra meetings on the weekends
We will record together in person and will try Chatswood Highschool or UNi

# Hugo Chen:
"We will plot the second graph to rule out the possible accreted clusters. For example, M_V versus R_G or HBType versus [Fe/H]."
"We will need to fix all the coding error in the previous files and decide the role for everyone in the final video."
"We can add kinematic analysis as an option for the final video."
"Choose a day on week 6 to record the final video."
"Extra meeting on Sunday."



Three lines of codes:
# Will first do the codes for M_V versus R_G above 
# We need to filter the stars with high HBType, as high HBType means strongly blue horizontal branch. These are the older and metal-poor clusters. and it's a strong indication of accreted galaxy (The reference will provided in the final project).
# We will keep all rows with HBtype > 8
HB_merged_data = merged_data[merged_data['HBtype'] > 8]
print(HB_merged_data)

# Create the figure and axis
fig, axis1 = plt.subplots(figsize=(10, 5))

# label the M_V in y axis and R_G in the x axis.
plt.xlabel('M_V(mag)')
plt.ylabel('R_G(kpc)')

# Plot the scatter plot and set up the colour as blue
plt.scatter(HB_merged_data['M_V(mag)'], HB_merged_data['R_G(kpc)'], color = "green", marker='o')

# Abhi code

#Loop through each row in the 'cand' DataFrame (these are the potential accreted clusters)
for _, row in cand.iterrows():
    
    # Skip any rows where coordinate or label values are missing (to avoid errors)
    if not (pd.isna(row["R_G"]) or pd.isna(row["HBtype"]) or pd.isna(row["NGC"])):
        
        # Add a small text label ("NGC ####") near the plotted data point
        ax.annotate(
            f"NGC {row['NGC']}",        # Text displayed on the plot (e.g., "NGC 104")
            xy=(row["R_G"], row["HBtype"]),  # The (x, y) coordinates of the data point
            xytext=(4, 4),              # Slightly offset the label by 4 pixels in both directions
            textcoords="offset points", # Interpret xytext as a small offset (not absolute coordinates)
            fontsize=9,                 # Label text size (small enough not to clutter)
            fontweight="bold",          # Bold text for clarity
            color="black",              # Black text for visibility on most backgrounds
            alpha=0.9                   # Slight transparency so text isn’t overly harsh
        )
