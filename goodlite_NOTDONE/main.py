from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

goodlite = {"name": [], "description": [], "link_url": [], "image_url": [], "unique_id": [], "manufacturer_id": []}

for i in range(1, 10):
    url = "https://gllite.com/"
    url2 = url + f"shop/page/{i}/"
    driver.get(url2)

    goodlite_product_page_urls = []
    goodlite_url = driver.find_elements(By.XPATH, ".//div[@class='prd-btn']/a")
    for url in goodlite_url:
        link = url.get_attribute("href")
        goodlite_product_page_urls.append(link)
        goodlite["link_url"].append(link)
    
    for x in goodlite_product_page_urls:
        driver.get(x)
        time.sleep(4)
        name = driver.find_element(By.XPATH, "//h2[@class='product_title entry-title']").text
        goodlite["name"].append(name)
        #print(name)

        try:
            description = driver.find_element(By.XPATH, "//div[@class='des-txt']/p").text
            #print(description)
            goodlite["description"].append(description)
        except:
            print("no description available")
            description = "no description available"
            goodlite["description"].append(description)

        image = driver.find_element(By.XPATH, "//*[@class='woocommerce-product-gallery__image wpgs_image']/img").get_attribute('src')
        goodlite["image_url"].append(image)
        #print(image)

        try:
            unique_id = driver.find_element(By.XPATH, "//*[@class='item-code sku']").text
            #print(unique_id)
            goodlite["unique_id"].append(unique_id)
        except:
            print("no unique id available")
            unique_id = "no unique id available"
            goodlite["unique_id"].append(unique_id)

        manufacturer_id = 3106
        goodlite["manufacturer_id"].append(manufacturer_id)

goodlite_data = pd.DataFrame(goodlite).to_csv("goodlite_csv.csv", index=False)
driver.close()
