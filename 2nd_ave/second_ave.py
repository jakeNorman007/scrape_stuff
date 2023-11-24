from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#CANNOT BE HEADLESS ON A CONTINUOUS SCROLL!!!
options = Options()
# options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://2ndave.com/shop/')
time.sleep(2)

chunk_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk2_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk3_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk4_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk5_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk6_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk7_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk8_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
chunk9_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

# the following block of code uses JS within selenium, in the console so I can obtain the screen height. Scrolls one screen length at a time. Once selenium reaches the bottom of the page it triggers enough time to allow the next chunk of screen to load. This will keep scrolling until the page reaches the bottom and stops.

scroll_pause_time = 6
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while True:
  driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
  i += 1
  time.sleep(scroll_pause_time)
  scroll_height = driver.execute_script("return document.body.scrollHeight;")
  if (screen_height) * i > scroll_height:
    break

second_ave_product_urls = []
second_ave_products = driver.find_elements(By.XPATH, ".//*[@class='post-image product-image']/a")

for second_links in second_ave_products:
  product_links = second_links.get_attribute('href')
  second_ave_product_urls.append(product_links)

# destructures the main array into 9 smaller arrays so we can try to iterate 500 products at a time
# this solves the issue
chunk, chunk2, chunk3, chunk4, chunk5, chunk6, chunk7, chunk8, chunk9 = [second_ave_product_urls[x:x+500] for x in range(0, len(second_ave_product_urls), 500)]

for i in chunk:
  driver.get(i)
  time.sleep(2)
  url = driver.current_url
  chunk_data["link_url"].append(url)
  
  name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
  chunk_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//div[@class='product-description']/p").text
    chunk_data["description"].append(description)
  except:
    description = "no description available."
    chunk_data["description"].append(description)
  
  image = driver.find_element(By.XPATH, "//li[@class='woocommerce-product-gallery__image flex-active-slide']/a").get_attribute('href')
  chunk_data["image_url"].append(image)

  manufacturer_id = 1261
  chunk_data["manufacturer_id"].append(manufacturer_id)

second_one = pd.DataFrame(chunk_data).to_csv('second_ave_one.csv', index=False)

for i in chunk2:
  driver.get(i)
  time.sleep(2)
  url = driver.current_url
  chunk2_data["link_url"].append(url)
  
  name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
  chunk2_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//div[@class='product-description']/p").text
    chunk2_data["description"].append(description)
  except:
    description = "no description available."
    chunk2_data["description"].append(description)
  
  image = driver.find_element(By.XPATH, "//li[@class='woocommerce-product-gallery__image flex-active-slide']/a").get_attribute('href')
  chunk2_data["image_url"].append(image)

  manufacturer_id = 1261
  chunk2_data["manufacturer_id"].append(manufacturer_id)

second_two = pd.DataFrame(chunk2_data).to_csv('second_ave_two.csv', index=False)

for i in chunk3:
  driver.get(i)
  time.sleep(2)
  url = driver.current_url
  chunk3_data["link_url"].append(url)
  
  name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
  chunk3_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//div[@class='product-description']/p").text
    chunk3_data["description"].append(description)
  except:
    description = "no description available."
    chunk3_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//li[@class='woocommerce-product-gallery__image flex-active-slide']/a").get_attribute('href')
    chunk3_data["image_url"].append(image)
  except:
    image = "no image available."
    chunk3_data["image_url"].append(image)

  manufacturer_id = 1261
  chunk3_data["manufacturer_id"].append(manufacturer_id)

second_three = pd.DataFrame(chunk3_data).to_csv('second_ave_three.csv', index=False)

for i in chunk4:
  driver.get(i)
  time.sleep(2)
  url = driver.current_url
  chunk4_data["link_url"].append(url)
  
  name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
  chunk4_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//div[@class='product-description']/p").text
    chunk4_data["description"].append(description)
  except:
    description = "no description available."
    chunk4_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//li[@class='woocommerce-product-gallery__image flex-active-slide']/a").get_attribute('href')
    chunk4_data["image_url"].append(image)
  except:
    image = "no image available."
    chunk4_data["image_url"].append(image)
  
  manufacturer_id = 1261
  chunk4_data["manufacturer_id"].append(manufacturer_id)

