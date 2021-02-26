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

covid_r2 = []
covid_d2 = []
flu_r2 = []
flu_d2 = []
mask_r2 =[]
mask_d2 = []
contact_r2 = []
contact_d2 = []
finance_r2 = []
finance_d2 = []
anosmia_r2 = []
anosmia_d2 = []
vaccine_acpt_r2 = []
vaccine_acpt_d2 = []
covid_vaccine_r2 = []
covid_vaccine_d2 = []
trust_fam_r2 = []
trust_fam_d2 = []
trust_healthcare_r2 = []
trust_healthcare_d2 = []
trust_who_r2 = []
trust_who_d2 = []
trust_govt_r2 = []
trust_govt_d2 = []
trust_politicians_r2 = []
trust_politicians_d2 = []
twodoses_r2 = []
twodoses_d2 = []
concerned_sideeffects_r2 = []
concerned_sideeffects_d2 = []
hesitant_sideeffects_r2 = []
hesitant_sideeffects_d2 = []
modified_acceptance_r2 = []
modified_acceptance_d2 = []
access_wash_r2 = []
access_wash_d2 = []
wash_hands_24h_3to6_r2 = []
wash_hands_24h_3to6_d2 = []
wash_hands_24h_7orMore_r2 = []
wash_hands_24h_7orMore_d2 = []
cmty_covid_r2 = []
cmty_covid_d2 = []
hes_side_effects_r2 = []
hes_side_effects_d2 = []
hes_wontwork_r2 = []
hes_wontwork_d2 = []
hes_dontbelieve_r2 = []
hes_dontbelieve_d2 = []
hes_dontlike_r2 = []
hes_dontlike_d2 = []
hes_waitlater_r2 = []
hes_waitlater_d2 = []
hes_otherpeople_r2 = []
hes_otherpeople_d2 = []
hes_cost_r2 = []
hes_cost_d2 = []
hes_religious_r2 = []
hes_religious_d2 = []
hes_other_r2 = []
hes_other_d2 = []
trust_doctors_r2 = []
trust_doctors_d2 = []

df1 = pd.read_csv("countries/"+sys.argv[1]+".csv")
for i in range(len(df1)):
    if str(df1.loc[i][1]) == sys.argv[3].lower():
        
        covid_r.append((df1.loc[i][0])*100)
        covid_d.append(str(df1.loc[i][2]))

    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        flu_r.append((df1.loc[i][0]) * 100)
        flu_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        mask_r.append((df1.loc[i][0]) * 100)
        mask_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        contact_r.append((df1.loc[i][0]) * 100)
        contact_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        finance_r.append((df1.loc[i][0]) * 100)
        finance_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        anosmia_r.append((df1.loc[i][0]) * 100)
        anosmia_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        vaccine_acpt_r.append((df1.loc[i][0]) * 100)
        vaccine_acpt_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        covid_vaccine_r.append((df1.loc[i][0]) * 100)
        covid_vaccine_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        trust_fam_r.append(df1.loc[i][0])
        trust_fam_d.append(str(df1.loc[i][2]))

    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        trust_healthcare_r.append(df1.loc[i][0])
        trust_healthcare_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        trust_who_r.append(df1.loc[i][0])
        trust_who_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        trust_govt_r.append(df1.loc[i][0])
        trust_govt_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        trust_politicians_r.append(df1.loc[i][0])
        trust_politicians_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        twodoses_r.append(df1.loc[i][0])
        twodoses_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        concerned_sideeffects_r.append(df1.loc[i][0])
        concerned_sideeffects_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
    
        hesitant_sideeffects_r.append(df1.loc[i][0])
        hesitant_sideeffects_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        modified_acceptance_r.append(df1.loc[i][0])
        modified_acceptance_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        access_wash_r.append(df1.loc[i][0])
        access_wash_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        wash_hands_24h_3to6_r.append(df1.loc[i][0])
        wash_hands_24h_3to6_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        wash_hands_24h_7orMore_r.append(df1.loc[i][0])
        wash_hands_24h_7orMore_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        cmty_covid_r.append(df1.loc[i][0])
        cmty_covid_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        
        hes_side_effects_r.append((df1.loc[i][0]) * 100)
        hes_side_effects_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        hes_wontwork_r.append(df1.loc[i][0])
        hes_wontwork_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        hes_dontbelieve_r.append(df1.loc[i][0])
        hes_dontbelieve_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        hes_dontlike_r.append(df1.loc[i][0])
        hes_dontlike_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        hes_waitlater_r.append(df1.loc[i][0])
        hes_waitlater_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        hes_otherpeople_r.append(df1.loc[i][0])
        hes_otherpeople_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        hes_cost_r.append(df1.loc[i][0])
        hes_cost_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        hes_religious_r.append(df1.loc[i][0])
        hes_religious_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        hes_other_r.append(df1.loc[i][0])
        hes_other_d.append(str(df1.loc[i][2]))
        
    elif str(df1.loc[i][1]) == sys.argv[3].lower():
        trust_doctors_r.append(df1.loc[i][0])
        trust_doctors_d.append(str(df1.loc[i][2]))

