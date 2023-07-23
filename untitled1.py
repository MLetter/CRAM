import numpy as np 
import pandas as pd
from scipy import stats

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier, LinearRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.utils import shuffle

# reading the data
df = pd.read_csv("covidData.csv", delimiter=",")
#print(datainput)
'''
dI['LOS'] = dI['LOS'].astype('float64')
X = dI.select_dtypes('float64').values
Y = dI['Severity'].values
'''
#given the large amount of variables many were taken out to so the less impactfull variables were removed. 
proDf = df.loc[:, 'Derivation cohort':'Death']
proDf = pd.concat([proDf, df.loc[:, 'Severity':'Age.1']], axis='columns')
print(proDf)

O2_mean = df[df['OsSats'] > 0]['OsSats'].mean()
proDf['o2sats'] = df['OsSats'].apply(lambda x: O2_mean if x == 0 else x)

temp_mean = df[df['Temp'] > 0]['Temp'].mean()
proDf['temp'] = df['Temp'].apply(lambda x: temp_mean if x < 0 else x)

map_mean = df[df['MAP'] > 0]['MAP'].mean()
proDf['map'] = df['MAP'].apply(lambda x: map_mean if x == 0 else x)

ddimer_mean = df[df['Ddimer'] > 0]['Ddimer'].mean()
proDf['ddimer'] = df['Ddimer'].apply(lambda x: ddimer_mean if x == 0 else x)

plt_mean = df[df['Plts'] > 0]['Plts'].mean()
proDf['plt'] = df['Plts'].apply(lambda x: plt_mean if x == 0 else x)

inr_mean = df[df['INR'] > 0]['INR'].mean()
proDf['inr'] = df['INR'].apply(lambda x: inr_mean if x == 0 else x)

bun_mean = df[df['BUN'] > 0]['BUN'].mean()
proDf['bun'] = df['BUN'].apply(lambda x: bun_mean if x == 0 else x)

creatinine_mean = df[df['Creatinine'] > 0]['Creatinine'].mean()
proDf['creatinine'] = df['Creatinine'].apply(lambda x: creatinine_mean if x == 0 else x)

sodium_mean = df[df['Sodium'] > 0]['Sodium'].mean()
proDf['sodium'] = df['Sodium'].apply(lambda x: sodium_mean if x == 0 else x)

glucose_mean = df[df['Glucose'] > 0]['Glucose'].mean()
proDf['glucose'] = df['Glucose'].apply(lambda x: glucose_mean if x == 0 else x)

ast_mean = df[df['AST'] > 0]['AST'].mean()
proDf['ast'] = df['AST'].apply(lambda x: ast_mean if x == 0 else x)

alt_mean = df[df['ALT'] > 0]['ALT'].mean()
proDf['alt'] = df['ALT'].apply(lambda x: alt_mean if x == 0 else x)

wbc_mean = df[df['WBC'] > 0]['WBC'].mean()
proDf['wbc'] = df['WBC'].apply(lambda x: alt_mean if x == 0 else x)

lympho_mean = df[df['Lympho'] > 0]['Lympho'].mean()
proDf['lympho'] = df['Lympho'].apply(lambda x: alt_mean if x == 0 else x)

IL6_mean = df[df['IL6'] > 0]['IL6'].median()
proDf['il6'] = df['IL6'].apply(lambda x: IL6_mean if x == 0 else x)

ferritin_mean = df[df['Ferritin'] > 0]['Ferritin'].median()
proDf['ferritin'] = df['Ferritin'].apply(lambda x: ferritin_mean if x == 0 else x)

crct_mean = df[df['CrctProtein'] > 0]['CrctProtein'].mean()
proDf['crct'] = df['CrctProtein'].apply(lambda x: crct_mean if x == 0 else x)

procal_mean = df[df['Procalcitonin'] > 0]['Procalcitonin'].median()
proDf['procalcitonin'] = df['Procalcitonin'].apply(lambda x: procal_mean if x == 0 else x)

trop_mean = df[df['Troponin'] > 0]['Troponin'].median()
proDf['troponin'] = df['Troponin'].apply(lambda x: procal_mean if x == 0 else x)



data = shuffle(proDf)
X = data.drop(['Death', 'Severity', 'Derivation cohort'], axis='columns')
y1 = data['Death']
y2 = data['Severity']

print(data)

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


#--------------------------------------------------------------------
rf_model = GridSearchCV(RandomForestClassifier(), {
    'n_estimators': [25, 50, 75, 100, 150, 200],
    'criterion': ['gini', 'entropy'],
    'max_features': ['sqrt', 'log2', None]
})
'''
print(rf_model.fit(X_scaled, y1))

rf_description = pd.DataFrame(rf_model)
print(rf_description[['param_criterion', 'param_max_features', 'param_n_estimators', 'mean_test_score']])
'''

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y2, test_size=0.2, stratify=y2)
rfr_best_model = RandomForestRegressor(n_estimators=50, max_features=None, criterion='squared_error')
print(rfr_best_model.fit(X_train, y_train))
print(rfr_best_model.score(X_test, y_test))






