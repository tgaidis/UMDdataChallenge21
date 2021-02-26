#import packages
import pandas as pd
import matplotlib as plt
import csv

#import dataframe
bigDF = pd.read_csv('schengendataset.csv')
#change to Datetime
bigDF['Date'] = pd.to_datetime(bigDF['Date'], format = '%Y%m%d')

#list of countries (for reference)
countryList = []
with open('schengenCountries.csv', newline='') as inputFile:
    for row in csv.reader(inputFile):
        countryList.append(row[1])
countryList.remove('Country')

#list of indicators
indicatorList = ["CLI", "Flu", "Mask","Contact",
"Finance", "Anosmia","Vaccine_acpt","Covid_vaccine",
"Trust_fam","Trust_healthcare","Trust_who","Trust_govt",
"Trust_politicians","Twodoses","concerned_sideeffects",
"hesitant_sideeffects","modified_acceptance","access_wash",
"wash_hands_24h_3to6","wash_hands_24h_7orMore","cmty_covid"
]

#Analysis Functions!

#Country Selection Function
def countrySelector(countries):
    val = 'go'
    selection = []
    print('Please select the countries you wish to graph. type "all" to select all. type "next" when done.')
    print('The list of countries is as follows: ', countries)
    while val != 'next':
        val = input("Enter a country (or next): ")
        if val in countries:
            selection.append(val)
        if val == "next" and len(selection) != 0:
            return selection
        if val =="all":
            return countries
        if val != "next" and val not in countries:
            print("The country you selected is not valid.  Please try another.")
            val = input("Enter a country (or next): ")

def indicatorSelector(indicators):
    val = 'go'
    selection = []
    print('Please select the indicators you would like to graph. type "all" to select all. type "next" when done.')
    print('The list of indicators is as follows: ', indicators)
    while val != 'next':
        val = input("Enter an indicator (or next): ")
        if val in indicators:
            selection.append(val)
        if val == "next" and len(selection) != 0:
            return selection
        if val == "all":
            return indicators
        if val != "next" and val not in indicators:
            print("The indicator(s) you selected are not valid.  Please try another.")
            val = input("Enter an indicator (or next): ")

def dataShaper(countries, bigData):
    #retrieve data from other functions
    #selectedI = indicatorSelector(indicators)
    #make dataset for each country
    selectedC = bigData.loc[bigData['Country'].isin(countries)]
    return selectedC

def graphMaker(info, indicators):
    #info['Date'] = pd.to_datetime(info['Date'], format = '%Y%m%d')
    lines = info.plot(x='Date', y=indicators)
    return lines

xc = countrySelector(countryList)
yi = indicatorSelector(indicatorList)
df = dataShaper(xc, bigDF)
graphMaker(df, yi)