df2 = pd.read_csv("countries/"+sys.argv[2]+".csv")
for i in range(len(df2)):
    if str(df2.loc[i][1]) == sys.argv[3].lower():
        covid_r2.append((df2.loc[i][0])*100)
        covid_d2.append(str(df2.loc[i][2]))

    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        flu_r2.append((df2.loc[i][0]) * 100)
        flu_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        mask_r2.append((df2.loc[i][0]) * 100)
        mask_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        contact_r2.append((df2.loc[i][0]) * 100)
        contact_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        finance_r2.append((df2.loc[i][0]) * 100)
        finance_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        anosmia_r2.append((df2.loc[i][0]) * 100)
        anosmia_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        vaccine_acpt_r2.append((df2.loc[i][0]) * 100)
        vaccine_acpt_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        covid_vaccine_r2.append((df2.loc[i][0]) * 100)
        covid_vaccine_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        trust_fam_r2.append(df2.loc[i][0])
        trust_fam_d2.append(str(df2.loc[i][2]))

    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        trust_healthcare_r2.append(df2.loc[i][0])
        trust_healthcare_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        trust_who_r2.append(df2.loc[i][0])
        trust_who_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        trust_govt_r2.append(df2.loc[i][0])
        trust_govt_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        trust_politicians_r2.append(df2.loc[i][0])
        trust_politicians_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        twodoses_r2.append(df2.loc[i][0])
        twodoses_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        concerned_sideeffects_r2.append(df2.loc[i][0])
        concerned_sideeffects_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        hesitant_sideeffects_r2.append(df2.loc[i][0])
        hesitant_sideeffects_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        modified_acceptance_r2.append(df2.loc[i][0])
        modified_acceptance_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        access_wash_r2.append(df2.loc[i][0])
        access_wash_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        wash_hands_24h_3to6_r2.append(df2.loc[i][0])
        wash_hands_24h_3to6_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        wash_hands_24h_7orMore_r2.append(df2.loc[i][0])
        wash_hands_24h_7orMore_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        cmty_covid_r2.append(df2.loc[i][0])
        cmty_covid_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        hes_side_effects_r2.append((df2.loc[i][0]) * 100)
        hes_side_effects_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        hes_wontwork_r2.append(df2.loc[i][0])
        hes_wontwork_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        hes_dontbelieve_r2.append(df2.loc[i][0])
        hes_dontbelieve_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        hes_dontlike_r2.append(df2.loc[i][0])
        hes_dontlike_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        hes_waitlater_r2.append(df2.loc[i][0])
        hes_waitlater_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        hes_otherpeople_r2.append(df2.loc[i][0])
        hes_otherpeople_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        hes_cost_r2.append(df2.loc[i][0])
        hes_cost_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        hes_religious_r2.append(df2.loc[i][0])
        hes_religious_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        hes_other_r2.append(df2.loc[i][0])
        hes_other_d2.append(str(df2.loc[i][2]))
        
    elif str(df2.loc[i][1]) == sys.argv[3].lower():
        
        trust_doctors_r2.append(df2.loc[i][0])
        trust_doctors_d2.append(str(df2.loc[i][2]))



