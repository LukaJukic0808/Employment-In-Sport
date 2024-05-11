import pandas as pd
import numpy as np
import math
import json

data_young_thousands = pd.read_csv("datasets/byAge-processed/sport_young_thousands.csv", index_col='geo')
data_young_percentage = pd.read_csv("datasets/byAge-processed/sport_young_percentage.csv", index_col ='geo')
data_middle_thousands = pd.read_csv("datasets/byAge-processed/sport_middle_thousands.csv", index_col='geo')
data_middle_percentage = pd.read_csv("datasets/byAge-processed/sport_middle_percentage.csv", index_col='geo')
data_old_thousands = pd.read_csv("datasets/byAge-processed/sport_old_thousands.csv", index_col='geo')
data_old_percentage = pd.read_csv("datasets/byAge-processed/sport_old_percentage.csv", index_col='geo')

data_primary_thousands = pd.read_csv("datasets/byEducation-processed/sport_primary_thousands.csv", index_col='geo')
data_primary_percentage = pd.read_csv("datasets/byEducation-processed/sport_primary_percentage.csv", index_col='geo')
data_secondary_thousands = pd.read_csv("datasets/byEducation-processed/sport_secondary_thousands.csv", index_col='geo')
data_secondary_percentage = pd.read_csv("datasets/byEducation-processed/sport_secondary_percentage.csv", index_col='geo')
data_tertiary_thousands = pd.read_csv("datasets/byEducation-processed/sport_tertiary_thousands.csv", index_col='geo')
data_tertiary_percentage = pd.read_csv("datasets/byEducation-processed/sport_tertiary_percentage.csv", index_col='geo')
data_noResponse_thousands = pd.read_csv("datasets/byEducation-processed/sport_noResponse_thousands.csv", index_col='geo')
data_noResponse_percentage = pd.read_csv("datasets/byEducation-processed/sport_noResponse_percentage.csv", index_col='geo')

data_male_thousands = pd.read_csv("datasets/bySex-processed/sport_male_thousands.csv", index_col='geo')
data_male_percentage = pd.read_csv("datasets/bySex-processed/sport_male_percentage.csv", index_col='geo')
data_female_thousands = pd.read_csv("datasets/bySex-processed/sport_female_thousands.csv", index_col='geo')
data_female_percentage = pd.read_csv("datasets/bySex-processed/sport_female_percentage.csv", index_col='geo')

data_total_thousands = pd.read_csv("datasets/total-processed/sport_total_thousands.csv", index_col='geo')
data_total_percentage = pd.read_csv("datasets/total-processed/sport_total_percentage.csv", index_col='geo')

countries = np.unique(data_secondary_percentage.index)
dataDict = {country: None for country in countries}
years = {"2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"}
names= {
    'AT': "Austria",
    'BE': "Belgium",
    'BG': "Bulgaria",
    'CH': "Switzerland", 
    'CY': "Cyprus", 
    'CZ': "Czechia", 
    'DE': "Germany", 
    'DK': "Denmark", 
    'EE': "Estonia", 
    'EL': "Greece", 
    'ES': "Spain", 
    'EU27_2020': "European Union", 
    'FI': "Finland",
    'FR': "France", 
    'HR': "Croatia", 
    'HU': "Hungary", 
    'IE': "Ireland", 
    'IS': "Iceland", 
    'IT': "Italy", 
    'LT': "Lithuania", 
    'LU': "Luxembourg", 
    'LV': "Latvia", 
    'ME': "Montenegro", 
    'MK': "North Macedonia", 
    'MT': "Malta", 
    'NL': "Netherlands", 
    'NO': "Norway",
    'PL': "Poland", 
    'PT': "Portugal", 
    'RO': "Romania", 
    'RS': "Serbia", 
    'SE': "Sweden", 
    'SI': "Slovenia", 
    'SK': "Slovakia", 
    'TR': "Turkey",
    'UK': "United Kingdom"
}

