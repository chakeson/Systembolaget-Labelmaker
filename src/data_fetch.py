from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from wine import Wine

import time

# import time

# Input URL, index, webdriver which is used to fetch it
# Output soup of page
def dataurl_data_fetcher(url, index, driver):

    try:
        driver.get(url)

        # Check if this is the first time opening. If it is press the age accept button.
        if index == 0:
            # Wait until the accept button has loaded.
            test = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="__next"]/div[1]/div[2]/div/section/div/div/div[3]/a[2]',
                    )
                )
            )
            driver.find_element(
                By.XPATH,
                '//*[@id="__next"]/div[1]/div[2]/div/section/div/div/div[3]/a[2]',
            ).click()  # Press the accept button.
            print('"Accepted" age button pressed.')

        # Wait until the page has loaded by checking until the wine title has loaded.
        # time.sleep(3) # Debug broken page waits.
        test = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-m7kuem"))
        )
        soup = BeautifulSoup(driver.page_source, "html.parser")

    except Exception as e:
        with open("errorfile.txt", "w") as errorfile:
            errorfile.write(str(e) + "\n" + str(index) + "\n" + str(url))
        print(e)
        return

    return soup


# Input string version of the site
# Output instance of class wine with the data filed.
def extract_drink_data(page_html):

    try:
        # Gets title name
        wine_name = page_html.find("h1", class_="css-1uk1gs8 e6czixi0").next.contents[0]
    except Exception as e:
        wine_name = f"Failed to fetch wine name. {e} "

    try:
        # Gets sub name
        wine_name2 = page_html.find(
            "h1", class_="css-1uk1gs8 e6czixi0"
        ).next.next_sibling.contents[0]
    except AttributeError as e:
        print(f"Failed to find sub name for wine {wine_name}.\nError:\n{e}")
        wine_name2 = (
            ""  # Most likely wine is like 256601 Gazella and has no second name.
        )
    except Exception as e:
        wine_name2 = f"Failed to fetch wine sub name. {e} "

    try:
        # Gets the country and potentially region
        wine_location = page_html.find_all("div", class_="css-chaqmn e12xogow0")
        wine_location = (
            wine_location[1].contents[0].text + ", " + wine_location[1].contents[1].text
        )
    except Exception as e:
        wine_location = f"Failed to fetch wine location 1. {e} "

    try:
        # Gets the wine price
        wine_price = page_html.find("p", class_="css-ylm6mu eqfj59s0").contents[0]
        wine_price = wine_price[0:-2]
    except Exception as e:
        wine_price = f"Failed to fetch wine price. {e} "

    try:
        # Gets the systembolaget productnr
        wine_productnr = page_html.find("span", class_="css-1sd13ch eqfj59s0").contents[
            0
        ]
    except Exception as e:
        wine_productnr = f"Failed to fetch wine product number. {e} "

    try:
        # Gets the alcohol procentage
        wine_alc_procentage = (
            page_html.find("div", class_="css-eb75o2 e12xogow0").contents[-1].text
        )
    except Exception as e:
        wine_alc_procentage = f"Failed to fetch wine alcohol procentage. {e} "

    try:
        # Get the suger content of the drink
        wine_suger_content = page_html.find_all("p", class_="css-1962of eqfj59s0")[
            8
        ].text
        # wine_suger_content = wine_suger_content[0:-8]  # '0,4 g/100ml' -> '0,4'
    except Exception as e:
        wine_suger_content = f"Failed to fetch wine sugar content. {e} "

    try:
        # Gets the taste and usage recommendations
        wine_taste_and_usage = page_html.find_all("p", class_="css-173act9 eqfj59s0")[
            20
        ].text
    except Exception as e:
        wine_taste_and_usage = f"Failed to fetch wine taste. {e} "

    # Create and fill the class with data and return it
    class_instance_wine = Wine(
        wine_name,
        wine_name2,
        wine_location,
        wine_price,
        wine_productnr,
        wine_alc_procentage,
        wine_suger_content,
        wine_taste_and_usage,
    )
    return class_instance_wine
