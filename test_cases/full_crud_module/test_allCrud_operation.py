import time
import pytest

from pages.add_model import Add_model
from pages.delete_modal import Delete_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.modify_modal import Modify_page


@pytest.mark.usefixtures("setup")
class Test_AllCrud():
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.add_model = Add_model(self.driver)
        self.modify_modal = Modify_page(self.driver)
        self.delete_modal = Delete_page(self.driver)

    def test_login(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")

    def test_navigate(self):
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")

    def test_add(self):
        self.hp.click_add_button()
        self.add_model.add("new sample2", "added for testing", "8838yo203")
        self.add_model.add_toaster()

    def test_search(self):
        self.hp.enter_search_input("new sample2")
        self.hp.click_search_button()

    def test_modify(self):
        self.hp.click_modify_btn()
        self.modify_modal.modify("sampleTracker_modify", "Modified data", "810Ybecse")
        self.modify_modal.modify_toaster()

    def test_delete(self):
        self.hp.click_delete_btn()
        self.delete_modal.click_delete_confirm()
        self.delete_modal.delete_toaster()
