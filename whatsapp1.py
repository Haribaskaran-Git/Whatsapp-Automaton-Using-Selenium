from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/Hari/AppData/Local/Google/Chrome/User Data")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome('chromedriver.exe',chrome_options=options)
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,100)

target='"Bhadrinarayanan"'
message="h"
number_of_times=5 #No. of times to send a message

contact_path='//span[contains(@title,'+ target +')]'
contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
contact.click()
message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
for x in range(number_of_times):
    message_box.send_keys(message + Keys.ENTER)
    time.sleep(0.2)