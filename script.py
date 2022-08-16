

from dotenv import load_dotenv
load_dotenv()


import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


#Funtion to Fill info for changing Termin!
def change_termin():
    driver.get("https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Change Appointment").click()
    time.sleep(6)
    driver.find_element(By.ID,"xi-tf-948").send_keys(os.environ.get("FULL_NAME"))
    driver.find_element(By.ID,"xi-tf-949").send_keys(os.environ.get("LAST_NAMES"))
    driver.find_element(By.ID,"xi-tf-951").send_keys(os.environ.get("PROCESS_NUM"))
    driver.find_element(By.ID,"xi-tf-972").send_keys(os.environ.get("CHANGE_NUM"))
    driver.find_element(By.ID,"xi-tf-950").send_keys(os.environ.get("BD"))
    driver.find_element(By.ID,"applicationForm:managedForm:proceed").click()


def get_termin():
    driver.get("https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en")
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,"Book Appointment").click()
    time.sleep(2)
    driver.find_element(By.ID,"xi-cb-1").click()
    driver.find_element(By.ID,"applicationForm:managedForm:proceed").click()
    time.sleep(3)
    # driver.find_element(By.ID,"xi-sel-400").click()
    driver.find_element(By.ID, "xi-sel-400").click()
    time.sleep(3)
    driver.find_elements(By.LINK_TEXT,'Albania')


    




    


change_termin()
# get_termin()






# conda activate env2
#python3 -m pip install selenium
#pip install os
# python3 -m pip install python-dotenv
# or conda install -c conda-forge python-dotenv
