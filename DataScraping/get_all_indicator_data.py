import requests
import json
import pandas as pd
import csv
"""
This program will create 21 CSV files named after the 21 indicators provided by
UMD's covid Symptom Tracker API

Each CSV file will contain all countries and will be sorted by date.
Each file will start on the 1st of May and end in the present.

Make sure to change the date to May 1st if you dont have the files yet. Once you
have it all, each time you want to update it set the date to the last entry received 
to only append new entries.
"""

def link_builder(indicator, fil, s_year, s_month, s_day):
    with open("indicators/"+fil, "a", newline='') as output_file:
        url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=all&date="
        string = s_year + s_month + s_day
        response = requests.get(url + string).text 
        if response != "Internal Server Error":
            jsonData = json.loads(response)
            toCSV = jsonData.get('data')
            if toCSV != []:
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                if output_file.tell() == 0:
                    dict_writer.writeheader()
                dict_writer.writerows(toCSV)
        else:
            pass
        
def get_by_indicator(indicator, fil):
    month = 5
    day = 1
    year = 2020

    while year <= 2021 and month <= 12 and day <= 31:
        
        if day >= 1 and day <= 9 and month <= 9:  #0-9 day, 0-9 month
            s_year = str(year)
            s_day = "0" + str(day)
            s_month = "0" + str(month)
            link_builder(indicator, fil, s_year, s_month, s_day)
            day += 1
            
        elif day >= 10 and day <= 29 and  month <= 9:  #10-29 day, 0-9 month
            s_year = str(year)
            s_day = str(day)
            s_month = "0" + str(month)
            link_builder(indicator, fil, s_year, s_month, s_day)
            day += 1
        
        elif day == 30 and month <= 9:
            s_year = str(year)
            s_day = str(day)
            s_month = "0" + str(month)
            link_builder(indicator, fil, s_year, s_month, s_day)
            day = 1
            month = month + 1
            
        elif day >= 1 and day <= 9 and month >= 10:
            s_year = str(year)
            s_day = "0" + str(day)
            s_month = str(month)
            link_builder(indicator, fil, s_year, s_month, s_day)
            day += 1

        elif day >= 10 and day <= 29 and month >= 10 :
            s_year = str(year)
            s_day = str(day)
            s_month = str(month)
            link_builder(indicator, fil, s_year, s_month, s_day)
            day += 1
        
        elif day == 30 and month >= 10 and month != 12:
            s_year = str(year)
            s_day = str(day)
            s_month = str(month)
            link_builder(indicator, fil, s_year, s_month, s_day)
            day = 1
            month = month + 1
        
        elif day == 30 and month == 12:
            s_year = str(year)
            s_day = str(day)
            s_month = str(month)
            link_builder(indicator, fil, s_year, s_month, s_day)
            day = 1
            month = 1
            year = year + 1
        
        
        
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
    "cmty_covid",
    "hes_side_effects",
    "hes_wontwork",
    "hes_dontbelieve",
    "hes_dontlike",
    "hes_waitlater",
    "hes_otherpeople",
    "hes_cost",
    "hes_religious",
    "hes_other",
    "trust_doctors"
    ]

for indicator in indicator_list:
    get_by_indicator(indicator, indicator+".csv")

            

    
    
    
    


