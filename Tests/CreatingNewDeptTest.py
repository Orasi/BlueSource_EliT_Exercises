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

#create new department in admin departments homepage
admin_btn = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[1]").click()
dropdown = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[1]/ul/li/a[1]").click()
dept_button = driver.find_element_by_xpath('//*[@id="content"]/a').click()
dept_name_field = driver.find_element_by_id("department_name").send_keys("BETttt")
control_select = driver.find_element_by_id("department_alternate_approver_id")
Select(control_select).select_by_visible_text("Company Admin")
submit_dept_button = driver.find_element_by_name("commit").click()

#Validates whether then Dept has been created or not

sleep(2)

assert driver.find_element_by_xpath('//*[@class="alert alert-danger alert-dismissable"]').is_displayed(), "Dept Created"

assert driver.find_element_by_xpath('//*[@class="alert alert-success alert-dismissable"]').is_displayed(), "Dept Not Created"

