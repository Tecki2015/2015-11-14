# -*- coding: utf-8 -*-
import urllib.request
import string
from bs4 import BeautifulSoup
#import re
import csv
import os
import codecs
import subprocess

#import time
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys

datei = "anwaelteC.txt"
path = "output2.csv"


#remove existing outputfile
os.remove(path)

# Open the file in R/W and create if it doesn't exist. 
os.open(path, os.O_RDWR | os.O_CREAT)

#write expliced unicode bom in file:
f = open(path, "wb")
f.write(codecs.BOM_UTF8)


#path notepad++
pnpp = "C:/Program Files (x86)/Notepad++/Notepad++.exe"



#print (os.path.dirname(os.path.realpath(__file__)))






def csv_writer(data, path):
        with open(path, 'a', encoding='utf8', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';', quotechar = '"', quoting=csv.QUOTE_ALL)
                writer.writerow(data)
            #for line in data:
                #writer.writerow(line)







buchstabe = None
alpha = list(string.ascii_uppercase)
alphaZ = 0

with open(datei) as f:
    links = f.read().splitlines()

#print(links)

for asite in links:
        source = urllib.request.urlopen(asite)
        html = source.read()
        tree = BeautifulSoup(html, "lxml")
        g_data = tree.find_all("div", {"id": "viewsegmentB"})
        for item in g_data:
               
                try:
                        Titel = (item.find_all("strong", {"itemprop": "name"})[0]).text.split(" ")[-3]
                except:
                        Titel = ""
                try:
                        Vorname = (item.find_all("strong", {"itemprop": "name"})[0]).text.split(" ")[-2]
                except:
                        Vorname = ""
                
                Nachname = (item.find_all("strong", {"itemprop": "name"})[0]).text.split(" ")[-1]
                try:
                        jobTitel = (item.find_all("span", {"itemprop": "jobTitle"})[0]).text
                except:
                        jobTitel = ""

                FullName =  Vorname = (item.find_all("strong", {"itemprop": "name"})[0]).text



                Legal = (item.find_all("strong", {"itemprop": "legalName"})[0]).text
                Strasse = (item.find_all("p", {"itemprop": "streetAddress"})[0]).text
                PLZ = (item.find_all("span", {"itemprop": "postalCode"})[0]).text
                Ort = (item.find_all("span", {"itemprop": "addressLocality"})[0]).text
                Tele = (item.find_all("span", {"itemprop": "telephone"})[0]).text
                try:
                        eMail = (item.find_all("a", {"itemprop": "email"})[0]).text
                except:
                        eMail = ""
                try:
                        inet = (item.find_all("a", {"itemprop": "url"})[0]).text
                except:
                        inet = ""


                block = [Legal, Titel, FullName, Vorname, Nachname, jobTitel, Strasse, PLZ, Ort, Tele, eMail, inet]
                print(block)
            
                

                csv_writer(block, path) 


                #stuff = (Legal + ";" + Titel + ";" + FullName + ";" + Vorname + ";" + Nachname + ";" + jobTitel + ";" + Strasse + ";" + PLZ + ";" + Ort + ";" + Tele + ";" + eMail+ ";" + inet)
                
                
                #with open (csv, "a") as fh:
                        #fh.write(stuff + "\n")

# open notepadd ++ with file
subprocess.Popen([pnpp, path])
              
