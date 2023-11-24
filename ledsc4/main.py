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

leds_see_four = {"name": [], "description": [], "link_url": [], "image_url": [], "unique_id": [], "manufacturer_id": []}

driver.get("https://ledsc4.us/en/3-products")
driver.implicitly_wait(10)

leds_product_links = []
products = driver.find_elements(By.XPATH, "//div[@class='product-description']/a")

for link in products:
  page = link.get_attribute('href')
  leds_product_links.append(page)
  leds_see_four["link_url"].append(page)
  
for url in leds_product_links:
  driver.get(url)
  name = driver.find_element(By.XPATH, "//h1[@class='h1 page-title']").text
  leds_see_four["name"].append(name)
  
  description = driver.find_element(By.XPATH, "//div[@class='rte-content']/p[1]").text
  leds_see_four["description"].append(description)

  image = driver.find_element(By.XPATH, "//*[@id='product-images-large']/div[1]/div[1]/img").get_attribute('src')
  leds_see_four["image_url"].append(image)
  
  unique_id = driver.find_element(By.XPATH, "//*[@id='col-product-info']/div[1]/div[3]/div/span").text
  leds_see_four["unique_id"].append(unique_id)
  
  manufacturer_id = 598
  leds_see_four["manufacturer_id"].append(manufacturer_id)
  
led_data = pd.DataFrame(leds_see_four).to_csv('ledsC4_csv.csv', index=False)
driver.close() 
