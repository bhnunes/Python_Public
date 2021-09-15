import os
import xlsxwriter
import pandas as pd

path=r'C:\Users\BrunoHenriqueNunes\Desktop\Consolidate Python\EDRIM_Loader_OutPut\EDRIM_Loader_OutPut'
report_tree=r'C:\Users\BrunoHenriqueNunes\Desktop\Consolidate Python\Report.xlsx'

files = os.listdir(path)

i=1

df = pd.DataFrame()
for f in files:
    try:
        fo=path+"\\"+f
        data = pd.read_excel(fo, header = None,encoding='latin-1')
        data['Name_File'] = f
        df = df.append(data)
        print("File "+str(f)+" Processed - Number "+str(i)+" of "+str(len(files)))
        i=i+1
    except Exception as e:
        print("File "+str(f)+" Failed - Number "+str(i)+" of "+str(len(files))+" - "+str(e))
        i=i+1


writer = pd.ExcelWriter(report_tree, engine='xlsxwriter', options={'strings_to_urls': False})
df.to_excel(writer, header=True, index=False)
writer.save()
print('Finished')