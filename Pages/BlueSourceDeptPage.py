from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.NavBarElement import NavBar

class BlueSourceDeptPage(BasePage):


    _dropdown_menus = (By.CLASS_NAME, 'dropdown')
    _drop_down_dept = (By.CSS_SELECTOR, '.dropdown-menu a[href="/admin/departments"]')
    _add_dept_btn = (By.XPATH, '//*[@id="content"]/a')
    _dept_name_field = (By.ID, 'department_name')
    _parent_dept_field = (By.CLASS_NAME, 'department[department_id]')
    _min_hr_increment = (By.ID, 'department_minimum_hour_increment')
    _alternate_approver = (By.ID, 'department_alternate_approver_id')
    _create_dept_btn = (By.XPATH, '//*[@id="new_department"]/div[6]/input')
    _alert_success = (By.CLASS_NAME, 'alert-success')

    @property
    def dropdown_menus(self):
        return self.find('_dropdown_menus')

    @property
    def drop_down_dept(self):
        return self.find('_drop_down_dept')

    @property
    def add_dept_btn(self):
        return self.find('_add_dept_btn')

    @property
    def dept_name_field(self):
        return self.find('_dept_name_field')

    @property
    def parent_dept_field(self):
        return self.find('_parent_dept_field')

    @property
    def min_hr_increment(self):
        return self.find('_min_hr_increment')

    @property
    def alternate_approver(self):
        return self.find('_alternate_approver')

    @property
    def create_dept_btn(self):
        return self.find('_create_dept_btn')

    @property
    def alert_success(self):
        return self.find('_alert_success')
