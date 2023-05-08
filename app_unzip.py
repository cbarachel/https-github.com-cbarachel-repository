import os
import zipfile

# Set the directory paths
zip_dir = 'worldbank_zipfiles'
data_dir = 'worldbank_data'

# Create the data directory if it does not exist
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

# Create a list of zip files in the zip directory
zip_files = [f for f in os.listdir(zip_dir) if f.endswith('.zip')]

# Loop over the zip files and extract their contents
for zip_file in zip_files:
    with zipfile.ZipFile(os.path.join(zip_dir, zip_file), 'r') as zip_ref:
        zip_ref.extractall(data_dir)
