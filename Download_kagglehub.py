import kagglehub
import os
import shutil

# Download latest version
path = kagglehub.dataset_download("shubhambathwal/flight-price-prediction", force_download=True)

print(path)


# Define the target directory
data_dir = os.path.join(os.getcwd(), 'data')

# Create the directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)

# Get list of all files in the dataset directory
files = os.listdir(path)
print(files)

# Iterate over all the files and move them to the "data" directory
for file_name in files:
    # Construct full file path
    full_file_name = os.path.join(path, file_name)
    
    # Check if it's a file (not a directory) and move it
    if os.path.isfile(full_file_name):
        shutil.move(full_file_name, data_dir)

print("Files have been moved to the 'data' directory.")