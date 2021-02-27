import requests
import json
import pandas as pd
import csv
import statistics
import sys
import random
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import matplotlib.dates as mdates
import matplotlib.cbook as cbook 
from matplotlib import ticker
import datetime as dt

'''This program will create one graph comparing a chosen indicator and the two chosen countries. 
IN ORDER TO RUN:
You must specify two countries in the terminal and a specific indicator, and have all necessary files.
'''


covid_r = [[], [], [], [], []]
covid_d = [[], [], [], [], []]
flu_r = [[], [], [], [], []]
flu_d = [[], [], [], [], []]
mask_r =[[], [], [], [], []]
mask_d = [[], [], [], [], []]
contact_r = [[], [], [], [], []]
contact_d = [[], [], [], [], []]
finance_r = [[], [], [], [], []]
finance_d = [[], [], [], [], []]
anosmia_r = [[], [], [], [], []]
anosmia_d = [[], [], [], [], []]
vaccine_acpt_r = [[], [], [], [], []]
vaccine_acpt_d = [[], [], [], [], []]
covid_vaccine_r = [[], [], [], [], []]
covid_vaccine_d = [[], [], [], [], []]
trust_fam_r = [[], [], [], [], []]
trust_fam_d = [[], [], [], [], []]
trust_healthcare_r = [[], [], [], [], []]
trust_healthcare_d = [[], [], [], [], []]
trust_who_r = [[], [], [], [], []]
trust_who_d = [[], [], [], [], []]
trust_govt_r = [[], [], [], [], []]
trust_govt_d = [[], [], [], [], []]
trust_politicians_r = [[], [], [], [], []]
trust_politicians_d = [[], [], [], [], []]
twodoses_r = [[], [], [], [], []]
twodoses_d = [[], [], [], [], []]
concerned_sideeffects_r = [[], [], [], [], []]
concerned_sideeffects_d = [[], [], [], [], []]
hesitant_sideeffects_r = [[], [], [], [], []]
hesitant_sideeffects_d = [[], [], [], [], []]
modified_acceptance_r = [[], [], [], [], []]
modified_acceptance_d = [[], [], [], [], []]
access_wash_r = [[], [], [], [], []]
access_wash_d = [[], [], [], [], []]
wash_hands_24h_3to6_r = [[], [], [], [], []]
wash_hands_24h_3to6_d = [[], [], [], [], []]
wash_hands_24h_7orMore_r = [[], [], [], [], []]
wash_hands_24h_7orMore_d = [[], [], [], [], []]
cmty_covid_r = [[], [], [], [], []]
cmty_covid_d = [[], [], [], [], []]
hes_side_effects_r = [[], [], [], [], []]
hes_side_effects_d = [[], [], [], [], []]
hes_wontwork_r = [[], [], [], [], []]
hes_wontwork_d = [[], [], [], [], []]
hes_dontbelieve_r = [[], [], [], [], []]
hes_dontbelieve_d = [[], [], [], [], []]
hes_dontlike_r = [[], [], [], [], []]
hes_dontlike_d = [[], [], [], [], []]
hes_waitlater_r = [[], [], [], [], []]
hes_waitlater_d = [[], [], [], [], []]
hes_otherpeople_r = [[], [], [], [], []]
hes_otherpeople_d = [[], [], [], [], []]
hes_cost_r = [[], [], [], [], []]
hes_cost_d = [[], [], [], [], []]
hes_religious_r = [[], [], [], [], []]
hes_religious_d = [[], [], [], [], []]
hes_other_r = [[], [], [], [], []]
hes_other_d = [[], [], [], [], []]
trust_doctors_r = [[], [], [], [], []]
trust_doctors_d = [[], [], [], [], []]

