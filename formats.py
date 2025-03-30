import os
import pandas as pd
from datetime import datetime

def detect_format(date_string):
    """
    Detects the date-time format of a given string.
    Parameters:
        date_string (str): The date-time string to analyze.
    Returns:
        str or None: The detected date-time format or None if no format matches.
    """
    date_formats = [
        "%Y-%m-%d %H:%M:%S",  # Example: 2020-02-12 00:52:00
        "%Y-%m-%d %H:%M",     # Example: 2020-02-12 00:52
        "%m/%d/%Y %H:%M:%S",  # Example: 02/12/2020 00:52:00
        "%m/%d/%Y %H:%M",     # Example: 02/12/2020 00:52
        "%Y/%m/%d %H:%M:%S",  # Example: 2020/02/12 00:52:00
        "%Y/%m/%d %H:%M"      # Example: 2020/02/12 00:52
    ]
    for fmt in date_formats:
        try:
            datetime.strptime(date_string, fmt)
            return fmt
        except ValueError:
            continue
    return None  # If no format matches

def list_unique_formats(input_folder):
    """
    Lists all unique date-time formats in the 'valid' column across Excel files in a folder.
    Parameters:
        input_folder (str): Path to the folder containing Excel files.
    Returns:
        set: A set of unique detected date-time formats.
    """
    unique_formats = set()

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                try:
                    # Read the Excel file
                    df = pd.read_excel(file_path)

                    # Check if the 'valid' column exists
                    if 'valid' in df.columns:
                        # Detect formats in the 'valid' column
                        for value in df['valid'].dropna():
                            date_str = str(value)
                            detected_format = detect_format(date_str)
                            if detected_format:
                                unique_formats.add(detected_format)
                            else:
                                print(f"Unrecognized format in file '{file}', value: {date_str}")
                
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

    return unique_formats