fig, axes = plt.subplots(1, 1, gridspec_kw={'hspace': 1, 'wspace': 0.4})
fig.suptitle(sys.argv[1] + " vs " + sys.argv[2] + " compare_countries_graphics.py")

line_labels = [sys.argv[1], sys.argv[2]]

    
(ax1) = axes

fmt = mdates.DateFormatter("%y-%m")
loc = ticker.LinearLocator(9)
#1 covid
ax1.xaxis.set_major_formatter(fmt)
ax1.xaxis.set_major_locator(loc)
for entry in ax1.xaxis.get_ticklabels():
    entry.set_rotation(45)
    
if sys.argv[3].lower() == "covid":
    x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_d]
    x11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_d2]
    l1 = ax1.plot(x1, covid_r, color="orange")
    l2 = ax1.plot(x11, covid_r2, color="blue")
    ax1.set_title("Covid")
    fig.legend([l1,l2], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[3].lower() == "flu":
    x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d]
    x11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in flu_d2]
    ax1.plot(x1, flu_r, color="orange")
    ax1.plot(x11, flu_d2, color="blue")
    ax1.set_title("Flu")
    fig.legend([l1,l2], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[3].lower() == "mask":
    x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d]
    x11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in mask_d2]
    ax1.plot(x1, mask_r, color="orange")
    ax1.plot(x11, mask_r2, color="blue")
    ax1.set_title("Mask")
    fig.legend([l1,l2], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[3].lower() == "contact":
    x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d]
    x11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in contact_d2]
    ax1.plot(x1, contact_r, color="orange")
    ax1.plot(x11, contact_r2, color="blue")
    ax1.set_title("Contact")
    fig.legend([l1,l2], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[3].lower() == "finance":
    x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d]
    x11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in finance_d2]
    ax1.plot(x1, finance_r, color="orange")
    ax1.plot(x11, finance_r2, color="blue")
    ax1.set_title("Finance")
    fig.legend([l1,l2], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[3].lower() == "anosmia":
    x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d]
    x11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in anosmia_d2]
    ax1.plot(x1, anosmia_r, color="orange")
    ax1.plot(x11, anosmia_r2, color="blue")
    ax1.set_title("Anosmia")
    fig.legend([l1,l2], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[3].lower() == "cmty covid":
    x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d]
    x11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in cmty_covid_d2]
    ax1.plot(x1, cmty_covid_r, color="orange")
    ax1.plot(x11, cmty_covid_r2, color="blue")
    ax1.set_title("Covid in Community")
    fig.legend([l1,l2], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[3].lower() == "covid vacc":
    x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d]
    x11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in covid_vaccine_d2]
    ax1.plot(x1, covid_vaccine_d, color="orange")
    ax1.plot(x11, covid_vaccine_d2, color="blue")
    ax1.set_title("Covid Vacc")
    fig.legend([l1,l2], labels=line_labels, loc='upper left')
    plt.show()

elif sys.argv[3].lower() == "two doses":
    x1 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in twodoses_d]
    x11 = [dt.datetime.strptime(d,"%Y%m%d").date() for d in twodoses_d2]
    ax1.plot(x1, twodoses_r, color="orange")
    ax1.plot(x11, twodoses_r2, color="blue")
    ax1.set_title("Two Doses")
    fig.legend([l1,l2], labels=line_labels, loc='upper left')
    plt.show()



