#!usr/bin/env python

''' Python program to check for news & updates on school website
    The current ID in the txt file is to be updated manually at the end of every year, setting it to the ID
    of the first news that has come out.
'''

import urllib.request as request
from bs4 import BeautifulSoup
import os

__author__ = "Tobia Valerio"
__license__ = "GPL"
__version__ = "V1.0"
__status__ = "Production"

def getPageContent(): #Get Updated news ID From school website
    page = request.urlopen("https://www.marconiverona.gov.it/portal/circolari").read()
    soup = BeautifulSoup(page, "html.parser")
    new_ID = soup.find("td", {"class":"db_app_circolari___numero fabrik_element fabrik_list_101_group_123 integer"}).text.strip()

    print("Connessione al webserver stabilita e dati scaricati.\n")

    return new_ID

def logAndCheckNewID(current_ID): #Check logs for past IDs and compare them with the (eventual) new ID
    if os.stat("lc_log.txt").st_size == 0:
        with open("lc_log.txt", "r+") as f:
            f.write(current_ID)
        print("Log circolari aggiornato.")   
    else:
        with open("lc_log.txt", "r") as f:
            past_ID = f.read()

        if past_ID < current_ID: #If the past ID is lesser than the new ID, there are new news
            print("Nuova Circolare!")
            updateLog(current_ID)
            return current_ID
        else:
            print("Niente di nuovo.")
            return 0

def updateLog(current_ID):
    with open("lc_log.txt", "w") as f:
        f.write(current_ID)
    
def main():
    actual_ID = getPageContent()
    news_or_not = logAndCheckNewID(actual_ID)
    if news_or_not != 0:
        if input("\nUscire dal programma? "):
            exit()
    else:
        if input("\nUscire dal programma? "):
            exit()
        
if __name__ == "__main__":
    main()
