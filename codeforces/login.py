from selenium import webdriver
from getpass import getpass

handle = input('Handle: ')
pwd = getpass('Password: ')

driver = webdriver.Firefox()
driver.get('http://codeforces.com/enter')

handle_box = driver.find_element_by_id('handle')
handle_box.send_keys(handle)

password_box = driver.find_element_by_id('password')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_class_name('submit')
login_btn.submit()