countries = ["Italy", "France", "Germany", "Austria", "Switzerland"]
counter = 0
for country in countries:
    df1 = pd.read_csv("countries/"+country+".csv")
    for i in range(len(df1)):
        if str(df1.loc[i][1]) == "covid":
            covid_r[counter].append((df1.loc[i][0])*100)
            covid_d[counter].append(str(df1.loc[i][2]))

        elif str(df1.loc[i][1]) == "flu":
            flu_r[counter].append((df1.loc[i][0]) * 100)
            flu_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "mask":
            mask_r[counter].append((df1.loc[i][0]) * 100)
            mask_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "contact":
            contact_r[counter].append((df1.loc[i][0]) * 100)
            contact_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "finance":
            finance_r[counter].append((df1.loc[i][0]) * 100)
            finance_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "anosmia":
            anosmia_r[counter].append((df1.loc[i][0]) * 100)
            anosmia_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "vaccine_acpt":
            
            vaccine_acpt_r[counter].append((df1.loc[i][0]) * 100)
            vaccine_acpt_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "covid_vaccine":
            
            covid_vaccine_r[counter].append((df1.loc[i][0]) * 100)
            covid_vaccine_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "trust_fam":
            
            trust_fam_r[counter].append(df1.loc[i][0])
            trust_fam_d[counter].append(str(df1.loc[i][2]))

        elif str(df1.loc[i][1]) == "trust_healthcare":
            
            trust_healthcare_r[counter].append(df1.loc[i][0])
            trust_healthcare_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "trust_who":
            
            trust_who_r[counter].append(df1.loc[i][0])
            trust_who_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "trust_govt":
            
            trust_govt_r[counter].append(df1.loc[i][0])
            trust_govt_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "trust_politicians":
            
            trust_politicians_r[counter].append(df1.loc[i][0])
            trust_politicians_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "twodoses":
            
            twodoses_r[counter].append(df1.loc[i][0])
            twodoses_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "concerned_sideeffects":
            
            concerned_sideeffects_r[counter].append(df1.loc[i][0])
            concerned_sideeffects_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hesitant_sideeffects":
            
            hesitant_sideeffects_r[counter].append(df1.loc[i][0])
            hesitant_sideeffects_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "modified_acceptance":
            
            modified_acceptance_r[counter].append(df1.loc[i][0])
            modified_acceptance_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "access_wash":
            
            access_wash_r[counter].append(df1.loc[i][0])
            access_wash_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "wash_hands_24h_3to6":
            
            wash_hands_24h_3to6_r[counter].append(df1.loc[i][0])
            wash_hands_24h_3to6_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "wash_hands_24h_7orMore":
            
            wash_hands_24h_7orMore_r[counter].append(df1.loc[i][0])
            wash_hands_24h_7orMore_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "cmty_covid":
            
            cmty_covid_r[counter].append(df1.loc[i][0])
            cmty_covid_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hes_side_effects":
            
            hes_side_effects_r[counter].append((df1.loc[i][0]) * 100)
            hes_side_effects_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hes_wontwork":
            
            hes_wontwork_r[counter].append(df1.loc[i][0])
            hes_wontwork_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hes_dontbelieve":
            
            hes_dontbelieve_r[counter].append(df1.loc[i][0])
            hes_dontbelieve_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hes_dontlike":
            hes_dontlike_r[counter].append(df1.loc[i][0])
            hes_dontlike_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hes_waitlater":
            
            hes_waitlater_r[counter].append(df1.loc[i][0])
            hes_waitlater_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hes_otherpeople":
            
            hes_otherpeople_r[counter].append(df1.loc[i][0])
            hes_otherpeople_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hes_cost":
            
            hes_cost_r[counter].append(df1.loc[i][0])
            hes_cost_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hes_religious":
            
            hes_religious_r[counter].append(df1.loc[i][0])
            hes_religious_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "hes_other":
            
            hes_other_r[counter].append(df1.loc[i][0])
            hes_other_d[counter].append(str(df1.loc[i][2]))
            
        elif str(df1.loc[i][1]) == "trust_doctors":
            
            trust_doctors_r[counter].append(df1.loc[i][0])
            trust_doctors_d[counter].append(str(df1.loc[i][2]))
    counter += 1

