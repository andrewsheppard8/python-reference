"""
===============================================================================
Script Name:       Parcel CSV Processor
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-29

Description:
-------------
This script reads a parcel CSV file, performs data cleaning, enrichment, and QA tasks.
Specifically, it:

    - Fixes/renames headers
    - Filters parcels based on acreage (>1 acre)
    - Adds a new field 'SQ_FT' (converts acreage to square feet)
    - Adds a 'CHECK' flag for Residential parcels
    - Detects duplicate PARCEL_IDs and flags them in 'DUPLICATE'
    - Sorts parcels by acreage (descending) for easier review

Usage:
------
1. Update `file_path`, `input_file`, and `output_file` to your environment.
2. Run the script. The output CSV will include the new fields and sorted/enriched data.
3. Review flagged duplicates for QA purposes.

Notes:
------
- This script loads the entire CSV into memory, so very large datasets may require optimization.
- Fieldnames are currently fixed; ensure input CSV columns match expected order or adjust `new_fields`.
===============================================================================
"""

import os
import glob
import shutil
import time

#Printing current directory of file
cwd=os.getcwd()
##print(cwd)

###listing all files in folder
##files=os.listdir('.')
##print(files)
##
###use glob to print all .py files in a folder
##py_files=glob.glob('*.py')
##print(py_files)

###using os.walk to traverse this folder recursively
##for dirpath, dirnames, filenames in os.walk(cwd):
##    for file in filenames:
##        if file.endswith('.csv'):
####            print(dirpath)
##            full_path = os.path.join(dirpath, file)
##            print(full_path)

#check for file existing and what type of object it is
##file_path=os.path.join(cwd,'csv_module.py')
##check_exist=os.path.exists(file_path)
##if check_exist:
##    print ("This object exists")
##check_file=os.path.isfile(file_path)
##if check_file:
##    print("This object is a file")
##check_folder=os.path.isdir(file_path)
##if check_folder:
##    print("This object is a folder")

#printing directory/file name from file path
##file_path=os.path.join(cwd,'csv_module.py')
##print(os.path.basename(file_path))
##print(os.path.dirname(file_path))

#split name of file, name and file extension type
##file='csv_module.py'
##name,ext=os.path.splitext(file)
##print(name)
##print(ext)

#batch rename
##for f in os.listdir(cwd):
##    if f.endswith(".py"):
##        old_path = os.path.join(cwd, f)
##        new_path = os.path.join(cwd, f.replace(" ", "_"))
##        os.rename(old_path, new_path)
##        print(f"{f} renamed")

#count number of files
csv_files=glob.glob(os.path.join(cwd,"*.csv"),recursive=True)
print("Number of CSV files: ", len(csv_files))

#Move files using the shutil module
##for csv in csv_files:
##    shutil.move(csv, r"C:\Users\andre\Desktop\GIT Resources\Python_Practice\Export")
##    print(f"{csv} moved to new location")

for csv in csv_files:
    if time.time() - os.path.getmtime(csv) < 7*24*3600: #modified in last 7 days
        print(csv)
    
