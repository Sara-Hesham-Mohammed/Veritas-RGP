import pandas as pd
import glob

# folder path
folder_path = "E:\Veritas Debate League\Registration"

def merge_excel_files(end_path):
    """
    @param end_path: List of file paths to Excel files
    @return: Final DataFrame containing data from all Excel files
    """

    excel_files = glob.glob(f"{folder_path}/{end_path}/*.xlsx")

    dataframes = [pd.read_excel(file) for file in excel_files]
    for df in dataframes:
        # Convert column to numeric type
        df['Speaker 1 Phone'] = df['Speaker 1 Phone'].astype('str')
        df['Speaker 2 Phone'] = df['Speaker 2 Phone'].astype('str')
        df['Speaker 3 Phone'] = df['Speaker 3 Phone'].astype('str')
        df.drop_duplicates(keep="last")
        df.astype(str)
        df.info()
        print(df.dtypes)

    final_df = pd.concat(dataframes, ignore_index=True).astype(str)

    final_df.to_excel(f"E:/Veritas Debate League/Registration/{end_path}.xlsx", index=False)
    print(final_df.head())  # Display the first few rows
    print(final_df.columns)  # Display the first few rows
    return final_df


merge_excel_files("High School")
# merge_excel_files("Middle School")