from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import threading
import csv
import time

with open("mensagem.txt") as msg_text:
        msg_text2 = msg_text.read()
        print(msg_text2)
            
driver = webdriver.Firefox()

with open("contact.csv", "r") as arquivo_csv:
        arquivo_csv = csv.reader(arquivo_csv) 
        toplinha = next(arquivo_csv)
        toplinha_var1 = "".join(map(str,toplinha))
        print(toplinha_var1)
        driver.get("https://messages.google.com/web/")

        time.sleep(10)
        cont = 0

while (cont < 10000):
    
        for consulta in toplinha_var1:  
               time.sleep(10)
               element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a')))
               element.click()
               element2 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/div/input')))
               element2.send_keys(str(toplinha_var1))
               element3 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/div/mw-contact-selector-button/button/span[2]/span/span')))
               element3.click()
               element4 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/div[2]/div/div/mws-autosize-textarea/textarea')))
               element4.send_keys(msg_text2)
               element5 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/mws-message-send-button/div/mw-message-send-button/button/span[4]')))
               element5.click()
               content = driver.switch_to.active_element
               content.send_keys(Keys.RETURN)   
               cont+=1
               import pandas as pd
               df = pd.read_csv('contact.csv')
               df.to_csv('contact.csv', header=False, index=False)
               with open("contact.csv", "r") as arquivo_csv:
                arquivo_csv = csv.reader(arquivo_csv)
                toplinha = next(arquivo_csv)
                toplinha_var1 = "".join(map(str,toplinha))
                print(toplinha_var1)

