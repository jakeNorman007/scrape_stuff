from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

studio = {"name": [], "description": [], "link_url": [], "image_url": [], "unique_id": [], "manufacturer_id": []}

driver.get("https://www.studiomlighting.com/indoor-lighting/collections/ceiling" )

scroll_pause_time = 6
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while True:
  driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
  i += 1
  time.sleep(scroll_pause_time)
  scroll_height = driver.execute_script("return document.body.scrollHeight;")
  try:
      driver.find_element(By.XPATH, "//div[@class='col-xs-12']/a").click()
  except:
      if (screen_height) * i > scroll_height:
        break

studio_ceiling_collection_urls =[]
studio_ceiling_collections = driver.find_elements(By.XPATH, ".//div[@class='pdf-thumb-box divProduct']/a")

for x in studio_ceiling_collections:
    product_url = x.get_attribute('href')
    studio_ceiling_collection_urls.append(product_url)

for product in studio_ceiling_collection_urls:
    driver.get(product)
    studio_product_urls = []
    studio_ceiling_collections = driver.find_elements(By.XPATH, ".//div[@class='pdf-thumb-box divProduct']/a")

    for foo in studio_ceiling_collections:
        url = foo.get_attribute('href')
        studio_product_urls.append(url)
        studio["link_url"].append(url)
        
    for bar in studio_product_urls:
        driver.get(bar)

        try:
            name_one = driver.find_element(By.XPATH, "//*[@id='tab-1']/div/div[2]/div/table/tbody/tr[2]/td/span").text
            name_two = driver.find_element(By.XPATH, "//*[@id='tab-1']/div/div[2]/div/table/tbody/tr[1]/td/span").text
            name = name_one + " " + name_two
            studio["name"].append(name)
        except:
            name = "no name available"
            studio["name"].append(name)

        try:
            description = driver.find_element(By.XPATH, "//*[@id='divProdDesc']").text
            studio["description"].append(description)
        except:
            description = "no description available"
            studio["description"].append(description)

        try:
            image = driver.find_element(By.XPATH, "//*[@id='tab-1']/div/div[3]/div[2]/a[2]/img").get_attribute('src')
            studio["image_url"].append(image)
        except:
            image = "no image available"
            studio["image_url"].append(image)

        try:
            unique_id = driver.find_element(By.XPATH, "//*[@id='Span1']").text
            studio["unique_id"].append(unique_id)
        except:
            unique_id = "no id available"
            studio["unique_id"].append(unique_id)

        manufacturer_id = 1113
        studio["manufacturer_id"].append(manufacturer_id)

studio_data = pd.DataFrame(studio).to_csv("ceiling_csv.csv", index=False)
