import time
import pytest
import unittest

from ddt import data, unpack, ddt, file_data
from utilities.utilities import utils

from pages.login_page import LoginPage
from pages.home_page import HomePage

ul = utils()


@pytest.mark.usefixtures("setup")
@ddt
class Test_Credential(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

    @data(
        *ul.read_data_from_excel("../../test_data/login_data.xlsx", 'Sheet1'))
    @unpack
    def test_login(self, user_name, password):
        self.lp.login(user_name, password)
        self.lp.check_login()
