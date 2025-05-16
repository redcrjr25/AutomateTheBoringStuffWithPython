# Python Project Checklist for VS Code

Use this checklist before running Python scripts (e.g., Automate the Boring Stuff with Python projects) to ensure your environment, files, and setup are correct. Save this as python_project_checklist.md in your project folder for quick reference.

1. Confirm Project Directory

Goal: Ensure VS Code and the terminal are in the correct project folder.
Steps:
Open VS Code and navigate to your project folder (e.g., /Users/cjr/Projects/AutomateTheBoringStuffWithPython or a chapter subfolder like ch13).
Use File > Open Folder or drag the folder into VS Code.

Open the VS Code terminal (View > Terminal).
Check the current directory:pwd

Example output: /Users/cjr/Projects/AutomateTheBoringStuffWithPython/ch13

If in the wrong directory, navigate to the correct one:cd /Users/cjr/Projects/AutomateTheBoringStuffWithPython/ch13

Check: The terminal’s directory matches where your script (e.g., readCensusExcel.py) is located.

2.Verify Script and Required Files

Goal: Confirm your Python script and any required files (e.g., censuspopdata.xlsx) are in the project directory.
Steps:
List files in the terminal:ls

Look for your script (e.g., readCensusExcel.py) and any required files (e.g., censuspopdata.xlsx).

If a file is missing (e.g., censuspopdata.xlsx):
Check its location:find ~/Documents -name "censuspopdata.xlsx"

Move it to the project directory:mv /path/to/censuspopdata.xlsx /Users/cjr/Projects/AutomateTheBoringStuffWithPython/ch13

Or update the script with the full path:wb = openpyxl.load_workbook("/path/to/censuspopdata.xlsx")

Open the script in VS Code and ensure it’s saved with the correct name (e.g., readCensusExcel.py).

Check: All required files are listed by ls, and the script opens correctly in VS Code.

3.Activate Virtual Environment

Goal: Ensure you’re using the correct Python version and dependencies (e.g., Python 3.9.6, openpyxl 2.6.2).
Steps:
Activate the virtual environment:source /Users/cjr/Projects/AutomateTheBoringStuffWithPython/.venv/bin/activate

The prompt should show (.venv).

Verify Python version:python --version

Should show Python 3.9.6 (or your project’s version).

Check required packages:pip list

Ensure openpyxl, pyperclip, etc., are installed (e.g., openpyxl==2.6.2 for book compatibility).
Install missing packages:pip install openpyxl==2.6.2

Check: Terminal prompt shows (.venv), Python version is correct, and required packages are installed.

4.Check Code for Errors

Goal: Ensure the script is free of syntax errors and matches the book’s example.
Steps:
Open the script in VS Code and review for typos (e.g., countyData vs. county.Data).
Compare with the book’s code or online resources (e.g., <https://nostarch.com/automatestuff2/>).
Add debug prints if needed:print(f"Max rows: {sheet.max_row}")

Save the file (File > Save or Command + S).

Check: Script matches the book’s example, and no obvious errors are present.

5.Run the Script

Goal: Execute the script and verify output.
Steps:
Run the script in the VS Code terminal:python readCensusExcel.py

Watch for errors or output (e.g., “Opening workbook... Done.”).
If errors occur, note the message and troubleshoot (see Step 6).
Check for output files (e.g., census2010.py):ls

- Test the output (if applicable):
  <!-- markdownlint-disable MD052 -->
  ```python
  import census2010
  print(census2010.allData['AK']['Anchorage']['pop'])

Check: Script runs without errors, and expected output (e.g., file or terminal output) is produced.

6.Troubleshoot Issues

Goal: Address common errors quickly.
Common Issues:
FileNotFoundError: File (e.g., censuspopdata.xlsx) is missing or path is wrong. Move file or update path.
KeyError: Sheet name is incorrect. Open the Excel file to confirm the sheet name (e.g., “Population by Census Tract”).
ModuleNotFoundError: Missing package. Install it (e.g., pip install openpyxl).
PermissionError: Can’t write to directory. Move project to a writable folder:mv ./* ~/project
cd ~/project

No Output: Add debug prints to check loop execution:for row in range(2, sheet.max_row + 1):
    print(f"Row {row}: {sheet['B' + str(row)].value}")

Check: Issue is resolved, and script runs successfully.

7.Save and Document

Goal: Keep your project organized and reusable.
Steps:
Save all files (Command + S in VS Code).
Commit changes to GitHub (if using):git add .
git commit -m "Completed Chapter 13 project"
git push origin main

Note any modifications or issues in a project log (e.g., a text file or README.md).

Check: Project files are saved, and changes are committed to GitHub.

Notes

File Extensions: Ensure scripts use .py (not .pyw unless specified, as .pyw may affect GitHub syncing).
VS Code Tips: Use the “Run” button or F5 to run scripts, and check the “Problems” tab for syntax errors.
Book Resources: Download files or check code at <https://nostarch.com/automatestuff2/>.
Stuck?: Search the error message online or ask for help, providing:
Script name and chapter.
Error message.
Terminal output.
