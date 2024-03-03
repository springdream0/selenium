
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

chrome_driver_file = 'chromedriver.exe'
service = Service(executable_path = os.chmod(chrome_driver_file, 0o755) )  
chrome_options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(
                service = service ,                
                options = chrome_options
            )     

driver.get('https://www.naver.com/')

time.sleep(5)  

element_value = driver.find_element("xpath", '//*[@id="query"]')
 
element_value.send_keys('ChromeDriver')

time.sleep(3) 

element_value.submit()

time.sleep(15)  

driver.quit()
 