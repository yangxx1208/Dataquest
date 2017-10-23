## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for f in data_files:
    file_path = "schools/{}".format(f)
    key_name = f.replace(".csv","")
    data[key_name] = pd.read_csv(file_path)
    print(file_path)
    
    

## 5. Exploring the SAT Data ##

print(data["sat_results"].head(5))

## 6. Exploring the Remaining Data ##

for item in data:
   print(data[item].head(5))
print(len(data))    


## 8. Reading in the Survey Data ##

all_survey = pd.read_csv("schools/survey_all.txt",delimiter = "\t",encoding = "windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt",delimiter = "\t",encoding = "windows_1252")
print(all_survey.head(5))
print(d75_survey.head(5))
survey = pd.concat([all_survey,d75_survey],axis = 0)
print(survey.head(5))

## 9. Cleaning Up the Surveys ##

survey["DBN"] = survey["dbn"]
survey_column = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey = survey.loc[:,survey_column]
data["survey"]=survey
print(survey.head())

## 11. Inserting DBN Fields ##

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def  pad_csd(num):
    string_representation = str(num)
    if len(string_representation) > 1:
        return string_representation
    else:
        return string_representation.zfill(2)
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]
print(data["class_size"].head())

## 12. Combining the SAT Scores ##

def sat_tran(row):
    col = ["SAT Math Avg. Score","SAT Critical Reading Avg. Score","SAT Writing Avg. Score"]
    sat_all = 0
    for item in col:
        sat_all +=pd.to_numeric(row[item],errors = "coerce")
    return sat_all
    
    
data["sat_results"]["sat_score"] = data["sat_results"].apply(sat_tran,axis = 1)

print(data["sat_results"]["sat_score"])

## 13. Parsing Geographic Coordinates for Schools ##

import re

def find_lat(loc):   
    coords = re.findall("\(.+\)", loc)
    lat = coords[0].split(",")[0].replace("(", "")
    return lat

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(find_lat)

print(data["hs_directory"].head())
    

## 14. Extracting the Longitude ##

import re
def find_lon(loc):
    cord = re.findall("\(.+\)",loc)
    lon = cord[0].split(',')[1].replace(")","")
    return lon

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(find_lon)

data["hs_directory"]["lon"] =pd.to_numeric( data["hs_directory"]["lon"],errors = "coerce")
data["hs_directory"]["lat"] =pd.to_numeric( data["hs_directory"]["lat"], errors = "coerce")

print(data["hs_directory"]["lon"])