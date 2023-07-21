import pandas as pd
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import LocalOutlierFactor
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
datainput = pd.read_csv("covidData.csv", delimiter=",")
#print(datainput)


datainput['LOS'] = datainput['LOS'].astype('float64')
X = datainput.select_dtypes('float64').values
Y = datainput['Severity'].values


print(X.shape)
print(Y.shape)
print(" ")

#---------------------------------------------------------------------------

ytest = LocalOutlierFactor().fit_predict(X)
mask = ytest != -1
X, Y = X[mask, :], Y[mask]


print(X.shape)
print(Y.shape)
print(" ")

#---------------------------------------------------------------------------
'''
pipeline = Pipeline(
    [
        ('min/max scaler', MinMaxScaler()), 
        ('model', LinearRegression())
    ]
)

param_grid = {'model__fit_intercept': [True, False],
              'model__copy_X': [True, False],
              'model__n_jobs': [None, 1, 2, 3],
              'model__positive': [True, False]
              }

search = GridSearchCV(
    estimator = pipeline,
    param_grid = param_grid,
    n_jobs=-1,
    scoring="neg_mean_squared_error",
    cv=5,
    verbose=0
)

#print(search.fit(X, Y))
print(search.best_params_)
'''
#-----------------------------------------------------------------------------
model = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, positive=False)
scores = cross_val_score(model, X, Y, cv=5, scoring='neg_root_mean_squared_error')
print("Mean score of %0.2f with a standard deviation of %0.2f" % (scores.mean(), scores.std()))



def severity_categorization(value):
    if 0 <= value < 4:
        return 'Low Severity Level'
    elif 4 <= value < 9:
        return 'Middle Severity Level'
    else:
        return 'High Severity Level'
severity_df = pd.get_dummies(datainput['Severity'].apply(lambda value: severity_categorization(value)))
int_df = datainput.drop(['Death', 'Severity'], axis=1).select_dtypes('int64')
severity_columns = severity_df.columns
for column in severity_columns:
    int_df[column] = severity_df[column]
X = int_df.values
y = datainput['Death'].values
print(X.shape)
print(Y.shape)
print(" ")



yhat = LocalOutlierFactor().fit_predict(X)
mask = yhat != -1
X, Y = X[mask, :], y[mask]
print(X.shape)
print(Y.shape)
print(" ")



'''
model = LogisticRegression(solver='saga', random_state=0)

param_grid = {'penalty': ['l1', 'l2', 'elasticnet', None],
              'C': [0.8, 1.0, 1.2, 1.4]
              }

search = GridSearchCV(
    estimator = model,
    param_grid = param_grid,
    n_jobs=-1,
    scoring="accuracy",
    cv=5,
    verbose=0
)

print(search.fit(X, y))
print(search.best_params_)
'''
neighbors=30
knnModel=KNeighborsClassifier(neighbors)
knnScores = cross_val_score(knnModel, X, Y, cv=5, scoring='neg_root_mean_squared_error')
print("KNN: Mean score of %0.2f with a standard deviation of %0.2f" % (knnScores.mean(), knnScores.std()))
print("")

logModel=LogisticRegression(max_iter=10000)
logScores = cross_val_score(logModel, X, Y, cv=5, scoring='neg_root_mean_squared_error')
print("Logistic: Mean score of %0.2f with a standard deviation of %0.2f" % (logScores.mean(), logScores.std()))

















