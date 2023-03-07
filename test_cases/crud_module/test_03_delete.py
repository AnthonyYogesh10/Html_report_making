import time

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.delete_modal import Delete_page


@pytest.mark.usefixtures("setup")
class Test_Delete():
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.delete_modal = Delete_page(self.driver)

    def test_login(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")

    def test_navigate(self):
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")

    def test_delete(self):
        self.hp.click_delete_btn()
        self.dele_modal.click_delete_confirm()
        self.dele_modal.delete_toaster()
