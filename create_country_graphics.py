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

'''This program will create 9 graphs of each indicator we have chosen.
It will show the percentage of those indicators for a specified country.
IN ORDER TO RUN:
you must already have the necessary CSV files.
Simply type in the terminal:
python3 create_graphics.py "Country"
'''

df1 = pd.read_csv("countries/"+sys.argv[1]+".csv")
covid_r = []
covid_d = []
flu_r = []
flu_d = []
mask_r =[]
mask_d = []
contact_r = []
contact_d = []
finance_r = []
finance_d = []
anosmia_r = []
anosmia_d = []
vaccine_acpt_r = []
vaccine_acpt_d = []
covid_vaccine_r = []
covid_vaccine_d = []
trust_fam_r = []
trust_fam_d = []
trust_healthcare_r = []
trust_healthcare_d = []
trust_who_r = []
trust_who_d = []
trust_govt_r = []
trust_govt_d = []
trust_politicians_r = []
trust_politicians_d = []
twodoses_r = []
twodoses_d = []
concerned_sideeffects_r = []
concerned_sideeffects_d = []
hesitant_sideeffects_r = []
hesitant_sideeffects_d = []
modified_acceptance_r = []
modified_acceptance_d = []
access_wash_r = []
access_wash_d = []
wash_hands_24h_3to6_r = []
wash_hands_24h_3to6_d = []
wash_hands_24h_7orMore_r = []
wash_hands_24h_7orMore_d = []
cmty_covid_r = []
cmty_covid_d = []
hes_side_effects_r = []
hes_side_effects_d = []
hes_wontwork_r = []
hes_wontwork_d = []
hes_dontbelieve_r = []
hes_dontbelieve_d = []
hes_dontlike_r = []
hes_dontlike_d = []
hes_waitlater_r = []
hes_waitlater_d = []
hes_otherpeople_r = []
hes_otherpeople_d = []
hes_cost_r = []
hes_cost_d = []
hes_religious_r = []
hes_religious_d = []
hes_other_r = []
hes_other_d = []
trust_doctors_r = []
trust_doctors_d = []

for i in range(len(df1)):
    if str(df1.loc[i][1]) == "covid":
        
        covid_r.append((df1.loc[i][0])*100)
        covid_d.append(str(df1.loc[i][2]))

    elif str(df1.loc[i][1]) == "flu":
        
        flu_r.append((df1.loc[i][0]) * 100)
        flu_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "mask":
        
        mask_r.append((df1.loc[i][0]) * 100)
        mask_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "contact":
        
        contact_r.append((df1.loc[i][0]) * 100)
        contact_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "finance":
        
        finance_r.append((df1.loc[i][0]) * 100)
        finance_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "anosmia":
        
        anosmia_r.append((df1.loc[i][0]) * 100)
        anosmia_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "vaccine_acpt":
        
        vaccine_acpt_r.append((df1.loc[i][0]) * 100)
        vaccine_acpt_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "covid_vaccine":
        
        covid_vaccine_r.append((df1.loc[i][0]) * 100)
        covid_vaccine_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "trust_fam":
        
        trust_fam_r.append(df1.loc[i][0])
        trust_fam_d.append(str(df1.loc[i][2]))

    elif str(df1.loc[i][1]) == "trust_healthcare":
        
        trust_healthcare_r.append(df1.loc[i][0])
        trust_healthcare_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "trust_who":
        
        trust_who_r.append(df1.loc[i][0])
        trust_who_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "trust_govt":
        
        trust_govt_r.append(df1.loc[i][0])
        trust_govt_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "trust_politicians":
        
        trust_politicians_r.append(df1.loc[i][0])
        trust_politicians_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "twodoses":
        
        twodoses_r.append(df1.loc[i][0])
        twodoses_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "concerned_sideeffects":
        
        concerned_sideeffects_r.append(df1.loc[i][0])
        concerned_sideeffects_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hesitant_sideeffects":
        
        hesitant_sideeffects_r.append(df1.loc[i][0])
        hesitant_sideeffects_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "modified_acceptance":
        
        modified_acceptance_r.append(df1.loc[i][0])
        modified_acceptance_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "access_wash":
        
        access_wash_r.append(df1.loc[i][0])
        access_wash_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "wash_hands_24h_3to6":
        
        wash_hands_24h_3to6_r.append(df1.loc[i][0])
        wash_hands_24h_3to6_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "wash_hands_24h_7orMore":
        
        wash_hands_24h_7orMore_r.append(df1.loc[i][0])
        wash_hands_24h_7orMore_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "cmty_covid":
        
        cmty_covid_r.append(df1.loc[i][0])
        cmty_covid_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hes_side_effects":
        
        hes_side_effects_r.append((df1.loc[i][0]) * 100)
        hes_side_effects_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hes_wontwork":
        
        hes_wontwork_r.append(df1.loc[i][0])
        hes_wontwork_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hes_dontbelieve":
        
        hes_dontbelieve_r.append(df1.loc[i][0])
        hes_dontbelieve_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hes_dontlike":
        hes_dontlike_r.append(df1.loc[i][0])
        hes_dontlike_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hes_waitlater":
        
        hes_waitlater_r.append(df1.loc[i][0])
        hes_waitlater_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hes_otherpeople":
        
        hes_otherpeople_r.append(df1.loc[i][0])
        hes_otherpeople_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hes_cost":
        
        hes_cost_r.append(df1.loc[i][0])
        hes_cost_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hes_religious":
        
        hes_religious_r.append(df1.loc[i][0])
        hes_religious_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "hes_other":
        
        hes_other_r.append(df1.loc[i][0])
        hes_other_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == "trust_doctors":
        
        trust_doctors_r.append(df1.loc[i][0])
        trust_doctors_d.append(str(df1.loc[i][2]))

