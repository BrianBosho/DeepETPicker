import os
import shutil

# Define the base directory
base_dir = '10007_subset'
# Define the directory to store the copied .mrc files
output_dir = os.path.join(base_dir, 'mrc_files')

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize a counter for the number of .mrc files
mrc_file_count = 0

# Iterate over folders in the base directory
for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)

    if not os.path.isdir(folder_path):
        continue

    # Check for subfolders ending with .mrc
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)

        if subfolder.endswith('.mrc') and os.path.isdir(subfolder_path):
            # Locate the .mrc file within the subfolder
            for file in os.listdir(subfolder_path):
                if file.endswith('.mrc'):
                    mrc_file = os.path.join(subfolder_path, file)
                    # Define the destination path for the .mrc file
                    dest_path = os.path.join(output_dir, file)

                    # Check if the file already exists in the destination
                    if not os.path.isfile(dest_path):
                        # Copy the .mrc file to the output directory
                        shutil.copy2(mrc_file, dest_path)
                        print(f"Copied {mrc_file} to {dest_path}")
                        mrc_file_count += 1
                    else:
                        print(f"File {file} already exists in the destination. Skipping copy.")
                    break
            else:
                print(f"No .mrc file found in {subfolder_path}")

print(f"Total number of .mrc files processed: {mrc_file_count}")
