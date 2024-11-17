train_configs = {
    "dset_name": "SHREC_2021_train",
    "base_path": "/home/brian_bosho/xulab/data/SHREC_2021",
    "coord_path": "/home/brian_bosho/xulab/data/SHREC_2021/coords",
    "coord_format": ".coords",
    "tomo_path": "/home/brian_bosho/xulab/data/SHREC_2021/data_std",
    "tomo_format": ".mrc",
    "num_cls": 14,
    "label_name": "gaussian9",
    "label_path": "/home/brian_bosho/xulab/data/SHREC_2021/gaussian9",
    "label_type": "gaussian",
    "label_diameter": 9,
    "ocp_type": "sphere",
    "ocp_diameter": "7,7,7,7,7,9,9,9,11,11,13,13,13,17",
    "ocp_name": "data_ocp",
    "ocp_path": "/home/brian_bosho/xulab/data/SHREC_2021/data_ocp",
    "norm_type": "standardization",
    "model_name": "ResUNet",
    "train_set_ids": "0-7",
    "val_set_ids": "8",
    "batch_size": 32,
    "patch_size": 72,
    "padding_size": 12,
    "lr": 0.0005,
    "max_epochs": 60,
    "seg_thresh": 0.5,
    "gpu_ids": "0"
}

# python train_bash.py --train_configs /shared/home/v_brian_bosho/local_scratch/DeepETPicker/configs/SHREC_2021_train.json

# python train_bash.py --train_configs /home/brian_bosho/xulab/DeepETPicker/configs/SHREC_2021_train.json

# python test_bash.py --train_configs 'Train_Config_Name' --checkpoints 'Checkpoint_Path'

# python test_bash.py --train_configs /home/brian_bosho/xulab/DeepETPicker/configs/SHREC_2021_train.json --checkpoints /home/brian_bosho/xulab/data/SHREC_2021/runs/SHREC_2021_train/SHREC_2021_train_ResUNet_BlockSize72_DiceLoss_MaxEpoch30_bs32_lr0.0005_IP1_bg1_coord1_Softmax1_bn__TNNone/version_0/checkpoints/epoch=27-step=9407.ckpt

# train config: /home/brian_bosho/xulab/DeepETPicker/configs/SHREC_2021_train.json

# checkpoint: /home/brian_bosho/xulab/data/SHREC_2021/runs/SHREC_2021_train/SHREC_2021_train_ResUNet_BlockSize72_DiceLoss_MaxEpoch30_bs32_lr0.0005_IP1_bg1_coord1_Softmax1_bn__TNNone/version_0/checkpoints/epoch=27-step=9407.ckpt