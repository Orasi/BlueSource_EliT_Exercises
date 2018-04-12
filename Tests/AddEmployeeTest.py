from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import Select
from time import sleep

#Create Webdriver
driver = webdriver.Chrome()
driver.get("https://bluesourcestaging.herokuapp.com/login")

#Login to bluesource
user_name_field = driver.find_element_by_id("employee_username").send_keys("company.admin")
pass_word_field = driver.find_element_by_id("employee_password").send_keys("123")
login_btn = driver.find_element_by_name("commit").submit()

if driver.find_element_by_name('button'):
     print('Successfully Logged in')
else:
    print('Failed Login')

#Adding a new employee to the Department

add_btn_emp = driver.find_element_by_xpath('//*[@id="all-content"]/div[2]/div/div[2]').click()
sleep(2)

username_emp = driver.find_element_by_xpath('//*[@id="employee_username"]').send_keys('Brian505051')
first_name_emp = driver.find_element_by_xpath('//*[@id="employee_first_name"]').send_keys('Brian')
last_name_emp = driver.find_element_by_id('employee_last_name').send_keys('Thompson')
emp_btn_create = driver.find_element_by_name("commit").click()

#Green bar states that the employee has been created

if driver.find_element_by_xpath('//*[@id="all-content"]/div[1]'):
    print('Employee Created')
else:
    print('Employee NOT Created')

sleep(2)

#this will search for 'Brian' to edit the employee
search_param = driver.find_element_by_css_selector("input#search-bar").send_keys("Brian")
sleep(2)
emp_edit_link = driver.find_element_by_css_selector("a[href='employees/1740']").click()

#this will update info for 'Brian'
edit_emp_info_btn = driver.find_element_by_css_selector('#accordion > div > div:nth-child(5) > button').click()
im_client_drop_down = driver.find_element_by_id('employee_im_client')
sleep(3)
Select(im_client_drop_down).select_by_visible_text('Skype')
update_emp_btn = driver.find_element_by_name('commit').click()

if driver.find_element_by_xpath('//*[@id="content"]/div[1]'):
    print('Employee updated')
else:
    print('Employee not updated')


emp_btn_nav = driver.find_element_by_css_selector("body > header > div > nav > ul > li:nth-child(7) > a").click()

#Asserts if the employee is on the list

sleep(3)

if driver.find_element_by_css_selector('a[href="employees/1741"].ng-binding'):
    print('Employee is visible on the list')





