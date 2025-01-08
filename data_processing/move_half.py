import os
import shutil

# Define source and destination folders
source_folder = "/home/brian_bosho/xulab/data/10007_subset/raw_data_denoised"
destination_folder = "/home/brian_bosho/xulab/data/10007_subset/raw_data_denoised1"

# Get all .mrc files in the source folder
mrc_files = [f for f in os.listdir(source_folder) if f.endswith('.mrc')]

# Calculate the number of files to move (half of the total)
files_to_move = len(mrc_files) // 2

# Function to move a file and its corresponding .coords file
def move_file_pair(filename):
    base_name = os.path.splitext(filename)[0]
    
    # Move .mrc file
    mrc_source = os.path.join(source_folder, filename)
    mrc_dest = os.path.join(destination_folder, filename)
    shutil.move(mrc_source, mrc_dest)
    
    # Move corresponding .coords file if it exists
    coords_filename = f"{base_name}.coords"
    coords_source = os.path.join(source_folder, coords_filename)
    coords_dest = os.path.join(destination_folder, coords_filename)
    if os.path.exists(coords_source):
        shutil.move(coords_source, coords_dest)
        return True
    return False

# Move the first half of the files to the destination folder
moved_mrc = 0
moved_coords = 0

for file in mrc_files[:files_to_move]:
    moved_mrc += 1
    if move_file_pair(file):
        moved_coords += 1

print(f"Moved {moved_mrc} .mrc files to {destination_folder}")
print(f"Moved {moved_coords} corresponding .coords files to {destination_folder}")
