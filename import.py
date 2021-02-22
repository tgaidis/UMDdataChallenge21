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

#print(len(dateList[0]), len(linkList[0]))

iteratedList = []
for i in dateList[::21]:
    iteratedList.append(i)

datesDF = DataFrame (iteratedList, columns = ['Country', 'Month', 'Day'])
#print(len(datesDF))

#print(datesDF)


#datagrab functions
def covidGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_cli"])
        except:
            return None

def covidGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None

def fluGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_ili"])
        except:
            return None

def fluGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def maskGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_mc"])
        except:
            return None
            
def maskGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size_mc"])
        except:
            return None
            
def contactGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_dc"])
        except:
            return None
            
def contactGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size_dc"])
        except:
            return None
            
def financeGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_hf"])
        except:
            return None
            
def financeGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size_hf"])
        except:
            return None
            
def anosmiaGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_anos"])
        except:
            return None
            
def anosmiaGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size_anos"])
        except:
            return None
            
def vaccine_acptGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_vu"])
        except:
            return None
            
def vaccine_acptGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size_vu"])
        except:
            return None
            
def covid_vaccineGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_covid_vaccine"])
        except:
            return None
            
def covid_vaccineGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def trust_famGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_trust_fam"])
        except:
            return None
            
def trust_famGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def trust_healthcareGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_trust_healthcare"])
        except:
            return None
            
def trust_healthcareGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def trust_whoGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_trust_who"])
        except:
            return None
            
def trust_whoGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def trust_govtGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_trust_govt"])
        except:
            return None
            
def trust_govtGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def trust_politiciansGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_trust_politicians"])
        except:
            return None
            
def trust_politiciansGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def twodosesGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_twodoses"])
        except:
            return None
            
def twodosesGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def concerned_sideeffectsGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_concerned_sideeffects"])
        except:
            return None
            
def concerned_sideeffectsGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def hesitant_sideeffectsGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_hesitant_sideeffects"])
        except:
            return None
            
def hesitant_sideeffectsGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size_hesitant_sideeffects"])
        except:
            return None
            
def modified_acceptanceGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_modified_acceptance"])
        except:
            return None
            
def modified_acceptanceGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def access_washGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_access_wash"])
        except:
            return None
            
def access_washGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def wash_hands_24h_3to6Grab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_wash_hands_24h_3to6"])
        except:
            return None
            
def wash_hands_24h_3to6GrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def wash_hands_24h_7orMoreGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_wash_hands_24h_7ormore"])
        except:
            return None
            
def wash_hands_24h_7orMoreGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            
def cmty_covidGrab(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["smoothed_community_cli"])
        except:
            return None
            
def cmty_covidGrabSS(index1, printData):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    if printData == "True":
        print(jsonData)
    else:
        try:
            return(jsonData["data"][0]["sample_size"])
        except:
            return None
            

preDataFrame = []
counter = 0
showData = "False"

