from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from wine import Wine

# import time

# Input URL, index, webdriver which is used to fetch it
# Output soup of page
def dataurl_data_fetcher(url, index, driver):

    try:
        driver.get(url)
        # time.sleep(3) # Debug broken page waits.
        test = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-3f5hx2"))
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
        wine_name = page_html.find("h1", class_="css-3f5hx2 e1gytpgj0").next.contents[0]
    except Exception as e:
        wine_name = f"Failed to fetch wine name. {e} "

    try:
        # Gets sub name
        wine_name2 = page_html.find(
            "h1", class_="css-3f5hx2 e1gytpgj0"
        ).next.next_sibling.contents[0]
    except Exception as e:
        wine_name2 = f"Failed to fetch wine sub name. {e} "

    try:
        # Gets the country and potentially region
        wine_location = page_html.find_all("p", class_="css-l7e9hy enp2lf70")[
            6
        ].contents[0]
    except Exception as e:
        wine_location = f"Failed to fetch wine location 1. {e} "

    try:
        # Gets the wine price
        wine_price = page_html.find("p", class_="css-mzsruq enp2lf70").contents[0]
        wine_price = wine_price[0:-2]
    except Exception as e:
        wine_price = f"Failed to fetch wine price. {e} "

    try:
        # Gets the systembolaget productnr
        wine_productnr = page_html.find("span", class_="css-1f2m4s6 enp2lf70").contents[
            0
        ]
    except Exception as e:
        wine_productnr = f"Failed to fetch wine product number. {e} "

    try:
        # Gets the alcohole procentage
        wine_alc_procentage = page_html.find_all("p", class_="css-12l74ml er6ap680")[
            1
        ].contents[0]
    except Exception as e:
        wine_alc_procentage = f"Failed to fetch wine alcohole procentage. {e} "

    try:
        # Get the suger content of the drink
        wine_suger_content = page_html.find_all("p", class_="css-l7e9hy enp2lf70")[
            8
        ].contents[0]
    except Exception as e:
        wine_suger_content = f"Failed to fetch wine sugar content. {e} "

    try:
        # Gets the taste and usage recommendations
        wine_taste_and_usage = page_html.find(
            "p", class_="css-1cuz951 enp2lf70"
        ).contents[0]
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
