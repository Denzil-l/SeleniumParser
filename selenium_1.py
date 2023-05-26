from selenium import webdriver
import time
url ='https://www.instagram.com/'
driver = webdriver.Chrome('C:/Users/den-s/OneDrive/Desktop/selenium/chromedriver')


try:
    driver.get(url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()