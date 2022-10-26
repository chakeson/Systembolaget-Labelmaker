from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_chrome_driver():

    chrome_options = Options()
    # chrome_options.add_argument("--headless") # TODO Fix seems to break when on.
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), chrome_options=chrome_options
    )

    return driver
