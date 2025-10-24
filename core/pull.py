import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class DataPuller:
    def __init__(self, browser_name="FireFox", driver_path="~/stathat"):
        self.browser_name = browser_name
        self.driver_path = driver_path

        self._initialize_driver()
    
    def _initialize_driver(self):
        if self.browser_name.lower() == "chrome":
            if self.driver_path:
                os.environ["PATH"] += os.pathsep + self.driver_path
            chrome_options = webdriver.ChromeOptions()
            prefs = {
                "download.default_directory": os.path.expanduser("./stathat-downloads"),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            }
            chrome_options.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver = webdriver.Chrome()
        elif self.browser_name.lower() == "firefox":
            if self.driver_path:
                os.environ["PATH"] += os.pathsep + self.driver_path
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.set_preference("browser.download.folderList", 2)
            firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
            firefox_options.set_preference("browser.download.dir", os.path.expanduser("./stathat-downloads"))
            firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", 
                                      "application/pdf,text/csv,application/csv,application/vnd.ms-excel,application/zip")
            self.driver = webdriver.Firefox(options=firefox_options)
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")
    
    def goto_url(self, url):
        self.driver.get(url)

    def title(self):
        return self.driver.title
    
    def find_elm_by_PARTEXT(self, locator, timeout=30):
        print("Finding Element...")
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, locator)))

    def click_elm(self, elm):
        '''Pass in a selenium.webdriver.remote.webelement.WebElement'''
        elm.click()
    
    def download_file(self, download_locator, wait_time=45):
        import time
        download_dir = os.path.expanduser("./stathat-downloads")
        before_download = set(os.listdir(download_dir))

        self.click_elm(download_locator)
        start_time = time.time()
        while time.time() - start_time < wait_time:
            after_download = set(os.listdir(download_dir))
            new_files = after_download - before_download
            if new_files:
                downloading = False
                for file in new_files:
                    if file.endswith(('.part', '.crdownload', '.tmp')):
                        downloading = True
                        break
            
                if not downloading:
                    downloaded_file = list(new_files)[0]
                    return os.path.join(download_dir, downloaded_file)
            time.sleep(1)
        raise TimeoutError(f"Download did not complete within {wait_time} seconds")
    
    def wait_for_download(self, file, timeout=45):
        import time
        download_dir = os.path.expanduser("./stathat-downloads")
        filepath = os.path.join(download_dir, file)

        start_time = time.time()
        while time.time() - start_time < timeout:
            if os.path.exists(filepath):
                initial_size = os.path.getsize(filepath)
                time.sleep(1)
                current_size = os.path.getsize(filepath)
            
            if initial_size == current_size and current_size > 0:
                return filepath
            time.sleep(1)
        raise TimeoutError(f"File {file} did not download within {timeout} seconds")

    def close(self):
        if self.driver:
            self.driver.quit()