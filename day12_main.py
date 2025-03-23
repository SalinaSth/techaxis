# Entire module import
import data_load.day12_data_load as ddl
# from data_load import day12_data_load as ddl

# Using function in this module
filepath = "data/file-append.txt"
status, content = ddl.load_text_data('path/to/the/file')
# print(status, content)

if status:
    print(content)
else:
    print("File doesn't exist.")

#################################################################

#Import particular function from a module
from data_load.day12_data_load import load_text_data, load_excel_data
filepath = 'data/file-append.txt'
status, content = load_text_data(filepath)
load_excel_data(filepath)