for i in range(34048):
    tempRow = []

    covid = covidGrab(counter, showData)
    tempRow.append(covid)
    covidSS = covidGrabSS(counter, showData)
    tempRow.append(covidSS)
    counter += 1

    flu = fluGrab(counter, showData)
    tempRow.append(flu)
    fluSS = fluGrabSS(counter, showData)
    tempRow.append(fluSS)
    counter += 1

    mask = maskGrab(counter, showData)
    tempRow.append(mask)
    maskSS = maskGrabSS(counter, showData)
    tempRow.append(maskSS)
    counter += 1

    contact = contactGrab(counter, showData)
    tempRow.append(contact)
    contactSS = contactGrabSS(counter, showData)
    tempRow.append(contactSS)
    counter += 1

    finance = financeGrab(counter, showData)
    tempRow.append(finance)
    financeSS = financeGrabSS(counter, showData)
    tempRow.append(financeSS)
    counter += 1

    anosmia = anosmiaGrab(counter, showData)
    tempRow.append(anosmia)
    anosmiaSS = anosmiaGrabSS(counter, showData)
    tempRow.append(anosmiaSS)
    counter += 1

    vaccine_acpt = vaccine_acptGrab(counter, showData)
    tempRow.append(vaccine_acpt)
    vaccine_acptSS = vaccine_acptGrabSS(counter, showData)
    tempRow.append(vaccine_acptSS)
    counter += 1

    covid_vaccine = covid_vaccineGrab(counter, showData)
    tempRow.append(covid_vaccine)
    covid_vaccineSS = covid_vaccineGrabSS(counter, showData)
    tempRow.append(covid_vaccineSS)
    counter += 1

    trust_fam = trust_famGrab(counter, showData)
    tempRow.append(trust_fam)
    trust_famSS = trust_famGrabSS(counter, showData)
    tempRow.append(trust_famSS)
    counter += 1

    trust_healthcare = trust_healthcareGrab(counter, showData)
    tempRow.append(trust_healthcare)
    trust_healthcareSS = trust_healthcareGrabSS(counter, showData)
    tempRow.append(trust_healthcareSS)
    counter += 1

    trust_who = trust_whoGrab(counter, showData)
    tempRow.append(trust_who)
    trust_whoSS = trust_whoGrabSS(counter, showData)
    tempRow.append(trust_whoSS)
    counter += 1

    trust_govt = trust_govtGrab(counter, showData)
    tempRow.append(trust_govt)
    trust_govtSS = trust_govtGrabSS(counter, showData)
    tempRow.append(trust_govtSS)
    counter += 1

    trust_politicians = trust_politiciansGrab(counter, showData)
    tempRow.append(trust_politicians)
    trust_politiciansSS = trust_politiciansGrabSS(counter, showData)
    tempRow.append(trust_politiciansSS)
    counter += 1

    twodoses = twodosesGrab(counter, showData)
    tempRow.append(twodoses)
    twodosesSS = twodosesGrabSS(counter, showData)
    tempRow.append(twodosesSS)
    counter += 1

    concerned_sideeffects = concerned_sideeffectsGrab(counter, showData)
    tempRow.append(concerned_sideeffects)
    concerned_sideeffectsSS = concerned_sideeffectsGrabSS(counter, showData)
    tempRow.append(concerned_sideeffectsSS)
    counter += 1

    hesitant_sideeffects = hesitant_sideeffectsGrab(counter, showData)
    tempRow.append(hesitant_sideeffects)
    hesitant_sideeffectsSS = hesitant_sideeffectsGrabSS(counter, showData)
    tempRow.append(hesitant_sideeffectsSS)
    counter += 1

    modified_acceptance = modified_acceptanceGrab(counter, showData)
    tempRow.append(modified_acceptance)
    modified_acceptanceSS = modified_acceptanceGrabSS(counter, showData)
    tempRow.append(modified_acceptanceSS)
    counter += 1

    access_wash = access_washGrab(counter, showData)
    tempRow.append(access_wash)
    access_washSS = access_washGrabSS(counter, showData)
    tempRow.append(access_washSS)
    counter += 1

    wash_hands_24h_3to6 = wash_hands_24h_3to6Grab(counter, showData)
    tempRow.append(wash_hands_24h_3to6)
    wash_hands_24h_3to6SS = wash_hands_24h_3to6GrabSS(counter, showData)
    tempRow.append(wash_hands_24h_3to6SS)
    counter += 1

    wash_hands_24h_7orMore = wash_hands_24h_7orMoreGrab(counter, showData)
    tempRow.append(wash_hands_24h_7orMore)
    wash_hands_24h_7orMoreSS = wash_hands_24h_7orMoreGrabSS(counter, showData)
    tempRow.append(wash_hands_24h_7orMoreSS)
    counter += 1

    cmty_covid = cmty_covidGrab(counter, showData)
    tempRow.append(cmty_covid)
    cmty_covidSS = cmty_covidGrabSS(counter, showData)
    tempRow.append(cmty_covidSS)
    counter += 1

    preDataFrame.append(tempRow)

    print(str((counter/34048)*100) + "% Done")

print(len(preDataFrame))

if len(datesDF) == len(preDataFrame):
    print("success.... Merging Data")


apiDataset = DataFrame (preDataFrame, columns=[
'CLI', 'CLI SS', 
 'Flu', 'Flu SS', 
 'Mask', 'Mask SS', 
 'Contact', 'Contact SS',
 'Finance', 'Finance SS', 
 'Anosmia', 'Anosmia SS',
 'Vaccine_acpt', 'Vaccine_acpt SS', 
 'Covid_Vaccine', 'Covid_Vaccine SS', 
 'Trust_fam', 'Trust_fam SS', 
 'Trust_Healthcare', 'Trust_healthcare SS',
 'Trust_who', 'Trust_who SS', 
 'Trust_govt', 'Trust_govt SS', 
 'Trust_politicians', 'Trust_politicians SS', 
 'Twodoses', 'Twodoses SS', 
 'concerned_sideeffects', 'concerned_sideeffects SS',
 'hesitant_sideeffects', 'hesitant_sideeffects SS', 
 'modified_acceptance', 'modified_acceptance SS',
 'access_wash', 'access_wash SS', 
 'wash_hands_24h_3to6', 'wash_hands_24h_3to6 SS',
 'wash_hands_24h_7orMore', 'wash_hands_24h_7orMore SS', 
 'cmty_covid', 'cmty_covid SS'
 ] )


finalDataset = pd.merge(datesDF, apiDataset, how = 'outer', on = 'x1')

finalDataset.to_csv('allData.csv')
print('Done')