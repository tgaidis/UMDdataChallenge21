import requests 
import json 
import pandas as pd
from pandas import DataFrame
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
                    ind_list = []
                    curr_indicator = j
                    #print(monthName, monthDate, dayRange)
                    api_link = urlBase + curr_indicator + "&type=smoothed&country=" + curr_country + "&date=" + str(monthDate + day)
                    #print(api_link)
                    ind_list.append(curr_country)
                    ind_list.append(monthName)
                    ind_list.append(str(day+1))
                    ind_list.append(curr_indicator)
                    ind_list.append(api_link)
                    linkList.append(ind_list)
                    #print(ind_list)


linkBuilder(urlBase, datesList, indicatorList, countryList, linkList)

#linkDF = DataFrame (linkList, columns = ['Country', 'Month', 'Day', 'Indicator', 'Link'])
#linkDF.to_csv('indicatorsandLinks.csv')

dateList = [x[:] for x in linkList]

for i in dateList:
    del i[4]
    del i[3]

iteratedList = []
for i in dateList[::21]:
    iteratedList.append(i)

datesDF = DataFrame (iteratedList, columns = ['Country', 'Month', 'Day'])
#print(len(datesDF))

dataList = ["smoothed_cli", "smoothed_ili", "smoothed_mc", "smoothed_dc", 
"smoothed_hf", "smoothed_anos", "smoothed_vu", "smoothed_covid_vaccine", 
"smoothed_trust_fam", "smoothed_trust_healthcare", "smoothed_trust_who",
"smoothed_trust_govt", "smoothed_trust_politicians", "smoothed_twodoses",
"smoothed_concerned_sideeffects", "smoothed_hesitant_sideeffects", "smoothed_modified_acceptance", 
"smoothed_access_wash", "smoothed_wash_hands_24h_3to6", "smoothed_wash_hands_24h_7ormore", 
"smoothed_community_cli"]


#datagrab function
def dataGrab(index1, index2):
    try:
        response = requests.get(linkList[index1][4]).text
        jsonData = json.loads(response)
        return(jsonData["data"][0][dataList[index2]])
    except:
        return None
            

preDataFrame = []
counter1 = 0
counter2 = 0

for i in range(34048):
    tempRow = []

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

    print(tempRow)
    preDataFrame.append(tempRow)

    print(str((counter1/34048)*100) + "% Done")

print(len(preDataFrame))

if len(datesDF) == len(preDataFrame):
    print("success.... Merging Data")


apiDataset = DataFrame (preDataFrame, columns=[
'CLI', 'Flu', 'Mask', 'Contact', 'Finance',
'Anosmia', 'Vaccine_acpt', 'Covid_Vaccine',
'Trust_fam', 'Trust_Healthcare', 'Trust_who',  
'Trust_govt', 'Trust_politicians', 'Twodoses', 
'concerned_sideeffects', 'hesitant_sideeffects',
'modified_acceptance', 'access_wash', 'wash_hands_24h_3to6',
'wash_hands_24h_7orMore', 'cmty_covid',
])


finalDataset = pd.merge(datesDF, apiDataset, how = 'outer', on = 'x1')

finalDataset.to_csv('allData.csv')
print('Done')