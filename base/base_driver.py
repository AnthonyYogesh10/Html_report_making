import time

from selenium.common import ElementClickInterceptedException
from pages.home_page import HomePage
from utilities.utilities import utils
from pytest_excel import pytest_excel


class BaseDriver:
    log = utils().custom_logger(mode='a')

    def __init__(self, driver):
        self.driver = driver
        self.hp = HomePage(self.driver)

    def scroll_data_box(self, scroll_multiplier):
        data_box = self.hp.get_data_box_field()
        current_scroll_position = 0
        target_scroll_position = 1200 * scroll_multiplier
        scroll_increment = 100
        scroll_delay = 0.05  # in seconds
        total_scroll_time = scroll_multiplier  # in seconds
        start_time = time.time()

        while time.time() - start_time < total_scroll_time:
            self.driver.execute_script(f"arguments[0].scrollTop = {current_scroll_position}", data_box)
            current_scroll_position += scroll_increment
            time.sleep(scroll_delay)

            if current_scroll_position >= target_scroll_position:
                break
        time.sleep(3)

    def scroll_n_click_next(self, data_per_page):
        scroll_value = None
        if data_per_page == '10 per Page':
            scroll_value = 1
        elif data_per_page == '25 per Page':
            scroll_value = 3
        elif data_per_page == '50 per Page':
            scroll_value = 6
        page_numbers = self.hp.get_page_numbers_field()
        length_page = len(page_numbers)
        if length_page == 0:
            length_of_page_numbers = 0
        else:
            length_of_page_numbers = lenth_page - 3
        length_of_data_list = []
        for i in range(0, length_of_page_numbers):
            data_list = len(self.hp.get_data_list_field())
            length_of_data_list.insert(1, data_list)
            if i < length_of_page_numbers:
                self.scroll_data_box(scroll_value)
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
