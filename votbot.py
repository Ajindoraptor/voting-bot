import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chromedriver)

link = 'https://docs.google.com/forms/d/e/1FAIpQLSdgSLozEfmb5gKE8d_hyxBVRiXpvuFFUXdTVlPOVuRLfDxySg/viewform'
driver.get(link)

x_p = ''
sumbit_xp = ''

count = 0

while(count < 25):
    d = driver.find_element_by_xpath(x_p)
    d.click()
    time.sleep(0.5)
    sumbit = driver.find_element_by_xpath(sumbit_xp)
    sumbit.click()
    count = count + 1
    driver.get(link)
