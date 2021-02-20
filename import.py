import requests 
import json 
import pandas as pd
import csv

datesList = [
    ("May", 20200501, 31),
    ("June", 20200601, 30),
    ("July", 20200701, 31),
    ("August", 20200801, 31),
    ("September", 20200901, 30),
    ("October", 20201001, 31),
    ("November", 20201101, 30), 
    ("December", 20201201, 31),
    ("January", 20210101, 31),
    ("February", 20210201, 28)
]

indicatorList = [
    "covid", 
    "flu", 
    "mask",
    "contact",
    "finance", 
    "anosmia",
    "vaccine_acpt",
    "covid_vaccine",
    "trust_fam",
    "trust_healthcare",
    "trust_who",
    "trust_govt",
    "trust_politicians",
    "twodoses",
    "concerned_sideeffects",
    "hesitant_sideeffects",
    "modified_acceptance",
    "access_wash",
    "wash_hands_24h_3to6",
    "wash_hands_24h_7orMore",
    "cmty_covid"
]

countryList = []
with open('DC21Country.csv', newline='') as inputFile:
    for row in csv.reader(inputFile):
        countryList.append(row[1])
countryList.remove('country')
#print(countryList)

linkList = []

urlBase = "https://covidmap.umd.edu/api/resources?indicator="

def linkBuilder(urlBase, datesList, indicatorList, countryList, linkList):
    for i in countryList:
        curr_country = i
        #print(curr_country)
        for i in datesList:
            monthName = i[0]
            monthDate = i[1]
            dayRange = i[2]
            #print(curr_country, monthName)
            for l in range(dayRange):
                day = l
                #print(monthName, monthDate, dayRange, l)
                for j in indicatorList:
                    curr_indicator = j
                    #print(monthName, monthDate, dayRange)
                    api_link = urlBase + curr_indicator + "&type=smoothed&country=" + curr_country + "&date=" + str(monthDate + day)
                    print(api_link)
                    #print(curr_country, monthName)


linkBuilder(urlBase, datesList, indicatorList, countryList, linkList)


"""
for i in range(1):
    newdate= maydate + i
    #COVIDurl
    newCOVIDurl = COVIDurl + str(newdate)
    newCOVIDurl = str(newCOVIDurl)
    #print(newCOVIDurl)
    #MASKurl
    newMASKurl = MASKurl + str(newdate)
    newMASKurl = str(newMASKurl)
    #COVIDreturns
    responseCOVID = requests.get(newCOVIDurl).text
    jsonDataCOVID = json.loads(responseCOVID)
    print(jsonDataCOVID)
    #MASKreturns
    responseMASK = requests.get(newMASKurl).text
    jsonDataMASK = json.loads(responseMASK)
    print(jsonDataMASK)
"""

    
