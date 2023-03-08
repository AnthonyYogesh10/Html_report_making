import time

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.modify_modal import Modify_page


@pytest.mark.usefixtures("setup")
class Test_Modify():
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.modify_modal = Modify_page(self.driver)

    def test_modify(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")
        self.hp.click_modify_btn()
        self.modify_modal.modify("sampleTracker_modify", "Modified data", "810Ybecse")
        self.modify_modal.modify_toaster()
