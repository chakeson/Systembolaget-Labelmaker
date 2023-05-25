# Systembolaget-Labelmaker
Uses webscraping to take and url and create a label for the bottle.
![Preview of program](https://github.com/chakeson/Systembolaget-Labelmaker/blob/main/base.png)

# Purpose
My parent make labels for their wine bottles to know what the wine fits with and what it contains and some other information.
This program automates this process. 


# Build instructions
The py installer spec was created with:

```pyi-makespec Systembolaget_Label.py --onefile```

To run the executable creation run:

```pyinstaller --clean Systembolaget_Label.spec```

--clean ensures all temporary files and caches are removed before building the executable.



# How does it work?
It takes URL's in an input.txt (creates it if missing) and sorts the real URL's with regular expressions.
These validated URLs are then fetched with selenium, and then parsed with beautifulsoup4 for the data which is put into a wine class.
It is then written to and output.txt and output.docx file.

# Code
Code was formated by python black. Python-docx for creating the word document for print out ontop of output.txt
Uses selenium to scrape it since it allows for running of the Javascript to populate the page. The site is based on Next Js.Uses the built-in html parser.

## Testing
We test with three wines to catch most cases. 

256601 for a wine without full name.

225701 a wine with multiple bottle types.

626301 wine with higher price and diffrent location data, non integer alcohol procentage.

# Notes

This uses the chromium webdriver because the firefox one has alot of small edges and versions which are incompatible with selenium. Thus using the chromium webdriver I saved alot of time and effort. It quite frankly seems like the chromium one is getting all the attantion and developer time. The webdriver is downloaded and handled by the webdriver managment library. For a manual set up get the lastest chromium driver download it [here](https://chromedriver.chromium.org/downloads)

## Upgrades for next version
Add GUI

## TODO

Split out constants

Create tests

Consider adding an icon.

Consider adding python black in with a (github action)[https://black.readthedocs.io/en/stable/integrations/github_actions.html]
