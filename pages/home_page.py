import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.utilities import utils


class HomePage:
    log = utils().custom_logger(mode='a')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    # Locators (it is used to change url easily and essy to maintain)
    menubar_field = "//i[@class='fas fa-bars fa-2x']"

    side_nav_options_field = "//ul[@id='scroll-container']/mdb-sidenav-item/li/div/a"
    side_nav_admin_drdw_field = "//ul[@class='sidenav-collapse collapse show']/li"
    under_categories_field = "//mdb-sidenav-item[@class='ng-star-inserted']//li[@class='sidenav-item']/div/a"

    add_button_field = "//button[normalize-space()='Add']"
    modify_btn_field = "//button[normalize-space()='Modify']"

    delete_btn_field = "//button[normalize-space()='Delete']"
    search_input_field = "//input[@id='quick-search']"
    search_button_field = "//i[@class='fa fa-search']"

    show_btn_field = "//td[@id='list-table-left-column-top']//table//tr/td/div/button"
    per_page_list_field = "//body/div/div[@class ='cdk-overlay-connected-position-bounding-box']/div/div/ul/li"

    data_box_field = "//div[@id='mid-list']"
    data_list_field = "//div[@id='mid-list']/a"

    page_numbers_field = "//ul[@class='pagination pagination-sm justify-content-center']/li"
    next_page_field = "//a[normalize-space()='>']"

    sample_names_field = "//*[@id = 'mid-list']/a/div[1]"

    facility_btn_field = "//button[contains(text(),'Facility')]"
    facility_all_value = "//a[normalize-space()='All']"

    document_field = "//span[normalize-space()='Documents']"
    add_document_field = "//button[normalize-space()='Add Documents']"

    tag_input_field = "//ng-select[@name='documentTags']//span[@class='ng-arrow-wrapper']"
    tag_value_field = "//div[@class='ng-dropdown-panel-items scroll-host']/div[2]/div[1]"

    file_upload_field = "//li[1]//label[1]/div"
    file_input = "//li[1]//label[1]/div/input"

    # Loactors to Use (It is used to avoid store variables
    #                 eg: name = xpath
    #                     name.click )
    def get_menubar_field(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.menubar_field))
        )

    def get_side_nav_options_field(self):
        return self.driver.find_elements(By.XPATH, self.side_nav_options_field)

    def get_side_nav_admin_drdw_field(self):
        return self.driver.find_elements(By.XPATH, self.side_nav_admin_drdw_field)

    def get_under_categories_field(self):
        return self.driver.find_elements(By.XPATH, self.under_categories_field)

    def get_add_button_field(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.add_button_field))
        )
        # return self.driver.find_element(By.XPATH, self.add_button_field)

    def get_modify_btn_field(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.modify_btn_field))
        )

    def get_delete_btn_field(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.delete_btn_field))
        )

    def get_search_input_field(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.search_input_field))
        )

    def get_search_button_field(self):
        return self.driver.find_element(By.XPATH, self.search_button_field)

    def get_show_button_field(self):
        return self.driver.find_element(By.XPATH, self.show_btn_field)

    def get_per_page_list_field(self):
        return self.driver.find_elements(By.XPATH, self.per_page_list_field)

    def get_data_list_field(self):
        return self.driver.find_elements(By.XPATH, self.data_list_field)

    def get_data_box_field(self):
        return self.driver.find_element(By.XPATH, self.data_box_field)

    def get_page_numbers_field(self):
        return self.driver.find_elements(By.XPATH, self.page_numbers_field)

    def get_next_field(self):
        return self.driver.find_element(By.XPATH, self.next_page_field)

    def get_sample_names(self):
        return self.driver.find_elements(By.XPATH, self.sample_names_field)

    def click_menu_bar(self):
        self.get_menubar_field().click()
        self.log.info("Click on menubar")
        time.sleep(3)

    def select_side_nav(self, nav_options):
        side_nav = self.get_side_nav_options_field()
        for option in side_nav:
            if option.text == nav_options:
                option.click()
                self.log.info("Click on side_nav")

    def select_nav_admin_drdw(self, dropdown_options):
        administration_dropdown = self.get_side_nav_admin_drdw_field()
        for dropdown_option in administration_dropdown:  # change it to utlities folder
            if dropdown_option.text == dropdown_options:
                dropdown_option.click()
                self.log.info("Click on administration")

    def select_under_categories(self, category_option):
        category_dropdown = self.get_under_categories_field()
        for dropdown in category_dropdown:  # change it to utlities folder
            if dropdown.text == category_option:
                dropdown.click()
                self.log.info("Click on category")

    def click_add_button(self):
        self.get_add_button_field().click()
        self.log.info("Click on add button")
        time.sleep(3)

    def click_modify_btn(self):
        self.get_modify_btn_field().click()
        self.log.info("Click on modify")
        time.sleep(5)

    def click_delete_btn(self):
        self.get_delete_btn_field().click()
        self.log.info("Click on delete button")
        time.sleep(3)

    # added for search operation
    def enter_search_input(self, search_value):
        self.get_search_input_field().send_keys(search_value)
        self.log.info("Assign " + search_value + ' into search input')
        time.sleep(3)

    def click_search_button(self):
        self.get_search_input_field().clear()
        time.sleep(2)
        self.get_search_button_field().click()
        self.log.info("Click on search button")
        time.sleep(3)

    def click_show_button(self):
        self.get_show_button_field().click()
        time.sleep(5)

    def select_per_page_list(self, data_per_page):
        page_numbers = self.get_per_page_list_field()
        for options in page_numbers:
            if options.text == data_per_page:
                options.click()
                self.log.info(f"Click on {data_per_page}")
        time.sleep(5)

    def select_facility_all_value_btn(self):
        self.driver.find_element(By.XPATH, self.facility_btn_field).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_all_value).click()
        time.sleep(2)

    def click_document_btn(self):
        self.driver.find_element(By.XPATH, self.document_field).click()
        time.sleep(4)

    def click_add_document_btn(self):
        self.driver.find_element(By.XPATH, self.add_document_field).click()
        time.sleep(5)

    def select_tag_filed_values(self):
        self.driver.find_element(By.XPATH, self.tag_input_field).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.tag_value_field).click()
        time.sleep(4)

    def outside_click(self):
        self.driver.find_element(By.XPATH, "//form[@role='form']//div[@class='modal-header']").click()
        time.sleep(5)

    def upload_data(self, file_path_of_upload_file):
        # self.driver.find_element(By.XPATH, self.file_upload_field).click()
        # time.sleep(5)
        self.driver.find_element(By.XPATH, self.file_input).send_keys(file_path_of_upload_file)
        time.sleep(5)
        add_btn = self.driver.find_element(By.XPATH, "//button[@class='btn btn-sm btn-primary text-white']")
        add_btn.click()
        time.sleep(5)


    # def samples_names(self, name):
    #     list_of_samples = self.get_sample_names()
    #     for sample_name in list_of_samples:
    #         if name == sample_name.text.strip(): # strip method is used to remove extra space from the string
    #             sample_name.click()
    #             time.sleep(3) test git

    def navigate_to(self, navigate_to, administration, category):
        self.select_side_nav(navigate_to)
        time.sleep(3)
        self.select_nav_admin_drdw(administration)
        time.sleep(3)
        self.select_under_categories(category)
        time.sleep(3)
