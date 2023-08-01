import time
import pytest

from pages.add_model import Add_model
from pages.delete_modal import Delete_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.modify_modal import Modify_page
from base.base_driver import BaseDriver


@pytest.mark.usefixtures("setup")
class Test_AllCrud:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.add_model = Add_model(self.driver)
        self.modify_modal = Modify_page(self.driver)
        self.delete_modal = Delete_page(self.driver)
        self.base = BaseDriver(self.driver)

    # def test_login(self):
    #     self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
    def test_01_invalid_username(self):
        self.lp.login("test@gmail.com", "*Welcome&Tech2022")
        self.lp.check_login()

    def test_02_invalid_password(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2021")
        self.lp.check_login()

    def test_03_invalid_username_and_password(self):
        self.lp.login("test@gmail.com", "*Welcome&Tech2021")
        self.lp.check_login()

    def test_04_valid_username_and_password(self, capsys):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
        self.lp.check_login()
        captured = capsys.readouterr()
        time.sleep(5)

    def test_05_navigate(self):
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")

    def test_06_add(self):
        self.hp.click_add_button()
        self.add_model.add("new sample2", "added for testing", "8838yo203")
        self.add_model.add_toaster()

    def test_07_search(self):
        self.hp.enter_search_input("new sample2")
        self.hp.click_search_button()

    def test_08_modify(self):
        self.hp.click_modify_btn()
        self.modify_modal.modify("sampleTracker_modify", "Modified data", "810Ybecse")
        self.modify_modal.modify_toaster()

    def test_09_delete(self):
        self.hp.click_delete_btn()
        self.delete_modal.click_delete_confirm()
        self.delete_modal.delete_toaster()

    def test_10_search(self):
        self.hp.click_search_button()
        self.hp.click_show_button()
        self.hp.select_per_page_list("50 per Page")
        self.base.scroll_n_click_next("50 per Page")
        time.sleep(5)


