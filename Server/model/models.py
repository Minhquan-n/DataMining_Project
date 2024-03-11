import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

# Xay dung cac ham khoi tao model da duoc tinh chinh cac tham so
def RFC_model(features, labels):
    model = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=42, min_samples_leaf=1, max_depth=183)
    model.fit(features, labels.values.ravel())

    return model

def NB_model(features, labels):
    model = GaussianNB()
    model.fit(features, labels.values.ravel())
    return model

def DT_model(features, labels):
    model = DecisionTreeClassifier(criterion='entropy', random_state=42)
    model.fit(features, labels.values.ravel())
    return model