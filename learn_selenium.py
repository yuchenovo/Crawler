from selenium import webdriver
from selenium.webdriver.common.by import By

path = 'msedgedriver.exe'

driver = webdriver.Edge(path)

url = 'https://www.baidu.com/'

driver.get(url)

# 获取网页源码
content = driver.page_source
element = driver.find_element(By.ID,'su')
print(element.get_attribute('class'))
print(element.tag_name)
print(element.text)
