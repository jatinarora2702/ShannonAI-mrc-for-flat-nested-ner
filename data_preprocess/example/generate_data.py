#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 


# Author: Xiaoy LI
# description:
# 


import os
import sys

ROOT_PATH = "/".join(os.path.realpath(__file__).split("/")[:-3])
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)

from data_preprocess.generate_mrc_dataset import generate_query_ner_dataset


def test_nested_ner():
    d_repo = "../../../sec-ner/data/GENIA_Std"

    # source_file_path = os.path.join(ROOT_PATH, "data_preprocess/test/dev_ace05.json")
    # target_file_path = os.path.join(ROOT_PATH, "data_preprocess/test/mrc-dev_ace05.json")

    entity_sign = "nested"
    # dataset_name = "en_ace2005"
    dataset_name = "en_jnlpba"
    query_sign = "default"

    source_file_path = os.path.join(d_repo, "mrc_train.json")
    target_file_path = os.path.join(d_repo, "mrc-ner.train")
    generate_query_ner_dataset(source_file_path, target_file_path, entity_sign=entity_sign, dataset_name=dataset_name,
                               query_sign=query_sign)

    source_file_path = os.path.join(d_repo, "mrc_dev.json")
    target_file_path = os.path.join(d_repo, "mrc-ner.dev")
    generate_query_ner_dataset(source_file_path, target_file_path, entity_sign=entity_sign, dataset_name=dataset_name,
                               query_sign=query_sign)

    source_file_path = os.path.join(d_repo, "mrc_test.json")
    target_file_path = os.path.join(d_repo, "mrc-ner.test")
    generate_query_ner_dataset(source_file_path, target_file_path, entity_sign=entity_sign, dataset_name=dataset_name,
                               query_sign=query_sign)


def test_flat_ner():
    # source_file_path = os.path.join(ROOT_PATH, "data_preprocess/test/dev_msra.bmes")
    # target_file_path = os.path.join(ROOT_PATH, "data_preprocess/test/mrc-dev_msra.json")

    # d_repo = "../../../sec-ner/data/JNLPBA"
    d_repo = "../../../sec-ner/data/GENIA_term_3.02"

    entity_sign = "flat"
    dataset_name = "en_jnlpba"
    # dataset_name = "en_fine_genia"
    query_sign = "default"

    source_file_path = os.path.join(d_repo, "train.tsv")
    # source_file_path = os.path.join(d_repo, "jnlpba_train.tsv")
    target_file_path = os.path.join(d_repo, "mrc-ner.train")
    generate_query_ner_dataset(source_file_path, target_file_path, entity_sign=entity_sign, dataset_name=dataset_name,
                               query_sign=query_sign)

    source_file_path = os.path.join(d_repo, "dev.tsv")
    # source_file_path = os.path.join(d_repo, "jnlpba_dev.tsv")
    target_file_path = os.path.join(d_repo, "mrc-ner.dev")
    generate_query_ner_dataset(source_file_path, target_file_path, entity_sign=entity_sign, dataset_name=dataset_name,
                               query_sign=query_sign)

    source_file_path = os.path.join(d_repo, "test.tsv")
    # source_file_path = os.path.join(d_repo, "jnlpba_test.tsv")
    target_file_path = os.path.join(d_repo, "mrc-ner.test")
    generate_query_ner_dataset(source_file_path, target_file_path, entity_sign=entity_sign, dataset_name=dataset_name,
                               query_sign=query_sign)


if __name__ == "__main__":
    test_nested_ner()
    test_flat_ner()
