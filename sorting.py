import pandas as pd
import os

def sort_by_time(input_file, output_dir):
    """
    Sorts data by date and time, grouping by rounded hours, and saves each group to an Excel file.
    Parameters:
        input_file (str): Path to the input CSV file.
        output_dir (str): Path to the output folder where hourly Excel files will be saved.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Ensure the 'valid' column is in datetime format
    df['valid'] = pd.to_datetime(df['valid'])
    
    # Round the time in the 'valid' column to the nearest hour
    df['valid_rounded'] = df['valid'].dt.ceil('H')
    
    # Create an output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Group the data by the rounded hour and save each group to a separate Excel file
    for hour, group in df.groupby('valid_rounded'):
        file_name = hour.strftime('%Y-%m-%d_%H-%M') + '.xlsx'
        output_file_path = os.path.join(output_dir, file_name)
        group.to_excel(output_file_path, index=False)
        print(f"Saved data for hour {hour} to {output_file_path}")

def sort_by_station(input_file, output_dir):
    """
    Sorts data by stations, grouping by the 'station' column, and saves each group to an Excel file.
    Parameters:
        input_file (str): Path to the input CSV file.
        output_dir (str): Path to the output folder where station-specific Excel files will be saved.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Ensure the 'station' column exists in the DataFrame
    if 'station' not in df.columns:
        raise ValueError("The column 'station' is missing in the input file.")
    
    # Create an output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Group the data by the 'station' column and save each group to a separate Excel file
    for station, group in df.groupby('station'):
        file_name = f"{station}.xlsx"
        output_file_path = os.path.join(output_dir, file_name)
        group.to_excel(output_file_path, index=False)
        print(f"Saved data for station {station} to {output_file_path}")

def sort_by_variable(input_file, variables, base_columns, output_dir):
    """
    Sorts data by variables, extracting data for each variable and saving to separate Excel files.
    Parameters:
        input_file (str): Path to the input CSV file.
        variables (list): List of variable columns to process (e.g., ['tmpf', 'dwpf']).
        base_columns (list): List of base columns to include (e.g., ['station', 'valid', 'lon', 'lat']).
        output_dir (str): Path to the output folder where variable-specific Excel files will be saved.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Ensure the 'valid' column is in datetime format
    df['valid'] = pd.to_datetime(df['valid'])
    
    for variable in variables:
        if variable in df.columns:  # Ensure the variable exists in the DataFrame
            columns_to_keep = base_columns + [variable]
            filtered_df = df[columns_to_keep]
            
            # Drop rows with missing values in the variable or base columns
            filtered_df = filtered_df.dropna(subset=[variable] + base_columns, how='any')
            
            # Drop columns with all missing values
            filtered_df = filtered_df.dropna(how='all', axis=1)
            
            # Create a folder for the variable
            variable_folder = os.path.join(output_dir, f"{variable}_Files")
            os.makedirs(variable_folder, exist_ok=True)
            
            # Save the cleaned DataFrame to an Excel file
            output_file_path = os.path.join(variable_folder, f"{variable}.xlsx")
            filtered_df.to_excel(output_file_path, index=False)
            print(f"Saved data for variable '{variable}' to {output_file_path}")
        else:
            print(f"Warning: Variable '{variable}' not found in the data.")
