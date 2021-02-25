import requests
import json
import pandas as pd
import csv
import statistics
import sys
import random
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

"""
This program will create two line graphs, one for each country specified in the command line. 
It'll create the line graph by creating two country CSV files, 
fill it with that month's data, average the months data, and finally write it into compare.csv
Using compare.csv matplotlib then creates the line graph.

It is still very messy. Much room for improvement.
"""
    
def get_data(country1, country2, indicator, date):
    date1 = str(date)
    with open(country1+".csv", "w") as output_file:
        counter1 = 0
        while counter1 <= 30:
            url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=" + country1 + "&date=" + date1
            response = requests.get(url).text
            if response != "Internal Server Error":
                jsonData = json.loads(response)
                toCSV = jsonData.get('data')
                try:
                    keys = toCSV[0].keys()
                except IndexError:
                    keys = ''
                    pass
                dict_writer = csv.DictWriter(output_file, keys)
                if output_file.tell() == 0:
                    dict_writer.writeheader()
                try:
                    dict_writer.writerow(toCSV[0])
                except IndexError:
                    pass
                date1 = str(int(date1) +  1)
                counter1 += 1  
            else:
                pass
                counter1 += 1
         
    date2 = str(date)
    with open(country2+".csv", "w") as output_file:
        counter2 = 0
        while counter2 <= 30:
            #print(counter2)
            url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=" + country2 + "&date=" + date2
            response = requests.get(url).text 
            if response != "Internal Server Error":
                jsonData = json.loads(response)
                toCSV = jsonData.get('data')
                try:
                    keys = toCSV[0].keys()
                except IndexError:
                    keys = ''
                    pass
                dict_writer = csv.DictWriter(output_file, keys)
                if output_file.tell() == 0:
                    dict_writer.writeheader()
                try:
                    dict_writer.writerow(toCSV[0])
                except IndexError:
                    pass
                date2 = str(int(date2) +  1)
                counter2 += 1
            else:
                pass
                counter2 += 1

def get_average(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    avg1 = round((sum(df1["percent_cli"]) / len(df1)) * 100, 2)
    avg2 = round((sum(df2["percent_cli"]) / len(df1)) * 100, 2)
    with open("compare.csv", "a") as fd:
        headers = ["Percent", "Country", "Date"]
        dict_writer = csv.DictWriter(fd, headers)
        if fd.tell() == 0:
            dict_writer.writeheader()
        fd.write(str(avg1))
        fd.write(",")
        fd.write(sys.argv[1].capitalize())
        fd.write(",")
        fd.write(str(date)[4:6])
        fd.write("\n")
        fd.write(str(avg2))
        fd.write(",")
        fd.write(sys.argv[2].capitalize())
        fd.write(",")
        fd.write(str(date)[4:6])
        fd.write("\n")
        
def create_graphic(fil):
    with open("compare.csv", newline='') as f:
        data = csv.DictReader(f)
        result1 = []
        result2 = []
        for i in data:
            if i.get("Country") == str(sys.argv[1].capitalize()):
                result1.append(float(i.get("Percent")))
            else:
                result2.append(float(i.get("Percent")))
    avg_month1 = sum(result1)/len(result1)
    avg_month2 = sum(result2)/len(result2)
    
    dates1 = ["05", "06", "07","08","09","10","11","12", "01", "02"]
    plt.plot(dates1,result1, marker="o", label=sys.argv[1].capitalize())
    plt.plot(dates1, result2, marker="o", label=sys.argv[2].capitalize())
    plt.title("A Comparison of " + sys.argv[1].capitalize() + " and " + sys.argv[2].capitalize() + " Based on " + sys.argv[3].capitalize())
    plt.xlabel("Month")
    plt.ylabel("Percent Indicator")
    plt.legend()
    plt.show()

        
if __name__ == "__main__":
    date = 20200501
    count = 0
    while count < 11:
        try:
            get_data(sys.argv[1].lower(), sys.argv[2].lower(), sys.argv[3], date)
            get_average(sys.argv[1]+".csv", sys.argv[2]+".csv")
            if int(str(date)[4:6]) != 12:
                date += 100
            elif int(str(date)[4:6]) == 12:
                date = 20210101
            count += 1
        except pd.errors.EmptyDataError:
            break
    create_graphic("compare.csv")
    