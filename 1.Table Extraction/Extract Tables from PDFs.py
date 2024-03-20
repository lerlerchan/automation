#remember to have the library install first
#pip install camelot-py

import camelot

# For the main modules of OpenCV
#pip install opencv-python

# If you need the full package including both main and contrib/extra modules
#pip install opencv-contrib-python

# For a headless version of OpenCV (without GUI functionality)
#pip install opencv-python-headless

import os

# Define the path to the new directory
new_directory = r'C:\Users\LerLerChan\Documents\GitHub\automation\1.Table Extraction'


# Change the current working directory to the new directory
os.chdir(new_directory)
# Get the current working directory
folder_path = os.getcwd()

# Print the current working directory to confirm the change
print("Current working directory:", os.getcwd())


try:
    # List all files and directories in the current working directory
    entries = os.listdir(folder_path)

    # Print all files (excluding directories)
    for entry in entries:
        full_path = os.path.join(folder_path, entry)
        if os.path.isfile(full_path):
            print(entry)
except Exception as e:
    print(f"An error occurred: {e}")



folder_link = os.getcwd()
file_path = f'{folder_link}\\foo.pdf'  # For Windows path

from PyPDF2 import PdfReader

# Open the PDF file
reader = PdfReader(file_path)

# Now you can use reader to access the PDF content
# For example, to print the text of each page
for page in reader.pages:
    print(page.extract_text())


# Read the PDF and print the tables
#tables = camelot.read_pdf(file_path, pages='1', flavor='lattice')
#tables1 = camelot.read_pdf('2.pdf', pages='1', flavor='stream')
#print(tables)

#tables.export('foo.csv', f='csv', compress=True)
#tables[0].to_csv('foo.csv')  # to a csv file
#print(tables[0].df)  # to a df
