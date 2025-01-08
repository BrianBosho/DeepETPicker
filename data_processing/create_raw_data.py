import os
import shutil
import json
import mrcfile

# define the base directory
base_dir = '10007_subset'
raw_data_dir = os.path.join(base_dir, 'raw_data')
# Create the raw_data directory if it doesn't exist
os.makedirs(raw_data_dir, exist_ok=True)
# copy the ndjson and mrc file to the raw_data directory


def convert_ndjson_to_coords(ndjson_path, coords_path):
    """Converts an ndjson file to a coords file."""
    with open(ndjson_path, 'r') as ndjson_file, open(coords_path, 'w') as coords_file:
        for line in ndjson_file:
            data = json.loads(line)
            x, y, z = data["location"]["x"], data["location"]["y"], data["location"]["z"]
            coords_file.write(f"1 {x} {y} {z}\n")
    print(f"Converted {ndjson_path} to {coords_path}")

num_mrc_files = 0
num_ndjson_files = 0
# print the name of all folders in the base directory
for folder in os.listdir(base_dir):
    folder_name = folder
    # inside the folder search for other folders containing a .mrc in the name
    for subfolder in os.listdir(os.path.join(base_dir, folder)):
        if '.mrc' in subfolder:
            mrc_file = os.path.join(base_dir, folder, subfolder)
            # print mrc file path
            print(f"mrc file path: {mrc_file}")
            num_mrc_files += 1           
    
    # in the folder search for the ndjson file
    for subfolder in os.listdir(os.path.join(base_dir, folder)):
        if '.ndjson' in subfolder:
            ndjson_file = os.path.join(base_dir, folder, subfolder)
            # rename a copy the ndjson file to the folder name first check if uit exists
            
            dest_ndjson_file = os.path.join(base_dir, folder, folder_name + '.ndjson')
            # check if the file exists with the name of the folder dest_ndjson_file
            if os.path.isfile(dest_ndjson_file):
                print(f"ndjson file already exists for folder {folder}")
            else:
                shutil.copy2(ndjson_file, dest_ndjson_file)

            # convert the ndjson file to coords file
            dest_coords_file = os.path.join(base_dir, folder, folder_name + '.coords')
            # if there is no coords file for the folder convert the ndjson file to coords file
            if not os.path.isfile(dest_coords_file):
                convert_ndjson_to_coords(dest_ndjson_file, dest_coords_file)
            else:
                print(f"coords file already exists for folder {folder}")           
            
            num_ndjson_files += 1
        else:
            print(f"ndjson file not found for folder {folder}")
    
    print(f"Number of mrc files: {num_mrc_files}")
    print(f"Number of ndjson files: {num_ndjson_files}")



# loop through each folder, find the .mrc and .coords files and copy them to the new folder called raw data
for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    
    mrc_file = os.path.join(folder_path, f'{folder}.mrc')
    # mrc_file = mrc_folder 

    # check for ndjson file
    ndjson_file = os.path.join(folder_path, f'{folder}.ndjson')
    coords_file = os.path.join(folder_path, f'{folder}.coords')

    # move the mrc file to the raw_data directory
    # chek subfolder for mrc files
    for subfolder in os.listdir(folder_path):
        if '.mrc' in subfolder:
            mrc_folder = os.path.join(folder_path, subfolder)
            # mrc file is sinside mrc folder with same name
            mrc_file = os.path.join(mrc_folder, f'{folder}.mrc')
            print(f"mrc file path: {mrc_file}")
            # move the file to the raw_data directory
            new_mrc_dest = os.path.join(raw_data_dir, f'{folder}.mrc')
            # check if new_mrc_dest exists
            if not os.path.isfile(new_mrc_dest):
                shutil.copy2(mrc_file, new_mrc_dest)
                print(f"copied {mrc_file} to {new_mrc_dest}")
            else:
                print(f"mrc file already exists for folder {folder}")
            
            break
    


    # move the coords file to the raw_data directory
    new_coords_dest = os.path.join(raw_data_dir, f'{folder}.coords')
    if os.path.isfile(coords_file):
        # check if file exists else copy
        if not os.path.isfile(new_coords_dest):
            shutil.copy2(coords_file, new_coords_dest)
            print(f"copied {coords_file} to {new_coords_dest}")
        else:
            print(f"coords file already exists for folder {folder}")
    else:
        print(f"coords file not found for folder {folder}")






            
            

