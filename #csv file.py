#Computational assignment

#first step, define and install all package that we need.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Import csv file to python (testing whether it works)
from csv import DictReader
file_handle = open("Krause21.csv", "r", encoding = "utf-8")
csv_reader = DictReader(file_handle, delimiter = ",")
for row in csv_reader:
    print(row)

file_handle.close()

#import csv file to pandas (real)
Galaxydata_1 = pd.read_csv("Krause21.csv")
print(Galaxydata_1)

#Plot the graph wrt Age
plt.scatter(Galaxydata_1.Object, Galaxydata_1.Age, color = "blue", marker = "o")
plt.xlabel("Object")
plt.ylabel("Age")
plt.title("Age of different galaxies")
plt.show()

#Plot the graph wrt metallicity
plt.scatter(Galaxydata_1.Object, Galaxydata_1.FeH, color = "red", marker = "o")
plt.xlabel("Object")
plt.ylabel("FeH")
plt.title("metalicity of different galaxies")
plt.show()
#The graph of the object vs FeH show that most of the stellar populations in Krause are metal poor except a few stellar populations like LMC, SMC, NGC 6822 etc. which are metal rich.

#Plot the graph wrt Mass
plt.scatter(Galaxydata_1.Object, Galaxydata_1.Mstar, color = "green", marker = "o")
plt.xlabel("Object")
plt.ylabel("MStar")
plt.title("Mass of different galaxies")
plt.show()
#The graph of the object vs Mstar show that most of the stellar populations in Krause are low mass except a few stellar populations like LMC, SMC, NGC 6822 etc. which are high mass.

#rₕ vs. M★ → reveals how galaxy size scales with stellar mass
#rₕ vs. redshift → shows how galaxies evolve in size over cosmic time
#Plot the graph wrt rh
plt.scatter(Galaxydata_1.Object, Galaxydata_1.rh, color = "green", marker = "o")
plt.xlabel("Object")
plt.ylabel("rh")
plt.title("half-light radius of different galaxies")
plt.show()
#The graph of the object vs rh show that most of the stellar populations in Krause have small half-light radius except a few stellar populations like LMC, SMC, NGC 6822 etc. which have large half-light radius.

