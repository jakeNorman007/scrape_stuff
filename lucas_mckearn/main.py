from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

lucas_mckearn = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

for i in range(1, 22):
  url = 'https://lucasmckearn.com/products/interior-lighting/'
  url2 = url + f"page/{i}/"
  driver.get(url2)

  lucas_products = []
  product_links = driver.find_elements(By.XPATH, "//*[@class='product-image']/a")
  for product in product_links:
    link = product.get_attribute('href')
    lucas_products.append(link)
    lucas_mckearn["link_url"].append(link)

  for x in lucas_products:
    driver.get(x)
    name = driver.find_element(By.XPATH, "//h2[@class='product_title entry-title show-product-nav']").text 
    lucas_mckearn["name"].append(name)
  
    try:
      description = driver.find_element(By.XPATH, "//*[@class='tab-content resp-tab-content resp-tab-content-active']/p").text
      print(description)
      lucas_mckearn["description"].append(description)
    except:
      print("no description available.")
      description = "no description available."
      lucas_mckearn["description"].append(description)
  
    image = driver.find_element(By.XPATH, "//div[@class='inner']/img").get_attribute('src')
    lucas_mckearn["image_url"].append(image)

    manufacturer_id = 1835
    lucas_mckearn["manufacturer_id"].append(manufacturer_id)
  
lucas_mckearn_data = pd.DataFrame(lucas_mckearn).to_csv("lucas_mckear_cs.csv", index=False)
driver.close()
