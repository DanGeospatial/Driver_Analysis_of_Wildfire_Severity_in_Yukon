"""
Remove features to improve accuracy and efficiency by dropping features that are unimportant, add error, etc.
"""
import sklearn.metrics
import pandas as pd
from sklearn.feature_selection import RFECV
from xgboost.sklearn import XGBRegressor
from sklearn.model_selection import train_test_split

checked_data = "I:/Wildfire_Datasets_v2/combined_checked.csv"

df = pd.read_csv(checked_data)

y = df["dNBR"]
x = df.drop("dNBR", axis=1)

train_y, test_y = train_test_split(y, test_size=0.25)
train_x, test_x = train_test_split(x, test_size=0.25)

estimator = XGBRegressor()
eliminator = RFECV(estimator=estimator, cv=5, scoring='neg_mean_squared_error', min_features_to_select=1, step=1)
rfe = eliminator.fit(train_x, train_y)
print('Best Parameters:', rfe.best_params_)
print(rfe.cv_results_)

