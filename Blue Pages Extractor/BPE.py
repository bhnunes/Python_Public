import pandas as pd
import requests
from datetime import datetime
import sys
import json
import xlsxwriter
import re

#This will work only in Blue Pages API, but can be customized for other JSONs

def check_email(email, regex_pattern):
    regex_pattern=r"@\w{0,2}\.*ibm\.com"
    matches=re.findall(regex_pattern,email)
    if len(matches)!=0:
        status=True
    else:
        status=False

    return status

url=r'YOUR_ENDPOINT'
report_tree=r'Your_PATH'
regex_pattern=r"YOU_REGEX"

response = requests.get(url)
result=response.json()
status_code=response.status_code

if status_code==200:
    print("API Worked")
else:
    print("API Failed")
    sys.exit()


emails=[]
complete_names=[]
serial_numbers=[]
ismanagers=[]

for key in result['search']['entry']:
    counter=0
    for entry in key['attribute']:
        if entry['name']=='mail':
            email=entry['value'][0]
            if check_email(email, regex_pattern)==True:
                counter=counter+1
            else:
                pass
        elif entry['name']=='cn':
            complete_name=entry['value'][0]
            counter=counter+1
        elif entry['name']=='serialnumber':
            serialnumber=entry['value'][0]
            counter=counter+1
        elif entry['name']=='ismanager':
            ismanager=entry['value'][0]
            if ismanager.upper().strip()!="Y":
                counter=counter+1
            else:
                pass
        else:
            pass

    if counter==4:
        emails.append(email)
        complete_names.append(complete_name)
        serial_numbers.append(serialnumber)
        ismanagers.append(ismanager)
    else:
        pass

#print("email: " + str(len(emails)))
#print("complete_name: " + str(len(complete_names)))
#print("serial_number: " + str(len(serial_numbers)))
#print("ismanager: " + str(len(ismanagers)))


try:
    df = pd.DataFrame.from_dict({'Email':emails,'Complete Name':complete_names,'Serial Number':serial_numbers,'ismanager':ismanagers})
    writer = pd.ExcelWriter(report_tree, engine='xlsxwriter')
    df.to_excel(writer, header=True, index=False)
    writer.save()
    status_return='Report generated'
except Exception as e:
    status_return='Report Failed : '+ str(e)
    
print(status_return)


