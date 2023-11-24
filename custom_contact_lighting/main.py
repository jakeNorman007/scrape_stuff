from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://customcontractlighting.com/product-search/')
time.sleep(5)

chunk_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk2_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk3_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk4_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk5_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk6_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk7_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk8_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk9_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

scroll_pause_time = 4
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while True:
  driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
  i += 1
  time.sleep(scroll_pause_time)
  scroll_height = driver.execute_script("return document.body.scrollHeight;")
  if (screen_height) * i > scroll_height:
    break

custom_contract_product_urls = []
custom_contract_products = driver.find_elements(By.XPATH, ".//a[@class='wpgb-card-layer-link']")

for contract_links in custom_contract_products:
  product_links = contract_links.get_attribute('href')
  custom_contract_product_urls.append(product_links)

chunk, chunk2, chunk3, chunk4, chunk5, chunk6, chunk7, chunk8, chunk9 = [custom_contract_product_urls[x:x+500] for x in range(0, len(custom_contract_product_urls), 500)]

for i in chunk:
  driver.get(i)
  driver.implicitly_wait(5)
  url = driver.current_url
  chunk_data["link_url"].append(url)
  
  try:
    name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
    print(name)
    chunk_data["name"].append(name)
  except:
    name = "no name available"
    print(name)
    chunk_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//table[@class='woocommerce-product-attributes shop_attributes']/tbody/tr").text
    print(description)
    chunk_data["description"].append(description)
  except:
    description = "no description available."
    chunk_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//div[@class='tf_swiper-slide woocommerce-main-image woocommerce-product-gallery__image post-image tf_swiper-slide-active']/img").get_attribute('src')
    print(image)
    chunk_data["image_url"].append(image)
  except:
    image = "no description available."
    chunk_data["image_url"].append(image)


  manufacturer_id = 2521 
  print(manufacturer_id)
  chunk_data["manufacturer_id"].append(manufacturer_id)

contract_one = pd.DataFrame(chunk_data).to_csv('contract_one.csv', index=False)

for i in chunk2:
  driver.get(i)
  driver.implicitly_wait(5)
  url = driver.current_url
  chunk2_data["link_url"].append(url)
  
  try:
    name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
    print(name)
    chunk2_data["name"].append(name)
  except:
    name = "no name available"
    print(name)
    chunk2_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//table[@class='woocommerce-product-attributes shop_attributes']/tbody/tr").text
    print(description)
    chunk2_data["description"].append(description)
  except:
    description = "no description available."
    chunk2_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//div[@class='tf_swiper-slide woocommerce-main-image woocommerce-product-gallery__image post-image tf_swiper-slide-active']/img").get_attribute('src')
    print(image)
    chunk2_data["image_url"].append(image)
  except:
    image = "no description available."
    chunk2_data["image_url"].append(image)

  manufacturer_id = 2521 
  print(manufacturer_id)
  chunk2_data["manufacturer_id"].append(manufacturer_id)

contract_two = pd.DataFrame(chunk2_data).to_csv('contract_two.csv', index=False)

for i in chunk3:
  driver.get(i)
  driver.implicitly_wait(5)
  url = driver.current_url
  chunk3_data["link_url"].append(url)
  
  try:
    name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
    print(name)
    chunk3_data["name"].append(name)
  except:
    name = "no name available"
    print(name)
    chunk3_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//table[@class='woocommerce-product-attributes shop_attributes']/tbody/tr").text
    print(description)
    chunk3_data["description"].append(description)
  except:
    description = "no description available."
    chunk3_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//div[@class='tf_swiper-slide woocommerce-main-image woocommerce-product-gallery__image post-image tf_swiper-slide-active']/img").get_attribute('src')
    print(image)
    chunk3_data["image_url"].append(image)
  except:
    image = "no description available."
    chunk3_data["image_url"].append(image)


  manufacturer_id = 2521 
  print(manufacturer_id)
  chunk3_data["manufacturer_id"].append(manufacturer_id)

contract_three = pd.DataFrame(chunk3_data).to_csv('contract_three.csv', index=False)

for i in chunk4:
  driver.get(i)
  driver.implicitly_wait(5)
  url = driver.current_url
  chunk4_data["link_url"].append(url)
  
  try:
    name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
    print(name)
    chunk4_data["name"].append(name)
  except:
    name = "no name available"
    print(name)
    chunk4_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//table[@class='woocommerce-product-attributes shop_attributes']/tbody/tr").text
    print(description)
    chunk4_data["description"].append(description)
  except:
    description = "no description available."
    chunk4_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//div[@class='tf_swiper-slide woocommerce-main-image woocommerce-product-gallery__image post-image tf_swiper-slide-active']/img").get_attribute('src')
    print(image)
    chunk4_data["image_url"].append(image)
  except:
    image = "no description available."
    chunk4_data["image_url"].append(image)


  manufacturer_id = 2521 
  print(manufacturer_id)
  chunk4_data["manufacturer_id"].append(manufacturer_id)

contract_four = pd.DataFrame(chunk4_data).to_csv('contract_four.csv', index=False)

