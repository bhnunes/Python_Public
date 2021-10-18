import os
import xlsxwriter
import pandas as pd

path=r'C:\Users\039762631\Downloads\GPA_Download\GPA_Download'
report_tree=r'C:\Users\039762631\Desktop\Consolidate Several files in One\Report.xlsx'

files = os.listdir(path)
File_names=[]

i=1

for f in files:
    try:
        File_names.append(f)
        print("File "+str(f)+" Processed - Number "+str(i)+" of "+str(len(files)))
        i=i+1
    except Exception as e:
        print("File "+str(f)+" Failed - Number "+str(i)+" of "+str(len(files))+" - "+str(e))
        i=i+1



df = pd.DataFrame.from_dict({'File Names':File_names})
writer = pd.ExcelWriter(report_tree, engine='xlsxwriter')
df.to_excel(writer, header=True, index=False)
writer.save()
print('Finished')