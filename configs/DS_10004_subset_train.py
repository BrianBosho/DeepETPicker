train_configs = {
    "dset_name": "DS_10004_subset_train",
    "base_path": "/home/brian_bosho/xulab/data/10004_subset",
    "coord_path": "/home/brian_bosho/xulab/data/10004_subset/coords",
    "coord_format": ".coords",
    "tomo_path": "/home/brian_bosho/xulab/data/10004_subset/data_std",
    "tomo_format": ".mrc",
    "num_cls": 1,
    "label_type": "gaussian",
    "label_diameter": 25,
    "ocp_type": "sphere",
    "ocp_diameter": "35",
    "norm_type": "standardization",
    "label_name": "gaussian25",
    "label_path": "/home/brian_bosho/xulab/data/10004_subset/gaussian25",
    "ocp_name": "data_ocp",
    "ocp_path": "/home/brian_bosho/xulab/data/10004_subset/data_ocp",
    "model_name": "ResUNet",
    "train_set_ids": "0-1",
    "val_set_ids": "2",
    "batch_size": 16,
    "patch_size": 72,
    "padding_size": 12,
    "lr": 0.001,
    "max_epochs": 100,
    "seg_thresh": 0.5,
    "gpu_ids": "0"
}

# python bin/train_bash.py --train_configs /home/brian_bosho/xulab/DeepETPicker/configs/DS_10004_subset_train.json

# python bin/test_bash.py --train_configs /home/brian_bosho/xulab/DeepETPicker/configs/DS_10004_subset_train.json --checkpoints /home/brian_bosho/xulab/data/10004_subset/runs/DS_10004_subset_train/DS_10004_subset_train_ResUNet_BlockSize72_DiceLoss_MaxEpoch35_bs16_lr0.001_IP1_bg1_coord1_Softmax0_bn__TNNone/version_8/checkpoints/epoch=0-step=57.ckpt