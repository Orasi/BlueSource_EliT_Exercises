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

#edit a title
admin_btn = browser.find_element_by_xpath('/html/body/header/div/nav/ul/li[1]/a').click()
title_btn = browser.find_element_by_xpath('/html/body/header/div/nav/ul/li[1]/ul/li/a[2]').click()
pencil_icon = browser.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[68]/td/div/a[1]').click()
name_field = browser.find_element_by_id('title_name').send_keys('99')
update_title_btn = browser.find_element_by_name('commit').click()

#Assets whether the Title was updated or not

if browser.find_element_by_xpath('//*[@id="content"]/div'):
    print('Title Updated Successfully')
else:
    print('Title NOT Updated')
