import urllib.request
import string
from bs4 import BeautifulSoup
from selenium import webdriver
import re

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

datei = "anwaelte.txt"
buchstabe = None
alpha = list(string.ascii_uppercase)
alphaZ = 0


def writeStuff():
        print (buchstabe)
        url = "http://www.anwaltsregister.de/Anwaelte_aus_Deutschland/Nachnamen_beginnend_mit_%s.html" %buchstabe
        browser = webdriver.Firefox()
        browser.get(url)
        #time.sleep(5)
        html = browser.page_source
        tree = BeautifulSoup(html)
        
        
        
        g_data = tree.find_all("nav", {"id": "attorneylistLinks"})
        #f = open("test.txt", "w")
        #f.write(str(g_data))
        #f.close()
        #browser.quit() 

        for item in g_data:
                 name = ((item.find_all("span", {"class": "displayName"})[0]).text)
                 print(name)
                 #address = ((item.find_all("div", {"itemtype": "http://schema.org/LocalBusiness"})[0]).text.replace("\n",""))
                 #sep = ' | '
                 #address = address.split(sep, 1)[0]
                 #try:
                 #        tel = ((item.find_all("span", {"itemprop": "telephone"})[0]).text)
                 #except:
                 #        tel = "NA"
                 #try:
                 #        contact1 = ((item.find_all("a", {"class": "search-website searchActionLinks"})[0]["href"]))
                 #except:
                 #        contact1 = "NA"
                        
                 #try:
                 #        rating = ((item.find_all("a", {"class": "ratingStarSearch"})[0]).text)
                 #except:
                 #        rating = "NA"

                 #stuff = (name + ";" + address + ";" + tel + ";" + contact1 + ";" + rating)
                 #stuff = str(stuff)
                 #stuff = re.sub(' +',' ',stuff)
                 #stuff = stuff.replace("\r","")
                 #stuff = stuff.replace("\t","")
                 #stuff = "".join(stuff.splitlines())
                 #print (stuff)
                 #with open (datei, "a") as fh:
                 #        fh.write(stuff + "\n")
                        
                 
                 
        #print (g_data)
        browser.quit()        



for i in range(1):
        buchstabe = alpha[0]
        print(i)
        writeStuff()
        alphaZ = alphaZ + 1




 browser = webdriver.Firefox()
        browser.get(url)
        html = browser.page_source
        tree = BeautifulSoup(html)

        
        g_data = tree.find_all("a")
        print(len(g_data))
        counter = 0
        
        for item in g_data:
                 
                 if "Rechtsanw" in item.text:
                         link = (item['href'])

                         print (item['href'])
                         with open (datei, "a") as fh:
                                 fh.write(link + "\n")

                         
                 
               
        browser.quit()        



