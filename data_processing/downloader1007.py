import os
import logging
from cryoet_data_portal import Client, Dataset
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the client and dataset
client = Client()
dataset = Dataset.get_by_id(client, 10007)

# Define the destination directory
dest_dir = '10007_subset'
os.makedirs(dest_dir, exist_ok=True)

# Define retry decorator for network-related errors
@retry(
    stop=stop_after_attempt(5),  # Retry up to 5 times
    wait=wait_exponential(multiplier=1, min=4, max=10),  # Exponential backoff
    retry=retry_if_exception_type((requests.exceptions.RequestException,)),
    reraise=True
)
def download_with_retry(download_func, *args, **kwargs):
    try:
        download_func(*args, **kwargs)
    except requests.exceptions.RequestException as e:
        logger.warning(f"Network issue encountered: {e}. Retrying...")
        raise

# Iterate over the first three runs
for run in dataset.runs[50:100]:
    logger.info(f"Processing run {run.name}")
    run_dir = os.path.join(dest_dir, run.name)
    os.makedirs(run_dir, exist_ok=True)

    # Iterate over tomogram voxel spacings
    for tvs in run.tomogram_voxel_spacings:
        for tomogram in tvs.tomograms:
            # Define file path for the tomogram
            mrc_file_path = os.path.join(run_dir, f"{tomogram.name}.mrc")

            # Download the tomogram in MRC format if it doesn't exist
            if not os.path.exists(mrc_file_path):
                logger.info(f"Downloading {mrc_file_path}")
                try:
                    download_with_retry(tomogram.download_mrcfile, dest_path=mrc_file_path)
                except requests.exceptions.RequestException:
                    logger.error(f"Failed to download {mrc_file_path} after multiple attempts.")
            else:
                logger.info(f"{mrc_file_path} already exists. Skipping download.")

            # Download all annotations associated with the tomogram
            logger.info(f"Downloading annotations for {tomogram.name}")
            try:
                download_with_retry(tomogram.download_all_annotations, dest_path=run_dir)
            except requests.exceptions.RequestException:
                logger.error(f"Failed to download annotations for {tomogram.name} after multiple attempts.")

    logger.info(f"Run {run.name} processed")