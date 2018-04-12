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

#Department in admin departments homepage
sleep(5)
admin_btn = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[1]").click()
dropdown = driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[1]/ul/li/a[1]").click()
delete_btn = driver.find_element_by_xpath('//*[@id="content"]/div/ul[1]/li/div/a[2]/span').click()


#Alert prompt window
sleep(2)

alert = driver.switch_to_alert()
alert.accept()
print('Deletion successful')

