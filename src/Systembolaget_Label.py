from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from wine import Wine
from file_loading_validation import load_url_file, input_validation
from label_creation import create_labels, create_output_docx
from resource_path import resource_path

# Input URL and index which is used to name it
# Output
def dataurl_data_fetcher(url, index):
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    exe_path = resource_path('./driver/chromedriver.exe')
    
    try:
        driver = webdriver.Chrome(executable_path=exe_path, chrome_options=chrome_options)

        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        driver.close()


    except Exception as e:
        with open("errorfile.txt", "w") as errorfile:
            errorfile.write(str(e)+"\n"+str(index)+"\n"+str(url))
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
        wine_name2 = page_html.find("h1", class_="css-3f5hx2 e1gytpgj0").next.next_sibling.contents[0]
    except Exception as e:
        wine_name2 = f"Failed to fetch wine sub name. {e} "

    try:
        # Gets the country and potentially region
        wine_location = page_html.find_all("p", class_="css-l7e9hy enp2lf70")[6].contents[0]
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
        wine_productnr = page_html.find("span", class_="css-1f2m4s6 enp2lf70").contents[0]
    except Exception as e:
        wine_productnr = f"Failed to fetch wine product number. {e} "

    try:
        # Gets the alcohole procentage
        wine_alc_procentage = page_html.find_all("p", class_="css-12l74ml er6ap680")[1].contents[0]
    except Exception as e:
        wine_alc_procentage = f"Failed to fetch wine alcohole procentage. {e} "

    try:
        # Get the suger content of the drink       
        wine_suger_content = page_html.find_all("p", class_="css-l7e9hy enp2lf70")[8].contents[0]
    except Exception as e:
        wine_suger_content = f"Failed to fetch wine sugar content. {e} "

    try:
        # Gets the taste and usage recommendations
        wine_taste_and_usage = page_html.find("p", class_="css-1cuz951 enp2lf70").contents[0]
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


def main():

    filen_name = "input.txt"
    pages = load_url_file(filen_name)
    # print(pages) Test output of load_url_file

    pages = input_validation(pages)
    # print(pages) #check that the validation works

    site_data = []  # Variable list with entries being site data
    for index, url in enumerate(pages):
        site_data.append(dataurl_data_fetcher(url, index))

    class_list_wines = []
    for site in site_data:
        class_list_wines.append(extract_drink_data(site))

    try:  # remove for loops steppers.
        del site
    except:
        pass

    create_labels(class_list_wines)
    create_output_docx(class_list_wines)


if __name__ == "__main__":
    main()
