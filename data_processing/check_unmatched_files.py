import os

def check_and_list_unmatched_files(base_dir):
    """
    Checks if each .coords file has a corresponding .mrc file in the given directory structure.
    Lists the files that do not have counterparts.

    Args:
        base_dir (str): The base directory containing folders with .coords and .mrc files.
    """
    unmatched_files = []

    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)

        if not os.path.isdir(folder_path):
            continue

        coords_file = os.path.join(folder_path, f'{folder}.coords')
        mrc_file = os.path.join(folder_path, f'{folder}.mrc')

        if os.path.isfile(coords_file) and not os.path.isfile(mrc_file):
            unmatched_files.append(coords_file)
        elif os.path.isfile(mrc_file) and not os.path.isfile(coords_file):
            unmatched_files.append(mrc_file)

    if unmatched_files:
        print("The following files do not have counterparts:")
        for file in unmatched_files:
            print(file)
    else:
        print("All files have matching counterparts.")

    # total number of .coords files
    total_coords = len([file for file in os.listdir(base_dir) if file.endswith('.coords')])
    # total number of .mrc files
    total_mrc = len([file for file in os.listdir(base_dir) if file.endswith('.mrc')])

    print(f"Total number of .coords files: {total_coords}")
    print(f"Total number of .mrc files: {total_mrc}")

# Define the base directory
base_dir = '/home/brian_bosho/xulab/data/10007_subset/raw_data_denoised'

# Check and list unmatched files
check_and_list_unmatched_files(base_dir)
