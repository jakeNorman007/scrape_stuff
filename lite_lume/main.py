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

lite_lume = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

for i in range(1, 12):
    url = "https://litelume.com/store/"
    url2 = url + f"?pagenum={i}"
    driver.get(url2)

    lite_lume_product_urls = []
    lite_lume_url = driver.find_elements(By.XPATH, ".//h3[@class='ec_product_title_type1']/a")
    
    for url in lite_lume_url:
        product_link = url.get_attribute('href')
        lite_lume_product_urls.append(product_link)
        lite_lume["link_url"].append(product_link)

    for product in lite_lume_product_urls:
        driver.get(product)

        try:
            name = driver.find_element(By.XPATH, "//h1[@class='main-title entry-title ']").text
            print(name)
            lite_lume["name"].append(name)
        except:
            name = "no name available"
            print(name)
            lite_lume["name"].append(name)

        try:
            description = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/main/article/div/div/section/div[2]/div[1]/div/ul").text
            print(description)
            lite_lume["description"].append(description)
        except:
            description = "no description available"
            print(description)
            lite_lume["description"].append(description)

        try:
            image = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/main/article/div/div/section/div[1]/div[2]/div[1]/img").get_attribute('src')
            print(image)
            lite_lume["image_url"].append(image)
        except:
            image = "no image available"
            print(image)
            lite_lume["image_url"].append(image)

        manufacturer_id = 2248
        print(manufacturer_id)
        lite_lume["manufacturer_id"].append(manufacturer_id)

lite_lume_data = pd.DataFrame(lite_lume).to_csv("lite_lume_csv.csv", index=False)
