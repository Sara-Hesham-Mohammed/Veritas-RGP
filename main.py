import pandas as pd
import glob
import duckdb

# folder path
folder_path = "E:/Veritas Debate League/Registration/Feb. 7"

def validity_check(df):
    if df[df['col'].isna()]:
        pass



def merge_excel_files(end_path):
    """
    @param end_path: List of file paths to Excel files
    @return: Final DataFrame containing data from all Excel files
    """

    excel_files = glob.glob(f"{folder_path}/{end_path}/*.xlsx")

    dataframes = []
    for file in excel_files:
        try:
            df = pd.read_excel(file,  sheet_name='Template')
            dataframes.append(df)
        except Exception as e:
            print(f"Could not read {file.title}: {e}")

    for df in dataframes:
        try:
            # Convert all columns to string (modify original)
            df.astype(str)
        except Exception as e:
            print(f"Exception in dataframe with columns {list(df.columns)}: {e}")

    final_df = pd.concat(dataframes, ignore_index=True).astype(str)

    final_df.to_excel(f"{folder_path}/{end_path}.xlsx", index=False)
    return final_df

def tabroom_format(file, end_path):
    """
    @param file: Excel file path
    @return: DataFrame formatted for Tabroom import
    currently has error of no output in whatever row that doesnt have one of the selected columns filled. NEED TO FIX
    """
    df = pd.read_excel(file)

    # Example formatting steps (customize as needed)
    df['Speaker Names'] = df['Speaker 1 Last'] + ' & ' + df['Speaker 2 Last'] + ' & ' + df['Speaker 3 Last']
    df['School'] = df['School Name']

    # Select relevant columns for Tabroom
    tabroom_df = df[['Speaker Names','School']]

    tabroom_df.to_excel(f"{folder_path}\Tabroom-{end_path}.xlsx", index=False)
    return tabroom_df


merge_excel_files("High School")
merge_excel_files("Middle School")
