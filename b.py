import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import classification_report

import sklearn.metrics as metrics

data = pd.read_csv('test.csv')

pre = [89, 80, 87, 86, 85]
u_strand = 'ICT'
dummies = pd.get_dummies(data['Strand'])
for s in dummies.columns.values:
    if s == u_strand:
        pre.append(1)
    else:
        pre.append(0)

merged = pd.concat([data, dummies], axis='columns')
a = merged.drop(['Strand'], axis='columns')
merged = merged.drop(['Course', 'Strand'], axis='columns')

c = data['Course'].values
# course = pd.Series(data['Course'])
#print(a)
course = []
for i in c:
    course.append(i)
    
y = [i for i in range(len(c))]
print(a)
        

drop = [-1]
for i in range(10):
    if len(y) <= 0:
        break;
    
    if drop[0] != -1:
        merged = merged.drop(drop, axis='rows').reset_index(drop=True)
        a = a.drop(drop, axis='rows').reset_index(drop=True)
        course.pop(drop[0])
        print(a)
        # course = pd.Series(data['Course']).drop(drop)
        
    x = merged.values
    model = LinearRegression()
    model.fit(x, y)
    print(model.score(x, y))
    p = model.predict([pre])
   
    
    y.pop()
    predicted = round(p[0])
    if predicted >= len(y)-1:
        drop[0] = len(y)-1
    elif predicted <= 0:
        drop[0] = 0
    else:
        drop[0] = predicted
    
    print(predicted)
    y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)
    print('predicted response:', y_pred, sep='\n')
    # print(model.intercept_, model.coef_)
    #print(course.values[drop[0]])
    print(course[drop[0]])
    # print(model.coef_, model.intercept_)