for i in chunk5:
  driver.get(i)
  driver.implicitly_wait(5)
  url = driver.current_url
  chunk5_data["link_url"].append(url)
  
  try:
    name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
    print(name)
    chunk5_data["name"].append(name)
  except:
    name = "no name available"
    print(name)
    chunk5_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//table[@class='woocommerce-product-attributes shop_attributes']/tbody/tr").text
    print(description)
    chunk5_data["description"].append(description)
  except:
    description = "no description available."
    chunk5_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//div[@class='tf_swiper-slide woocommerce-main-image woocommerce-product-gallery__image post-image tf_swiper-slide-active']/img").get_attribute('src')
    print(image)
    chunk5_data["image_url"].append(image)
  except:
    image = "no description available."
    chunk5_data["image_url"].append(image)


  manufacturer_id = 2521 
  print(manufacturer_id)
  chunk5_data["manufacturer_id"].append(manufacturer_id)

contract_five = pd.DataFrame(chunk5_data).to_csv('contract_five.csv', index=False)

for i in chunk6:
  driver.get(i)
  driver.implicitly_wait(5)
  url = driver.current_url
  chunk6_data["link_url"].append(url)
  
  try:
    name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
    print(name)
    chunk6_data["name"].append(name)
  except:
    name = "no name available"
    print(name)
    chunk6_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//table[@class='woocommerce-product-attributes shop_attributes']/tbody/tr").text
    print(description)
    chunk6_data["description"].append(description)
  except:
    description = "no description available."
    chunk6_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//div[@class='tf_swiper-slide woocommerce-main-image woocommerce-product-gallery__image post-image tf_swiper-slide-active']/img").get_attribute('src')
    print(image)
    chunk6_data["image_url"].append(image)
  except:
    image = "no description available."
    chunk6_data["image_url"].append(image)


  manufacturer_id = 2521 
  print(manufacturer_id)
  chunk6_data["manufacturer_id"].append(manufacturer_id)

contract_six = pd.DataFrame(chunk6_data).to_csv('contract_six.csv', index=False)

for i in chunk7:
  driver.get(i)
  driver.implicitly_wait(5)
  url = driver.current_url
  chunk7_data["link_url"].append(url)
  
  try:
    name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
    print(name)
    chunk7_data["name"].append(name)
  except:
    name = "no name available"
    print(name)
    chunk7_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//table[@class='woocommerce-product-attributes shop_attributes']/tbody/tr").text
    print(description)
    chunk7_data["description"].append(description)
  except:
    description = "no description available."
    chunk7_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//div[@class='tf_swiper-slide woocommerce-main-image woocommerce-product-gallery__image post-image tf_swiper-slide-active']/img").get_attribute('src')
    print(image)
    chunk7_data["image_url"].append(image)
  except:
    image= "no description available."
    chunk7_data["image_url"].append(image)


  manufacturer_id = 2521 
  print(manufacturer_id)
  chunk7_data["manufacturer_id"].append(manufacturer_id)

contract_seven = pd.DataFrame(chunk7_data).to_csv('contract_seven.csv', index=False)

for i in chunk8:
  driver.get(i)
  driver.implicitly_wait(5)
  url = driver.current_url
  chunk8_data["link_url"].append(url)
  
  try:
    name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
    print(name)
    chunk8_data["name"].append(name)
  except:
    name = "no name available"
    print(name)
    chunk8_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//table[@class='woocommerce-product-attributes shop_attributes']/tbody/tr").text
    print(description)
    chunk8_data["description"].append(description)
  except:
    description = "no description available."
    chunk8_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//div[@class='tf_swiper-slide woocommerce-main-image woocommerce-product-gallery__image post-image tf_swiper-slide-active']/img").get_attribute('src')
    print(image)
    chunk8_data["image_url"].append(image)
  except:
    image= "no description available."
    chunk8_data["image_url"].append(image)


  manufacturer_id = 2521 
  print(manufacturer_id)
  chunk8_data["manufacturer_id"].append(manufacturer_id)

contract_eight = pd.DataFrame(chunk8_data).to_csv('contract_eight.csv', index=False)

for i in chunk9:
  driver.get(i)
  driver.implicitly_wait(5)
  url = driver.current_url
  chunk9_data["link_url"].append(url)
  
  try:
    name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
    print(name)
    chunk9_data["name"].append(name)
  except:
    name = "no name available"
    print(name)
    chunk9_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//table[@class='woocommerce-product-attributes shop_attributes']/tbody/tr").text
    print(description)
    chunk9_data["description"].append(description)
  except:
    description = "no description available."
    chunk9_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//div[@class='tf_swiper-slide woocommerce-main-image woocommerce-product-gallery__image post-image tf_swiper-slide-active']/img").get_attribute('src')
    print(image)
    chunk9_data["image_url"].append(image)
  except:
    image= "no description available."
    chunk9_data["image_url"].append(image)


  manufacturer_id = 2521 
  print(manufacturer_id)
  chunk9_data["manufacturer_id"].append(manufacturer_id)

contract_nine = pd.DataFrame(chunk9_data).to_csv('contract_nine.csv', index=False)
driver.quit()
