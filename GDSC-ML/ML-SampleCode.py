import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier #Multi label classification

from sklearn import datasets

from sklearn.metrics import accuracy_score

data=datasets.load_digits()

X=data.data                #Feature
y=data.target              #Labels

(X_train,X_test,y_train,y_test)=train_test_split(X,y,test_size=0.30)

y_train[10]

X_train[10].reshape(8,8)

plt.imshow(X_train[10].reshape(8,8))