from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://eclass.dongguk.edu')
driver.switch_to_frame('main')
time.sleep(1)
driver.find_element_by_id('userId').send_keys('2016110056')
driver.find_element_by_id('password').send_keys('cockcodk0_')
driver.find_element_by_class_name('btn_login').click()
driver.close()
