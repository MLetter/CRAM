'''
Data set manipulation and training using RandomForestRegressor 
'''

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, SGDClassifier, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.utils import shuffle
from matplotlib import pyplot as plt

# reading the data
df = pd.read_csv("covidData.csv", delimiter=",")
#print(datainput)

#given the large amount of variables many were taken out to so the less impactfull variables were removed. 
proDf = df.loc[:, 'Derivation cohort':'Death']
proDf = pd.concat([proDf, df.loc[:, 'Severity':'Age.1']], axis='columns')
#print(proDf)




#Assigns X and y for training 
data = shuffle(proDf)
X = data.drop(['Death', 'Severity', 'Derivation cohort'], axis='columns')
y1 = data['Death']
y2 = data['Severity']
#print(data)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

log_scores = cross_val_score(LogisticRegression(max_iter=1000000), X_scaled, y1)
sgd_scores = cross_val_score(SGDClassifier(), X_scaled, y1)
svc_scores = cross_val_score(SVC(), X_scaled, y1)
rf_scores = cross_val_score(RandomForestClassifier(), X_scaled, y1)

print('Log score: ' + str(log_scores.mean()))
print('SGD score: ' + str(sgd_scores.mean()))
print('SVC score: ' + str(svc_scores.mean()))
print('RF score: ' + str(rf_scores.mean()))

rf_modelx = GridSearchCV(RandomForestClassifier(), {
    'n_estimators': [25, 50, 75, 100, 150, 200],
    'criterion': ['gini', 'entropy'],
    'max_features': ['sqrt', 'log2', None]
})

rf_model = rf_modelx.fit(X_scaled, y1)
#print(rf_model.fit(X_scaled, y1))

#this modual will look fot the best paramiters for the model
#rf_description = pd.DataFrame(rf_model.cv_results_)
#print(rf_description[['param_criterion', 'param_max_features', 'param_n_estimators', 'mean_test_score']])
#print(rf_model.best_params_)

#trains the model
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y2, test_size=0.2, random_state=0)


#input the best params 
rfr_best_model = RandomForestRegressor(n_estimators=100, max_features='sqrt', criterion='squared_error')
#rfr_best_model = LogisticRegression()
rfr_best_model.fit(X_train, y_train)

y_pred = rfr_best_model.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

#plotting the predicted model 
df1 = df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


