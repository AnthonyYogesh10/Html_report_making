import time
import unittest

import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.add_model import Add_model
from ddt import data, unpack, ddt, file_data
from utilities.utilities import utils

ul = utils()


@pytest.mark.usefixtures("setup")
@ddt  # place this ddt above class below fixture
class Test_Add(unittest.TestCase):  # unittest.TestCase without this it cant work
    @pytest.fixture(autouse=True)
    def class_setup(self):
        # self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.add_model = Add_model(self.driver)

    # def test_01_login(self):
    #     # self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
    #     self.hp.click_menu_bar()
    #     self.hp.navigate_to("Administration", "Categories", "Sample Types")

    @data(
        *ul.read_data_from_excel("/home/chris/Desktop/automation/Html_report_making/test_data/add_data.xlsx", 'Sheet1'))
    @unpack
    def test_01_add_by_ddt_method(self, name, description, bussiness_code):
        self.hp.click_add_button()
        self.add_model.add(name, description, bussiness_code)
        print('data from excel ', name, description, bussiness_code)
        self.add_model.add_toaster()









