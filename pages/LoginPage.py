
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage



class LoginPage(BasePage):
    # store Locators 
    email_input = (By.ID, "input-email")
    password_input = (By.ID, "input-password")
    login_button = (By.XPATH, "//input[@value='Login']")
    error_message = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    # Actions
    
    