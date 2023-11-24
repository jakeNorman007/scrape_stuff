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

driver.get('https://visionairelighting.com/product-families/v-collection/')

v_collection_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

try:
  alert = driver.switch_to.alert
  alert_text = alert.text
  alert.accept()
except:
  pass

v_collection_links = []
products = driver.find_elements(By. XPATH,".//*[@class='et_pb_portfolio_grid_items']/div/a")
product_names = driver.find_elements(By.XPATH, ".//*[@class='et_pb_module_header']")

for n in product_names:
  foo = n.text
  v_collection_data["name"].append(foo)
  
for p in products:
  product_link = p.get_attribute('href')
  v_collection_links.append(product_link)
  v_collection_data["link_url"].append(product_link)
  
for url in v_collection_links:
  driver.get(url)

  try:
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
  except:
    pass
  
  all_pics = []
  pictures = driver.find_elements(By.XPATH, ".//div[@class='et_pb_gallery_image landscape']/a")
  
  for p in pictures:
    pic_ref = p.get_attribute('href')
    all_pics.append(pic_ref)
  
  v_collection_data["image_url"].append(all_pics)
 
  try:
    description = driver.find_element(By.XPATH, "//*[@class='et_pb_text_inner']/p[2]").text
    v_collection_data["description"].append(description)
  except:
    print("no description available")
    description = "no description available"
    v_collection_data["description"].append(description)

  manufacturer_id = 159
  v_collection_data["manufacturer_id"].append(manufacturer_id)
    
v_data = pd.DataFrame(v_collection_data)
v_data.to_csv("v_collection_csv.csv", index=False)

print(v_collection_data)
driver.close()