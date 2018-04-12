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

#create a new title
admin_btn = browser.find_element_by_xpath('/html/body/header/div/nav/ul/li[1]/a').click()
title_btn = browser.find_element_by_xpath('/html/body/header/div/nav/ul/li[1]/ul/li/a[2]').click()
new_title_btn = browser.find_element_by_xpath('//*[@id="content"]/a').click()
title_name_field = browser.find_element_by_id('title_name').send_keys('NewTitle-BET')
create_title_btn = browser.find_element_by_name('commit').click()

#Validates whether the title has been created or not

if browser.find_element_by_xpath('//*[@id="content"]/div'):
    print('Title Created')
if browser.find_element_by_xpath('//*[@id="content"]/div/ul/li'):
    print('Title already created')




