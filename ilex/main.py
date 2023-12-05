from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

ilex_links = ("led", "flush", "chandeliers", "pendants", "series", "sconces", "ada-sconce")

ilex = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

for i in ilex_links:
    driver.get(f'https://www.ilexlight.com/{i}')
    time.sleep(3)

    driver.find_element(By.XPATH, "//div[@class='row pagination-view-row']/div[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//ul[@class='page-view-list true']/li[5]").click()
    time.sleep(8)

    ilex_product_urls = []
    ilex_url = driver.find_elements(By.XPATH, ".//div[@class='col-lg-12 product-item-image-column']/a")

    for url in ilex_url:
        link = url.get_attribute('href')
        ilex_product_urls.append(link)
        ilex["link_url"].append(link)
    
    for x in ilex_product_urls:
        driver.get(x)
        time.sleep(7)

        name = driver.find_element(By.XPATH, "//h3[@class='product-name']").text
        print(name)
        ilex["name"].append(name)

        try:
            description = driver.find_element(By.XPATH, "//div[@class='col-12 description']/p").text
            print(description)
            ilex["description"].append(description)
        except:
            description = "no description available"
            print(description)
            ilex["description"].append(description)

        try:
            image = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/img").get_attribute('src')
            print(image)
            ilex["image_url"].append(image)
        except:
            image = "no image available"
            print(image)
            ilex["image_url"].append(image)

        manufacturer_id = 420
        print(manufacturer_id)
        ilex["manufacturer_id"].append(manufacturer_id)

ilex_data = pd.DataFrame(ilex).to_csv("ilex_csv.csv", index=False)

driver.close()