fig, axes = plt.subplots(1, 1, gridspec_kw={'hspace': 1, 'wspace': 0.4})
fig.suptitle("Comparison of Five Bordering EU Countries")

line_labels = countries

    
(ax1) = axes

fmt = mdates.DateFormatter("%b-%Y")
loc = ticker.LinearLocator(9)
#1 covid
ax1.xaxis.set_major_formatter(fmt)
ax1.xaxis.set_major_locator(loc)
for entry in ax1.xaxis.get_ticklabels():
    entry.set_rotation(45)
    
if sys.argv[1].lower() == "covid":
    d11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_d[0]]
    d12 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_d[1]]
    d13 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_d[2]]
    d14 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_d[3]]
    d15 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_d[4]]
    l1 = ax1.plot(d11, covid_r[0], color="orange", label="Italy")
    l2 = ax1.plot(d12, covid_r[1], color="blue", label="France")
    l3 = ax1.plot(d13, covid_r[2], color="purple", label="Germany")
    l4 = ax1.plot(d14, covid_r[3], color="green", label="Austria")
    l5 = ax1.plot(d15, covid_r[4], color="red", label="Switzerland")
    ax1.set_title("Covid Like Illnesses")
    ax1.set_ylabel("Percent")
    ax1.set_xlabel("Date")
    fig.legend([l1, l2, l3, l4, l5], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[1].lower() == "flu":
    d11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[0]]
    d12 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[1]]
    d13 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[2]]
    d14 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[3]]
    d15 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[4]]
    l1 = ax1.plot(d11, flu_r[0], color="orange", label="Italy")
    l2 = ax1.plot(d12, flu_r[1], color="blue", label="France")
    l3 = ax1.plot(d13, flu_r[2], color="purple", label="Germany")
    l4 = ax1.plot(d14, flu_r[3], color="green", label="Austria")
    l5 = ax1.plot(d15, flu_r[4], color="red", label="Switzerland")
    ax1.set_title("Flu Like Illnesses")
    ax1.set_ylabel("Percent")
    ax1.set_xlabel("Date")
    fig.legend([l1, l2, l3, l4, l5], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[1].lower() == "mask":
    d11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[0]]
    d12 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[1]]
    d13 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[2]]
    d14 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[3]]
    d15 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[4]]
    l1 = ax1.plot(d11, mask_r[0], color="orange", label="Italy")
    l2 = ax1.plot(d12, mask_r[1], color="blue", label="France")
    l3 = ax1.plot(d13, mask_r[2], color="purple", label="Germany")
    l4 = ax1.plot(d14, mask_r[3], color="green", label="Austria")
    l5 = ax1.plot(d15, mask_r[4], color="red", label="Switzerland")
    ax1.set_title("Percent Wore Mask")
    ax1.set_ylabel("Percent")
    ax1.set_xlabel("Date")
    fig.legend([l1, l2, l3, l4, l5], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[1].lower() == "contact":
    d11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[0]]
    d12 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[1]]
    d13 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[2]]
    d14 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[3]]
    d15 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[4]]
    l1 = ax1.plot(d11, contact_r[0], color="orange", label="Italy")
    l2 = ax1.plot(d12, contact_r[1], color="blue", label="France")
    l3 = ax1.plot(d13, contact_r[2], color="purple", label="Germany")
    l4 = ax1.plot(d14, contact_r[3], color="green", label="Austria")
    l5 = ax1.plot(d15, contact_r[4], color="red", label="Switzerland")
    ax1.set_title("Contact outside household")
    ax1.set_ylabel("Percent")
    ax1.set_xlabel("Date")
    fig.legend([l1, l2, l3, l4, l5], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[1].lower() == "finance":
    d11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[0]]
    d12 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[1]]
    d13 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[2]]
    d14 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[3]]
    d15 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[4]]
    l1 = ax1.plot(d11, finance_r[0], color="orange", label="Italy")
    l2 = ax1.plot(d12, finance_r[1], color="blue", label="France")
    l3 = ax1.plot(d13, finance_r[2], color="purple", label="Germany")
    l4 = ax1.plot(d14, finance_r[3], color="green", label="Austria")
    l5 = ax1.plot(d15, finance_r[4], color="red", label="Switzerland")
    ax1.set_title("Percent worried about Finances")
    ax1.set_ylabel("Percent")
    ax1.set_xlabel("Date")
    fig.legend([l1, l2, l3, l4, l5], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[1].lower() == "anosmia":
    d11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[0]]
    d12 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[1]]
    d13 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[2]]
    d14 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[3]]
    d15 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[4]]
    l1 = ax1.plot(d11, anosmia_r[0], color="orange", label="Italy")
    l2 = ax1.plot(d12, anosmia_r[1], color="blue", label="France")
    l3 = ax1.plot(d13, anosmia_r[2], color="purple", label="Germany")
    l4 = ax1.plot(d14, anosmia_r[3], color="green", label="Austria")
    l5 = ax1.plot(d15, anosmia_r[4], color="red", label="Switzerland")
    ax1.set_title("Percent Reporting Anosmia")
    ax1.set_ylabel("Percent")
    ax1.set_xlabel("Date")
    fig.legend([l1, l2, l3, l4, l5], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[1].lower() == "cmty covid":
    d11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[0]]
    d12 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[1]]
    d13 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[2]]
    d14 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[3]]
    d15 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[4]]
    l1 = ax1.plot(d11, cmty_covid_r[0], color="orange", label="Italy")
    l2 = ax1.plot(d12, cmty_covid_r[1], color="blue", label="France")
    l3 = ax1.plot(d13, cmty_covid_r[2], color="purple", label="Germany")
    l4 = ax1.plot(d14, cmty_covid_r[3], color="green", label="Austria")
    l5 = ax1.plot(d15, cmty_covid_r[4], color="red", label="Switzerland")
    ax1.set_title("Percent Know Person with Covid in Community")
    ax1.set_ylabel("Percent")
    ax1.set_xlabel("Date")
    fig.legend([l1, l2, l3, l4, l5], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[1].lower() == "covid vacc":
    d11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[0]]
    d12 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[1]]
    d13 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[2]]
    d14 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[3]]
    d15 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[4]]
    l1 = ax1.plot(d11, covid_vaccine_r[0], color="orange", label="Italy")
    l2 = ax1.plot(d12, covid_vaccine_r[1], color="blue", label="France")
    l3 = ax1.plot(d13, covid_vaccine_r[2], color="purple", label="Germany")
    l4 = ax1.plot(d14, covid_vaccine_r[3], color="green", label="Austria")
    l5 = ax1.plot(d15, covid_vaccine_r[4], color="red", label="Switzerland")
    ax1.set_title("Percent Vaccinated with Covid")
    ax1.set_ylabel("Percent")
    ax1.set_xlabel("Date")
    fig.legend([l1, l2, l3, l4, l5], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[1].lower() == "trust healthcare":
    d11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_healthcare_d[0]]
    d12 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_healthcare_d[1]]
    d13 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_healthcare_d[2]]
    d14 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_healthcare_d[3]]
    d15 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_healthcare_d[4]]
    l1 = ax1.plot(d11, trust_healthcare_r[0], color="orange", label="Italy")
    l2 = ax1.plot(d12, trust_healthcare_r[1], color="blue", label="France")
    l3 = ax1.plot(d13, trust_healthcare_r[2], color="purple", label="Germany")
    l4 = ax1.plot(d14, trust_healthcare_r[3], color="green", label="Austria")
    l5 = ax1.plot(d15, trust_healthcare_r[4], color="red", label="Switzerland")
    ax1.set_title("Percent of Respondent Trust Vaccine from Local Healthcare")
    ax1.set_ylabel("Percent")
    ax1.set_xlabel("Date")
    fig.legend([l1, l2, l3, l4, l5], labels=line_labels, loc='upper left')
    plt.show()
