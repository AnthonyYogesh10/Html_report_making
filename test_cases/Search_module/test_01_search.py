import json
import time

import pytest

from base.base_driver import BaseDriver
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class Test_Search():
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.base = BaseDriver(self.driver)

    def test_search(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
        # self.hp.click_menu_bar()
        # self.hp.navigate_to("Administration", "Categories", "Sample Types")
        # self.hp.enter_search_input('test')
        self.hp.click_search_button()
        self.hp.click_show_button()
        self.hp.select_per_page_list('25 per Page')
        self.base.scroll_n_click_next()
        time.sleep(3)
        # self.hp.data_list()
        # time.sleep(5)
