import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

driver.get('https://www.gov.uk/')

st.write(driver.page_source)
