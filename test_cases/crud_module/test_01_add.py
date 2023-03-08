import time

import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.add_model import Add_model


@pytest.mark.usefixtures("setup")
class Test_Add:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.add_model = Add_model(self.driver)

    def test_Add(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")
        self.hp.click_add_button()
        self.add_model.add("Add test testcase", "added for testing", "new for addTest")
        self.add_model.add_toaster()
