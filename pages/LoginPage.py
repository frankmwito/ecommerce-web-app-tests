
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utilities.locators import ChangePasswordLocatorFields
from utilities.Test_data import TestData



class LoginPage(BasePage):
    # store Locators 
    email_input = (By.ID, "input-email")
    password_input = (By.ID, "input-password")
    login_button = (By.XPATH, "//input[@value='Login']")
    error_message = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def open(self):
        self.driver.get(TestData.url)
        
    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    
    def get_error_message(self, error_message):
        return self.driver.find_element(*self,error_message).text
    
    