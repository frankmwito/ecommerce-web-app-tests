# Base page class that all page models can inherit from

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)
        
    def find(self, *Locator):
        return self.driver.find_element(*Locator)
    
    def click(self, *Locator):
        self.find(*Locator).click()
        
    def input_text(self, *Locator, text):
        self.find(*Locator).send_keys(text)
        
    def wait_for_element(self, *Locator):
        self.wait.until(EC.visibility_of_element_located(*Locator))
        
    def wait_for_element_clickable(self, *Locator):
        self.wait.until(EC.element_to_be_clickable(*Locator))
    
    def hover(self, *Locator):
        self.actions.move_to_element(self.find(*Locator)).perform()
        
    def get_text(self, *Locator):
        return self.find(*Locator).text
    
    def get_title(self):
        return self.driver.title
    
    def click_right_menu_page(self, *Locator, page_name):
        page = By.XPATH, "//aside[@id='column-right']//a[text()='"+  page_name +"']"
        self.click(page)
    
    # Below Page aAllows Us to Click page, check if page is visible, and more actions
    def page(self, page_name):
        return By.XPATH, "//aside[@id='column-right']//a[text()='"+ page_name +"']"