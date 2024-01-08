from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

rab = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

rab_url_bank = ("indoor", "residential", "outdoor", "lamps", "controls", "electric-vehicle-chargers")
rab_bank = []

for foo in rab_url_bank:
    driver.get(f'https://www.rablighting.com/{foo}')
    link_url = driver.find_elements(By.XPATH, ".//div[@class='mg-detail']/a")

    for link in link_url:
        bar = link.get_attribute('href')
        rab_bank.append(bar)
        rab["link_url"].append(bar)

    for i in rab_bank:
        driver.get(i)

        try:
            name = driver.title
            print(name)
            rab["name"].append(name)
        except:
            name = "no name available"
            print(name)
            rab["name"].append(name)

        try:
            description = driver.find_element(By.XPATH, "//div[@class='border border-bottom border-color-base m-b-2']").text
            print(description)
            rab["description"].append(description)
        except:
            description = "no description available"
            print(description)
            rab["description"].append(description)

        try:
            image = driver.find_element(By.XPATH, "//div[@class='col-xs-3']/img").get_attribute('src')
            print(image)
            rab["image_url"].append(image)
        except:
            image = "no image available"
            print(image)
            rab["image_url"].append(image)
        
        manufacturer_id = 1218
        print(manufacturer_id)
        rab["manufacturer_id"].append(manufacturer_id)

rab_data = pd.DataFrame(rab).to_csv('rab_csv.csv', index=False)
