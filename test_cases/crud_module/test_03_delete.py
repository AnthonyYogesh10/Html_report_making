import time
import unittest

import pytest
from pages.home_page import HomePage
from pages.delete_modal import Delete_page
from ddt import data, unpack, ddt

from utilities.utilities import utils

ul = utils()


@pytest.mark.usefixtures("setup")
@ddt
class Test_Delete(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.delete_modal = Delete_page(self.driver)

    def test_01_login(self):
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")

    @data(*ul.read_data_from_excel(
        "/home/chris/Desktop/automation/Html_report_making/test_data/del_data.xlsx", "Sheet1"
    ))
    @unpack
    def test_02_delete(self, name):
        self.hp.enter_search_input(name)
        self.hp.click_search_button()
        self.hp.click_delete_btn()
        self.delete_modal.click_delete_confirm()
        self.delete_modal.delete_toaster()


