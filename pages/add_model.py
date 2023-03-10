import time

from selenium.webdriver.common.by import By

from utilities.utilities import utils


class Add_model():
    log = utils().custom_logger(mode='a')

    def __init__(self, driver):
        self.driver = driver

    name_input_field = "//input[@id='shipment-type-name']"
    description_testbox_field = "//textarea[@id='shipment-type-description']"
    bussiness_code_input_field = "//input[@id='businessCode']"
    item_status_inactive_field = "//input[@id='deliverable-item-status']"
    submit_btn_field = "//body[1]/div[1]/div[2]/div[1]/mdb-modal-container[1]/div[1]/div[1]/add-shipment-type-modal[1]/div[3]/button[1]"
    add_toaster_field = "//strong[normalize-space()='Success']"
    cancel_btn_field = "//button[normalize-space()='Cancel']"

    def get_name_input_field(self):
        return self.driver.find_element(By.XPATH, self.name_input_field)

    def get_description_field(self):
        return self.driver.find_element(By.XPATH, self.description_testbox_field)

    def get_bussiness_code_input_field(self):
        return self.driver.find_element(By.XPATH, self.bussiness_code_input_field)

    def get_item_status_inactive_field(self):
        return self.driver.find_element(By.XPATH, self.item_status_inactive_field)

    def get_submit_btn_field(self):
        return self.driver.find_element(By.XPATH, self.submit_btn_field)

    def get_add_toaster_field(self):
        return self.driver.find_element(By.XPATH, self.add_toaster_field)

    def get_cancel_btn_field(self):
        return self.driver.find_element(By.XPATH, self.cancel_btn_field)

    def enter_name_input(self, input_value):
        self.get_name_input_field().clear()
        self.get_name_input_field().send_keys(input_value)
        self.log.info('Assign ' + input_value + ' into name')

    def enter_description_testbox(self, description_value):
        self.get_description_field().clear()
        self.get_description_field().send_keys(description_value)
        self.log.info('Assign ' + description_value + ' into description')

    def enter_bussiness_code_input(self, input_value):
        self.get_bussiness_code_input_field().clear()
        self.get_bussiness_code_input_field().send_keys(input_value)
        self.log.info('Assign ' + input_value + ' into bussiness code')

    def click_item_status_inactive(self):
        self.get_item_status_inactive_field().click()
        self.log.info("Click on status button")

    def click_submit_btn(self):
        self.get_submit_btn_field().click()
        self.log.info("Click on submit button")

    def click_cancel_btn(self):
        self.get_cancel_btn_field().click()
        self.log.info("Click on cancel button")

    def add_toaster(self):
        toaster_success = self.get_add_toaster_field().text
        if toaster_success == "Success":
            self.log.info("testcase add passed")
        else:
            self.log.info("testcase add failed")

    time.sleep(6)

    def add(self, name, description, bussiness_code):

        self.enter_name_input(name)
        self.enter_description_testbox(description)
        self.enter_bussiness_code_input(bussiness_code)
        time.sleep(3)
        self.click_submit_btn()
        time.sleep(5)
