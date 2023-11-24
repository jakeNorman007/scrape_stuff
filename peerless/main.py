from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

peerless= {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

for i in range(1,6):
  url = "https://usa.peerless-electric.com/products/" 
  url2 = url + f"page/{i}/"
  driver.get(url2)
  
  peerless_products = []
  product_links = driver.find_elements(By.XPATH, ".//ul[@id='carousel']/li/a")
  for product in product_links:
    link = product.get_attribute('href')
    peerless_products.append(link)
    peerless["link_url"].append(link)

  for x in peerless_products:
    driver.get(x)
    name = driver.find_element(By.XPATH, "//div[@class='fixture-title-div']/h3").text
    peerless["name"].append(name)
  
    try:
      description = driver.find_element(By.XPATH, "//div[@class='column']").text
      print(description)
      peerless["description"].append(description)
    except:
      print("no description available.")
      description = "no description available."
      peerless["description"].append(description)
  
    image = driver.find_element(By.XPATH, "//div[@class='zoom slick-slide slick-current slick-active']/img[1]").get_attribute('src')
    peerless["image_url"].append(image)

    manufacturer_id = 1524 
    peerless["manufacturer_id"].append(manufacturer_id)
  
peerless_data= pd.DataFrame(peerless).to_csv("peerless_csv.csv", index=False)
time.sleep(5)
driver.close()