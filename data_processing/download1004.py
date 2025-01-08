from cryoet_data_portal import Client, Dataset

client = Client()
dataset = Dataset.get_by_id(client, 10004)

import os

# Define the destination directory
dest_dir = '10004_subset'
os.makedirs(dest_dir, exist_ok=True)

# Iterate over the first three runs
for run in dataset.runs[:3]:
    print(f"Downloading run {run.name}")
    run_dir = os.path.join(dest_dir, run.name)
    os.makedirs(run_dir, exist_ok=True)

    # Iterate over tomogram voxel spacings
    for tvs in run.tomogram_voxel_spacings:
        for tomogram in tvs.tomograms:
            # Download the tomogram in MRC format
            tomogram.download_mrcfile(dest_path=run_dir)

            # Download all annotations associated with the tomogram
            tomogram.download_all_annotations(dest_path=run_dir)
    print(f"Run {run.name} downloaded")