#1,1, gridspec_kw={'hspace': 1, 'wspace': 0.2}
#mdates.DateFormatter('%Y%m')


fig, ax = plt.subplots(3,3, gridspec_kw={'hspace': 1, 'wspace': 0.4})
plt.suptitle(sys.argv[1])

(ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)  = ax

#1 covid
fmt = mdates.DateFormatter("%y-%m")
ax1.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax1.xaxis.set_major_locator(loc)
for entry in ax1.xaxis.get_ticklabels():
    entry.set_rotation(45)
x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_d]
ax1.plot(x1, covid_r, color="red")
ax1.set_title("Covid")

#2 flu
fmt = mdates.DateFormatter("%y-%m")
ax2.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax2.xaxis.set_major_locator(loc)
for entry in ax2.xaxis.get_ticklabels():
    entry.set_rotation(45)
x2 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d]
ax2.plot(x2, flu_r, color="blue")
ax2.set_title("Flu")

#3 mask
fmt = mdates.DateFormatter("%y-%m")
ax3.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax3.xaxis.set_major_locator(loc)
for entry in ax3.xaxis.get_ticklabels():
    entry.set_rotation(45)
x3 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d]
ax3.plot(x3, mask_r, color="green")
ax3.set_title("Mask")

#4 contact
fmt = mdates.DateFormatter("%y-%m")
ax4.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax4.xaxis.set_major_locator(loc)
for entry in ax4.xaxis.get_ticklabels():
    entry.set_rotation(45)
x4 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d]
ax4.plot(x4, contact_r, color="orange")
ax4.set_title("Contact")

#4 finance
fmt = mdates.DateFormatter("%y-%m")
ax5.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax5.xaxis.set_major_locator(loc)
for entry in ax5.xaxis.get_ticklabels():
    entry.set_rotation(45)
x5 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d]
ax5.plot(x5, finance_r, color="brown")
ax5.set_title("Finance")

#6 anosmia
fmt = mdates.DateFormatter("%y-%m")
ax6.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax6.xaxis.set_major_locator(loc)
for entry in ax6.xaxis.get_ticklabels():
    entry.set_rotation(45)
x6 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d]
ax6.plot(x6, anosmia_r, color="purple")
ax6.set_title("Anosmia")

#7 cmty covid
fmt = mdates.DateFormatter("%y-%m")
ax7.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax7.xaxis.set_major_locator(loc)
for entry in ax7.xaxis.get_ticklabels():
    entry.set_rotation(45)
x7 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d]
ax7.plot(x7, cmty_covid_r, color="green")
ax7.set_title("Cmty Covid")

#8 covid vacc
fmt = mdates.DateFormatter("%y-%m")
ax8.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax8.xaxis.set_major_locator(loc)
for entry in ax8.xaxis.get_ticklabels():
    entry.set_rotation(45)
x8 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d]
ax8.plot(x8, covid_vaccine_r, color="red")
ax8.set_title("Covid Vaccine")

#9 two doses
fmt = mdates.DateFormatter("%y-%m")
ax9.xaxis.set_major_formatter(fmt)
loc = ticker.LinearLocator(9)
ax9.xaxis.set_major_locator(loc)
for entry in ax9.xaxis.get_ticklabels():
    entry.set_rotation(45)
x9 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in twodoses_d]
ax9.plot(x9, twodoses_r, color="blue")
ax9.set_title("Two doses")

plt.show()



