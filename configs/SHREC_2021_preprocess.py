pre_config = {
    "dset_name": "SHREC_2021_preprocess",
    "base_path": "/home/brian_bosho/xulab/data/SHREC_2021",
    "coord_path": "/home/brian_bosho/xulab/data/SHREC_2021/raw_data",
    "coord_format": ".coords",
    "tomo_path": "/home/brian_bosho/xulab/data/SHREC_2021/raw_data",
    "tomo_format": ".mrc",
    "num_cls": 14,
    "label_type": "gaussian",
    "label_diameter": 9,
    "ocp_type": "sphere",
    "ocp_diameter": "7,7,7,7,7,9,9,9,11,11,13,13,13,17",
    "norm_type": "standardization"
}

# sample command: python bin/preprocess.py --pre_configs /home/brian_bosho/xulab/DeepETPicker/configs/SHREC_2021_preprocess.json

# base_path: /home/brian_bosho/xulab/data/SHREC_2021

# location: local_scratch/DeepETPicker/bin/train_bash.py
# /shared/home/v_brian_bosho/local_scratch/DeepETPicker/bin/train_bash.py