import os
import sys
import time
import datetime

from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Browser:
    browser, service = None, None

    def __init__(self):
        options = ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--kiosk")

        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        
        self.browser = webdriver.Chrome(options=options)

    def open_page(self, url):
        self.browser.get(url)

    def close(self):
        self.browser.close()

    def refresh(self):
        self.browser.refresh()

    def add_input(self, by, value, text):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)

    def click_submit(self, by, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()

    def login(self, password: str):
        self.add_input(by=By.CLASS_NAME, value='form-control', text=password)
        self.click_submit(by=By.CLASS_NAME, value='btn-primary')


def get_password():
	with open(f"/home/bszw/Documents/raspi-kiosk/pw.txt", newline='') as f:
		reader = csv.reader(f, delimiter=';', quotechar=' ')
		for row in reader:
			return row[0]

def main(args):
    try:
        url = sys.argv[1]
    except:
        url = "https://google.de" #Default

    browser = Browser()
    browser.open_page(url)

    browser.login(get_password())

    while (1):
        browser.refresh()

        now = datetime.datetime.now()
        
        #Kritisch: Was ist, wenn man den Raspberry nach 18 Uhr startet, schaltet er sich gleich wieder ab!
        today6pm = now.replace(hour=17, minute=59, second=0, microsecond=0)
        
        if now > today6pm:
            #os.system('sudo shutdown -h 0')
            print("SHUTDOWN")

        time.sleep(10)
