# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""Utilities for data input/output common in ML projects."""

# GLOBAL IMPORTS

import csv
import os

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

# none for now


# PUBLIC INTERFACE


# STANDARD INPUT


def read_labelled_dataset_csv_as_pandas_df(labelled_dataset_csv_path, index_field_header):
    """Method to construct pandas data frame for a labelled input csv dataset."""
    # read in the labelled metadata csv file as a pandas data frame
    data_frame = pandas.read_csv(labelled_dataset_csv_path)
    # set an input field as the index
    data_frame.set_index(index_field_header, inplace=True)
    # return our customized data frame
    return data_frame


# STANDARD OUTPUT


def write_record_to_csv(csv_outfile_path, data_record, csv_headers=None):
    """ Easily write or append a record to csv output format. """
    if csv_headers is None:
        csv_headers = []
    if not os.path.isfile(csv_outfile_path):
        with open(r'' + csv_outfile_path, 'w') as output_stream:
            writer = csv.writer(output_stream)
            writer.writerow(csv_headers)
    with open(r'' + csv_outfile_path, 'a') as output_stream:
        writer = csv.writer(output_stream)
        writer.writerow(data_record)


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
