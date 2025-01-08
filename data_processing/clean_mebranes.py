import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def delete_membrane_files_in_position_folders(root_dir):
    # Iterate over each item in the root directory
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)

        # Check if the item is a directory and starts with 'Position_'
        if os.path.isdir(folder_path) and folder.startswith('ay'):
            logger.info(f"Processing folder: {folder_path}")

            # Iterate over files within the 'Position_' folder
            for root, _, files in os.walk(folder_path):
                for file in files:
                    # Check if file name contains "membrane" or "membraine"
                    if "membrane" in file.lower() or "membrain" in file.lower():
                        file_path = os.path.join(root, file)
                        try:
                            os.remove(file_path)
                            logger.info(f"Deleted membrane-related file: {file_path}")
                        except Exception as e:
                            logger.warning(f"Could not delete file {file_path}: {e}")

# Define the root directory where 'Position_' folders are located
root_directory = '/home/brian_bosho/xulab/data/10007_subset'  # Replace with the path to your directory
delete_membrane_files_in_position_folders(root_directory)
