import os, zipfile

dir_name = r'C:\Users\BrunoHenriqueNunes\Desktop\Consolidate Python\EDRIM_Loader_OutPut\EDRIM_Loader_OutPut'
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

i=1
start=len(os.listdir(dir_name))

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = file_name = dir_name + "/" + item # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file
        print("File "+str(i)+" Processed - Number "+str(i)+" of "+str(start))
        i=i+1
