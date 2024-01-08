from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

ledvance_lamps = {"name": [], "link_url": [], "description": [], "image_url": [], "maunfacturer_id": []}

driver.get("https://www.ledvanceus.com/products/led-lamps/Pages/default.aspx")

lamp_link = []
products = driver.find_elements(By.XPATH, ".//div[@class='ncTile_img']/a[1]")

for x in products:
    group_url = x.get_attribute('href')
    lamp_link.append(group_url)

for link in lamp_link:
    driver.get(link)

    product_pages = []
    product_links = driver.find_elements(By.XPATH, "//div[@class='ncTile_img']/a[1]")

    for foo in product_links:
        product_url = foo.get_attribute('href')
        product_pages.append(product_url)
        ledvance_lamps["link_url"].append(product_url)

    for bar in product_pages:
        driver.get(bar)

        try:
            name = driver.find_element(By.XPATH, "//div[@class='ms-rtestate-field']/h1").text
            print(name)
            ledvance_lamps["name"].append(name)
        except:
            name = "no name available"
            print(name)
            ledvance_lamps["name"].append(name)

        try:
            description = driver.find_element(By.XPATH, "/html/body/form/div[12]/div[3]/div[2]/div[3]/div[1]/div/div/section[2]/div/article/div/div[2]/div[1]/div/div[1]/p").text
            print(description)
            ledvance_lamps["description"].append(description)
        except:
            description = "no description available"
            print(description)
            ledvance_lamps["description"].append(description)

driver.close()
