import selenium
from selenium import webdriver
import os

class DataPuller:
    def __init__(self, browser_name="FireFox", driver_path="~/stathat"):
        self.browser_name = browser_name
        self.driver_path = driver_path

        self._initialize_driver

    def _initialize_driver(self):
        """Initializes the WebDriver instance based on the specified browser."""
        if self.browser_name.lower() == "chrome":
            if self.driver_path:
                os.environ["PATH"] += os.pathsep + self.driver_path
            self.driver = webdriver.Chrome()
        elif self.browser_name.lower() == "firefox":
            if self.driver_path:
                os.environ["PATH"] += os.pathsep + self.driver_path
            self.driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")