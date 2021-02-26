import requests
import json
import pandas as pd
import csv
import statistics
import sys
import random
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

'''This program gets all the data of a specific country from May 1st to the present.
In order to run this program you must have already ran "get_all_indicator_data.py" 
which would have created all the necessary CSV files for this program to work'''
countries = [
    "Austria",
    "Belgium",
    "Czech Republic",
    "Denmark",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Italy",
    "Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland"
    ]
for country in countries:
    with open("countries/"+country+".csv", "a") as f:
        headers = ["Percent", "Indicator", "Date"]
        dict_writer = csv.DictWriter(f, headers)
        if f.tell() == 0:
            dict_writer.writeheader()
            
        df1 = pd.read_csv("indicators/covid.csv")
        for i in range(len(df1)):
            if str(df1.loc[i][5]) == country:
                f.write(str(df1.loc[i][0]))
                f.write(",")
                f.write("covid")
                f.write(",")
                f.write(str(df1.loc[i][8]))
                f.write("\n")
                
        df2 = pd.read_csv("indicators/flu.csv")
        for i in range(len(df2)):
            if str(df2.loc[i][5]) == country:
                f.write(str(df2.loc[i][0]))
                f.write(",")
                f.write("flu")
                f.write(",")
                f.write(str(df2.loc[i][8]))
                f.write("\n")
                
        df3 = pd.read_csv("indicators/mask.csv")
        for i in range(len(df3)):
            if str(df3.loc[i][5]) == country:
                f.write(str(df3.loc[i][0]))
                f.write(",")
                f.write("mask")
                f.write(",")
                f.write(str(df3.loc[i][8]))
                f.write("\n")
                
        df4 = pd.read_csv("indicators/contact.csv")
        for i in range(len(df4)):
            if str(df4.loc[i][5]) == country:
                f.write(str(df4.loc[i][0]))
                f.write(",")
                f.write("contact")
                f.write(",")
                f.write(str(df4.loc[i][8]))
                f.write("\n")
                
        df5 = pd.read_csv("indicators/finance.csv")
        for i in range(len(df5)):
            if str(df5.loc[i][5]) == country:
                f.write(str(df5.loc[i][0]))
                f.write(",")
                f.write("finance")
                f.write(",")
                f.write(str(df5.loc[i][8]))
                f.write("\n")
        
        df6 = pd.read_csv("indicators/anosmia.csv")
        for i in range(len(df6)):
            if str(df6.loc[i][5]) == country:
                f.write(str(df6.loc[i][0]))
                f.write(",")
                f.write("anosmia")
                f.write(",")
                f.write(str(df6.loc[i][8]))
                f.write("\n")
        
        df7 = pd.read_csv("indicators/vaccine_acpt.csv")
        for i in range(len(df7)):
            if str(df7.loc[i][5]) == country:
                f.write(str(df7.loc[i][0]))
                f.write(",")
                f.write("vaccine_acpt")
                f.write(",")
                f.write(str(df7.loc[i][8]))
                f.write("\n")
                
        df8 = pd.read_csv("indicators/covid_vaccine.csv")
        for i in range(len(df8)):
            if str(df8.loc[i][5]) == country:
                f.write(str(df8.loc[i][0]))
                f.write(",")
                f.write("covid_vaccine")
                f.write(",")
                f.write(str(df8.loc[i][8]))
                f.write("\n")
                
        df9 = pd.read_csv("indicators/trust_fam.csv")
        for i in range(len(df9)):
            if str(df9.loc[i][5]) == country:
                f.write(str(df9.loc[i][0]))
                f.write(",")
                f.write("trust_fam")
                f.write(",")
                f.write(str(df9.loc[i][8]))
                f.write("\n")
                
        df10 = pd.read_csv("indicators/trust_healthcare.csv")
        for i in range(len(df10)):
            if str(df10.loc[i][5]) == country:
                f.write(str(df10.loc[i][0]))
                f.write(",")
                f.write("trust_healthcare")
                f.write(",")
                f.write(str(df10.loc[i][8]))
                f.write("\n")
                
        df11 = pd.read_csv("indicators/trust_who.csv")
        for i in range(len(df11)):
            if str(df11.loc[i][5]) == country:
                f.write(str(df11.loc[i][0]))
                f.write(",")
                f.write("trust_who")
                f.write(",")
                f.write(str(df11.loc[i][8]))
                f.write("\n")
                
        df12 = pd.read_csv("indicators/trust_govt.csv")
        for i in range(len(df12)):
            if str(df12.loc[i][5]) == country:
                f.write(str(df12.loc[i][0]))
                f.write(",")
                f.write("trust_govt")
                f.write(",")
                f.write(str(df12.loc[i][8]))
                f.write("\n")
        
        df13 = pd.read_csv("indicators/trust_politicians.csv")
        for i in range(len(df13)):
            if str(df13.loc[i][5]) == country:
                f.write(str(df13.loc[i][0]))
                f.write(",")
                f.write("trust_politicians")
                f.write(",")
                f.write(str(df13.loc[i][8]))
                f.write("\n")
        
        df14 = pd.read_csv("indicators/twodoses.csv")
        for i in range(len(df14)):
            if str(df14.loc[i][5]) == country:
                f.write(str(df14.loc[i][0]))
                f.write(",")
                f.write("twodoses")
                f.write(",")
                f.write(str(df14.loc[i][8]))
                f.write("\n")
        
        df15 = pd.read_csv("indicators/concerned_sideeffects.csv")
        for i in range(len(df15)):
            if str(df15.loc[i][5]) == country:
                f.write(str(df15.loc[i][0]))
                f.write(",")
                f.write("concerned_sideeffects")
                f.write(",")
                f.write(str(df15.loc[i][8]))
                f.write("\n")
                
        df16 = pd.read_csv("indicators/hesitant_sideeffects.csv")
        for i in range(len(df16)):
            if str(df16.loc[i][5]) == country:
                f.write(str(df16.loc[i][0]))
                f.write(",")
                f.write("hesitant_sideefects")
                f.write(",")
                f.write(str(df16.loc[i][8]))
                f.write("\n")
                
        df17 = pd.read_csv("indicators/modified_acceptance.csv")
        for i in range(len(df17)):
            if str(df17.loc[i][5]) == country:
                f.write(str(df17.loc[i][0]))
                f.write(",")
                f.write("modified_acceptance")
                f.write(",")
                f.write(str(df17.loc[i][8]))
                f.write("\n")
                
        df18 = pd.read_csv("indicators/access_wash.csv")
        for i in range(len(df18)):
            if str(df18.loc[i][5]) == country:
                f.write(str(df18.loc[i][0]))
                f.write(",")
                f.write("access_wash")
                f.write(",")
                f.write(str(df18.loc[i][8]))
                f.write("\n")
                
        df19 = pd.read_csv("indicators/wash_hands_24h_3to6.csv")
        for i in range(len(df19)):
            if str(df19.loc[i][5]) == country:
                f.write(str(df19.loc[i][0]))
                f.write(",")
                f.write("wash_hands_24h_7orMore")
                f.write(",")
                f.write(str(df19.loc[i][8]))
                f.write("\n")
        
        df20 = pd.read_csv("indicators/wash_hands_24h_7orMore.csv")
        for i in range(len(df20)):
            if str(df20.loc[i][5]) == country:
                f.write(str(df20.loc[i][0]))
                f.write(",")
                f.write("wash_hands_24h_7orMore")
                f.write(",")
                f.write(str(df20.loc[i][8]))
                f.write("\n")
        
        df21 = pd.read_csv("indicators/cmty_covid.csv")
        for i in range(len(df21)):
            if str(df21.loc[i][5]) == country:
                f.write(str(df21.loc[i][0]))
                f.write(",")
                f.write("cmty_covid")
                f.write(",")
                f.write(str(df21.loc[i][8]))
                f.write("\n")
        
        df22 = pd.read_csv("indicators/hes_side_effects.csv")
        for i in range(len(df22)):
            if str(df22.loc[i][5]) == country:
                f.write(str(df22.loc[i][0]))
                f.write(",")
                f.write("hes_side_effects")
                f.write(",")
                f.write(str(df22.loc[i][8]))
                f.write("\n")
        
        df23 = pd.read_csv("indicators/hes_wontwork.csv")
        for i in range(len(df23)):
            if str(df23.loc[i][5]) == country:
                f.write(str(df23.loc[i][0]))
                f.write(",")
                f.write("hes_wontwork")
                f.write(",")
                f.write(str(df23.loc[i][8]))
                f.write("\n")
        
        df24 = pd.read_csv("indicators/hes_dontbelieve.csv")
        for i in range(len(df24)):
            if str(df24.loc[i][5]) == country:
                f.write(str(df24.loc[i][0]))
                f.write(",")
                f.write("hes_dontbelieve")
                f.write(",")
                f.write(str(df24.loc[i][8]))
                f.write("\n")
        
        df25 = pd.read_csv("indicators/hes_dontlike.csv")
        for i in range(len(df25)):
            if str(df25.loc[i][5]) == country:
                f.write(str(df25.loc[i][0]))
                f.write(",")
                f.write("hes_dontlike")
                f.write(",")
                f.write(str(df25.loc[i][8]))
                f.write("\n")
                
        df26 = pd.read_csv("indicators/hes_waitlater.csv")
        for i in range(len(df26)):
            if str(df26.loc[i][5]) == country:
                f.write(str(df26.loc[i][0]))
                f.write(",")
                f.write("hes_waitlater")
                f.write(",")
                f.write(str(df26.loc[i][8]))
                f.write("\n")
                
        df27 = pd.read_csv("indicators/hes_otherpeople.csv")
        for i in range(len(df27)):
            if str(df27.loc[i][5]) == country:
                f.write(str(df27.loc[i][0]))
                f.write(",")
                f.write("hes_otherpeople")
                f.write(",")
                f.write(str(df27.loc[i][8]))
                f.write("\n")
                
        df28 = pd.read_csv("indicators/hes_cost.csv")
        for i in range(len(df28)):
            if str(df28.loc[i][5]) == country:
                f.write(str(df28.loc[i][0]))
                f.write(",")
                f.write("hes_cost")
                f.write(",")
                f.write(str(df28.loc[i][8]))
                f.write("\n")
                
        df29 = pd.read_csv("indicators/hes_religious.csv")
        for i in range(len(df29)):
            if str(df29.loc[i][5]) == country:
                f.write(str(df29.loc[i][0]))
                f.write(",")
                f.write("hes_religious")
                f.write(",")
                f.write(str(df29.loc[i][8]))
                f.write("\n")
        
        df30 = pd.read_csv("indicators/hes_other.csv")
        for i in range(len(df30)):
            if str(df30.loc[i][5]) == country:
                f.write(str(df30.loc[i][0]))
                f.write(",")
                f.write("hes_other")
                f.write(",")
                f.write(str(df30.loc[i][8]))
                f.write("\n")
        
        df31 = pd.read_csv("indicators/trust_doctors.csv")
        for i in range(len(df31)):
            if str(df31.loc[i][5]) == country:
                f.write(str(df31.loc[i][0]))
                f.write(",")
                f.write("trust_doctors")
                f.write(",")
                f.write(str(df31.loc[i][8]))
                f.write("\n")
    
    
        