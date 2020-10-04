#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 



# Author: Xiaoy LI 
# Description:
# mrc_ner_data_processor.py


import os

from data_loader.mrc_utils import read_mrc_ner_examples


class QueryNERProcessor(object):
    # processor for the query-based ner dataset 
    def get_train_examples(self, data_dir):
        data = read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.train"))
        return data

    def get_dev_examples(self, data_dir):
        return read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.dev"))

    def get_test_examples(self, data_dir):
        return read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.test"))


class Conll03Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["ORG", "PER", "LOC", "MISC", "O"]


class MSRAProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["NS", "NR", "NT", "O"]


class Onto4ZhProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["LOC", "PER", "GPE", "ORG", "O"]


class Onto5EngProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['ORDINAL', 'CARDINAL', 'LOC', 'WORK_OF_ART', 'LANGUAGE', 'ORG', 'FAC', 'PERSON', 'EVENT', 'TIME', 'LAW', 'NORP', 'PERCENT', 'DATE', 'GPE', 'QUANTITY', 'PRODUCT', 'MONEY', 'O']


class ResumeZhProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["ORG", "LOC", "NAME", "RACE", "TITLE", "EDU", "PRO", "CONT", "O"]


class GeniaProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['cell_line', 'cell_type', 'DNA', 'RNA', 'protein', "O"]


class FineGeniaProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['G#DNA_N/A', 'G#DNA_domain_or_region', 'G#DNA_family_or_group', 'G#DNA_molecule', 'G#DNA_substructure',
                'G#RNA_N/A', 'G#RNA_domain_or_region', 'G#RNA_family_or_group',
                'G#RNA_molecule', 'G#RNA_substructure', 'G#amino_acid_monomer', 'G#atom', 'G#body_part',
                'G#carbohydrate', 'G#cell_component', 'G#cell_line', 'G#cell_type', 'G#inorganic',
                'G#lipid', 'G#mono_cell', 'G#multi_cell', 'G#nucleotide', 'G#other_artificial_source', 'G#other_name',
                'G#other_organic_compound', 'G#peptide', 'G#polynucleotide',
                'G#protein_N/A', 'G#protein_complex', 'G#protein_domain_or_region', 'G#protein_family_or_group',
                'G#protein_molecule', 'G#protein_substructure', 'G#protein_subunit', 'G#tissue', 'G#virus', 'O']


class JnlpbaProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['cell_line', 'cell_type', 'DNA', 'RNA', 'protein', "O"]


class ACE2005Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["GPE", "ORG", "PER", "FAC", "VEH", "LOC", "WEA", "O"]


class ACE2004Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["GPE", "ORG", "PER", "FAC", "VEH", "LOC", "WEA", "O"]








