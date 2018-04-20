from hotdog.BaseElement import BaseElement
from selenium.webdriver.common.by import By

class NavBar(BaseElement):

    _dropdown_menus = (By.CLASS_NAME, 'dropdown')  # admin and calendar
    _drop_down_departments = (By.CSS_SELECTOR, '.dropdown-menu a[href="/admin/departments"]')
    _drop_down_titles = (By.CSS_SELECTOR, '.dropdown-menu a[href="/admin/titles"]')
    _admin_menu_email_users = (By.CSS_SELECTOR, 'a[data-target="#email_all_modal"]')
    _calendar = (By.CSS_SELECTOR, 'a[href="/calendar]')
    _calendar_menu_reporting = (By.CSS_SELECTOR, 'a[data-target="#vacation_reporting_modal"]')
    _message_center = (By.CSS_SELECTOR, 'body > header > div > nav > ul > li:nth-child(2) > a')
    _directory = (By.CSS_SELECTOR, 'body > header > div > nav > ul > li:nth-child(5) > a')
    _project = (By.CSS_SELECTOR, 'body > header > div > nav > ul > li:nth-child(6) > a')
    _employee = (By.CSS_SELECTOR, 'body > header > div > nav > ul > li:nth-child(7) > a')



    @property
    def admin_btn(self):
        return self.finds('_dropdown_menus')[0]


    @property
    def calendar_menu(self):
        return self.finds('_dropdown_menus')[1]


    @property
    def drop_down_departments(self):
        return self.find('_drop_down_departments')


    @property
    def drop_down_titles(self):
        return self.find('_drop_down_titles')


    @property
    def calendar(self):
        return self.find('_calendar')


    @property
    def calendar_menu_reporting(self):
        return self.find('_calendar_menu_reporting')


    @property
    def message(self):
        return self.find('_message')

    @property
    def calendar(self):
        return self.find('_calendar')

    @property
    def directory(self):
        return self.find('_directory')

    @property
    def project(self):
        return self.find('_project')

    @property
    def employee(self):
        return self.find('_employee')
