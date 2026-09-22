#!/usr/bin/env python3

import os

# Turn off oneDNN warning
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Suppress gRPC and Abseil logging
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "3"

import sys
import jupyterlab
import pandas
import pandas_datareader
import numpy
import matplotlib
import sklearn
import django
import seaborn
import openpyxl
import nltk
import statsmodels
import plotly
import tensorflow
import keras
import scipy
import cv2
import yfinance

# Python version
print('Python version: \n{0}'.format(sys.version), "\n")

# Python version information
print('Python version info: \n{0}'.format(sys.version_info), "\n")

# Package versions
print('jupyterlab: {0}'.format(jupyterlab.__version__))
print('pandas: {0}'.format(pandas.__version__))
print('pandas_datareader: {0}'.format(pandas_datareader.__version__))
print('numpy: {0}'.format(numpy.__version__))
print('matplotlib: {0}'.format(matplotlib.__version__))
print('sklearn: {0}'.format(sklearn.__version__))
print('django: {0}'.format(django.__version__))
print('seaborn: {0}'.format(seaborn.__version__))
print('openpyxl: {0}'.format(openpyxl.__version__))
print('nltk: {0}'.format(nltk.__version__))
print('statsmodels: {0}'.format(statsmodels.__version__))
print('plotly: {0}'.format(plotly.__version__))
print('tensorflow: {0}'.format(tensorflow.__version__))
print('keras: {0}'.format(keras.__version__))
print('scipy: {0}'.format(scipy.__version__))
print('cv2 (opencv-python): {0}'.format(cv2.__version__))
print('yfinance: {0}'.format(yfinance.__version__))
