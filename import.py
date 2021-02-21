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

linkDF = DataFrame (linkList, columns = ['Country', 'Month', 'Day', 'Indicator', 'Link'])
#print(linkDF)

#datagrab functions
def covidGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_cli"])

def covidGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size"])

def fluGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def fluGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size"])

def maskGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_mc"])

def maskGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_mc"])

def contactGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_dc"])

def contactGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_dc"])

def financeGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_hf"])

def financeGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_hf"])

def anosmiaGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_anos"])

def anosmiaGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_anos"])

def vaccine_acptGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_vu"])

def vaccine_acptGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_vu"])

def covid_vaccineGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def covid_vaccineGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def trust_famGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def trust_famGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def trust_healthcareGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def trust_healthcareGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def trust_whoGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def trust_whoGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def trust_govtGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def trust_govtGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def trust_politiciansGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def trust_politiciansGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def twodosesGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def twodosesGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def concerned_sideeffectsGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def concerned_sideeffectsGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def hesitant_sideeffectsGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def hesitant_sideeffectsGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def modified_acceptanceGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_ili"])

def modified_acceptanceGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size_ili"])

def access_washGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_access_wash"])

def access_washGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size"])

def wash_hands_24h_3to6Grab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_wash_hands_24h_3to6"])

def wash_hands_24h_3to6GrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size"])

def wash_hands_24h_7orMoreGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_wash_hands_24h_7ormore"])

def wash_hands_24h_7orMoreGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size"])

def cmty_covidGrab(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["smoothed_community_cli"])

def cmty_covidGrabSS(index1):
    response = requests.get(linkList[index1][4]).text
    jsonData = json.loads(response)
    #print(jsonData)
    return(jsonData["data"][0]["sample_size"])


