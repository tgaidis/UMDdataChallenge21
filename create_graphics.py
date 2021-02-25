import requests
import json
import pandas as pd
import csv
import statistics
import sys
import random
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

'''This program will create several line graphs of a countrys indicators.
To run, you must already have the CSV file for the country.
Simply type in the terminal:
python3 create_graphics.py "Country"
'''

df1 = pd.read_csv("countries/"+sys.argv[1]+".csv")
covid_r = []
covid_d = []
flu_r = []
flu_d = []
mask_r =[]
mask_d = []
contact_r = []
contact_d = []
finance_r = []
finance_d = []
anosmia_r = []
anosmia_d = []
vaccine_acpt_r = []
vaccine_acpt_d = []
covid_vaccine_r = []
covid_vaccine_d = []
trust_fam_r = []
trust_fam_d = []
trust_healthcare_r = []
trust_healthcare_d = []
trust_who_r = []
trust_who_d = []

for i in range(len(df1)):
    if str(df1.loc[i][1]) == "covid":
        covid_r.append(df1.loc[i][0])
        covid_d.append(i)
    elif str(df1.loc[i][1]) == "flu":
        flu_r.append(df1.loc[i][0])
        flu_d.append(i)
    elif str(df1.loc[i][1]) == "mask":
        mask_r.append(df1.loc[i][0])
        mask_d.append(i)
    elif str(df1.loc[i][1]) == "contact":
        contact_r.append(df1.loc[i][0])
        contact_d.append(i)
    elif str(df1.loc[i][1]) == "finance":
        finance_r.append(df1.loc[i][0])
        finance_d.append(i)
    elif str(df1.loc[i][1]) == "anosmia":
        anosmia_r.append(df1.loc[i][0])
        anosmia_d.append(i)
    elif str(df1.loc[i][1]) == "vaccine_acpt":
        vaccine_acpt_r.append(df1.loc[i][0])
        vaccine_acpt_d.append(i)
    elif str(df1.loc[i][1]) == "covid_vaccine":
        covid_vaccine_r.append(df1.loc[i][0])
        covid_vaccine_d.append(i)
    elif str(df1.loc[i][1]) == "trust_fam":
        trust_fam_r.append(df1.loc[i][0])
        trust_fam_d.append(i)
    elif str(df1.loc[i][1]) == "trust_healthcare":
        trust_healthcare_r.append(df1.loc[i][0])
        trust_healthcare_d.append(i)
    elif str(df1.loc[i][1]) == "trust_who":
        trust_who_r.append(df1.loc[i][0])
        trust_who_d.append(i)
    
plt.subplot(6,1,1)
plt.plot(covid_d, covid_r, color="blue", label="Covid")
plt.xlabel("Date")
plt.title("Covid")

plt.subplot(6,1,2)
plt.plot(flu_d, flu_r, color="red", label="Flu")
plt.xlabel("Date")
plt.title("Flu")

plt.subplot(6,1,3)
plt.plot(mask_d, mask_r, color="orange", label="Mask")
plt.xlabel("Date")
plt.title("Mask")

plt.subplot(6,1,4)
plt.plot(contact_d, contact_r, color="green", label="Contact")
plt.xlabel("Date")
plt.title("Contact")

plt.subplot(6,1,5)
plt.plot(finance_d, finance_r, color="yellow", label="Finace")
plt.xlabel("Date")
plt.title("Finance")

plt.subplot(6,1,6)
plt.plot(anosmia_d, anosmia_r, color="purple", label="Anosmia")
plt.xlabel("Date")
plt.title("Anosmia")


plt.tight_layout()
plt.show()
