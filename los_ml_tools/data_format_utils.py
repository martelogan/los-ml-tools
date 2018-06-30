# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""Utilities for data structure adaption common in ML projects."""

# GLOBAL IMPORTS

import os

import numpy

# LICENSE INFORMATION HEADER

__author__ = "Logan Martel"
__copyright__ = "Copyleft (c) 2018, Logan Martel"
__credits__ = ["Logan Martel"]
__license__ = "GPLv3+"
__version__ = "0.1.0"
__maintainer__ = "Logan Martel"
__email__ = "logan.martel@outlook.com"
__status__ = "Development"


# PUBLIC INTERFACE


# DATA LOGISTICS FUNCTIONS


def scale01(values, mini=None, maxi=None, tol=1e-6):
    """ Scale the values in [0, 1]. """
    if not mini:
        mini = numpy.amin(values)
    if not maxi:
        maxi = numpy.amax(values)
    scaled_values = [(val - mini) / (maxi - mini + tol) for val in values]
    return scaled_values, mini, maxi


def not_na(item):
    """ Remove NAs and empty values. """
    return not (item == "NA" or item == "")


def match_feature_vector_length(feature_vec_1, feature_vec_2):
    """
    Trim the feature vectors to the same size.
    """
    fg_len = len(feature_vec_1)
    bg_len = len(feature_vec_2)
    if fg_len > bg_len:
        feature_vec_1 = feature_vec_1[0:bg_len]
    elif bg_len > fg_len:
        feature_vec_2 = feature_vec_2[0:fg_len]
    return feature_vec_1, feature_vec_2


def get_immediate_subdirectory_names(working_dir_path):
    """Method to get all immediate subdirectory names of a given directory path."""
    return [element_name for element_name in os.listdir(working_dir_path)
            if os.path.isdir(os.path.join(working_dir_path, element_name))]


def extract_random_df_sample_matching_indexer_df(pandas_df, sample_size, indexer_df):
    """Method to extract a random pandas df sample of size k with indices matching indexer_df."""
    # construct a data frame filtered to match our target index
    filtered_df = pandas_df.loc[indexer_df]
    # leverage numpy to draw a random sample of row indices of size k
    rows = numpy.random.choice(filtered_df.index.values, sample_size)
    # construct a new data frame for our random sample
    sampled_df = filtered_df.ix[rows]
    # return our sampled data frame
    return sampled_df
