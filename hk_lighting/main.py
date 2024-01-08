from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

hk = {"name": [], "description": [], "link_url": [], "image_url": [], "maunfacturer_id": []}

hk_slug = ("accent_landscape/", "ceiling-mount/", "flood-wall-wash/", "hanging-catenary/", "image-projector/",
           "path-bollard", "sign-pole-mount/", "step-in-grade/", "wall-mount/", "accessories/")

for i in hk_slug:
    driver.get(f'https://www.hklighting.com/product-category/products/{i}')
    time.sleep(2)

    hk_links_l1 = []
    hk_layer_1 = driver.find_elements(By.XPATH, ".//div[@class='fusion-product-wrapper']/a")

    for x in hk_layer_1:
        hk_link_1 = x.get_attribute('href')
        hk_links_l1.append(hk_link_1)

    for y in hk_links_l1:
        driver.get(y)
        time.sleep(4)

        

driver.close()
