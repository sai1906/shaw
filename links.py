

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException 


import pandas
import pandas as pd
import numpy as np
import pickle

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

if __name__ == "__main__":

    links=[]
    alphabets=map(chr, range(97, 123))
    link ="https://shawfloors.com/stores/storelist?letter="
    driver = init_driver()

    for i in alphabets:    
        
        driver.get(link+i)
        
        time.sleep(3)
        box = driver.find_elements_by_css_selector("#dealerList a")

        for x in box:
            links.append(x.get_attribute('href'))
            
        time.sleep(3)

    df = pandas.DataFrame(data={"links":links})
    df.to_csv("D:/shaw_flooring/links.csv", sep=',',index=False)

'''
class - financing
css_selectors - #p_lt_ctl03_pageplaceholder_p_lt_ctl01_RetailerProfile_BadgeImage , #p_lt_ctl03_pageplaceholder_p_lt_ctl01_RetailerProfile_PhoneLink, .info span
for image use get_attribute("src")
'''



