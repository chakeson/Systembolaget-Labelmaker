# Systembolaget-Labelmaker
Uses webscraping to take and url and create a label for the bottle.

# Purpose
My parent make label for their wine bottles to know what the wine fits with and what it contains and some other information.
This program automates this process. 

# How does it work?
It takes URL's in an input.txt (creates it if missing) and sorts the real URL's with regular expressions.
These validated URLs are then fetched with urlib and then parsed with regurlar expressions for the data which is put into a wine class.
It is then written to and output.txt file.

# Upgrades for next version
Maybe sys.argv inputs for nrs
Consider fancy labels:
https://pypi.org/project/pylabels/
https://pypi.org/project/blabel/

Make output docx:
https://github.com/python-openxml/python-docx
https://python-docx.readthedocs.io/en/latest/user/quickstart.html
