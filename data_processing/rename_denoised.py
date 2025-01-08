import os

def rename_files_in_folder(folder_path):
    # Iterate through all files in the given folder
    for filename in os.listdir(folder_path):
        # Check if the file has a .coords extension
        if filename.endswith('.coords'):
            # Create the new filename by appending _denoised before the extension
            new_filename = filename.replace('.coords', '_denoised.coords')
            # Construct the full file paths
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Example usage
folder_path = '/home/brian_bosho/xulab/data/10007_subset/raw_data_denoised'
rename_files_in_folder(folder_path)