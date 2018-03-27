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

def get_page_content(): #Get Updated news ID From school website
    page = request.urlopen("https://www.marconiverona.gov.it/portal/circolari").read()
    soup = BeautifulSoup(page, "html.parser")
    new_id = soup.find("td", {"class":"db_app_circolari___numero fabrik_element fabrik_list_101_group_123 integer"}).text.strip()

    print("Richiesta al webserver eseguita con successo\n")

    return new_id

def log_and_check_new_id(current_id): #Check logs for past IDs and compare them with the (eventual) new ID
    if os.stat("lc_log.txt").st_size == 0:
        with open("lc_log.txt", "r+") as f:
            f.write(current_id)
        print("Log circolari aggiornato.")   
    else:
        with open("lc_log.txt", "r") as f:
            past_id = f.read()

        if past_id < current_id: #If the past ID is lesser than the new ID, there are new news
            print("Nuova Circolare!")
            update_log(current_id)
            return current_id
        else:
            print("Niente di nuovo.")
            return 0

def update_log(current_id):
    with open("lc_log.txt", "w") as f:
        f.write(current_id)
    
def main():
    actual_id = get_page_content()
    news_or_not = log_and_check_new_id(actual_id)
    
    if input("\nUscire dal programma? "):
        exit()
        
if __name__ == "__main__":
    main()
