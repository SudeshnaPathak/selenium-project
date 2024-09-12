from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium. webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

import time
from datetime import datetime

service = Service('chromedriver.exe')


def get_driver(link: str):
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")  # to prevent the infobars popups to interfere with the script
    options.add_argument("start-maximized")  # some webpages may change the content depending on the size of the window so we access the maximized version of the browser
    options.add_argument("disable-dev-shm-usage")  # to avoid issues while interacting with the browser on a linux computer and replit is a linux computer
    options.add_argument("no-sandbox")  # to disable sandbox in the browser
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(link)
    return driver

def main():
    link = 'https://maryvillegov.myebillingaccount.com/'

    driver = get_driver(link)