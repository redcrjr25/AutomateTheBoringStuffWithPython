#! /usr/bin/env python3

# readCensusExcel.py - Tabulates population and number of census tracts for each county.

import openpyxl, pprint

print("Opening workbook...")
wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb["Population by Census Tract"]
countyData = {}

# TODO: Fill in countyData with each county's population and tracts.

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    # Make sure the key for this state exists.
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {"tracts": 0, "pop": 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]["tracts"] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]["pop"] += int(pop)

# Open a new text file and write the contents of countyData to it.
print("Writing results...")
resultFile = open("census2010.py", "w")
resultFile.write("allData = " + pprint.pformat(countyData))
resultFile.close()
print("Done.")
