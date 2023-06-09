from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas')

products = []

for product in driver.find_elements(by=By.CSS_SELECTOR,value='.product-tile-v2'):
   
    price = product.find_element(by=By.CSS_SELECTOR,value='.primary').text
    title =product.find_element(by=By.CSS_SELECTOR,value='.product-tile-title').text
    products.append({'title':title,'price':price})

print(products)

driver.quit()
