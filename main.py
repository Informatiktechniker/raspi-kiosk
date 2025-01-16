import os
import sys
import time

from dotenv import load_dotenv
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    browser, service = None, None

    def __init__(self):
        options = ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--kiosk")

        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)

        self.browser = Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def open_page(self, url):
        self.browser.get(url)

    def close(self):
        self.browser.close()

    def refresh(self):
        self.browser.refresh()

    def add_input(self, by: By, value, text):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_submit(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login(self, password: str):
        self.add_input(by=By.CLASS_NAME, value='form-control', text=password)
        self.click_submit(by=By.CLASS_NAME, value='btn-primary')


def get_password():
    pw = os.environ.get("DIGIKABU_PASSWORD")
    if pw == None:
        load_dotenv()
        pw = os.getenv("DIGIKABU_PASSWORD")

    return pw


def main(args):
    print(args)


if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except:
        url = "https://google.de"

    browser = Browser()
    browser.open_page(url)
    time.sleep(1)

    browser.login(get_password())

    while (1):
        browser.refresh()
        time.sleep(10)
