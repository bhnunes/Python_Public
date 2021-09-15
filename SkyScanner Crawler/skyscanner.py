from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime  
from datetime import timedelta 
from datetime import date
import xlsxwriter
import pandas as pd

def replace_values(sMonth,sDay,sYear,eMonth,eDay,eYear,url):
    j=url.replace('@@@startmonth@@@',sMonth)
    j=j.replace('@@@startday@@@',sDay)
    j=j.replace('@@@startyear@@@',sYear)
    j=j.replace('@@@endmonth@@@',eMonth)
    j=j.replace('@@@endday@@@',eDay)
    j=j.replace('@@@endyear@@@',eYear)
    return j

def stop(sMonth,sDay,sYear,eMonth,eDay,eYear):
    sMonth=int(sMonth)
    sDay=int(sDay)
    sYear=int(sYear)
    eMonth=int(eMonth)
    eDay=int(eDay)
    eYear=int(eYear)

    if sMonth==12 and sDay>=15 and sYear>=2020:
        stop=True
    else:
        stop=False
    if eMonth==12 and eDay>=15 and eYear>=2020:
        stop=True
    else:
        stop=False
    return stop


def diff_dates(d2):
    return abs(d2-datetime.now().date()).days

driver_path=(r'C:\Users\BrunoHenriqueNunes\AppData\Local\SeleniumBasic\chromedriver.exe')

driver = webdriver.Chrome(driver_path)

report_tree=r'C:\Users\BrunoHenriqueNunes\Desktop\Report Travel\report.xlsx'

d2=date(2020,12,31)

limit=diff_dates(d2)

from_date=[]
thru_date=[]
price=[]
link=[]
sYear='@@@startyear@@@'
sMonth='@@@startmonth@@@'
sDay='@@@startday@@@'
eYear='@@@endyear@@@'
eMonth='@@@endmonth@@@'
eDay='@@@endday@@@'

urls=[r'https://www.expedia.com.br/Flights-Search?trip=roundtrip&leg1=from%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cto%3AJoanesburgo%2C%20%C3%81frica%20do%20Sul%20(JNB-Todos%20os%20aeroportos)%2Cdeparture%3A'+sDay+r'%2F'+sMonth+r'%2F'+sYear+r'TANYT&leg2=from%3AJoanesburgo%2C%20%C3%81frica%20do%20Sul%20(JNB-Todos%20os%20aeroportos)%2Cto%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cdeparture%3A'+eDay+r'%2F'+eMonth+r'%2F'+eYear+r'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com.br',
r'https://www.expedia.com.br/Flights-Search?trip=roundtrip&leg1=from%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cto%3ACidade%20do%20Cabo%2C%20%C3%81frica%20do%20Sul%20(CPT-Aeroporto%20Internacional%20de%20Cape%20Town)%2Cdeparture%3A'+sDay+r'%2F'+sMonth+r'%2F'+sYear+r'TANYT&leg2=from%3ACidade%20do%20Cabo%2C%20%C3%81frica%20do%20Sul%20(CPT-Aeroporto%20Internacional%20de%20Cape%20Town)%2Cto%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cdeparture%3A'+eDay+r'%2F'+eMonth+r'%2F'+eYear+r'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com.br',
r'https://www.expedia.com.br/Flights-Search?trip=roundtrip&leg1=from%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cto%3ADurban%2C%20%C3%81frica%20do%20Sul%20(DUR-King%20Shaka%20Intl.)%2Cdeparture%3A'+sDay+r'%2F'+sMonth+r'%2F'+sYear+r'TANYT&leg2=from%3ADurban%2C%20%C3%81frica%20do%20Sul%20(DUR-King%20Shaka%20Intl.)%2Cto%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cdeparture%3A'+eDay+r'%2F'+eMonth+r'%2F'+eYear+r'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com.br',
r'https://www.expedia.com.br/Flights-Search?trip=roundtrip&leg1=from%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cto%3APort%20Elizabeth%2C%20%C3%81frica%20do%20Sul%20(PLZ)%2Cdeparture%3A'+sDay+r'%2F'+sMonth+r'%2F'+sYear+r'TANYT&leg2=from%3APort%20Elizabeth%2C%20%C3%81frica%20do%20Sul%20(PLZ)%2Cto%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cdeparture%3A'+eDay+r'%2F'+eMonth+r'%2F'+eYear+r'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com.br',
r'https://www.expedia.com.br/Flights-Search?trip=roundtrip&leg1=from%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cto%3AEast%20London%2C%20%C3%81frica%20do%20Sul%20(ELS)%2Cdeparture%3A'+sDay+r'%2F'+sMonth+r'%2F'+sYear+r'TANYT&leg2=from%3AEast%20London%2C%20%C3%81frica%20do%20Sul%20(ELS)%2Cto%3AS%C3%A3o%20Paulo%2C%20Brasil%20(SAO)%2Cdeparture%3A'+eDay+r'%2F'+eMonth+r'%2F'+eYear+r'TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com.br']

k=0
for url in urls:
    stop_process=False
    i=0
    while i<limit and stop_process==False:
        initial=datetime.now().date()+timedelta(days=1+i)
        week_day=initial.weekday()
        if week_day==4:
            end=initial+timedelta(days=15)
            initial_conv=str(initial)
            end_conv=str(end)
            initial_conv=initial_conv.split("-")
            sYear=initial_conv[0]
            sMonth=initial_conv[1].zfill(2)
            sDay=initial_conv[2].zfill(2)
            end_conv=end_conv.split("-")
            eYear=end_conv[0]
            eMonth=end_conv[1].zfill(2)
            eDay=end_conv[2].zfill(2)
            stop_process=stop(sMonth,sDay,sYear,eMonth,eDay,eYear)
            if stop_process==True:
                break
            else:
                from_date.append(initial)
                thru_date.append(end)
                url_new=replace_values(sMonth,sDay,sYear,eMonth,eDay,eYear,url)
                link.append(url_new)
                driver.get(url_new)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'show-flight-details')))
                    time.sleep(3)
                    pricing=driver.find_element_by_xpath("//span[@data-test-id='listing-price-dollars']")
                    j=pricing.text
                    j=j.replace("R$ ", "")
                    j=j.replace(".", ",")
                    price.append(j)
                except:
                    price.append('error found')
            i=i+1
        else:
            i=i+1
    k=k+1
    print(str(k)+" of limit "+str(len(urls)))


driver.quit()

df = pd.DataFrame.from_dict({'from date':from_date,'Thru date':thru_date,'Link':link,'Price':price})
writer = pd.ExcelWriter(report_tree, engine='xlsxwriter')
df.to_excel(writer, header=True, index=False)
writer.save()
print("Process Terminated")

