from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

luxrite_data = {"name": [], "description": [], "link_url": [], "image_url": [], "unique_id": [], "manufacturer_id": []}

# using a tuple to store the product categories because it's faster, they are more memory efficient
luxrite_url_bank = ("luxsmart", "san-diego-collection", "baffled-trim", "smooth-flat-trim", "smooth-flat-trim?page=2", 
    "smooth-flat-trim?page=3", "gimal", "luxsafe", "1module", "2module", "2module?page=2", "3module", "4module", "4module?page=2",
    "5-6module", "multilight", "multihead", "tampa", "aklow", "aklow?page=2","aklow?page=3","cincinnati", "commercial", "raleigh",
    "richmond", "knoxville", "lexington", "charleston", "denver", "anti-glare", "cctwattageselectable-layin", "layin-components",
    "pensacola", "omaha", "boise", "tucson", "madison", "memphis", "phoenix", "melbourne", "charlotte", "naples", "seattle", "houston",
    "boulder", "nashville", "daytona", "sarasota", "destin-collection","ocala-collection", "dallas", "detroit-collection", "recessedchannels", 
    "recessedmudinchannel", "surfacemountchannels","cornerchannels", "cob-tape", "115wreeltape", "96wreeltape", "72wreeltape", 
    "48wreeltape", "rgbwwtapelight", "tapeconnectors", "drivers", "a-15", "a19", "a19?page=2","a19?page=3","a19?page=4","a21", 
    "a19-colored", "c7", "s14", "par-colored", "candle-colored", "specialtychannels", "decorative", "decorative?page=2", "candle", 
    "candle?page=2","candle?page=3","a-shape", "par", "par?page=2", "br", "br?page=2", "hid-flood", "garage", "mr-series", "mini-pin",
    "mr-16", "gu-10", "pin-base", "t5", "t8", "t8?page=2", "u6")

luxrite_bank = []

for foo in luxrite_url_bank:
    driver.get(f'https://luxrite.com/collections/{foo}')
    link_url = driver.find_elements(By.XPATH, ".//a[@class='spf-product-card__image-wrapper']")

    for link in link_url:
        l = link.get_attribute("href")
        luxrite_bank.append(l)
        luxrite_data["link_url"].append(l)

for i in luxrite_bank:
    driver.get(i)
    time.sleep(2)

    try:
        name = driver.find_element(By.XPATH, "//h1[@class='h2 product-single__title small--hide']").text
        luxrite_data["name"].append(name)
    except:
        name = "no name available"
        luxrite_data["name"].append(name)
    
    try:
        description = driver.find_element(By.XPATH, "//ul[@class='product-custom-data-wrapper']").text
        luxrite_data["description"].append(description)
    except:
        description = "no description available"
        luxrite_data["description"].append(description)

    try:
        image = driver.find_element(By.XPATH, "//img[@class='lazyautosizes lazyloaded']").get_attribute('srcset')
        luxrite_data["image_url"].append(image)
    except:
        image = "no image available"
        luxrite_data["image_url"].append(image)

    try:
        unique_id = driver.find_element(By.XPATH, "//p[@class='product-single__sku small--hide']").text
        luxrite_data["unique_id"].append(unique_id)
    except:
        unique_id = "no id available"
        luxrite_data["unique_id"].append(unique_id)

    manufacturer_id = 2722
    luxrite_data["manufacturer_id"].append(manufacturer_id)

luxrite_final = pd.DataFrame(luxrite_data).to_csv("luxrite_csv.csv", index=False)
