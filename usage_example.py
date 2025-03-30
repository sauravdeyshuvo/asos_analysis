from asos_analysis.sorting import sort_by_time, sort_by_station, sort_by_variable
from asos_analysis.cleaning import remove_duplicates
from asos_analysis.formats import list_unique_formats
from asos_analysis.reformat import standardize_datetime

# Define file paths
input_file = r"D:\tutorials\iss2025\ND_feb12.csv"
output_time = r"D:\tutorials\iss2025\Hourly_Files"
output_station = r"D:\tutorials\iss2025\Station_Files"
output_variables = r"D:\tutorials\iss2025\Variables_Files"

# Define variables and base columns for sorting by variables
variables = ['tmpf', 'dwpf', 'relh', 'drct', 'sknt', 'p01i', 'alti', 'mslp',
             'vsby', 'gust', 'skyc1', 'skyc2', 'skyc3', 'skyc4',
             'skyl1', 'skyl2', 'skyl3', 'skyl4']
base_columns = ['station', 'valid', 'lon', 'lat', 'elevation']

# Perform sorting by time
print("Sorting by time...")
sort_by_time(input_file, output_time)
print("Sorting by time completed!")

# Perform sorting by stations
print("Sorting by station...")
sort_by_station(input_file, output_station)
print("Sorting by station completed!")

# Perform sorting by variables
print("Sorting by variables...")
sort_by_variable(input_file, variables, base_columns, output_variables)
print("Sorting by variables completed!")

# Perform cleaning (removing duplicates)
input_folder = r"D:\tutorials\iss2025"
print("Removing duplicate entries...")
remove_duplicates(input_folder)
print("Duplicate removal completed!")

# List unique date-time formats
print("Listing unique date-time formats...")
unique_formats = list_unique_formats(input_folder)
print("Unique date-time formats detected:")
for fmt in unique_formats:
    print(fmt)

# Standardize date-time format
print("Standardizing date-time format...")
standardize_datetime(input_folder)
print("Date-time standardization completed!")
