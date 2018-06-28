# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""Utilities for data input/output common in ML projects."""

# GLOBAL IMPORTS

import csv

import numpy
import pandas
import sklearn_gbmi

# LICENSE INFORMATION HEADER

__author__ = "Logan Martel"
__copyright__ = "Copyleft (c) 2018, Logan Martel"
__credits__ = ["Logan Martel"]
__license__ = "GPLv3+"
__version__ = "0.1.0"
__maintainer__ = "Logan Martel"
__email__ = "logan.martel@outlook.com"
__status__ = "Development"

# GLOBAL VARIABLES

target_user_name = ""


# PUBLIC INTERFACE


# CLASSIFIER I/O

def output_classifier_predictions(predictions_data, prediction_headers, outfile_name):
    """ Print the classifier predictions in an output file. """
    pd_predictions = pandas.DataFrame(predictions_data)
    pandas.set_option('display.max_rows', len(pd_predictions))
    with open(outfile_name, 'w') as output_stream:
        output_stream.write('{0}\n'.format(pd_predictions.to_string(
            index=False, columns=prediction_headers)))


# INTERACTION TEST I/O


def output_gb_classifier_interaction_test_results(outfile_name, fitted_classifier,
                                                  target_feature_vectors, feature_vector_headers):
    """ Output interaction test results of fitted gradient-boosting classifier applied on target data. """
    target_dataframe = pandas.DataFrame(numpy.array(target_feature_vectors))
    target_dataframe.columns = feature_vector_headers
    h_stats = sklearn_gbmi.h_all_pairs(fitted_classifier, target_dataframe)
    with open(outfile_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in h_stats.items():
            # FEATURE NAME 1, FEATURE NAME 2, H_STATISTIC
            writer.writerow([key[0], key[1], value])
