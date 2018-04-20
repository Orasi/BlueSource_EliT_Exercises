from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.NavBarElement import NavBar


class BlueAddTitlePage(BasePage):

    _nav_bar = (By.CSS_SELECTOR, 'header.navbar', NavBar)
    _admin_btn = (By.XPATH, '/html/body/header/div/nav/ul/li[1]')
    _drop_down_titles = (By.CSS_SELECTOR, 'body > header > div > nav > ul > li.dropdown.open > ul > li > a:nth-child(2)', )
    _new_title_btn = (By.CSS_SELECTOR, "#content > a")
    _title_text_field = (By.CSS_SELECTOR, '#title_name')
    _create_title_btn = (By.XPATH, '//*[@id="new_title"]/div[3]/input')
    _delete_title_trash = (By.XPATH, '//*[@id="content"]/table/tbody/tr[3]/td/div/a[2]/span')
    _edit_title_pencil = (By.XPATH, '//*[@id="content"]/table/tbody/tr[3]/td/div/a[1]/span')
    _edit_title_txt = (By.ID, 'title_name')
    _update_title_btn = (By.CSS_SELECTOR, '#edit_title_1311 > div.actions > input')

    #properties for titles (adding, editing, and deleting)

    @property
    def nav_bar(self):
        return self.find('_nav_bar')

    @property
    def admin_btn(self):
        return self.find('_admin_btn')

    @property
    def drop_down_titles(self):
        return self.find('_drop_down_titles')

    @property
    def new_title_btn(self):
        return self.find('_new_title_btn')

    @property
    def title_text_field(self):
        return self.find('_title_text_field')

    @property
    def create_title_btn(self):
        return self.find('_create_title_btn')

    @property
    def delete_tit_trash(self):
        return self.find('_delete_title_trash')

    @property
    def edit_title_pencil(self):
        return self.find('_edit_title_pencil')

    @property
    def edit_title_txt(self):
        return self.find('_edit_title_txt')

    @property
    def update_title_btn(self):
        return self.find('_update_title_btn')




