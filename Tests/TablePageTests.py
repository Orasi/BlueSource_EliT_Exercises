from Helpers.BaseTest import BaseTest
from Pages.HomePage import HomePage
from Pages.TablesPage import TablesPage
from hotdog.TestStep import TestStep
from time import sleep


class TablePageTests(BaseTest):

    def test_sort_first_table_by_last_name_alphabetical(self):
        home = HomePage(self.driver)
        table = TablesPage(self.driver)

        self.driver.get(self.page_url)
        home.sync()

        home.navigate_to_data_table_page()
        table.sync()

        sort_step = TestStep("Start table sort logic")
        unsorted_last_names = table.example_1_table.get_last_names()
        table.example_1_table.sort_table_by('last name')
        sorted_last_name = table.example_1_table.get_last_names()
        sort_step("Complete")
        reverse = list(reversed(sorted_last_name))

        new_reverseAlph = list(reversed)
        new_reverseAlph.reverse()
        sleep(20)



        table_verification = TestStep("Verify last names are sorted and in alphabetical order")
        assert unsorted_last_names != sorted_last_name, "Table sort by last name didn't take place"
        self.assertAlphabetical(new_reverseAlph)
        table_verification("Complete")
        sleep(20)


    # test first table last name reversed alphabetical
    # table page element verifcation




