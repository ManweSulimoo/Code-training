"""Bundle d'imports partagé par training.ipynb (from data_generation import *)."""

# Standard library
import math
import os
import random
import re
from collections import defaultdict

# Third-party
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from scipy import signal
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import DataLoader, TensorDataset
from torchvision.transforms import v2
