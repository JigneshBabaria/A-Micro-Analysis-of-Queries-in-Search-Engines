#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome('D:/chromedriver')

url = 'https://in.search.yahoo.com/'

driver.get(url)
search_box = driver.find_element(By.ID,"yschsp")

text_to_search =  'IT companies in Bangalore'

search_box.send_keys(text_to_search)
search_box.send_keys(Keys.RETURN)

pages = 3#no of pages to search
count = 0
while(pages!=count):
	wait = WebDriverWait(driver, 10)
	items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.options-toggle a')))
	for item in items:
	    print(item.text, item.get_attribute('href'))

	button = driver.find_element(By.XPATH,'//a[normalize-space()=' + str(count+2) + ']')
	button.click()
	count+=1

