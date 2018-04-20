from Helpers.BaseTest import BaseTest
from selenium.webdriver.support.select import Select
from Pages.BlueLoginPage import BlueLoginPage
from Pages.EmployeePage import EmployeePage
from time import sleep

class EmployeeTest(BaseTest):

    def test_adding_employee(self):
        self.driver.get('http://bluesourcestaging.herokuapp.com/login')
        login = BlueLoginPage(driver=self.driver)
        add_employee = EmployeePage(self.driver)

        login.sync()

        login.login('company.admin', '1234')

        #click the add button to add employee

        employee_add_btn = add_employee.employee_add_btn
        employee_add_btn.click()
        sleep(3)

        #window comes up to fill out employee info

        username_field = add_employee.username_field
        username_field.send_keys('Billy1234567')

        first_name_field = add_employee.first_name_field
        first_name_field.send_keys('BillyBobb')


        last_name_field = add_employee.last_name_field
        last_name_field.send_keys('Smithsonn')

        employee_title = add_employee.employee_title
        Select(employee_title).select_by_visible_text('Host')

        employee_manager = add_employee.employee_manager
        Select(employee_manager).select_by_visible_text('Cam Newton')

        employee_status = add_employee.employee_status
        Select(employee_status).select_by_visible_text('Inactive')

        employee_location = add_employee.employee_location
        Select(employee_location).select_by_visible_text('Remote')

        # employee_start_date = add_employee._employee_start_date
        # employee_start_date.send_keys('1111111111')

        employee_cell_num = add_employee.employee_cell_num
        employee_cell_num.send_keys('(888)-888-8888')

        employee_office_num = add_employee.employee_office_num
        employee_office_num.send_keys('(888)-888-8888')

        employee_email = add_employee.employee_email
        employee_email.send_keys('bill12345@orasi.com')

        employee_im_name = add_employee.employee_im_name
        employee_im_name.send_keys('billy555555')

        employee_im_client = add_employee.employee_im_client
        Select(employee_im_client).select_by_visible_text('Skype')

        employee_dept_id = add_employee.employee_dept_id
        Select(employee_dept_id).select_by_visible_text('Group1')

        #click the create employee button
        create_emp_btn = add_employee.create_emp_btn
        create_emp_btn.click()

        #validate employee was create with green notification bar
        assert add_employee.alert_success.is_displayed, 'Employee NOT Created'

        sleep(2)


