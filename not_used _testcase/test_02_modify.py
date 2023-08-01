import time
import unittest

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.modify_modal import Modify_page
from ddt import ddt, data, unpack
from utilities.utilities import utils

ul = utils()


@pytest.mark.usefixtures("setup")
@ddt
class Test_Modify(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.modify_modal = Modify_page(self.driver)

    def test_01_login(self):
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")

    @data(*ul.read_data_from_excel(
        "/home/chris/Desktop/automation/Html_report_making/test_data/modify_data.xlsx", "Sheet1"
    ))
    @unpack
    def test_02_modify(self, search_data, name, description, bussiness_code):
        self.hp.enter_search_input(search_data)
        self.hp.click_search_button()
        self.hp.click_modify_btn()
        self.modify_modal.modify(name, description, bussiness_code)
        self.modify_modal.modify_toaster()
