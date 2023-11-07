VQAEX_TRAIN_COMMON_CFG = dict(
    type='VQAEXDataset',
    image_folder=r'/fast-vol/dataset/coco',
    template_file=r"{{fileDirname}}/template/VQA_CoT.json",
)

DEFAULT_TRAIN_VQAEX_VARIANT = dict(
    VQAE_train=dict(
        **VQAEX_TRAIN_COMMON_CFG,
        is_e_dataset=True,
        filename=r'/fast-vol/dataset/shikra/vqa_E_train.jsonl',
    ),
    VQAX_train=dict(
        **VQAEX_TRAIN_COMMON_CFG,
        is_e_dataset=False,
        filename=r'/fast-vol/dataset/shikra/vqa_X_train.jsonl',
    ),
)
