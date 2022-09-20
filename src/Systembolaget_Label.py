from file_loading_validation import load_url_file, input_validation
from label_creation import create_labels, create_output_docx
from data_fetch import dataurl_data_fetcher, extract_drink_data

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
