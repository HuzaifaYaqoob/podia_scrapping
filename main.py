
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import requests
import time


class PodiaScrapping():
    def __init__(self):
        print('Working')

        self.driver = self.initialize_driver()
        self.login()

    def initialize_driver(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=YourUserAgent')

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    
    def login(self):
        self.driver.get('https://app.podia.com/community/topics/10973/posts/542822-join-plant-based-living-in-an-omnivore-household-wednesday-october-9-2024-at-7pm-mst')
    
    def access_community(self):
        self.driver.get('https://app.podia.com/community')
        time.sleep(30)
        self.close()
    

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    padia = PodiaScrapping()
    padia.access_community()
    padia.close()
    