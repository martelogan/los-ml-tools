# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""Dynamically configurable constants for the los-ml-tools module."""

# IMPORTS

import os

# LICENSE INFORMATION HEADER

__author__ = "Logan Martel"
__copyright__ = "Copyleft (c) 2018, Logan Martel"
__credits__ = ["Logan Martel"]
__license__ = "GPLv3+"
__version__ = "0.1.0"
__maintainer__ = "Logan Martel"
__email__ = "logan.martel@outlook.com"
__status__ = "Development"

# PATH VARIABLES

PATH = os.path.dirname(os.path.realpath(__file__))
PRC_ROC_PNG = "_prc_roc.png"
CUMULATIVE_AUC_DIR = PATH
CUMULATIVE_AUC_CSV = "_cumulative_auc.csv"

# DEPENDENCY VARIABLES


# DATA FORMAT CONSTANTS

PRC_ROC_RESULT_HEADERS = ['Attr_Id', 'Publication_Label', 'Article_Name']
CUMULATIVE_AUC_HEADERS = ['Experiment_Name', 'Feature_Vector_Type', 'Target_Class', 'AUPRC', 'AUROC']

# CLASSIFICATION ALGORITHM CONSTANTS


# DATA STRUCTURE CONSTANTS


# SPECIAL STRING CONSTANTS


# CORE LOGIC CONSTANTS
