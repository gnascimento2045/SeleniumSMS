
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time as time

driver = webdriver.Firefox()
driver.get('https://messages.google.com/web/')
#sleep(25)
element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/div/mw-fab-link/a')))
element.click()
element2 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/mw-new-conversation-sub-header/div/div[2]/mw-contact-chips-input/div/div/input')))
element2.send_keys('61992724480')
element3 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-new-conversation-container/div/mw-contact-selector-button/button/span[2]/span/span')))
element3.click()
element4 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-message-compose/div/div[2]/div/div/mws-autosize-textarea/textarea')))
element4.send_keys('teste')
time.sleep(5)

print(element.is_displayed())