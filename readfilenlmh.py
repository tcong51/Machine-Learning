# -*- coding: utf-8 -*-
"""readfileNLMH.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zuva2h1NG246zYj2-bFYJXoPP8f7pTW7
"""

# Nap thu vien
import pandas as pd
from sklearn import tree
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from google.colab import drive
# drive.mount('/content/drive')

df=pd.read_csv("/content/drive/My Drive/NGUYEN LI MAY HOC/DO AN/Daegu_Real_Estate_data.csv")

#hien thi 5 dong dl

df.head()

#Kieu du lieu cua tung cot
# df.dtypes
#So dong du lieu va so cot dl
# df.shape
#kiem tra du lieu bi thieu 

# df.isnull().sum()

#mota

# df.describe()


# =============24 cot co dl so ,2 cot vua string vua numbers, 4 cot string
# chon dl so
# features = df.dtypes[df.dtypes != "object"].index

# khung dl moi, full numbers
# df = df[features]
# df.shape
#================