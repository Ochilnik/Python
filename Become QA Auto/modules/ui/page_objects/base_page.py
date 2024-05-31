from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    #PATH = r"/home/sbutenko/repos/LnD/Become QA Auto/"
    #DRIVER_NAME = "chromedriver"


    def __init__(self) -> None:
        #self.driver = webdriver.Chrome(
        #    service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        #    )
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def close(self):
        self.driver.close()
