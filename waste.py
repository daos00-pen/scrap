import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

service = Service()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.gov.uk/")
        
time.sleep(3)
# Explicitly wait for an essential element to ensure content is loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

st.write(driver.page_source)
