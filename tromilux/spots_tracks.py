from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# CANT GO HEADLESS BECAUSE CSS NEEDS TO LOAD TO GRAB DESCRIPTION
options = Options()
# options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

data = { "name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

driver.get("https://www.tromilux.com/en/products/indoor/spotlights-tracks/")

product_url = []
page = driver.find_elements(By.XPATH, ".//*[@class='product_item']/a")
for p in page:
  url = p.get_attribute('href')
  product_url.append(url)
  data["link_url"].append(url)

for link in product_url:
  driver.get(link)
  time.sleep(3)
  name = driver.find_element(By.XPATH, "//*[@class='container text-center']/h2").text
  print(name)
  data["name"].append(name)

  description = driver.find_element(By.XPATH, "//*[@id='descricao']").text
  print(description)
  data["description"].append(description)  

  image = driver.find_element(By.XPATH, "//div[@class='col-sm-12 img']/a/img").get_attribute('src')
  print(image)
  data["image_url"].append(image)
  
  manufacturer_id = 308
  print(manufacturer_id)
  data["manufacturer_id"].append(manufacturer_id)

tromilux = pd.DataFrame(data).to_csv("spots_tracks.csv", index=False)
driver.close()