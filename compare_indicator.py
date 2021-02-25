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
This program will create two line graphs, one for each indicator specified in the command line. 
It'll create the line graph by creating two indicator CSV files for a specific country, 
fill it with that country's data, and write it into comparec.csv
Using comparec.csv matplotlib then creates the line graph.

It is still very messy. Much room for improvement.
"""
    
def get_data(country, indicator1, indicator2, date):
    date1 = str(date)
    with open(country+"_"+indicator1+".csv", "a+") as output_file:
        counter1 = 0
        while counter1 <= 30:
            url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator1 + "&type=daily&country=" + country + "&date=" + date1
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
    with open(country+"_"+indicator2+".csv", "a+") as output_file:
        counter2 = 0
        while counter2 <= 30:
            #print(counter2)
            url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator2 + "&type=daily&country=" + country + "&date=" + date2
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


    with open("comparec.csv", "a") as fd:  
        headers = ["Percent", "Indicator", "Date"]
        dict_writer = csv.DictWriter(fd, headers)
        if fd.tell() == 0:
            dict_writer.writeheader()
        for i in range(len(df1)):
            fd.write(str(df1.loc[i][0]))
            fd.write(",")
            fd.write(str(sys.argv[2].capitalize()))
            fd.write(",")
            fd.write(str(df1.loc[i][-1]))
            fd.write("\n")
            fd.write(str(df2.loc[i][0]))
            fd.write(",")
            fd.write(str(sys.argv[3].capitalize()))
            fd.write(",")
            fd.write(str(df2.loc[i][-1]))
            fd.write("\n")
            
        
def create_graphic(fil):
    with open("comparec.csv", newline='') as f:
        data = csv.DictReader(f)
        result1 = []
        result2 = []
        date = 0
        for i in data:
            if i.get("Date")[4:6] != date:
                date = i.get("Date")
                if i.get("Indicator") == str(sys.argv[2].capitalize()):
                    result1.append( float(i.get("Percent"))*100)
                elif i.get("Indicator") == str(sys.argv[3].capitalize()):
                    result2.append(float(i.get("Percent"))*100)

    print(result2)
    plt.plot(result1, label=sys.argv[2].capitalize())
    plt.plot( result2, label=sys.argv[3].capitalize())
    plt.title("A Comparison of " + sys.argv[1].capitalize() + "'s indicators: " + sys.argv[2].capitalize() + " And " + sys.argv[3].capitalize())
    plt.xlabel("<--May 1st 2020 to the Present -->")
    plt.ylabel("Percent")
    plt.legend()
    plt.show()

        
if __name__ == "__main__":
    date = 20200501
    count = 0
    
    while count < 12:
        try:
            get_data(sys.argv[1].lower(), sys.argv[2].lower(), sys.argv[3], date)
            if int(str(date)[4:6]) != 12:
                date += 100
            elif int(str(date)[4:6]) == 12:
                date = 20210101
            count += 1
        except pd.errors.EmptyDataError:
            continue

    get_average(sys.argv[1]+"_"+sys.argv[2]+".csv", sys.argv[1]+"_"+sys.argv[3]+".csv")
    create_graphic("comparec.csv")
    