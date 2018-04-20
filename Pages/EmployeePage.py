from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.NavBarElement import NavBar


class EmployeePage(BasePage):

    _employee_add_btn = (By.CSS_SELECTOR, '#all-content > div.header-btn-section > div > div.btn-group.pull-right')
    _username_field = (By.ID, 'employee_username')
    _first_name_field = (By.ID, 'employee_first_name')
    _last_name_field = (By.ID, 'employee_last_name')
    _employee_title = (By.ID, 'employee_title_id')
    _employee_role = (By.ID, 'employee_role')
    _employee_manager = (By.ID, 'employee_manager_id')
    _employee_status = (By.ID, 'employee_status')
    _employee_location = (By.ID, 'employee_location')
    _employee_start_date =(By.CLASS_NAME, 'employee[start_date]')
    _employee_cell_num = (By.ID, 'employee_cell_phone')
    _employee_office_num = (By.ID, 'employee_office_phone')
    _employee_email = (By.ID, 'employee_email')
    _employee_im_name = (By.ID, 'employee_im_name')
    _employee_im_client = (By.ID, 'employee_im_client')
    _employee_dept_id = (By.ID, 'employee_department_id')
    _create_emp_btn = (By.CSS_SELECTOR, '#new_employee > div.form-group.modal-footer > input')
    _alert_success = (By.CLASS_NAME, 'alert-success')

    # properties for adding an employee

    @property
    def employee_add_btn(self):
        return self.find('_employee_add_btn')

    @property
    def username_field(self):
        return self.find('_username_field')

    @property
    def first_name_field(self):
        return self.find('_first_name_field')

    @property
    def last_name_field(self):
        return self.find('_last_name_field')

    @property
    def employee_title(self):
        return self.find('_employee_title')

    @property
    def employee_role(self):
        return self.first_name_field('_employee_role')

    @property
    def employee_manager(self):
        return self.find('_employee_manager')

    @property
    def employee_status(self):
        return self.find('_employee_status')

    @property
    def employee_location(self):
        return self.find('_employee_location')

    @property
    def employee_start_date(self):
        return self.find('_employee_start_date')

    @property
    def employee_cell_num(self):
        return self.find ('_employee_cell_num')

    @property
    def employee_office_num(self):
        return self.find('_employee_office_num')

    @property
    def employee_email(self):
        return self.find('_employee_email')

    @property
    def employee_im_name(self):
        return self.find('_employee_im_name')

    @property
    def employee_im_client(self):
        return self.find('_employee_im_client')

    @property
    def employee_dept_id(self):
        return self.find('_employee_dept_id')

    @property
    def create_emp_btn(self):
        return self.find('_create_emp_btn')

    @property
    def alert_success(self):
        return self.find('_alert_success')
