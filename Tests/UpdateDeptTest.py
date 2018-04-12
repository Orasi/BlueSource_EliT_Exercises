from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import Select



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
pencil_icon = driver.find_element_by_xpath('//*[@id="content"]/div/ul[1]/li/div/a[1]/span').click()
name_field = driver.find_element_by_id('department_name').send_keys('7777')
update_dept_btn = driver.find_element_by_name('commit').click()

#Asserts whether then Dept has been created or not

if driver.find_element_by_xpath('//*[@id="content"]/div[1]'):
    print('Successfully Updated Title')
else:
    print('Not Updated')


