import json
import time

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class Test_Search():
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

    def test_search(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")
        self.hp.enter_search_input('test')
        self.hp.click_search_button()
        self.hp.click_show_button()
        self.hp.select_page_number('10 per Page')
        time.sleep(5)
        self.hp.select_list_of_searched_data()
        time.sleep(5)
