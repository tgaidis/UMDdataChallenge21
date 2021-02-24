def dataGrab(index1, index2):
    try:
        response = requests.get(linkList[index1][4]).text
        jsonData = json.loads(response)
        return(jsonData["data"][0][dataList[index2]])
    except:
        return None


dataList = ["smoothed_cli", "smoothed_ili", "smoothed_mc", "smoothed_dc", 
"smoothed_hf", "smoothed_anos", "smoothed_vu", "smoothed_covid_vaccine", 
"smoothed_trust_fam", "smoothed_trust_healthcare", "smoothed_trust_who",
"smoothed_trust_govt", "smoothed_trust_politicians", "smoothed_twodoses",
"smoothed_concerned_sideeffects", "smoothed_hesitant_sideeffects", "smoothed_modified_acceptance", 
"smoothed_access_wash", "smoothed_wash_hands_24h_3to6", "smoothed_wash_hands_24h_7ormore", 
"smoothed_community_cli"]



