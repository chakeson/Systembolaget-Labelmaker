from data_fetch import dataurl_data_fetcher, extract_drink_data
from driver.chrome import create_chrome_driver
from file_loading_validation import input_validation, load_url_file
from label_creation import create_labels, create_output_docx


def main():

    filen_name = "input.txt"
    pages = load_url_file(filen_name)
    # print(pages) Test output of load_url_file

    pages = input_validation(pages)
    # print(pages) #check that the validation works

    print("Creating chrome driver")
    driver = create_chrome_driver()
    print("Starting the scraping process.")
    site_data = []  # Variable list with entries being site data
    for index, url in enumerate(pages):
        site_data.append(dataurl_data_fetcher(url, index, driver))
    driver.close()
    print(f'Scraped {len(site_data)} number of wine pages.')

    class_list_wines = []
    for site in site_data:
        class_list_wines.append(extract_drink_data(site))

    try:  # remove for loops steppers.
        del site
    except:
        pass
    
    print("Creating labels.")
    create_labels(class_list_wines)
    create_output_docx(class_list_wines)


if __name__ == "__main__":
    try:
        print("Launching program.")
        main()
        print("Program has ended.")
    except Exception as e:
        print(e)
        input("Press Enter to exit.")
