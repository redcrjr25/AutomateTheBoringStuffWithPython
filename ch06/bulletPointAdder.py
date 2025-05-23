# Project: Adding Bullets to Wiki Markup
#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip  # type: ignore

text = pyperclip.paste()
# Sepaarate lines and add stars.
lines = text.split("\n")
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[i] = "* " + lines[i]  # add star to each string in "lines" list
text = "\n".join(lines)
print(text)  # Add this line to print result to terminal
pyperclip.copy(text)
