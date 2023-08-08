import time
import pytest
import unittest

from ddt import data, unpack, ddt, file_data
from utilities.utilities import utils

from pages.add_model import Add_model
from pages.delete_modal import Delete_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.modify_modal import Modify_page
from base.base_driver import BaseDriver

ul = utils()


@pytest.mark.usefixtures("setup")
@ddt
class Test_AllCrud(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.add_model = Add_model(self.driver)
        self.modify_modal = Modify_page(self.driver)
        self.delete_modal = Delete_page(self.driver)
        self.base = BaseDriver(self.driver)

    @data(
        *ul.read_data_from_excel("../../test_data/login_data.xlsx", 'Sheet1'))
    @unpack
    def test_01_test_login(self, user_name, password):
        self.lp.login(user_name, password)
        self.lp.check_login()

    def test_02_navigate(self):
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")

    def test_03_add(self):
        self.hp.click_add_button()
        self.add_model.add("new sample2", "added for testing", "8838yo203")
        self.add_model.add_toaster()

    def test_04_search(self):
        self.hp.enter_search_input("new sample2")
        self.hp.click_search_button()

    def test_05_modify(self):
        self.hp.click_modify_btn()
        self.modify_modal.modify("sampleTracker_modify", "Modified data", "810Ybecse")
        self.modify_modal.modify_toaster()

    def test_06_delete(self):
        self.hp.click_delete_btn()
        self.delete_modal.click_delete_confirm()
        self.delete_modal.delete_toaster()

    def test_7_search(self):
        self.hp.click_search_button()
        self.hp.click_show_button()
        self.hp.select_per_page_list("50 per Page")
        self.base.scroll_n_click_next("50 per Page")
        time.sleep(5)
