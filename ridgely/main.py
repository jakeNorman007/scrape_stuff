from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

ridgely_data = {"name": [], "description": [], "link_url": [], "image_url": [], "manufacturer_id": []}

for i in range(1, 7):
    url = "https://www.ridgelystudioworks.com/collections/all"
    url2 = url + f"?page={i}"
    driver.get(url2)

    ridgely_product_urls = []
    product_link = driver.find_elements(By.XPATH, ".//div[@class='collection-products rows-of-4']/article/figure/a")
    for foo in product_link:
        bar = foo.get_attribute('href')
        ridgely_product_urls.append(bar)
        ridgely_data["link_url"].append(bar)

    for link in ridgely_product_urls:
        driver.get(link)
        try:
            name = driver.find_element(By.XPATH, "//h1[@class='product-title']").text
            ridgely_data["name"].append(name)
        except:
            name = "no name available"
            ridgely_data["name"].append(name)
        try:
            description = driver.find_element(By.XPATH, "//div[@class='product-description rte']/p[1]").text
            ridgely_data["description"].append(description)
        except:
            description = "no description available"
            ridgely_data["description"].append(description)
        try:
            image = driver.find_element(By.XPATH, "//div[@class='product-gallery--media-wrapper']/img").get_attribute("src")
            ridgely_data["image_url"].append(image)
        except:
            image = "no image available"
            ridgely_data["image_url"].append(image)

        manufacturer_id = 3180
        ridgely_data["manufacturer_id"].append(manufacturer_id)

ridgely_final = pd.DataFrame(ridgely_data).to_csv("ridgely_csv.csv", index=False)
driver.close()
