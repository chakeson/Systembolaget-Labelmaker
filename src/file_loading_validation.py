import re, sys

# Input 1 string
# Output list o
def load_url_file(file_to_load):
    
    try:
        with open(file_to_load, "r", encoding="utf-8") as urls:  # Opens the file with the URLs
            file_content = urls.readlines()
    except:
        print(
            "Missing input txt file. Creating that now as input.txt. PLease enter the URLS, row separated"
        )
        with open("input.txt", "w") as new_file:
            new_file = open("input.txt", "w")
            new_file.write("\n")

        sys.exit()

    for row in range(len(file_content)):
        file_content[row] = file_content[row].strip("\n")

    return file_content


# Input list with user input
# Output None, removes invalid input and prints what input was wrong and then returns the fixed list
def input_validation(list_of_pages):

    # Regular expression to practice, easier way is probably too just check if the first X characters of the string match one of the valid url versions.
    pattern_regex_website = re.compile(
        r"^(https:\/\/www.systembolaget.se/produkt/|http:\/\/www.systembolaget.se/produkt/|https:\/\/www.systembolaget.se/\d*)"
    )
    # pattern_regex_generated = re.compile(r'^https://www\.systembolaget\.se/produkt/[a-zA-Z]+/[a-zA-Z]+-[0-9]+/$')

    # check for number inputs
    pattern_regex_nr = re.compile(r"^(\d*)")
    for iterator in range(len(list_of_pages)):
        result = pattern_regex_nr.findall(list_of_pages[iterator])
        if result[0] != "":
            list_of_pages[iterator] = "https://www.systembolaget.se/" + str(
                list_of_pages[iterator]
            )

    # check website inputs including the constructed ones in the previous loop
    validated_pages = []
    index = 0
    for page in list_of_pages:
        result = pattern_regex_website.findall(page)
        if result != []:
            validated_pages.append(page)
        else:
            print("Link on row " + str(index + 1) + " is broken.")

        index += 1

    return validated_pages
