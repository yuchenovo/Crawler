import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
path = 'msedgedriver.exe'

driver = webdriver.Edge(path)
Options.set_capability()
url = 'https://www.baidu.com/'

driver.get(url)

time.sleep(2)

input = driver.find_element(By.ID, 'kw')

input.send_keys('周杰伦')

time.sleep(2)

button = driver.find_element(By.ID, 'su')

button.click()

time.sleep(2)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

time.sleep(2)

next = driver.find_element(By.CLASS_NAME, 'n')

next.click()

time.sleep(2)

driver.forward()

time.sleep(2)

driver.quit()