preDataFrame = []
counter = 0
for i in range(10):
    tempRow = []
    #tempRow.append()

    covid = covidGrab(counter)
    tempRow.append(covid)
    covidSS = covidGrabSS(counter)
    tempRow.append(covidSS)
    counter += 1

    flu = fluGrab(counter)
    tempRow.append(flu)
    fluSS = fluGrabSS(counter)
    tempRow.append(fluSS)
    counter += 1

    mask = maskGrab(counter)
    tempRow.append(mask)
    maskSS = maskGrabSS(counter)
    tempRow.append(maskSS)
    counter += 1

    contact = contactGrab(counter)
    tempRow.append(contact)
    contactSS = contactGrabSS(counter)
    tempRow.append(contactSS)
    counter += 1

    finance = financeGrab(counter)
    tempRow.append(finance)
    financeSS = financeGrabSS(counter)
    tempRow.append(financeSS)
    counter += 1

    anosmia = anosmiaGrab(counter)
    tempRow.append(anosmia)
    anosmiaSS = anosmiaGrabSS(counter)
    tempRow.append(anosmiaSS)
    counter += 1

    vaccine_acpt = vaccine_acptGrab(counter)
    tempRow.append(vaccine_acpt)
    vaccine_acptSS = vaccine_acptGrabSS(counter)
    tempRow.append(vaccine_acptSS)
    counter += 1

    covid_vaccine = covid_vaccineGrab(counter)
    tempRow.append(covid_vaccine)
    covid_vaccineSS = covid_vaccineGrabSS(counter)
    tempRow.append(covid_vaccineSS)
    counter += 1

    trust_fam = trust_famGrab(counter)
    tempRow.append(trust_fam)
    trust_famSS = trust_famGrabSS(counter)
    tempRow.append(trust_famSS)
    counter += 1

    trust_healthcare = trust_healthcareGrab(counter)
    tempRow.append(trust_healthcare)
    trust_healthcareSS = trust_healthcareGrabSS(counter)
    tempRow.append(trust_healthcareSS)
    counter += 1

    trust_who = trust_whoGrab(counter)
    tempRow.append(trust_who)
    trust_whoSS = trust_whoGrabSS(counter)
    tempRow.append(trust_whoSS)
    counter += 1

    trust_govt = trust_govtGrab(counter)
    tempRow.append(trust_govt)
    trust_govtSS = trust_govtGrabSS(counter)
    tempRow.append(trust_govtSS)
    counter += 1

    trust_politicians = trust_politiciansGrab(counter)
    tempRow.append(trust_politicians)
    trust_politiciansSS = trust_politiciansGrabSS(counter)
    tempRow.append(trust_politiciansSS)
    counter += 1

    twodoses = twodosesGrab(counter)
    tempRow.append(twodoses)
    twodosesSS = twodosesGrabSS(counter)
    tempRow.append(twodosesSS)
    counter += 1

    concerned_sideeffects = concerned_sideeffectsGrab(counter)
    tempRow.append(concerned_sideeffects)
    concerned_sideeffectsSS = concerned_sideeffectsGrabSS(counter)
    tempRow.append(concerned_sideeffectsSS)
    counter += 1

    hesitant_sideeffects = hesitant_sideeffectsGrab(counter)
    tempRow.append(hesitant_sideeffects)
    hesitant_sideeffectsSS = hesitant_sideeffectsGrabSS(counter)
    tempRow.append(hesitant_sideeffectsSS)
    counter += 1

    modified_acceptance = modified_acceptanceGrab(counter)
    tempRow.append(modified_acceptance)
    modified_acceptanceSS = modified_acceptanceGrabSS(counter)
    tempRow.append(modified_acceptanceSS)
    counter += 1

    access_wash = access_washGrab(counter)
    tempRow.append(access_wash)
    access_washSS = access_washGrabSS(counter)
    tempRow.append(access_washSS)
    counter += 1

    wash_hands_24h_3to6 = wash_hands_24h_3to6Grab(counter)
    tempRow.append(wash_hands_24h_3to6)
    wash_hands_24h_3to6SS = wash_hands_24h_3to6GrabSS(counter)
    tempRow.append(wash_hands_24h_3to6SS)
    counter += 1

    wash_hands_24h_7orMore = wash_hands_24h_7orMoreGrab(counter)
    tempRow.append(wash_hands_24h_7orMore)
    wash_hands_24h_7orMoreSS = wash_hands_24h_7orMoreGrabSS(counter)
    tempRow.append(wash_hands_24h_7orMoreSS)
    counter += 1

    cmty_covid = cmty_covidGrab(counter)
    tempRow.append(cmty_covid)
    cmty_covidSS = cmty_covidGrabSS(counter)
    tempRow.append(cmty_covidSS)
    counter += 1

    preDataFrame.append(tempRow)

    print(counter)

print(preDataFrame)

largeDataset = DataFrame (preDataFrame, columns=['Country', 'Month', 'Day', 'CLI', 'CLI SS',
 'Flu', 'Flu SS', 'Mask', 'Mask SS', 'Contact', 'Contact SS',
 'Finance', 'Finance SS', 'Anosmia', 'Anosmia SS',
 'Vaccine_acpt', 'Vaccine_acpt SS', 'Covid_Vaccine', 'Covid_Vaccine SS', 
 'Trust_fam', 'Trust_fam SS', 'Trust_Healthcare', 'Trust_healthcare SS',
 'Trust_who', 'Trust_who SS', 'Trust_govt', 'Trust_govt SS', 'Trust_politicians', 'Trust_politicians SS', 
 'Twodoses', 'Twodoses SS', 'concerned_sideeffects', 'concerned_sideeffects SS',
 'hesitant_sideeffects', 'hesitant_sideeffects SS', 'modified_acceptance', 'modified_acceptance SS',
 'access_wash', 'access_wash SS', 'wash_hands_24h_3to6', 'wash_hands_24h_3to6 SS',
 'wash_hands_24h_7orMore', 'wash_hands_24h_7orMore SS', 'cmty_covid', 'cmty_covid SS'] )

