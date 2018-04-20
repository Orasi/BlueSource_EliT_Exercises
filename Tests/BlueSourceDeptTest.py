from Helpers.BaseTest import BaseTest
from selenium.webdriver.support.select import Select
from Pages.BlueLoginPage import BlueLoginPage
from Pages.BlueSourceDeptPage import BlueSourceDeptPage
from time import sleep

class BlueSourceDeptTest(BaseTest):

    def test_creating_dept(self):
        self.driver.get('http://bluesourcestaging.herokuapp.com/login')
        login = BlueLoginPage(driver=self.driver)
        departments = BlueSourceDeptPage(self.driver)

        login.sync()

        login.login('company.admin', '1234')


        #click the admin button in the nav to drop down depts
        dropdown_menus = departments.dropdown_menus
        dropdown_menus.click()


        drop_down_dept = departments.drop_down_dept
        drop_down_dept.click()


        #click add new dept at the bottom of the page

        add_dept_btn = departments.add_dept_btn
        add_dept_btn.click()



        #fill out criteria for new dept on new page


        dept_name_field = departments.dept_name_field
        dept_name_field.send_keys('Avengers')

        # parent_dept_field = departments.parent_dept_field
        # Select(parent_dept_field).select_by_visible_text('Group1')

        min_hr_increment = departments.min_hr_increment
        Select(min_hr_increment).select_by_visible_text('1')

        alternate_approver = departments.alternate_approver
        Select(alternate_approver).select_by_visible_text('Company Admin')

        create_dept_btn = departments.create_dept_btn
        create_dept_btn.click()

        #validate department was create with green notification bar
        assert departments.alert_success.is_displayed, 'Department NOT Created'

        sleep(3)


    #def test_delete_dept