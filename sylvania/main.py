from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time

#options = Options()
#options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

sylvania = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

