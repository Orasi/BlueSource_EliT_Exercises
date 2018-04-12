from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select


#Create Webdriver
browser = webdriver.Chrome()
browser.get("http://bluesourcestaging.herokuapp.com/login")

#Login into BlueSource
username = browser.find_element_by_id("employee_username")
password = browser.find_element_by_id("employee_password")
username.send_keys("company.admin")
password.send_keys("1234")
login = browser.find_element_by_xpath('//*[@id="new_employee"]/div[2]/div[3]/input')
login.click()

if browser.find_element_by_name('button'):
     print('Successfully Logged in')
else:
    print('Failed Login')

#Deleting an existing title

admin_btn = browser.find_element_by_xpath('/html/body/header/div/nav/ul/li[1]/a').click()
title_btn = browser.find_element_by_xpath('/html/body/header/div/nav/ul/li[1]/ul/li/a[2]').click()
delete_title_icon = browser.find_element_by_css_selector('#content > table > tbody > tr:nth-child(72) > td > div > a:nth-child(2)').click()


#Alert prompt window

alert = browser.switch_to_alert()
alert.accept()
print('Prompt window displayed')

if browser.find_element_by_xpath('//*[@id="content"]/div'):
    print('Deletion successful')
else:
    print('Deletion unsuccessful')
