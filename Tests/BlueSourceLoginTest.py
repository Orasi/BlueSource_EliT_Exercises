from Helpers.BaseTest import BaseTest
from Pages.BlueLoginPage import BlueLoginPage

from time import sleep

#Login into Bluesource page
class BlueLoginTest(BaseTest):

    def test_login_bluesource(self):
        self.driver.get('http://bluesourcestaging.herokuapp.com/login')
        login = BlueLoginPage(driver=self.driver)
        login.sync()

        #populates username
        fill_user_name = login.get_username_field()
        fill_user_name.send_keys('company.admin')


        #populates password
        fill_pw = login.get_password_field()
        fill_pw.send_keys('4444')

        # Get the Login Button
        login_btn = login.get_login_btn()
        login_btn.click()
        sleep(3)





