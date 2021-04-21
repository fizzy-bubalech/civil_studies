import gspread 
from oauth2client.service_account import ServiceAccountCredentials  

import json 

scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("results").sheet1

#all_data = sheet.get_all_records()
#data = sheet.row_values(2)
#data = data[4:]
#print(len(all_data))

all_people = []
#for i in range(2,43):
 #   all_people.append(sheet.row_values(i)[4:])

parties = []
for i in range(2,43):
    print(sheet.row_values(i)[3])
    parties.append(sheet.row_values(i)[3])

with open("parties.txt", "w") as fp:
    json.dump(parties,fp)

#with open("all_people.txt", "w") as fp:
  #  json.dump(all_people,fp)




