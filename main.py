import time

from selenium import webdriver


driver = webdriver.Chrome('/Users/andrejusycenko/chromedriver/chromedriver1')  # Enter your path to the driver

driver.get('https://ya.ru/')

time.sleep(3)

driver.get('https://duckduckgo.com/')

time.sleep(3) 

search_box = driver.find_element_by_name('q')

search_box.send_keys('Это что, автоматизация какая-то ? ')

search_box.submit()

time.sleep(3)

driver.get('https://ya.ru/')

time.sleep(3)

search_box = driver.find_element_by_id('text')

search_box.send_keys('похоже на то')

search_box.submit()

time.sleep(5)

driver.quit()
