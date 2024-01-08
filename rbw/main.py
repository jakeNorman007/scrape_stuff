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

rbw = {"name": [], "link_url": [], "image_url": [], "unique_id": [], "manufacturer_id": []}

for i in range(1, 6):
    url = "https://rbw.com/"
    url2 = url + f"type/?page={i}"
    driver.get(url2)
    time.sleep(5)

    rbw_product_page_urls = []
    rbw_url = driver.find_elements(By.XPATH, ".//h2[@class='type-sans-130 styles-module--willHide--0e92f']/a")
    for url in rbw_url:
        link = url.get_attribute("href")
        rbw_product_page_urls.append(link)
        rbw["link_url"].append(link)

    for link in rbw_product_page_urls:
        driver.get(link)
        time.sleep(5)
        name = driver.find_element(By.XPATH, "//h1[@class='type-sans-830 lg:type-sans-930 mb-2 pr-2 md:pr-6']").text
        rbw["name"].append(name)
        print(name)

        '''
        try:
            description = driver.find_element(By.CSS_SELECTOR, "#accordion__panel-raa-31 > div > p").text
            rbw["description"].append(description)
        except:
            description = "no description available"
            rbw["description"].append(description)
        '''

        try:
            image_url = driver.find_element(By.XPATH, "//div[@class='js-swiper-slide-inner slide-inner']/img").get_attribute("src")
            rbw["image_url"].append(image_url)
        except:
            image_url = "no image available"
            rbw["image_url"].append(image_url)

        try:
            unique_id = driver.find_element(By.XPATH, "//p[@id='product_code']").text
            rbw["unique_id"].append(unique_id)
        except:
            unique_id = "no unique id available"
            rbw["unique_id"].append(unique_id)

        manufacturer_id = 1530
        rbw["manufacturer_id"].append(manufacturer_id)

rbw_data = pd.DataFrame(rbw).to_csv("rbw_csv.csv", index=False)
