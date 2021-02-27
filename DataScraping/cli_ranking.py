import requests
import json
import pandas as pd
import csv
import statistics
import sys
import random
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

'''This program creates an ordered dictionary where the keys are each of the
countries listed in the API and the value is the average covid like illness 
percentage those who took the survey showed for the dates between May 1st and 
the present.
'''

countries = {
    "Afghanistan": [],
    "Albania": [],
    "Algeria": [],
    "Angola": [],
    "Argentina": [],
    "Armenia": [],
    "Australia": [],
    "Austria": [],
    "Azerbaijan": [],
    "Bangladesh": [],
    "Belarus": [],
    "Belgium": [],
    "Benin": [],
    "Bolivia": [],
    "Bosnia and Herzegovina": [],
    "Brazil": [],
    "Bulgaria": [],
    "Burkina Faso": [],
    "Cambodia": [],
    "Cameroon": [],
    "Canada": [],
    "Chile": [],
    "Colombia": [],
    "Costa Rica": [],
    "CÃ´te d'Ivoire": [],
    "Croatia": [],
    "Czech Republic": [],
    "Denmark": [],
    "Dominican Republic": [],
    "Ecuador": [],
    "Egypt": [],
    "El Salvador": [],
    "Ethiopia": [],
    "Finland": [],
    "France": [],
    "Germany": [],
    "Ghana": [],
    "Greece": [],
    "Guatemala": [],
    "Haiti": [],
    "Honduras": [],
    "Hong Kong": [],
    "Hungary": [],
    "India": [],
    "Indonesia": [],
    "Iraq": [],
    "Ireland": [],
    "Israel": [],
    "Italy": [],
    "Japan": [],
    "Jordan": [],
    "Kazakhstan": [],
    "Kenya": [],
    "Kuwait": [],
    "Kyrgyzstan": [],
    "Lebanon": [],
    "Libya": [],
    "Malaysia": [],
    "Mali": [],
    "Mexico": [],
    "Moldova": [],
    "Morocco": [],
    "Mozambique": [],
    "Myanmar": [],
    "Nepal": [],
    "Netherlands": [],
    "New Zealand": [],
    "Nicaragua": [],
    "Nigeria": [],
    "Norway": [],
    "Oman": [],
    "Pakistan": [],
    "Palestine": [],
    "Panama": [],
    "Paraguay": [],
    "Peru": [],
    "Philippines": [],
    "Poland": [],
    "Portugal": [],
    "Puerto Rico, U.S.": [],
    "Qatar": [],
    "Romania": [],
    "Russia": [],
    "Saudi Arabia": [],
    "Senegal": [],
    "Serbia": [],
    "Singapore": [],
    "Slovakia": [],
    "Slovenia": [],
    "South Africa": [],
    "South Korea": [],
    "Spain": [],
    "Sri Lanka": [],
    "Sudan": [],
    "Sweden": [],
    "Switzerland": [],
    "Taiwan": [],
    "Tanzania": [],
    "Thailand": [],
    "Tunisia": [],
    "Turkey": [],
    "Ukraine": [],
    "United Arab Emirates": [],
    "United Kingdom": [],
    "United States of America": [],
    "Uruguay": [],
    "Uzbekistan": [],
    "Venezuela": [],
    "Vietnam": [],
    "Yemen": []
}

df1 = pd.read_csv("indicators/covid.csv")
for i in range(len(df1)):
    name = str(df1.loc[i][5])
    if countries[name] != False:
        countries[name].append(df1.loc[i][0]) 
    else:
        "ERROR"
        break
for country in countries:
    countries[country] = sum(countries.get(country)) / len(countries.get(country))
    
sorted_values = sorted(countries.values())
sorted_countries = {}

for i in sorted_values:
    for k in countries.keys():
        if countries[k] == i:
            sorted_countries[k] = countries[k]
            break
print(sorted_countries)

