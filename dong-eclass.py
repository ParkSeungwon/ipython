
# coding: utf-8

# In[4]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

drv = webdriver.Firefox()
drv.get('https://eclass.dongguk.edu')
delay = 20
main_frame = WebDriverWait(drv, delay).until(lambda x : x.find_element_by_xpath("//frame[@name='main']"))
drv.switch_to_frame(main_frame)
WebDriverWait(drv, delay).until(lambda x : x.find_element_by_partial_link_text('학생')).click()

id = drv.find_element_by_id('id')
id.clear()
id.send_keys('2016110056')

pw = drv.find_element_by_id('pw')
pw.clear()
pw.send_keys('cockcodk0_')
pw.send_keys(Keys.RETURN)

WebDriverWait(drv, delay).until(lambda x: x.find_element_by_id('layerPopup')).send_keys(Keys.ESCAPE)
drv.find_element_by_xpath('//button[contains(@onclick,"박미화")]').click()
WebDriverWait(drv, delay).until(lambda x: x.find_element_by_xpath("//ul[@id='leftMenu']/li[4]")).click()
WebDriverWait(drv, delay).until(lambda x: x.find_element_by_link_text('과제')).click()

