from dotenv import load_dotenv
load_dotenv()

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#Funtion to Fill info for changing Termin!
def change_termin():
    driver.get("https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en")
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Change Appointment").click()
    time.sleep(6)
    driver.find_element(By.ID,"xi-tf-948").send_keys(os.environ.get("FULL_NAME"))
    driver.find_element(By.ID,"xi-tf-949").send_keys(os.environ.get("LAST_NAMES"))
    driver.find_element(By.ID,"xi-tf-951").send_keys(os.environ.get("PROCESS_NUM"))
    driver.find_element(By.ID,"xi-tf-972").send_keys(os.environ.get("CHANGE_NUM"))
    driver.find_element(By.ID,"xi-tf-950").send_keys(os.environ.get("BD"))
    driver.find_element(By.ID,"applicationForm:managedForm:proceed").click()

    time.sleep(20)

    driver.refresh()

    time.sleep(20)


change_termin()







# conda activate env2
#python -m pip install selenium
#pip install os
# python -m pip install python-dotenv