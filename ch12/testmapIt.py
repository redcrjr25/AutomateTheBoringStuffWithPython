#! /usr/bin/env python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line arguments
    address = " ".join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

# Create Google Maps URL
url = "https://www.google.com/maps/place/" + address.replace(" ", "+")

# Open in web browser
webbrowser.open(url)
