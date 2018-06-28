# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""Utilities for data structure adaption common in ML projects."""

# GLOBAL IMPORTS

from numpy import amax, amin

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
        mini = amin(values)
    if not maxi:
        maxi = amax(values)
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
