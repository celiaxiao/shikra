POINT_TEST_COMMON_CFG_LOCAL = dict(
    type='Point_QA_local',
    image_folder='/fast-vol/dataset/visual-genome',
    template_file=r"{{fileDirname}}/template/VQA.json",
)

POINT_TEST_COMMON_CFG_TWICE = dict(
    type='Point_QA_twice',
    image_folder='/fast-vol/dataset/visual-genome',
    template_file=r"{{fileDirname}}/template/VQA.json",
)

POINT_TEST_COMMON_CFG_V7W = dict(
    type='V7W_POINT',
    image_folder='sh41:s3://MultiModal/Monolith/academic/v7w/data',
    template_file=r"{{fileDirname}}/template/VQA.json",
    do_shuffle_choice=True,
)

DEFAULT_TEST_POINT_VARIANT = dict(
    POINT_LOCAL_b_val=dict(**POINT_TEST_COMMON_CFG_LOCAL, version='b', filename='/fast-vol/dataset/shikra/pointQA_local_val.jsonl'),
    POINT_LOCAL_p_val=dict(**POINT_TEST_COMMON_CFG_LOCAL, version='p', filename='/fast-vol/dataset/shikra/pointQA_local_val.jsonl'),
    POINT_TWICE_oq_b_val=dict(**POINT_TEST_COMMON_CFG_TWICE, version='oq-b', filename='/fast-vol/dataset/shikra/pointQA_twice_val.jsonl'),
    POINT_TWICE_oq_p_val=dict(**POINT_TEST_COMMON_CFG_TWICE, version='oq-p', filename='/fast-vol/dataset/shikra/pointQA_twice_val.jsonl'),
    POINT_TWICE_sq_b_val=dict(**POINT_TEST_COMMON_CFG_TWICE, version='sq-b', filename='/fast-vol/dataset/shikra/pointQA_twice_val.jsonl'),
    POINT_TWICE_sq_p_val=dict(**POINT_TEST_COMMON_CFG_TWICE, version='sq-p', filename='/fast-vol/dataset/shikra/pointQA_twice_val.jsonl'),
    POINT_TWICE_gq_b_val=dict(**POINT_TEST_COMMON_CFG_TWICE, version='gq-b', filename='/fast-vol/dataset/shikra/pointQA_twice_val.jsonl'),
    POINT_TWICE_gq_p_val=dict(**POINT_TEST_COMMON_CFG_TWICE, version='gq-p', filename='/fast-vol/dataset/shikra/pointQA_twice_val.jsonl'),
    POINT_V7W_p_val=dict(**POINT_TEST_COMMON_CFG_V7W, version='p', filename='/fast-vol/dataset/shikra/v7w_pointing_val.jsonl'),
    POINT_V7W_b_val=dict(**POINT_TEST_COMMON_CFG_V7W, version='b', filename='/fast-vol/dataset/shikra/v7w_pointing_val.jsonl'),

    POINT_LOCAL_b_test=dict(**POINT_TEST_COMMON_CFG_LOCAL, version='b', filename='/fast-vol/dataset/shikra/pointQA_local_test.jsonl'),
    POINT_LOCAL_p_test=dict(**POINT_TEST_COMMON_CFG_LOCAL, version='p', filename='/fast-vol/dataset/shikra/pointQA_local_test.jsonl'),
    POINT_TWICE_oq_b_test=dict(**POINT_TEST_COMMON_CFG_TWICE, version='oq-b', filename='/fast-vol/dataset/shikra/pointQA_twice_test.jsonl'),
    POINT_TWICE_oq_p_test=dict(**POINT_TEST_COMMON_CFG_TWICE, version='oq-p', filename='/fast-vol/dataset/shikra/pointQA_twice_test.jsonl'),
    POINT_TWICE_sq_b_test=dict(**POINT_TEST_COMMON_CFG_TWICE, version='sq-b', filename='/fast-vol/dataset/shikra/pointQA_twice_test.jsonl'),
    POINT_TWICE_sq_p_test=dict(**POINT_TEST_COMMON_CFG_TWICE, version='sq-p', filename='/fast-vol/dataset/shikra/pointQA_twice_test.jsonl'),
    POINT_TWICE_gq_b_test=dict(**POINT_TEST_COMMON_CFG_TWICE, version='gq-b', filename='/fast-vol/dataset/shikra/pointQA_twice_test.jsonl'),
    POINT_TWICE_gq_p_test=dict(**POINT_TEST_COMMON_CFG_TWICE, version='gq-p', filename='/fast-vol/dataset/shikra/pointQA_twice_test.jsonl'),
    POINT_V7W_p_test=dict(**POINT_TEST_COMMON_CFG_V7W, version='p', filename='/fast-vol/dataset/shikra/v7w_pointing_test.jsonl'),
    POINT_V7W_b_test=dict(**POINT_TEST_COMMON_CFG_V7W, version='b', filename='/fast-vol/dataset/shikra/v7w_pointing_test.jsonl'),
)
