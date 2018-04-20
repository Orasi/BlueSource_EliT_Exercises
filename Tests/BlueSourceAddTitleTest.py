from Helpers.BaseTest import BaseTest
from Pages.BlueLoginPage import BlueLoginPage
from Pages.BlueAddTitlePage import BlueAddTitlePage
from time import sleep


class TitleTests(BaseTest):

    def test_add_title(self):
        self.driver.get('http://bluesourcestaging.herokuapp.com/login')
        login = BlueLoginPage(driver=self.driver)
        add_title = BlueAddTitlePage(self.driver)

        login.sync()

        login.login('company.admin', '1234')

        #click the admin btn in nav bar

        admin_btn = add_title.admin_btn
        admin_btn.click()


        #click the titles in the drop down option
        drop_down_titles = add_title.drop_down_titles
        drop_down_titles.click()

        # click the new title button at the bottom of the page
        new_titles_btn = add_title.new_title_btn
        new_titles_btn.click()


        #creating a new title

        title_text_field = add_title.title_text_field.send_keys('blahhbl')
        create_title_btn = add_title.create_title_btn
        create_title_btn.click()
        sleep(2)

    def test_delete_title(self):
        self.driver.get('http://bluesourcestaging.herokuapp.com/login')
        login = BlueLoginPage(driver=self.driver)
        login.sync()

        login.login('company.admin', '1234')

        delete_title = BlueAddTitlePage(driver=self.driver)

        # click the admin btn in nav bar
        admin_btn = delete_title.admin_btn
        admin_btn.click()

        # click the titles in the drop down option
        drop_down_titles = delete_title.drop_down_titles
        drop_down_titles.click()

        #click the trash icon to delete the title
        delete_title_trash = delete_title.delete_tit_trash
        delete_title_trash.click()
        sleep(2)
        self.driver.switch_to.alert.accept()


    def test_edit_title(self):
        self.driver.get('http://bluesourcestaging.herokuapp.com/login')
        login = BlueLoginPage(driver=self.driver)
        login.sync()

        login.login('company.admin', '1234')

        edit_title = BlueAddTitlePage(driver=self.driver)

        # click the admin btn in nav bar
        admin_btn_drop = edit_title.admin_btn
        admin_btn_drop.click()

        # click the titles in the drop down option
        drop_down_titles = edit_title.drop_down_titles
        drop_down_titles.click()

        sleep(1)
        #click the pencil icon to edit a title
        edit_pencil_icon = edit_title.edit_title_pencil
        edit_pencil_icon.click()

        #enter text in title text field to edit title and click update
        edit_title_txt = edit_title.edit_title_txt.send_keys('!!!')

        update_title_btn = edit_title.update_title_btn
        update_title_btn.click()
        sleep(2)





