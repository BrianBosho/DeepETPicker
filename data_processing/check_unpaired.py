import os

def clean_unpaired_files(directory):
    """
    Deletes files in the directory that do not have a corresponding counterpart with a different extension.

    Args:
        directory (str): Path to the directory containing .coords and .mrc files.
    """
    # Collect filenames without extensions for each file type
    coords_files = set()
    mrc_files = set()

    for file in os.listdir(directory):
        if file.endswith('.coords'):
            coords_files.add(os.path.splitext(file)[0])
        elif file.endswith('.mrc'):
            mrc_files.add(os.path.splitext(file)[0])

    # Identify unpaired files
    unpaired_coords = coords_files - mrc_files
    unpaired_mrc = mrc_files - coords_files

    # Report unpaired files
    print("Unpaired files:")
    for name in unpaired_coords:
        print(f"{name}.coords")
    for name in unpaired_mrc:
        print(f"{name}.mrc")

    # Delete unpaired files
    for name in unpaired_coords:
        coords_path = os.path.join(directory, f"{name}.coords")
        os.remove(coords_path)
        print(f"Deleted {coords_path}")
    
    for name in unpaired_mrc:
        mrc_path = os.path.join(directory, f"{name}.mrc")
        os.remove(mrc_path)
        print(f"Deleted {mrc_path}")



# Specify the directory containing the files
data_directory = '/home/brian_bosho/xulab/data/10007_subset/raw_data_denoised'

# Call the function
clean_unpaired_files(data_directory)
