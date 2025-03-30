import os
import pandas as pd

def remove_duplicates(input_folder, columns_to_check=['station', 'valid', 'lon', 'lat']):
    """
    Removes duplicate entries from all Excel files in the given folder.
    Parameters:
        input_folder (str): Path to the folder containing Excel files.
        columns_to_check (list): List of columns to check for duplicates.
    """
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                try:
                    # Read the Excel file into a DataFrame
                    df = pd.read_excel(file_path)

                    # Ensure the relevant columns exist in the DataFrame
                    missing_columns = [col for col in columns_to_check if col not in df.columns]
                    if missing_columns:
                        print(f"Skipping {file_path}: Missing columns {missing_columns}")
                        continue

                    # Identify duplicate rows based on the specified columns
                    duplicates = df.duplicated(subset=columns_to_check, keep='first')

                    # Print details of duplicate entries
                    duplicate_indices = df[duplicates].index.tolist()
                    if duplicate_indices:
                        print(f"Duplicate rows in file '{file}' (folder: {root}): {duplicate_indices}")

                    # Remove duplicate rows, keeping only the first occurrence
                    df_cleaned = df.drop_duplicates(subset=columns_to_check, keep='first')

                    # Save the cleaned DataFrame back to the same Excel file
                    df_cleaned.to_excel(file_path, index=False)

                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

    print("Duplicate cleaning completed!")
