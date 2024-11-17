import sys
import os
from os.path import dirname, abspath
import importlib
import json

DeepETPickerHome = dirname(abspath(__file__))
DeepETPickerHome = os.path.split(DeepETPickerHome)[0]
sys.path.append(DeepETPickerHome)
sys.path.append(os.path.split(DeepETPickerHome)[0])
coords2labels = importlib.import_module(".utils.coords2labels", package=os.path.split(DeepETPickerHome)[1])
coord_gen = importlib.import_module(f".utils.coord_gen", package=os.path.split(DeepETPickerHome)[1])
norm = importlib.import_module(f".utils.normalization", package=os.path.split(DeepETPickerHome)[1])
option = importlib.import_module(f".options.option", package=os.path.split(DeepETPickerHome)[1])

if __name__ == "__main__":
    print("Running preprocess.py")
    options = option.BaseOptions()
    args = options.gather_options()
#     print("Gathered arguments:", vars(args))  # Print all arguments

    with open(args.pre_configs, 'r') as f:
        pre_config = json.loads(''.join(f.readlines()).lstrip('pre_config='))

    # Add this after loading pre_config
    def print_file_counts(path, format):
      files = [f for f in os.listdir(path) if f.endswith(format)]
      print(f"Found {len(files)} files with format {format} in {path}:")
      # for f in files:
      #       # print(f"  - {f}")
      # return files

      # Add after pre_config loading:
    print("\nChecking MRC files:")
    mrc_files = print_file_counts(pre_config["tomo_path"], pre_config["tomo_format"])
    print("\nChecking coord files:")
    coord_files = print_file_counts(pre_config["coord_path"], pre_config["coord_format"])

      # Get list of coordinate files
    coord_path = pre_config["coord_path"]
    coord_format = pre_config["coord_format"]
    coord_files = [f for f in os.listdir(coord_path) if f.endswith(coord_format)]
    print(f"Found {len(coord_files)} coordinate files")

    # initial coords
    coord_gen.coords_gen_show(args=(pre_config["coord_path"],
                                    pre_config["coord_format"],
                                    pre_config["base_path"],
                                    None,
                                    )
                              )

    # normalization
    norm.norm_show(args=(pre_config["tomo_path"],
                         pre_config["tomo_format"],
                         pre_config["base_path"],
                         pre_config["norm_type"],
                         None,
                         )
                   )
    print("Normalization finished!, Procceding to label generation")

    # generate labels based on coords
    coords2labels.label_gen_show(args=(pre_config["base_path"],
                                       pre_config["coord_path"],
                                       pre_config["coord_format"],
                                       pre_config["tomo_path"],
                                       pre_config["tomo_format"],
                                       pre_config["num_cls"],
                                       pre_config["label_type"],
                                       pre_config["label_diameter"],
                                       None,
                                       )
                                 )
    print("Label generation finished!, Procceding to occupancy generation")

    # generate occupancy abased on coords
    coords2labels.label_gen_show(args=(pre_config["base_path"],
                                       pre_config["coord_path"],
                                       pre_config["coord_format"],
                                       pre_config["tomo_path"],
                                       pre_config["tomo_format"],
                                       pre_config["num_cls"],
                                       'data_ocp',
                                       pre_config["ocp_diameter"],
                                       None,
                                       )
                                 )
