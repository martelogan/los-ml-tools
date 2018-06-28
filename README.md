Los-ML-Tools
=================================================
[![Build Status](https://travis-ci.org/martelogan/los-ml-tools.svg?branch=master)](https://travis-ci.org/martelogan/los-ml-tools)

Description
------------

This repo is intended to host a collection of Logan Martel, ML Developer's, personal utilities for ML projects. 


Project Status
--------------

- [x] Add basic plotting utilities
- [x] Add basic data io utilities
- [x] Add basic data formatting utilities
- ...

Installation
------------

1. Make sure you have all the dependencies needed to build this project. In particular, immediately after git clone, you should be able to successfully build 
the project from a command-line environment under **[Python 2.7](http://docs.python-guide.org/en/latest/starting/install/linux/)** 
via the command:
```bash
   python setup.py develop
```

2. The recommended IDE for developer consistency is [PyCharm](https://www.jetbrains.com/pycharm/). 
Leveraging PyCharm, it would be ideal for project contributors to ensure that code conforms to [PEP 8 standards](https://www.python.org/dev/peps/pep-0008/).

(**RECOMMENDATION:** Ideally, it is advised to manage Python virtual environments via [`conda`](https://docs.continuum.io/anaconda/) in order to safely segregate module dependencies. In this case, it is recommended to locallize [`pip`](https://pip.pypa.io/en/stable/installing/) installations during conda environment creation, to avoid dependency conflicts, by instantiating the environment with its own [`pip`](https://pip.pypa.io/en/stable/installing/) setup, à la `conda create --name custom_venv_name pip`. Alternatively, a basic [`conda`](https://docs.continuum.io/anaconda/) venv, equipped with its own localized [`pip`](https://pip.pypa.io/en/stable/installing/), can be configured from this project directory simply by running `conda env create -f environment.yml` and then [activating the environment](https://conda.io/docs/user-guide/tasks/manage-environments.html#activating-an-environment) (linux example: `source activate los-ml-tools`)).

Development
-----------

Our development workflow will be simple:

**Always develop on your own branch. Only merge code to Master via PR's. Only merge code that has no conflicts with master. Only merge code that builds successfully via _python setup.py develop_**.

Execution
---------

To leverage the module, simply import any utilities of interest. For example, to apply a plotting utility:

```python
   >>> from los_ml_tools import plotting_utils as plotting
   >>> plotting.add_single_fold_prc_to_figure(0.95, 0.80, 'blue', 1)
   >>> plotting.output_one_fold_prc_roc_results('/tmp/', 'target_class')
```


License
-------

This code is under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

If you use or modify _los-ml-tools_, please credit the original author as

* Logan Martel - https://github.com/martelogan
