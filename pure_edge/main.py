from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

pure_edge = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

driver.get("https://www.pureedgelighting.com/products")

pure_edge_categories = []
pure_edge_category_links = driver.find_elements(By.XPATH, ".//*[@id='inner-content-wrapper']/div/div/div/div/div[2]/a")

for x in pure_edge_category_links:
    category_link = x.get_attribute('href')
    pure_edge_categories.append(category_link)

for foo in pure_edge_categories:
    driver.get(foo)
    pure_edge_products = []
    product_links = driver.find_elements(By.XPATH, ".//div[@class='prod_item_box_inner']/a")

    for bar in product_links:
        product_link = bar.get_attribute('href')
        pure_edge_products.append(product_link)
        pure_edge["link_url"].append(product_link)

    for i in pure_edge_products:
        driver.get(i)
        
        try:
            name = driver.find_element(By.XPATH, "//*[@id='pe-wrapper']/div[5]/div[1]/h1").text
            pure_edge["name"].append(name)
        except:
            name = "no name available"
            pure_edge["name"].append(name)

        try:
            description = driver.find_element(By.XPATH, "//*[@id='product_description_content']").text
            pure_edge["description"].append(description)
        except:
            description = "no description available"
            pure_edge["description"].append(description)

        try:
            image = driver.find_element(By.XPATH, "//*[@id='product_photo_cell']/div[1]/a/img").get_attribute('src')
            pure_edge["image_url"].append(image)
        except:
            image = "no image available"
            pure_edge["image_url"].append(image)

        manufacturer_id = 436 
        pure_edge["manufacturer_id"].append(manufacturer_id)

pure_edge_data = pd.DataFrame(pure_edge).to_csv("pure_edge.csv", index=False)
