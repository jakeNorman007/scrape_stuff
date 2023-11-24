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

driver.get('https://visionairelighting.com/product-families/bow-ii-collection/')

bow_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}
try:
  alert = driver.switch_to.alert
  alert_text = alert.text
  alert.accept()
except:
  pass

bow_links = []
products = driver.find_elements(By. XPATH,".//*[@class='et_pb_portfolio_grid_items']/div/a")
product_names = driver.find_elements(By.XPATH, ".//*[@class='et_pb_module_header']")

for n in product_names:
  foo = n.text
  bow_data["name"].append(foo)
  
for p in products:
  product_link = p.get_attribute('href')
  bow_links.append(product_link)
  bow_data["link_url"].append(product_link)
  
for url in bow_links:
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
   
  bow_data["image_url"].append(all_pics)
  
  try:
    description = driver.find_element(By.XPATH, "//*[@class='et_pb_text_inner']/p[2]").text
    bow_data["description"].append(description)
  except:
    print("no description available")
    description = "no description available"
    bow_data["description"].append(description)
    
  manufacturer_id = 159
  bow_data["manufacturer_id"].append(manufacturer_id)
    
bow_data = pd.DataFrame(bow_data)
bow_data.to_csv("bow_csv.csv", index=False)

driver.close()