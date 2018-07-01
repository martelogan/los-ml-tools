.. los-ml-tools documentation master file, created by
   sphinx-quickstart on Sat Jun 30 20:02:44 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Los-ML-Tools Documentation
==========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. py:module::los-ml-tools


Purpose
-------

This project, ``los-ml-tools``, exists to host a collection of Logan Martel, ML Developer's, personal utilities for ML projects.


Installation
------------

Basic install: ``pip install los-ml-tools``

Hackable install: 

.. code-block:: bash

   git clone https://github.com/martelogan/los-ml-tools.git
   cd los-ml-tools
   python setup.py develop

Example Usage
-------------

To leverage the module, simply import any utilities of interest. For example, to apply a plotting utility:

.. code-block:: python

   >>> from los_ml_tools import plotting_utils as plotting
   >>> plotting.add_single_fold_prc_to_figure(0.95, 0.80, 'blue', 1)
   >>> plotting.output_one_fold_prc_roc_results('/tmp/', 'target_class')

