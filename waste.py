import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--headless=new")
options.add_argument('--disable-gpu')

service = Service()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.gov.uk/')

st.write(driver.page_source)
