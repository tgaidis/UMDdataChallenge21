import requests 
import json 
import pandas as pd
from pandas import DataFrame
import csv
import time

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

dataList = ["smoothed_cli", "smoothed_ili", "smoothed_mc", "smoothed_dc", 
"smoothed_hf", "smoothed_anos", "smoothed_vu", "smoothed_covid_vaccine", 
"smoothed_trust_fam", "smoothed_trust_healthcare", "smoothed_trust_who",
"smoothed_trust_govt", "smoothed_trust_politicians", "smoothed_twodoses",
"smoothed_concerned_sideeffects", "smoothed_hesitant_sideeffects", "smoothed_modified_acceptance", 
"smoothed_access_wash", "smoothed_wash_hands_24h_3to6", "smoothed_wash_hands_24h_7ormore", 
"smoothed_community_cli"]

'''
countryList = []
with open('DC21Country.csv', newline='') as inputFile:
    for row in csv.reader(inputFile):
        countryList.append(row[1])
countryList.remove('country')
#print(countryList)

allSchengen = ['Austria', 'Belgium', 'Czech Republic',
'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland',
'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Norway', 'Poland',
'Portugal', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland']

schengenCountriesList = []
for i in allSchengen:
    for j in countryList:
        if i ==j:
            schengenCountriesList.append(i)

#print(schengenCountries)
schengenDataset = DataFrame (schengenCountriesList, columns=[
'Country'])
schengenDataset.to_csv('schengenCountries.csv')
print(schengenDataset)
'''
countryList = []
with open('schengenCountries.csv', newline='') as inputFile:
    for row in csv.reader(inputFile):
        countryList.append(row[1])
countryList.remove('Country')
#print(countryList)


urlBase = "https://covidmap.umd.edu/api/resources?indicator="
#country = 'New Zealand'

#list to store all links
linkList = []

#def linkBuilder(urlBase, country, datesList, indicatorList, linkList):
#curr_country = country
#print(curr_country)
for i in countryList:
    curr_country = i
    for i in datesList:
        monthName = i[0]
        monthDate = i[1]
        dayRange = i[2]
        #print(curr_country, monthName)
        for l in range(dayRange):
            day = l
            for j in indicatorList:
                row = []
                curr_indicator = j
                api_link = urlBase + curr_indicator + "&type=smoothed&country=" + curr_country + "&date=" + str(monthDate + day)
                row.append(curr_country)
                row.append(monthName)
                row.append(str(day+1))
                row.append(monthDate + day)
                row.append(api_link)
                linkList.append(row)
                #print(row)

#print(linkList)

#linkBuilder(urlBase, country, datesList, indicatorList, italy)

dateList = [x[:] for x in linkList]

for i in dateList:
    del i[4]

iteratedList = []
for i in dateList[::21]:
    iteratedList.append(i)

#print(len(iteratedList))

#datesDF = DataFrame (iteratedList, columns = ['Country', 'Month', 'Day', 'Date'])
#datesDF.to_csv('allDates.csv')
#print(datesDF)

#datagrab function
def dataGrab(index1, index2):
    try:
        response = requests.get(linkList[index1][4]).text
        jsonData = json.loads(response)
        return(jsonData["data"][0][dataList[index2]])
    except:
        return None

def countryGrab(index3):
    return linkList[index3][0]

def dateGrab(index4):
    return linkList[index4][3]

#more setup
preDataFrame = []
counter1 = 0
counter2 = 0
counter3 = 0

for i in range(len(iteratedList)):
    tempRow = []

    country = countryGrab(counter1)
    tempRow.append(country)

    date = dateGrab(counter1)
    tempRow.append(date)

    covid = dataGrab(counter1, counter2)
    tempRow.append(covid)
    counter1 += 1
    counter2 += 1

    flu = dataGrab(counter1, counter2)
    tempRow.append(flu)
    counter1 += 1
    counter2 += 1

    mask = dataGrab(counter1, counter2)
    tempRow.append(mask)
    counter1 += 1
    counter2 += 1

    contact = dataGrab(counter1, counter2)
    tempRow.append(contact)
    counter1 += 1
    counter2 += 1

    finance = dataGrab(counter1, counter2)
    tempRow.append(finance)
    counter1 += 1
    counter2 += 1

    anosmia = dataGrab(counter1, counter2)
    tempRow.append(anosmia)
    counter1 += 1
    counter2 += 1

    vaccine_acpt = dataGrab(counter1, counter2)
    tempRow.append(vaccine_acpt)
    counter1 += 1
    counter2 += 1

    covid_vaccine = dataGrab(counter1, counter2)
    tempRow.append(covid_vaccine)
    counter1 += 1
    counter2 += 1

    trust_fam =dataGrab(counter1, counter2)
    tempRow.append(trust_fam)
    counter1 += 1
    counter2 += 1

    trust_healthcare =dataGrab(counter1, counter2)
    tempRow.append(trust_healthcare)
    counter1 += 1
    counter2 += 1

    trust_who =dataGrab(counter1, counter2)
    tempRow.append(trust_who)
    counter1 += 1
    counter2 += 1

    trust_govt = dataGrab(counter1, counter2)
    tempRow.append(trust_govt)
    counter1 += 1
    counter2 += 1

    trust_politicians =dataGrab(counter1, counter2)
    tempRow.append(trust_politicians)
    counter1 += 1
    counter2 += 1

    twodoses = dataGrab(counter1, counter2)
    tempRow.append(twodoses)
    counter1 += 1
    counter2 += 1

    concerned_sideeffects = dataGrab(counter1, counter2)
    tempRow.append(concerned_sideeffects)
    counter1 += 1
    counter2 += 1

    hesitant_sideeffects = dataGrab(counter1, counter2)
    tempRow.append(hesitant_sideeffects)
    counter1 += 1
    counter2 += 1

    modified_acceptance = dataGrab(counter1, counter2)
    tempRow.append(modified_acceptance)
    counter1 += 1
    counter2 += 1

    access_wash = dataGrab(counter1, counter2)
    tempRow.append(access_wash)
    counter1 += 1
    counter2 += 1

    wash_hands_24h_3to6 = dataGrab(counter1, counter2)
    tempRow.append(wash_hands_24h_3to6)
    counter1 += 1
    counter2 += 1

    wash_hands_24h_7orMore = dataGrab(counter1, counter2)
    tempRow.append(wash_hands_24h_7orMore)
    counter1 += 1
    counter2 += 1

    cmty_covid = dataGrab(counter1, counter2)
    tempRow.append(cmty_covid)
    counter1 += 1
    counter2 = 0
    counter3 += 1

    print(tempRow)
    preDataFrame.append(tempRow)
    print(str((counter3/len(iteratedList))*100) + "% Done..." + str(len(iteratedList)-counter3) + " rows remaining")

apiDataset = DataFrame (preDataFrame, columns=[
'Country', 'Date', 'CLI', 'Flu', 'Mask', 'Contact', 'Finance',
'Anosmia', 'Vaccine_acpt', 'Covid_Vaccine',
'Trust_fam', 'Trust_Healthcare', 'Trust_who',  
'Trust_govt', 'Trust_politicians', 'Twodoses', 
'concerned_sideeffects', 'hesitant_sideeffects',
'modified_acceptance', 'access_wash', 'wash_hands_24h_3to6',
'wash_hands_24h_7orMore', 'cmty_covid',
])

apiDataset.to_csv('schengendataset.csv')


#finalDataset = pd.merge(datesDF, apiDataset, how = 'outer')
#finalDataset.to_csv('NZData.csv')
print('Done')