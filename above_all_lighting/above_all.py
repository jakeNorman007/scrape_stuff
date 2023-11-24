from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver)

driver.get('https://www.abovealllighting.com/')

above_all_dict = {"name": [], "description": [], "link_url": [], "image_url": []}

# outdoor hover click
outdoor_products = driver.find_element(By.XPATH, "//*[@id='nav_pro']")
outdoor_products_dropdown = driver.find_element(By.XPATH, "//*[@id='nav_pro_con']/div/div[1]/a[1]")
actions.move_to_element(outdoor_products).perform()
actions.move_to_element(outdoor_products_dropdown).click().perform()

# outdoor links
outdoor_lights_urls =[]
outdoor_lighing_products = driver.find_elements(By.XPATH, ".//*[@class='market_list']/a")

for outdoor_lights in outdoor_lighing_products:
  outdoor_link_url = outdoor_lights.get_attribute('href')
  outdoor_lights_urls.append(outdoor_link_url)
  image_url = driver.find_element(By.XPATH, "//div[@class='market_list']/a/div/img").get_attribute("src")
  above_all_dict["link_url"].append(outdoor_link_url)
  above_all_dict["image_url"].append(image_url)
  
for url in outdoor_lights_urls:
  driver.get(url)
  name = driver.find_element(By.XPATH, "//h2[@class='tit']").text
  description = driver.find_element(By.XPATH, "//p[@class='tit']").text
  above_all_dict["name"].append(name)
  above_all_dict["description"].append(description)
    
# link to indoor products, hover was weird so I used the footer links
indoor = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/div[1]/div/div/div[2]/p[2]/a").click()

# indoor links
indoor_lights_urls =[]
indoor_lighing_products = driver.find_elements(By.XPATH, ".//*[@class='market_list']/a")

for indoor_lights in indoor_lighing_products:
  indoor_link_url = indoor_lights.get_attribute('href')
  indoor_lights_urls.append(indoor_link_url)
  image_url = driver.find_element(By.XPATH, "//div[@class='img_out']/img").get_attribute('src')
  above_all_dict["link_url"].append(indoor_link_url)
  above_all_dict["image_url"].append(image_url)
  
for url in indoor_lights_urls:
  driver.get(url)
  name = driver.find_element(By.XPATH, "//h2[@class='tit']").text
  description = driver.find_element(By.XPATH, "//p[@class='tit']").text
  above_all_dict["name"].append(name)
  above_all_dict["description"].append(description)

# controls config, holy shit what a pain in the ass this was. But it works.
controls = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/div[1]/div/div/div[2]/p[3]/a").click()
controls_urls_nlc = []

nlc = driver.find_element(By.XPATH, "/html/body/section/section/div/div/div[1]/div/div/div/ul/li[1]/dl/dd[2]/a").click()

controls_products = driver.find_elements(By.XPATH, ".//*[@class='market_list']/a")

for controls in controls_products:
  control_link_url = controls.get_attribute('href')
  controls_urls_nlc.append(control_link_url)
  image_url = driver.find_element(By.XPATH, "//div[@class='img_out']/img").get_attribute('src')
  above_all_dict["link_url"].append(control_link_url)
  above_all_dict["image_url"].append(image_url)
  
for url in controls_urls_nlc:
    driver.get(url)
    name = driver.find_element(By.XPATH, "//h2[@class='tit']").text
    description = driver.find_element(By.XPATH, "//p[@class='tit']").text
    above_all_dict["name"].append(name)
    above_all_dict["description"].append(description)

controls = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/div[1]/div/div/div[2]/p[3]/a").click()
controls_urls_wsc = []

wcs = driver.find_element(By.XPATH, "/html/body/section/section/div/div/div[1]/div/div/div/ul/li[1]/dl/dd[3]/a").click()

controls_products = driver.find_elements(By.XPATH, ".//*[@class='market_list']/a")

for controls in controls_products:
  control_link_url = controls.get_attribute('href')
  controls_urls_wsc.append(control_link_url)
  image_url = driver.find_element(By.XPATH, "//div[@class='img_out']/img").get_attribute('src')
  above_all_dict["link_url"].append(control_link_url)
  above_all_dict["image_url"].append(image_url)
  
for url in controls_urls_wsc:
    driver.get(url)
    name = driver.find_element(By.XPATH, "//h2[@class='tit']").text
    description = driver.find_element(By.XPATH, "//p[@class='tit']").text
    above_all_dict["name"].append(name)
    above_all_dict["description"].append(description)

controls = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/div[1]/div/div/div[2]/p[3]/a").click()
controls_urls_lcs = []

lcs = driver.find_element(By.XPATH, "/html/body/section/section/div/div/div[1]/div/div/div/ul/li[1]/dl/dd[4]/a").click()

