# Systembolaget-Labelmaker
Uses webscraping to take and url and create a label for the bottle.
![Preview of program](https://github.com/chakeson/Systembolaget-Labelmaker/blob/main/base.png)

# Purpose
My parent make labels for their wine bottles to know what the wine fits with and what it contains and some other information.
This program automates this process. 

# How does it work?
It takes URL's in an input.txt (creates it if missing) and sorts the real URL's with regular expressions.
These validated URLs are then fetched with urlib and then parsed with regurlar expressions for the data which is put into a wine class.
It is then written to and output.txt file.

# Code
Code was formated by python black. Python-docx for creating the word document for print out ontop of output.txt

# Upgrades for next version
Add GUI
