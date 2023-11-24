from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

luminii = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

luminii_url_bank = ("linear", "bendable", "led-strip-lighting", "extrusions", "recessed-downlight", "cylinders",
                    "decorative-pendants", "stenos-micro-optics", "track", "backlighting", "controls", "power-supplies",
                    "remote-controlled", "express")

luminii_bank = []

for foo in luminii_url_bank:
    driver.get(f'https://luminiihom.com/products/{foo}')
    link_url = driver.find_elements(By.XPATH, ".//div[@class='images']/figure/a")

    for link in link_url:
       l = link.get_attribute("href")
       luminii_bank.append(l)
       luminii["link_url"].append(l)

for i in luminii_bank:
    driver.get(i)

    try:
        name = driver.find_element(By.XPATH, "//div[@class='inside']/h1").text
        luminii["name"].append(name)
    except:
        name = "no name available"
        luminii["name"].append(name)
    
    try:
        description = driver.find_element(By.XPATH, "//div[@class='inside']/ul").text
        luminii["description"].append(description)
    except:
        description = "no description available"
        luminii["description"].append(description)

    try:
        image = driver.find_element(By.XPATH, "//figure[@id='product_gallery_focus']/img").get_attribute('src')
        luminii["image_url"].append(image)
    except:
        image = "no image available"
        luminii["image_url"].append(image)

    manufacturer_id = 3102
    luminii["manufacturer_id"].append(manufacturer_id)

luminii_data = pd.DataFrame(luminii).to_csv("luminii_csv.csv", index=False)
    
