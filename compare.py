import requests
import json
import pandas as pd
import csv
import statistics
    
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
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                if output_file.tell() == 0:
                    dict_writer.writeheader()
                dict_writer.writerow(toCSV[0])
                date1 = str(int(date1) +  1)
                counter1 += 1  
            else:
                pass
            
            
    date2 = str(date)
    with open(country2+".csv", "w") as output_file:
        counter2 = 0
        while counter2 <= 30:
            url = "https://covidmap.umd.edu/api/resources?indicator=" + indicator + "&type=daily&country=" + country2 + "&date=" + date2
            response = requests.get(url).text 
            if response != "Internal Server Error":
                jsonData = json.loads(response)
                toCSV = jsonData.get('data')
                keys = toCSV[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                if output_file.tell() == 0:
                    dict_writer.writeheader()
                dict_writer.writerow(toCSV[0])
                date2 = str(int(date2) +  1)
                counter2 += 1
            else:
                pass 

def get_average(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    avg1 = (sum(df1["percent_cli"]) / len(df1)) * 100
    avg2 = (sum(df2["percent_cli"]) / len(df1)) * 100
    with open("compare.txt", "w") as fd:
        fd.write(str(avg1))
        fd.write(" Italy ")
        fd.write(str(date))
        fd.write("\n")
        fd.write(str(avg2))
        fd.write(" France ")
        fd.write(str(date))
        fd.write("\n")
        fd.write("\n")
        
        
if __name__ == "__main__":
    date = 20200501
    count = 0
    while count < 31:
        get_data("italy", "france", "covid", date)
        get_average("italy.csv", "france.csv")
        if str(date)[4:6] != 12:
            date += 100
        else:
            date = 20210101
        count += 1