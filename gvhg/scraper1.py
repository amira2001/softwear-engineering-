from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get('https://woolworths.com.au/')

categories = []

for category in driver.find_elements(by=By.CSS_SELECTOR,value='.offer-tile-item'):
    try:
        title_cat = category.find_element(By.CSS_SELECTOR, value='.offer-tile-header-title').text
    except:
        title_cat = category.find_element(By.CSS_SELECTOR, value='.sr-only').text
    
    lien = category.find_element("tag name", "a")
    lien_cat = lien.get_attribute('href')
    print(title_cat)
    print(lien_cat)
    options = webdriver.ChromeOptions()
    options.add_argument("D:\scrap")
    driver2 = webdriver.Chrome(options=options)
    driver2.get(lien_cat)
    time.sleep(2)
    status_code = driver2.execute_script("return window.performance.getEntries()[0].response.status")

    if status_code == 404:
        print("Erreur 404 - Page non trouvée")
    else:
        for product in driver2.find_elements(by=By.CSS_SELECTOR,value='.product-tile-v2'):
            titre_product = product.find_elements(by=By.CSS_SELECTOR,value='.product-title-link ng-star-inserted').text
            print(titre_product)
    categories.append({'title':title_cat})

print(categories)    
driver.quit()  