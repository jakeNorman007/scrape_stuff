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

driver.get('https://visionairelighting.com/product-families/oden-collection/')

oden_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

try:
  alert = driver.switch_to.alert
  alert_text = alert.text
  alert.accept()
except:
  pass

oden_links = []
products = driver.find_elements(By. XPATH,".//*[@class='et_pb_portfolio_grid_items']/div/a")
product_names = driver.find_elements(By.XPATH, ".//*[@class='et_pb_module_header']")

for n in product_names:
  foo = n.text
  oden_data["name"].append(foo)
  
for p in products:
  product_link = p.get_attribute('href')
  oden_links.append(product_link)
  oden_data["link_url"].append(product_link)
  
for url in oden_links:
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
  
  oden_data["image_url"].append(all_pics)
  
  try:
    description = driver.find_element(By.XPATH, "//*[@class='et_pb_text_inner']/p[2]").text
    oden_data["description"].append(description)
  except:
    print("no description available")
    description = "no description available"
    oden_data["description"].append(description)
    
  manufacturer_id = 159
  oden_data["manufacturer_id"].append(manufacturer_id)
    
oden_data = pd.DataFrame(oden_data)
oden_data.to_csv("oden_csv.csv", index=False)

driver.close()