# -*- coding: utf-8 -*-
"""
Created on Fri Dec 01 10:37:25 2017

@author: hp
"""


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
 
 
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

zipcode_df = pd.read_csv('D:\shaw_flooring\us_postal_codes.csv',
                      usecols=["Zip Code"])


 
'''
def lookup(driver, query):
    driver.get("http://www.google.com")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "btnK")))
        box.send_keys(query)
        button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")
'''


if __name__ == "__main__":
    driver = init_driver()
    driver.get("https://shawfloors.com/stores")
    time.sleep(5)

    Store=[]
    Address=[]
    City_state_zip=[]
    phone=[]
    Category=[]

    box = driver.find_element_by_css_selector(".filter:nth-child(4) .vertically-centered")
    box.click()
    box2 = driver.find_element_by_css_selector(".distance-filter div:nth-child(6)")
    box2.click()

    box3 = driver.find_element_by_css_selector(":nth-child(6) .vertically-centered")
    box3.click()
    box4 = driver.find_element_by_css_selector(".features-filter div:nth-child(1)")
    box4.click()

    for index, row in zipcode_df.iterrows():
        print row["Zip Code"]
        pincode = int(row["Zip Code"])

        box5 = driver.find_element_by_css_selector("#store-locator--find-retailer")
        box5.clear()
        box5.send_keys(pincode)
        box5.send_keys(u'\ue007')

        time.sleep(5)



        box6 = driver.find_elements_by_css_selector(".view-more-retailers")

        if len(box6) >0 and box6[0].is_displayed():
            box6[0].click()

        box7 = driver.find_elements_by_css_selector("span:nth-child(1) a")
        box9 = driver.find_elements_by_css_selector(".address")
        box10 = driver.find_elements_by_css_selector(".city-state-zip")
        box11 = driver.find_elements_by_css_selector(".phone")
        box8 = driver.find_elements_by_css_selector(".retailer-detail-template img")
        

        for x in range(len(box7)):
            Store.append(box7[x].text)
            Address.append(box9[x].text)
            City_state_zip.append(box10[x].text)
            phone.append(box11[x].text)
            Category.append(box8[x].get_attribute("src"))
            
                    
        time.sleep(5)            
   

    df = pandas.DataFrame(data={"Store": Store, "Address": Address,
                                "City_state_zip": City_state_zip, "phone": phone,
                                "Category":Category})
    
    df.to_csv("D:/shaw_flooring/file.csv", sep=',',index=False)
    
    





'''
    driver.quit()
'''
