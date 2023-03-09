import time

from selenium.common import ElementClickInterceptedException
from pages.home_page import HomePage
from utilities.utilities import utils

class BaseDriver():
    log = utils().custom_logger(mode='a')

    def __init__(self, driver):
        self.driver = driver
        self.hp = HomePage(self.driver)

    def scroll_n_click_next(self):
        page_numbers = self.hp.get_page_numbers_field()
        length_of_page_numbers = len(page_numbers) - 3
        length_of_data_list = []
        for i in range(0, length_of_page_numbers):
            data_list = len(self.hp.get_data_list_field())
            length_of_data_list.insert(1, data_list)
            if i < length_of_page_numbers:
                self.hp.scroll_data_box(3)
                try:
                    self.hp.get_next_field().click()
                    self.log.info("Click on next button")
                    time.sleep(5)
                except ElementClickInterceptedException:
                    print('')

        print(f'Total Items Found: {sum(length_of_data_list)}')
        self.log.info(f'Total Items Found: {sum(length_of_data_list)}')
        print(f'\n Total Pages: {length_of_page_numbers}')
        self.log.info(f'Total Pages: {length_of_page_numbers}')