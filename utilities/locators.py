# a way to store locators apart from the page class

from selenium.webdriver.common.by import By

class ChangePasswordLocatorFields:
    """
    A class to hold the locators for the change password fields in the web application.

    Attributes:
        password_field (tuple): Locator for the password input field.
        confirm_password_field (tuple): Locator for the confirm password input field.
        continue_button (tuple): Locator for the continue button.
        confirmation_error_message (tuple): Locator for the confirmation error message.
    """
    password_field = (By.ID, "input-password")
    confirm_password_field = (By.ID, "input-confirm")
    continue_button = (By.CSS_SELECTOR, "input[value='Continue']")
    confirmation_error_message = (By.XPATH,"//div[@class='text-danger']")