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
def reps():
    print("Do you want to send more msg to anyone")
    askUser = input("Press y for Yes and n for No : ")
    if (askUser == 'Y' or askUser == 'y'):
        msg()
    elif (askUser == 'N' or askUser == 'n'):
        print("Thank you see you soon")
    else:
        print("Please Enter Valid option :\n")
        reps()

def msg():
    name = input('\nEnter Group/User Name: ')
    message = input("Enter your message to group/user: ")

    # Find Whom to message     
    try:
        Count = int(input("Enter the message count:"))
        
        user = driver.find_element_by_xpath(
        '//span[@title = "{}"]'.format(name))
        user.click()
    except:
        msg()