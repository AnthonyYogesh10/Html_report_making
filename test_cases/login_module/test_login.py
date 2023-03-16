import time
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class Test_Credential:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

    def test_01_invalid_username(self):
        self.lp.login("test@gmail.com", "*Welcome&Tech2022")
        self.lp.check_login()

    def test_02_invalid_password(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2021")
        self.lp.check_login()

    def test_03_invalid_username_and_password(self):
        self.lp.login("test@gmail.com", "*Welcome&Tech2021")
        self.lp.check_login()

    def test_04_valid_username_and_password(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
        self.lp.check_login()
        time.sleep(5)
