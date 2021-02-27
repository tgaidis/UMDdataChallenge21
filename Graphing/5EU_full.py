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

'''This program will create 9 graphs for the 9 indicators we have chosen. 
Each graph will include a line graph of the two countries specified in the terminal.
The first country will be orange and the second will be blue.
IN ORDER TO RUN:
You must specify two countries in the terminal, and have all necessary files.

"python3 compare_allindic_countries.py Country1 Country2"
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


fig, axes = plt.subplots(3, 3, gridspec_kw={'hspace': 1, 'wspace': 0.4})
fig.suptitle("Comparison of Five Bordering EU Countries")

line_labels = ['Italy', "France", "Germany", "Austria", "Switzerland"]

    
(ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9) = axes

fmt = mdates.DateFormatter("%b-%y")
loc = ticker.LinearLocator(9)

#1 covid
ax1.xaxis.set_major_formatter(fmt)
ax1.xaxis.set_major_locator(loc)
for entry in ax1.xaxis.get_ticklabels(): 
    entry.set_rotation(45)

#print(covid_d)
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

#2 flu
ax2.xaxis.set_major_formatter(fmt)
ax2.xaxis.set_major_locator(loc)
for entry in ax2.xaxis.get_ticklabels():
    entry.set_rotation(45)
d21 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[0]]
d22 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[1]]
d23 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[2]]
d24 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[3]]
d25 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d[4]]
ax2.plot(d21, flu_r[0], color="orange", label="Italy")
ax2.plot(d22, flu_r[1], color="blue", label="France")
ax2.plot(d23, flu_r[2], color="purple", label="Germany")
ax2.plot(d24, flu_r[3], color="green", label="Austria")
ax2.plot(d25, flu_r[4], color="red", label="Switzerland")
ax2.set_title("Flu Like Illnesses")

#3 mask
ax3.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax3.xaxis.set_major_locator(loc)
for entry in ax3.xaxis.get_ticklabels():
    entry.set_rotation(45)
d31 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[0]]
d32 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[1]]
d33 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[2]]
d34 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[3]]
d35 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d[4]]
ax3.plot(d31, mask_r[0], color="orange", label="Italy")
ax3.plot(d32, mask_r[1], color="blue", label="France")
ax3.plot(d33, mask_r[2], color="purple", label="Germany")
ax3.plot(d34, mask_r[3], color="green", label="Austria")
ax3.plot(d35, mask_r[4], color="red", label="Switzerland")
ax3.set_title("Percent Wore Mask")

#4 contact
ax4.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax4.xaxis.set_major_locator(loc)
for entry in ax4.xaxis.get_ticklabels():
    entry.set_rotation(45)
d41 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[0]]
d42 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[1]]
d43 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[2]]
d44 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[3]]
d45 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d[4]]
ax4.plot(d41, contact_r[0], color="orange", label="Italy")
ax4.plot(d42, contact_r[1], color="blue", label="France")
ax4.plot(d43, contact_r[2], color="purple", label="Germany")
ax4.plot(d44, contact_r[3], color="green", label="Austria")
ax4.plot(d45, contact_r[4], color="red", label="Switzerland")
ax4.set_title("Percent had Contact Outside Household")
ax4.set_ylabel("Percent")


#5 finance
ax5.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax5.xaxis.set_major_locator(loc)
for entry in ax5.xaxis.get_ticklabels():
    entry.set_rotation(45)
d51 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[0]]
d52 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[1]]
d53 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[2]]
d54 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[3]]
d55 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d[4]]
ax5.plot(d51, finance_r[0], color="orange", label="Italy")
ax5.plot(d52, finance_r[1], color="blue", label="France")
ax5.plot(d53, finance_r[2], color="purple", label="Germany")
ax5.plot(d54, finance_r[3], color="green", label="Austria")
ax5.plot(d55, finance_r[4], color="red", label="Switzerland")
ax5.set_title("Percent Worried About Finances")

#6 anosmia
ax6.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax6.xaxis.set_major_locator(loc)
for entry in ax6.xaxis.get_ticklabels():
    entry.set_rotation(45)
d61 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[0]]
d62 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[1]]
d63 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[2]]
d64 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[3]]
d65 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d[4]]
ax6.plot(d61, anosmia_r[0], color="orange", label="Italy")
ax6.plot(d62, anosmia_r[1], color="blue", label="France")
ax6.plot(d63, anosmia_r[2], color="purple", label="Germany")
ax6.plot(d64, anosmia_r[3], color="green", label="Austria")
ax6.plot(d65, anosmia_r[4], color="red", label="Switzerland")
ax6.set_title("Percent Reporting Anosmia")

#7 cmty covid
ax7.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax7.xaxis.set_major_locator(loc)
for entry in ax7.xaxis.get_ticklabels():
    entry.set_rotation(45)
d71 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[0]]
d72 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[1]]
d73 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[2]]
d74 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[3]]
d75 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d[4]]
ax7.plot(d71, cmty_covid_r[0], color="orange", label="Italy")
ax7.plot(d72, cmty_covid_r[1], color="blue", label="France")
ax7.plot(d73, cmty_covid_r[2], color="purple", label="Germany")
ax7.plot(d74, cmty_covid_r[3], color="green", label="Austria")
ax7.plot(d75, cmty_covid_r[4], color="red", label="Switzerland")
ax7.set_title("Percent Know Person with Covid in Community")

#8 covid vacc
ax8.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax8.xaxis.set_major_locator(loc)
for entry in ax8.xaxis.get_ticklabels():
    entry.set_rotation(45)
d81 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[0]]
d82 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[1]]
d83 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[2]]
d84 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[3]]
d85 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d[4]]
ax8.plot(d81, covid_vaccine_r[0], color="orange", label="Italy")
ax8.plot(d82, covid_vaccine_r[1], color="blue", label="France")
ax8.plot(d83, covid_vaccine_r[2], color="purple", label="Germany")
ax8.plot(d84, covid_vaccine_r[3], color="green", label="Austria")
ax8.plot(d85, covid_vaccine_r[4], color="red", label="Switzerland")
ax8.set_title("Percent Vaccinated with Covid")
ax8.set_xlabel("Date")

#9 two doses
ax9.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax9.xaxis.set_major_locator(loc)
for entry in ax9.xaxis.get_ticklabels():
    entry.set_rotation(45)
d91 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_govt_d[0]]
d92 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_govt_d[1]]
d93 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_govt_d[2]]
d94 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_govt_d[3]]
d95 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in trust_govt_d[4]]
ax9.plot(d91, trust_govt_r[0], color="orange", label="Italy")
ax9.plot(d92, trust_govt_r[1], color="blue", label="France")
ax9.plot(d93, trust_govt_r[2], color="purple", label="Germany")
ax9.plot(d94, trust_govt_r[3], color="green", label="Austria")
ax9.plot(d95, trust_govt_r[4], color="red", label="Switzerland")
ax9.set_title("Percent of Respondent Trust Vaccine reccomended by Govt")

fig.legend([l1,l2,l3,l4,l5], labels=line_labels, loc='upper left')
plt.show()



