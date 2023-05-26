# -*- coding: utf-8 -*-

import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent

#xt0psk2 Very usefull class
#x1xzczws Very usefull class
# inputtext _55r1 _6luy
# email
# email
# _6lux
# _8esj _95k9 _8esf _8opv _8f3m _8ilg _8icx _8op_ _95ka
useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument(f'user-argent={useragent.random}')
driver = webdriver.Chrome(r'C:\Users\den-s\OneDrive\Desktop\selenium\chromedriver',options=options)
driver.maximize_window()
try:
    # driver.get("https://www.facebook.com/")
    # email = driver.find_element(By.ID,'email')
    # email.clear()
    # email.send_keys('denissuhart1@gmail.com')
    # password = driver.find_element(By.ID,'pass')
    # password.clear()
    # password.send_keys('Ddenis1737')
    # email = driver.find_element(By.NAME,'login').click()
    # time.sleep(1)
    # pickle.dump(driver.get_cookies(),open('cookies','wb'))
  
   
    driver.get("https://www.facebook.com/groups/708481315831119?sorting_setting=CHRONOLOGICAL")
    for cookie in pickle.load(open('cookies','rb')):
            driver.add_cookie(cookie)
    driver.refresh()
  

    x = 1
    while True:
            x+=1
            searching_element = driver.find_elements(By.LINK_TEXT,'1 д.')
            moving_elements = driver.find_elements(By.CLASS_NAME,'x1xzczws')
            time.sleep(1)

            if len(searching_element) == 0:
                action = ActionChains(driver)
                action.move_to_element(moving_elements[-2]).perform()
                print(f'{x}: scroll')
                time.sleep(1)
            else:
                print('Success')
                resp = driver.page_source
                with open('xxx.html','w',encoding = 'utf-8') as file:
                    file.write(resp)
                time.sleep(1)
                break
       

    # # element1s = driver.find_elements(By.CLASS_NAME,'inputtext _55r1 _6luy')
    # # element2s = driver.find_elements(By.ID,'email')
    # # element3s = driver.find_elements(By.NAME,'email')
    # # element4s = driver.find_elements(By.CLASS_NAME,'_6lux')
    # # element5s = driver.find_elements(By.CLASS_NAME,'_8esj _95k9 _8esf _8opv _8f3m _8ilg _8icx _8op_ _95ka')
    # # print(f' class {len(element1s)}')
    # # print( f' id {len(element2s)}')
    # # print( f' name {len(element3s)}')
    # # print( f' class {len(element4s)}')
    # # print( f' class {len(element5s)}')
   
 
    # # print(type(element))
    # # resp = driver.page_source
    # # with open('xxx.html','w',encoding = 'utf-8') as file:
    # #     file.write(resp)
    
    # # soup=BeautifulSoup(resp,'html.parser')
    # # items = soup.find_all('a',{'class':'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1xlr1w8'})
    # # for i in items:
    # #     print(i.text)







except Exception as ex:
    print(ex)
    # print(ex)
finally:
    driver.close()
    driver.quit()

