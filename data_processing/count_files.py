import os

folder_path = "/home/brian_bosho/xulab/data/10007_subset/mrc_files"  # Replace with your folder path
file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

print(f"Number of files in the folder: {file_count}")