second_four = pd.DataFrame(chunk4_data).to_csv('second_ave_four.csv', index=False)

for i in chunk5:
  driver.get(i)
  time.sleep(2)
  url = driver.current_url
  chunk5_data["link_url"].append(url)
  
  name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
  chunk5_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//div[@class='product-description']/p").text
    chunk5_data["description"].append(description)
  except:
    description = "no description available."
    chunk5_data["description"].append(description)
  
  image = driver.find_element(By.XPATH, "//li[@class='woocommerce-product-gallery__image flex-active-slide']/a").get_attribute('href')
  chunk5_data["image_url"].append(image)

  manufacturer_id = 1261
  chunk5_data["manufacturer_id"].append(manufacturer_id)

second_five = pd.DataFrame(chunk5_data).to_csv('second_ave_five.csv', index=False)

for i in chunk6:
  driver.get(i)
  time.sleep(2)
  url = driver.current_url
  chunk6_data["link_url"].append(url)
  
  name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
  chunk6_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//div[@class='product-description']/p").text
    chunk6_data["description"].append(description)
  except:
    description = "no description available."
    chunk6_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//li[@class='woocommerce-product-gallery__image flex-active-slide']/a").get_attribute('href')
    chunk6_data["image_url"].append(image)
  except:
    image = "no image available."
    chunk6_data["image_url"].append(image)

  manufacturer_id = 1261
  chunk6_data["manufacturer_id"].append(manufacturer_id)

second_six = pd.DataFrame(chunk6_data).to_csv('second_ave_six.csv', index=False)

for i in chunk7:
  driver.get(i)
  time.sleep(2)
  url = driver.current_url
  chunk7_data["link_url"].append(url)
  
  name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
  chunk7_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//div[@class='product-description']/p").text
    chunk7_data["description"].append(description)
  except:
    description = "no description available."
    chunk7_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//li[@class='woocommerce-product-gallery__image flex-active-slide']/a").get_attribute('href')
    chunk7_data["image_url"].append(image)
  except:
    image = "no image available."
    chunk7_data["image_url"].append(image)

  manufacturer_id = 1261
  chunk7_data["manufacturer_id"].append(manufacturer_id)

second_seven = pd.DataFrame(chunk7_data).to_csv('second_ave_seven.csv', index=False)

for i in chunk8:
  driver.get(i)
  time.sleep(2)
  url = driver.current_url
  chunk8_data["link_url"].append(url)
  
  name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
  chunk8_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//div[@class='product-description']/p").text
    chunk8_data["description"].append(description)
  except:
    description = "no description available."
    chunk8_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//li[@class='woocommerce-product-gallery__image flex-active-slide']/a").get_attribute('href')
    chunk8_data["image_url"].append(image)
  except:
    image = "no image available."
    chunk8_data["image_url"].append(image)

  manufacturer_id = 1261
  chunk8_data["manufacturer_id"].append(manufacturer_id)

second_eight= pd.DataFrame(chunk8_data).to_csv('second_ave_eight.csv', index=False)

for i in chunk9:
  driver.get(i)
  time.sleep(2)
  url = driver.current_url
  chunk9_data["link_url"].append(url)
  
  name = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text
  chunk9_data["name"].append(name)

  try:
    description = driver.find_element(By.XPATH, "//div[@class='product-description']/p").text
    chunk9_data["description"].append(description)
  except:
    description = "no description available."
    chunk9_data["description"].append(description)
  
  try:
    image = driver.find_element(By.XPATH, "//li[@class='woocommerce-product-gallery__image flex-active-slide']/a").get_attribute('href')
    chunk9_data["image_url"].append(image)
  except:
    image = "no image available."
    chunk9_data["image_url"].append(image)

  manufacturer_id = 1261
  chunk9_data["manufacturer_id"].append(manufacturer_id)

second_nine= pd.DataFrame(chunk9_data).to_csv('second_ave_nine.csv', index=False)

driver.close()