# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""Utilities for data visualization common in ML projects."""

# IMPORTS
from __future__ import print_function

import csv
import os
from itertools import cycle

import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import auc

import settings

# LICENSE INFORMATION HEADER

__author__ = "Logan Martel"
__copyright__ = "Copyleft (c) 2018, Logan Martel"
__credits__ = ["Logan Martel"]
__license__ = "GPLv3+"
__version__ = "0.1.0"
__maintainer__ = "Logan Martel"
__email__ = "logan.martel@outlook.com"
__status__ = "Development"

# GLOBAL PLOTTING PARAMETERS

# basic plot settings
colors = cycle(['indigo', 'blue', 'darkorange', 'yellow', 'green'])
lw = 1
# prc params
reversed_mean_precision = 0.0
mean_recall = np.linspace(0, 1, 100)
# roc params
mean_tpr = 0.0
mean_fpr = np.linspace(0, 1, 100)
# prc_roc figure params
fig = plt.figure()
prc = fig.add_subplot(211)
roc = fig.add_subplot(212)


# PUBLIC INTERFACE


# ROC/PRC CONSTRUCTION

def init_basic_plot_settings(user_colors, user_lw):
    global colors
    global lw
    colors = user_colors
    lw = user_lw


def init_prc_params(user_reversed_mean_precision, user_mean_recall):
    global reversed_mean_precision
    global mean_recall
    reversed_mean_precision = user_reversed_mean_precision
    mean_recall = user_mean_recall


def init_roc_params(user_mean_tpr, user_mean_fpr):
    global mean_tpr
    global mean_fpr
    mean_tpr = user_mean_tpr
    mean_fpr = user_mean_fpr


def init_prc_and_roc_figure(user_fig, user_prc, user_roc):
    global fig
    global prc
    global roc
    fig = user_fig
    prc = user_prc
    roc = user_roc


def add_single_fold_prc_to_figure(precision, recall, color, fold_number):
    from scipy import interp
    from sklearn.metrics import auc

    global reversed_mean_precision

    reversed_recall = np.fliplr([recall])[0]
    reversed_precision = np.fliplr([precision])[0]
    reversed_mean_precision += interp(mean_recall, reversed_recall, reversed_precision)
    reversed_mean_precision[0] = 0.0

    prc_auc = auc(recall, precision)
    prc.plot(recall, precision, lw=lw, color=color,
             label='PRC fold %d (area = %0.6f)' % (fold_number, prc_auc))
    return prc_auc


def add_single_fold_roc_to_figure(fpr, tpr, color, fold_number):
    from scipy import interp

    from sklearn.metrics import auc

    global mean_tpr

    mean_tpr += interp(mean_fpr, fpr, tpr)
    mean_tpr[0] = 0.0

    roc_auc = auc(fpr, tpr)
    roc.plot(fpr, tpr, lw=lw, color=color,
             label='ROC fold %d (area = %0.6f)' % (fold_number, roc_auc))
    return roc_auc


def aggregate_k_prc_folds(target_str, n_splits):
    global reversed_mean_precision
    global mean_recall
    reversed_mean_precision /= n_splits
    reversed_mean_precision[0] = 1
    mean_auprc = auc(mean_recall, reversed_mean_precision)
    prc.plot(np.fliplr([mean_recall])[0], np.fliplr([reversed_mean_precision])[0], color='g', linestyle='--',
             label='Mean PRC (area = %0.6f)' % mean_auprc, lw=lw)
    prc.axhline(y=0.5, xmin=0.05, xmax=1, c="black", linewidth=lw, linestyle='--', label='Luck')
    prc.set_xlim([-0.05, 1.05])
    prc.set_ylim([-0.05, 1.05])
    prc.set_xlabel('Recall')
    prc.set_ylabel('Precision')
    prc.set_title('Precision Recall Curve For Target: ' + target_str)
    prc.legend(loc="lower right", prop={'size': 12})
    return mean_auprc


def aggregate_k_roc_folds(target_str, n_splits):
    global mean_tpr
    global mean_fpr

    roc.plot([0, 1], [0, 1], linestyle='--', lw=lw, color='k',
             label='Luck')
    mean_tpr /= n_splits
    mean_tpr[-1] = 1.0
    mean_auroc = auc(mean_fpr, mean_tpr)
    roc.plot(mean_fpr, mean_tpr, color='g', linestyle='--',
             label='Mean ROC (area = %0.6f)' % mean_auroc, lw=lw)

    roc.set_xlim([-0.05, 1.05])
    roc.set_ylim([-0.05, 1.05])
    roc.set_xlabel('False Positive Rate')
    roc.set_ylabel('True Positive Rate')
    roc.set_title('Receiver operating characteristic For Target: ' + target_str)
    roc.legend(loc="lower right", prop={'size': 12})
    return mean_auroc


def output_k_fold_prc_roc_results(outfile_dir, target_str, should_output_csv=False,
                                  cumulative_csv_filepath='', csv_headers='', data_fields=None):
    # by default, just output the k-fold prc_roc figure
    if data_fields is None:
        data_fields = []
    fig.savefig(outfile_dir + '/' + target_str + settings.PRC_ROC_PNG, bbox_inches='tight')

    if should_output_csv:
        # if writing to csv, let's configure the appropriate paths
        if not cumulative_csv_filepath:
            cumulative_auc_dir = settings.CUMULATIVE_AUC_DIR
            cumulative_csv_filepath = \
                os.path.join(cumulative_auc_dir, target_str + settings.CUMULATIVE_AUC_CSV)
        # create the file if it does not yet exist
        if not os.path.isfile(cumulative_csv_filepath):
            with open(r'' + cumulative_csv_filepath, 'w') as f:
                writer = csv.writer(f)
                headers = csv_headers if csv_headers else settings.CUMULATIVE_AUC_HEADERS
                writer.writerow(headers)
        # write data to the csv
        with open(r'' + cumulative_csv_filepath, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data_fields)


def output_one_fold_prc_roc_results(outfile_dir, target_str):
    roc.plot([0, 1], [0, 1], linestyle='--', lw=lw, color='k',
             label='Luck')
    roc.set_xlim([-0.05, 1.05])
    roc.set_ylim([-0.05, 1.05])
    roc.set_xlabel('False Positive Rate')
    roc.set_ylabel('True Positive Rate')
    roc.set_title('Receiver operating characteristic For Target: ' + target_str)
    roc.legend(loc="lower right", prop={'size': 12})

    prc.axhline(y=0.5, xmin=0.05, xmax=1, c="black", linewidth=lw, linestyle='--', label='Luck')
    prc.set_xlim([-0.05, 1.05])
    prc.set_ylim([-0.05, 1.05])
    prc.set_xlabel('Recall')
    prc.set_ylabel('Precision')
    prc.set_title('Precision Recall Curve For Target: ' + target_str)
    prc.legend(loc="lower right", prop={'size': 12})

    fig.savefig(outfile_dir + '/' + target_str + settings.PRC_ROC_PNG, bbox_inches='tight')
