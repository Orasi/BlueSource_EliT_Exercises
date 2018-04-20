from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from time import sleep

class BlueLoginPage(BasePage):


    _login_btn = (By.NAME, 'commit')
    _username_field = (By.ID, 'employee_username')
    _password_field = (By.ID, 'employee_password')
    _find_nav_bar = (By.CLASS_NAME, 'navbar-collapse bs-navbar-collapse collapse')


    def get_login_btn(self):
        self.find('_login_btn')
        return self.find('_login_btn')

    def get_username_field(self):
        self.find('_username_field')
        return self.find('_username_field')

    def get_password_field(self):
        self.find('_password_field')
        return self.find('_password_field')

    def check_nav_bar(self):
        self.find('_find_nav_bar')
        return self.find('_find_nav_bar')


    def login(self, username, password):
        #populates username
        fill_user_name = self.get_username_field()
        fill_user_name.send_keys('company.admin')


        #populates password
        fill_pw = self.get_password_field()
        fill_pw.send_keys('4444')

        # Get the Login Button
        login_btn = self.get_login_btn()
        login_btn.click()
        sleep(3)




