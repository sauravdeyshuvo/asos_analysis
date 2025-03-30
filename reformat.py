import os
import pandas as pd

def standardize_datetime(input_folder, target_format="%Y-%m-%d %H:%M:%S"):
    """
    Standardizes the date-time format in the 'valid' column across all Excel files in a folder.
    Parameters:
        input_folder (str): Path to the folder containing Excel files.
        target_format (str): Desired date-time format to apply (default: '%Y-%m-%d %H:%M:%S').
    Returns:
        list: A list of file paths that were modified.
    """
    modified_files = []  # List to track modified files

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                try:
                    # Read the Excel file
                    df = pd.read_excel(file_path)
                    
                    # Check if the 'valid' column exists
                    if 'valid' in df.columns:
                        # Keep a copy of the original column for comparison
                        original_valid = df['valid'].copy()
                        
                        # Standardize the date-time format
                        df['valid'] = pd.to_datetime(df['valid'], errors='coerce')  # Convert to datetime
                        df['valid'] = df['valid'].dt.strftime(target_format)  # Apply the target format
                        
                        # Check if any changes were made
                        if not df['valid'].equals(original_valid):
                            # Save the modified DataFrame back to the same file
                            df.to_excel(file_path, index=False)
                            modified_files.append(file_path)  # Record the modified file
                            print(f"Modified file: {file_path}")
                
                except Exception as e:
                    print(f"Error processing file '{file_path}': {e}")
    
    return modified_files
