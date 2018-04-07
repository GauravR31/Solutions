from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "gauravramnani007@gmail.com"
password = "Incorrect"

browser = webdriver.Chrome()
browser.get(("https://facebook.com"))

browser.implicitly_wait(5)

username_field = browser.find_element_by_id('email')
print username_field
username_field.send_keys(username)

password_field = browser.find_element_by_id('pass')
print password_field
password_field.send_keys(password)

login_button = browser.find_element_by_id('loginbutton')
login_button.click()