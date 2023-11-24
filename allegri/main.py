from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

allegri = {"name": [], "description": [], "link_url": [], "image_url": [], "unique_id": [], "manufacturer_id": []}

for i in range(1, 22):
    url = "https://www.allegricrystal.com/product-category/collections"
    url2 = url + f"/page/{i}/"
    driver.get(url2)

    allegri_product_page_urls = []
    allegri_url = driver.find_elements(By.XPATH, ".//a[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']")
    for url in allegri_url:
        product_url = url.get_attribute('href')
        allegri_product_page_urls.append(product_url)
        allegri["link_url"].append(product_url)

    for x in allegri_product_page_urls:
        driver.get(x)

        try:
            name = driver.find_element(By.XPATH, "//div[@class='et_pb_module_inner']/h1").text
            print(name)
            allegri["name"].append(name)
        except:
            name = "no name available"
            print(name)
            allegri["name"].append(name)

        try:
            description = driver.find_element(By.XPATH, "//*[@id='et-boc']/div[3]/div/div/div[2]/div[2]/div[6]/div/p").text
            print(description)
            allegri["description"].append(description)
        except:
            description = "no description available"
            print(description)
            allegri["description"].append(description)

        try:
            image = driver.find_element(By.XPATH, "//img[@class='wp-post-image']").get_attribute('src')
            print(image)
            allegri["image_url"].append(image)
        except:
            image = "no image available"
            print(image)
            allegri["image"].append(image)

        try:
            unique_id = driver.find_element(By.XPATH, "//span[@class='sku']").text
            print(unique_id)
            allegri["unique_id"].append(unique_id)
        except:
            unique_id = "no unique id avaialble"
            print(unique_id)
            allegri["unique_id"].append(unique_id)

        manufacturer_id = 1251
        allegri["manufacturer_id"].append(manufacturer_id)

allegri_data = pd.DataFrame(allegri).to_csv("allegri_csv.csv", index=False)
