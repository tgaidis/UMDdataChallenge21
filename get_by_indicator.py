import requests
import json
import pandas as pd
import csv
'''Creates 21 seperate csv files named respectively after the 21 indicators provided
by UMD's Covid Symptom Tracker API.

Includes all countries and is sorted by date.
Starts May 1st and goes to the present

'''


def link_build_1(indicator, fil, year, month, day):
    with open(fil, "a", newline='') as output_file:
        url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=all&date="
        string = str(year) + str(month) + str(day)
        response = requests.get(url + string).text 
        if response != "Internal Server Error":
            jsonData = json.loads(response)
            toCSV = jsonData.get('data')
            if toCSV != []:
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(toCSV)
        else:
            pass
    
       
def link_build_2(indicator, fil, year, month, day):
    with open(fil, "a", newline='') as output_file:
        url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=all&date="
        string = str(year) + "0" + str(month) + "0" + str(day)
        response = requests.get(url + string).text 
        if response != "Internal Server Error":
            jsonData = json.loads(response)
            toCSV = jsonData.get('data')
            if toCSV != []:
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(toCSV)
        else:
            pass
   

def link_build_3(indicator, fil, year, month, day):
    with open(fil, "a", newline='') as output_file:
        url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=all&date="
        string = str(year) + "0" + str(month) + str(day)
        response = requests.get(url + string).text
        if response != "Internal Server Error":
            jsonData = json.loads(response)
            toCSV = jsonData.get('data')
            if toCSV != []:
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(toCSV)
        else:
            pass
    
        
def link_build_4(indicator, fil, year, month, day):
    with open(fil, "a", newline='') as output_file:
        url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=all&date="
        string = str(year) + str(month) + "0" + str(day)
        response = requests.get(url + string).text 
        if response != "Internal Server Error":
            jsonData = json.loads(response)
            toCSV = jsonData.get('data')
            if toCSV != []:
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(toCSV)
        else:
            pass
   
                  
def link_build_5(indicator, fil, year, month, day):
    with open(fil, "a", newline='') as output_file:
        url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=all&date="
        string = str(year) + str(month) + str(day)
        response = requests.get(url + string).text 
        if response != "Internal Server Error":
            jsonData = json.loads(response)
            toCSV = jsonData.get('data')
            if toCSV != []:
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(toCSV)
        else:
            pass
   
             
def link_build_6(indicator, fil, year, month, day):
    with open(fil, "a", newline='') as output_file:
        url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=all&date="
        string = str(year) + "0" + str(month) + str(day)
        response = requests.get(url + string).text 
        if response != "Internal Server Error":
            jsonData = json.loads(response)
            toCSV = jsonData.get('data')
            if toCSV != []:
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(toCSV)
        else:
            pass
   
    
def link_build_7(indicator, fil, year, month, day):
    with open(fil, "a", newline='') as output_file:
        url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=all&date="
        string = str(year) +  str(month) + str(day)
        response = requests.get(url + string).text 
        if response != "Internal Server Error":
            jsonData = json.loads(response)
            toCSV = jsonData.get('data')
            if toCSV != []:
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(toCSV)
        else:
            pass
   
    
        
def get_by_indicator(indicator, fil):
    month = 5
    day = 1
    year = 2020
    
    while year <= 2021 and month <= 12 and day <= 30:
        
        if month == 12 and day > 29:
            link_build_1(indicator, fil, year, month, day)
            year += 1
            day = 1
            month = 1
            
        
        elif day < 10 and month < 10:
            link_build_2(indicator, fil, year,month,day)
            day += 1
            

        elif day > 9 and month < 10 and day != 30 and day != 31:
            link_build_3(indicator, fil, year, month, day)
            day += 1
            

        elif day < 10 and month > 9 and day != 30 and day != 31:
            link_build_4(indicator, fil, year, month,day)
            day += 1
            
        
        elif day > 9 and month > 9 and day != 30 and day != 31: 
            link_build_5(indicator, fil, year,month,day)
            day += 1
            
        
        elif month < 10 and day == 30 or day == 31:
            link_build_6(indicator, fil, year, month, day)
            day = 1
            month = month + 1
            
        
        elif day == 30 or day == 31 and month > 9 and month != 12:
            link_build_7(indicator, fil, year, month, day)
            day = 1
            month = month + 1
            
    

          
count = 0
indicator_list = [
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

while count <= 21: 
    for indicator in indicator_list:
        get_by_indicator(indicator, indicator+".csv")

            

    
    
    
    


