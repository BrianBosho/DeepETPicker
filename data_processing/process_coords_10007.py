import os
import shutil
import json

def create_directory(directory_path):
    """Creates a directory if it does not exist."""
    os.makedirs(directory_path, exist_ok=True)

def convert_ndjson_to_coords(ndjson_path, coords_path):
    """Converts an ndjson file to a coords file."""
    with open(ndjson_path, 'r') as ndjson_file, open(coords_path, 'w') as coords_file:
        for line in ndjson_file:
            data = json.loads(line)
            x, y, z = data["location"]["x"], data["location"]["y"], data["location"]["z"]
            coords_file.write(f"1 {x} {y} {z}\n")
    print(f"Converted {ndjson_path} to {coords_path}")

def process_folder_for_ndjson(folder_path, folder_name, raw_data_dir):
    """Processes a folder to handle ndjson and coords files."""
    ndjson_file = os.path.join(folder_path, f'{folder_name}.ndjson')
    dest_ndjson_file = os.path.join(folder_path, f'{folder_name}.ndjson')
    dest_coords_file = os.path.join(folder_path, f'{folder_name}.coords')

    # Check and copy ndjson file
    if os.path.isfile(ndjson_file):
        if not os.path.isfile(dest_ndjson_file):
            shutil.copy2(ndjson_file, dest_ndjson_file)
            print(f"Copied {ndjson_file} to {dest_ndjson_file}")
        else:
            print(f"ndjson file already exists for folder {folder_name}")

        # Convert ndjson to coords file
        if not os.path.isfile(dest_coords_file):
            convert_ndjson_to_coords(dest_ndjson_file, dest_coords_file)
        else:
            print(f"coords file already exists for folder {folder_name}")

        # Move coords file to raw_data_dir
        new_coords_dest = os.path.join(raw_data_dir, f'{folder_name}.coords')
        if not os.path.isfile(new_coords_dest):
            shutil.copy2(dest_coords_file, new_coords_dest)
            print(f"Moved {dest_coords_file} to {new_coords_dest}")
        else:
            print(f"coords file already exists in raw_data directory for folder {folder_name}")
    else:
        print(f"No ndjson file found in folder {folder_name}")

def process_base_directory(base_dir, raw_data_dir):
    """Processes the base directory to handle all folders."""
    create_directory(raw_data_dir)

    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)

        if not os.path.isdir(folder_path):
            continue

        process_folder_for_ndjson(folder_path, folder, raw_data_dir)

# Define the base directory and raw data directory
base_dir = '10007_subset'
raw_data_dir = os.path.join(base_dir, 'coords_files')

# Process the base directory
process_base_directory(base_dir, raw_data_dir)
