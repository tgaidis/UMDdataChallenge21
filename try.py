import requests
import json
import pandas as pd
import csv
import statistics
import sys
import random
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

'''This program will create several line graphs of a countrys indicators.
To run, you must already have the CSV file for the country.
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
        day = 1
        covid_r.append(df1.loc[i][0])
        covid_d.append(day)
        day +=1
    elif str(df1.loc[i][1]) == "flu":
        day = 1
        flu_r.append(df1.loc[i][0])
        flu_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "mask":
        day = 1
        mask_r.append(df1.loc[i][0])
        mask_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "contact":
        day = 1
        contact_r.append(df1.loc[i][0])
        contact_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "finance":
        day = 1
        finance_r.append(df1.loc[i][0])
        finance_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "anosmia":
        day = 1
        anosmia_r.append(df1.loc[i][0])
        anosmia_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "vaccine_acpt":
        day = 1
        vaccine_acpt_r.append(df1.loc[i][0])
        vaccine_acpt_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "covid_vaccine":
        day = 1
        covid_vaccine_r.append(df1.loc[i][0])
        covid_vaccine_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "trust_fam":
        day = 1
        trust_fam_r.append(df1.loc[i][0])
        trust_fam_d.append(day)
        day +=1
    elif str(df1.loc[i][1]) == "trust_healthcare":
        day = 1
        trust_healthcare_r.append(df1.loc[i][0])
        trust_healthcare_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "trust_who":
        day = 1
        trust_who_r.append(df1.loc[i][0])
        trust_who_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "trust_govt":
        day = 1
        trust_govt_r.append(df1.loc[i][0])
        trust_govt_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "trust_politicians":
        day = 1
        trust_politicians_r.append(df1.loc[i][0])
        trust_politicians_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "twodoses":
        day = 1
        twodoses_r.append(df1.loc[i][0])
        twodoses_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "concerned_sideeffects":
        day = 1
        concerned_sideeffects_r.append(df1.loc[i][0])
        concerned_sideeffects_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hesitant_sideeffects":
        day = 1
        hesitant_sideeffects_r.append(df1.loc[i][0])
        hesitant_sideeffects_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "modified_acceptance":
        day = 1
        modified_acceptance_r.append(df1.loc[i][0])
        modified_acceptance_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "access_wash":
        day = 1
        access_wash_r.append(df1.loc[i][0])
        access_wash_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "wash_hands_24h_3to6":
        day = 1
        wash_hands_24h_3to6_r.append(df1.loc[i][0])
        wash_hands_24h_3to6_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "wash_hands_24h_7orMore":
        day = 1
        wash_hands_24h_7orMore_r.append(df1.loc[i][0])
        wash_hands_24h_7orMore_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "cmty_covid":
        day = 1
        cmty_covid_r.append(df1.loc[i][0])
        cmty_covid_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hes_side_effects":
        day = 1
        hes_side_effects_r.append(df1.loc[i][0])
        hes_side_effects_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hes_wontwork":
        day = 1
        hes_wontwork_r.append(df1.loc[i][0])
        hes_wontwork_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hes_dontbelieve":
        day = 1
        hes_dontbelieve_r.append(df1.loc[i][0])
        hes_dontbelieve_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hes_dontlike":
        day = 1
        hes_dontlike_r.append(df1.loc[i][0])
        hes_dontlike_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hes_waitlater":
        day = 1
        hes_waitlater_r.append(df1.loc[i][0])
        hes_waitlater_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hes_otherpeople":
        day = 1
        hes_otherpeople_r.append(df1.loc[i][0])
        hes_otherpeople_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hes_cost":
        day = 1
        hes_cost_r.append(df1.loc[i][0])
        hes_cost_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hes_religious":
        day = 1
        hes_religious_r.append(df1.loc[i][0])
        hes_religious_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "hes_other":
        day = 1
        hes_other_r.append(df1.loc[i][0])
        hes_other_d.append(day)
        day += 1
    elif str(df1.loc[i][1]) == "trust_doctors":
        day = 1
        trust_doctors_r.append(df1.loc[i][0])
        trust_doctors_d.append(day)
        day += 1
    
fig, axs = plt.subplots(3,3, sharex=True, sharey=False, gridspec_kw={'hspace': 0, 'wspace': 0})
(axs1, axs2, axs3), (axs4, axs5, axs6), (axs7, axs8, axs9) = axs
fig.suptitle(sys.argv[1])
axs1.plot(covid_r, covid_d, color="red", label="Covid")
axs2.plot(flu_d, flu_r, color="blue", label="Flu")
axs3.plot(mask_d, mask_r, color="green", label="Mask")
axs4.plot(contact_d, contact_r, color="orange", label="Contact")
axs5.plot(finance_d, finance_r, color="purple", label="Finance")
axs6.plot(anosmia_d, anosmia_r, color="brown", label="Anosmia")
axs7.plot(vaccine_acpt_d, vaccine_acpt_r, color="green", label="Vacc Acpt")
axs8.plot(covid_vaccine_d, covid_vaccine_r, color="red", label="Covid Vacc")
axs9.plot(hes_side_effects_d, hes_side_effects_r, color="blue", label="Hesitant Side Effects")
plt.tight_layout()
plt.show()
