import os
import json

def convert_ndjson_to_coords(ndjson_path, coords_path):
    with open(ndjson_path, 'r') as ndjson_file, open(coords_path, 'w') as coords_file:
        for line in ndjson_file:
            # Parse each JSON object
            data = json.loads(line)
            # Extract x, y, z coordinates
            x = data["location"]["x"]
            y = data["location"]["y"]
            z = data["location"]["z"]
            # Write to .coords file in the desired format
            coords_file.write(f"1 {x} {y} {z}\n")
    print(f"Converted {ndjson_path} to {coords_path}")

# Define the base directory where your .ndjson files are located
base_dir = '/home/brian_bosho/xulab/data/10004_subset/raw_data'  # Update this path as necessary

# Loop through all .ndjson files in the directory and convert them
for filename in os.listdir(base_dir):
    if filename.endswith('.ndjson'):
        ndjson_path = os.path.join(base_dir, filename)
        coords_filename = filename.replace('.ndjson', '.coords')
        coords_path = os.path.join(base_dir, coords_filename)
        
        # Convert the file
        convert_ndjson_to_coords(ndjson_path, coords_path)
