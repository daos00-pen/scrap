import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

driver.get('https://www.uradprace.cz')

st.write(driver.page_source)