controls_products = driver.find_elements(By.XPATH, ".//*[@class='market_list']/a")

for controls in controls_products:
  control_link_url = controls.get_attribute('href')
  controls_urls_lcs.append(control_link_url)
  image_url = driver.find_element(By.XPATH, "//div[@class='img_out']/img").get_attribute('src')
  above_all_dict["link_url"].append(control_link_url)
  above_all_dict["image_url"].append(image_url)
  
for url in controls_urls_lcs:
    driver.get(url)
    name = driver.find_element(By.XPATH, "//h2[@class='tit']").text
    description = driver.find_element(By.XPATH, "//p[@class='tit']").text
    above_all_dict["name"].append(name)
    above_all_dict["description"].append(description)
 
controls = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/div[1]/div/div/div[2]/p[3]/a").click()
controls_urls_hcls = []

hcls = driver.find_element(By.XPATH, "/html/body/section/section/div/div/div[1]/div/div/div/ul/li[1]/dl/dd[5]/a").click()

controls_products = driver.find_elements(By.XPATH, ".//*[@class='market_list']/a")

for controls in controls_products:
  control_link_url = controls.get_attribute('href')
  controls_urls_hcls.append(control_link_url)
  image_url = driver.find_element(By.XPATH, "//div[@class='img_out']/img").get_attribute('src')
  above_all_dict["link_url"].append(control_link_url)
  above_all_dict["image_url"].append(image_url)
  
for url in controls_urls_hcls:
    driver.get(url)
    name = driver.find_element(By.XPATH, "//h2[@class='tit']").text
    description = driver.find_element(By.XPATH, "//p[@class='tit']").text
    above_all_dict["name"].append(name)
    above_all_dict["description"].append(description)
 
controls = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/div[1]/div/div/div[2]/p[3]/a").click()
controls_urls_etcs = []

etcs = driver.find_element(By.XPATH, "/html/body/section/section/div/div/div[1]/div/div/div/ul/li[1]/dl/dd[6]/a").click()

controls_products = driver.find_elements(By.XPATH, ".//*[@class='market_list']/a")

for controls in controls_products:
  control_link_url = controls.get_attribute('href')
  controls_urls_etcs.append(control_link_url)
  image_url = driver.find_element(By.XPATH, "//div[@class='img_out']/img").get_attribute('src')
  above_all_dict["link_url"].append(control_link_url)
  above_all_dict["image_url"].append(image_url)
  
for url in controls_urls_etcs:
    driver.get(url)
    name = driver.find_element(By.XPATH, "//h2[@class='tit']").text
    description = driver.find_element(By.XPATH, "//p[@class='tit']").text
    above_all_dict["name"].append(name)
    above_all_dict["description"].append(description)
 
taa = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/div[1]/div/div/div[2]/p[4]/a").click()

# taa products links
taa_urls =[]
taa_products = driver.find_elements(By.XPATH, ".//*[@class='market_list']/a")

for taas in taa_products:
  taa_link_url = taas.get_attribute('href')
  taa_urls.append(taa_link_url)
  image_url = driver.find_element(By.XPATH, "//div[@class='img_out']/img").get_attribute('src')
  above_all_dict["link_url"].append(taa_link_url)
  above_all_dict["image_url"].append(image_url)

for url in taa_urls:
  driver.get(url)
  name = driver.find_element(By.XPATH, "//h2[@class='tit']").text
  description = driver.find_element(By.XPATH, "//p[@class='tit']").text
  above_all_dict["name"].append(name)
  above_all_dict["description"].append(description)

quick_ship = driver.find_element(By.XPATH, "/html/body/footer/div/div[1]/div[1]/div/div/div[2]/p[5]/a").click()

# quick ship products links
quick_ship_urls =[]
quick_ship_products = driver.find_elements(By.XPATH, ".//*[@class='market_list']/a")

for taas in quick_ship_products:
  quick_ship_link_url = taas.get_attribute('href')
  quick_ship_urls.append(quick_ship_link_url)
  image_url = driver.find_element(By.XPATH, "//div[@class='img_out']/img").get_attribute('src')
  above_all_dict["link_url"].append(quick_ship_link_url)
  above_all_dict["image_url"].append(image_url)

for url in quick_ship_urls:
  driver.get(url)
  name = driver.find_element(By.XPATH, "//h2[@class='tit']").text
  description = driver.find_element(By.XPATH, "//p[@class='tit']").text
  above_all_dict["name"].append(name)
  above_all_dict["description"].append(description)

above_all_data = pd.DataFrame(above_all_dict)
above_all_data.replace('', np.nan)
above_all_data.to_csv('above_all_controls_csv.csv', index=False)

print(above_all_dict)
driver.close()