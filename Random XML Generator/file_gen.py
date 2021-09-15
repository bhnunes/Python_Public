# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:52:28 2019

@author: BrunoHenriqueNunes
"""
import shutil
import string
import random

def r_l():
    a=random.choice(string.ascii_letters)
    return a

def r_n():
    a=random.randint(0,9)
    return a

source_path=(r'C:\Users\BrunoHenriqueNunes\Desktop\test xmls\Resource\000EC527-D3F0-0744-85B5-D4543930F9DA.xml')
to_path=(r'C:\Users\BrunoHenriqueNunes\Desktop\test xmls\Copy files')

number=int(input("Insert the value to be copied:"))

i=1
while i<=number:
        name="000EC527-D3F0-0744-85B5-"+r_l()+str(r_n())+r_l()+str(r_n())+r_l()+str(r_n())+r_l()+str(r_n())+r_l()+str(r_n())+r_l()+str(r_n())
        new_path=to_path+"\\"+name+".xml"
        shutil.copy(source_path,new_path)
        print("Moved file "+str(i)+" of "+str(number))
        print(new_path)
        i=i+1






