# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
url ='https://whatmyuseragent.com/#:~:text=Useragent%20is%20a%20small%20piece,ensure%20optimal%20performance%20and%20compatibility'

new_agent = UserAgent()
user_agents =[
    'xxxx','yyyy','zzzz'
]
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={new_agent.random}")

driver = webdriver.Chrome('C:/Users/den-s/OneDrive/Desktop/selenium/chromedriver',options=options)

try:
    driver.get(url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()