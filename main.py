import pandas as pd

'''
@:param file_paths: List of file paths to Excel files
@:return: Final DataFrame containing data from all Excel files
'''

# files path
file_paths = []

# loop through each and load them into a dataframe
for file in file_paths:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file)
    print(df.head()) # Display the first few rows