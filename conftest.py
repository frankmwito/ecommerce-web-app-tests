# cross browser pytest fixture for selenium setup and teardown
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as eddgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


@pytest.fixture(params=["chrome", "firefox", "edge"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service = chromeService(ChromeDriverManager().install()))
    elif request.param == "firefox":
        driver = webdriver.Firefox(service = firefoxService(GeckoDriverManager().install()))
    elif request.param == "edge":
        driver = webdriver.Edge(service = eddgeService(EdgeChromiumDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    print("/nStart browser for test....")
    # return driver instance to test case using fixture name // browser (setup)
    yield driver # cleanup // request.cls.driver = driver used in class based test instead of yield
    # quit the driver instance
    
    print("/nQuit browser....")
    driver.quit()
    
    
    