for key in dataDict:
    dataDict[key] = {
        "name": "placeHolder",
        "2013": None,
        "2014": None,
        "2015": None,
        "2016": None,
        "2017": None,
        "2018": None,
        "2019": None,
        "2020": None,
        "2021": None,
        "2022": None
        }
    for year in years:
        dataDict[key][year] = {
            "totalTH": None,
            "totalPR": None,
            "maleTH": None,
            "malePR": None,
            "femaleTH": None,
            "femalePR": None,
            "primaryTH": None,
            "primaryPR": None,
            "secondaryTH": None,
            "secondaryPR": None,
            "tertiaryTH": None,
            "tertiaryPR": None,
            "noResponseTH": None,
            "noResponsePR": None,
            "youngTH": None,
            "youngPR": None,
            "middleTH": None,
            "middlePR": None,
            "oldTH": None,
            "oldPR": None
        }

for key in dataDict:
    dataDict[key]["name"] = names[key] 

#### YOUNG ####
existingCountries = data_young_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_young_thousands.loc[key, year])):
                dataDict[key][year]["youngTH"] = data_young_thousands.loc[key,year]
            if(not math.isnan(data_young_percentage.loc[key, year])):
                dataDict[key][year]["youngPR"] = data_young_percentage.loc[key,year]

### MIDDLE ###
existingCountries = data_middle_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_middle_thousands.loc[key, year])):
                dataDict[key][year]["middleTH"] = data_middle_thousands.loc[key,year]
            if(not math.isnan(data_middle_percentage.loc[key, year])):
                dataDict[key][year]["middlePR"] = data_middle_percentage.loc[key,year]

### OLD ###
existingCountries = data_old_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_old_thousands.loc[key, year])):
                dataDict[key][year]["oldTH"] = data_old_thousands.loc[key,year]
            if(not math.isnan(data_old_percentage.loc[key, year])):
                dataDict[key][year]["oldPR"] = data_old_percentage.loc[key,year]

### MALE ###
existingCountries = data_male_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_male_thousands.loc[key, year])):
                dataDict[key][year]["maleTH"] = data_male_thousands.loc[key,year]
            if(not math.isnan(data_male_percentage.loc[key, year])):
                dataDict[key][year]["malePR"] = data_male_percentage.loc[key,year]

### FEMALE ###
existingCountries = data_female_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_female_thousands.loc[key, year])):
                dataDict[key][year]["femaleTH"] = data_female_thousands.loc[key,year]
            if(not math.isnan(data_female_percentage.loc[key, year])):
                dataDict[key][year]["femalePR"] = data_female_percentage.loc[key,year]

### PRIMARY ###
existingCountries = data_primary_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_primary_thousands.loc[key, year])):
                dataDict[key][year]["primaryTH"] = data_primary_thousands.loc[key,year]
            if(not math.isnan(data_primary_percentage.loc[key, year])):
                dataDict[key][year]["primaryPR"] = data_primary_percentage.loc[key,year]

### SECONDARY ###
existingCountries = data_secondary_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_secondary_thousands.loc[key, year])):
                dataDict[key][year]["secondaryTH"] = data_secondary_thousands.loc[key,year]
            if(not math.isnan(data_secondary_percentage.loc[key, year])):
                dataDict[key][year]["secondaryPR"] = data_secondary_percentage.loc[key,year]

### TERTIARY ###
existingCountries = data_tertiary_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_tertiary_thousands.loc[key, year])):
                dataDict[key][year]["tertiaryTH"] = data_tertiary_thousands.loc[key,year]
            if(not math.isnan(data_tertiary_percentage.loc[key, year])):
                dataDict[key][year]["tertiaryPR"] = data_tertiary_percentage.loc[key,year]

### NO RESPONSE ###
existingCountries = data_noResponse_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_noResponse_thousands.loc[key, year])):
                dataDict[key][year]["noResponseTH"] = data_noResponse_thousands.loc[key,year]
            if(not math.isnan(data_noResponse_percentage.loc[key, year])):
                dataDict[key][year]["noResponsePR"] = data_noResponse_percentage.loc[key,year]

### TOTAL ###
existingCountries = data_total_thousands.index.values # thousands and percentage tables are same

for key in dataDict:
    if(key in existingCountries):
        for year in years:
            if(not math.isnan(data_total_thousands.loc[key, year])):
                dataDict[key][year]["totalTH"] = data_total_thousands.loc[key,year]
            if(not math.isnan(data_total_percentage.loc[key, year])):
                dataDict[key][year]["totalPR"] = data_total_percentage.loc[key,year]

dataJson = json.dumps(dataDict)

f = open("sport.json", "a")
f.write(dataJson)
f.close()