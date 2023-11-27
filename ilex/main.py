from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

ilex_links = ("led", "flush", "chandeliers", "pendants", "series", "sconces", "ada-sconce")

ilex = {"name": [], "description": [], "link_url": [], "image_url": [], "unique_id": [], "manufacturer_id": []}

for i in ilex_links:
    driver.get(f'https://www.ilexlight.com/{i}')
    time.sleep(3)

driver.close()
