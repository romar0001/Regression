import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import numpy as np

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
merged = merged.drop(['Course', 'Strand', 'ICT'], axis='columns')
print(merged)
c = data['Course'].values
# course = pd.Series(data['Course'])
#print(a)
course = []
for i in c:
    course.append(i)
    
y = [i for i in range(len(c))]

drop = [-1]
for i in range(10):
    if len(y) <= 0:
        break;
    
    if drop[0] != -1:
        merged = merged.drop(drop, axis='rows').reset_index(drop=True)
        a = a.drop(drop, axis='rows').reset_index(drop=True)
        course.pop(drop[0])
        # course = pd.Series(data['Course']).drop(drop)
        print(a)
    x = merged.values
    x = sm.add_constant(x) # adding a constant
 
    model = sm.OLS(y, x).fit()
    predictions = model.predict(x) 
    print(predictions)
    print_model = model.summary()
    print(print_model)
    break;
    '''
    p = model.predict([pre])
    #print(p)
    y.pop()
    predicted = round(p[0])
    if predicted >= len(y)-1:
        drop[0] = len(y)-1
    elif predicted <= 0:
        drop[0] = 0
    else:
        drop[0] = predicted
    
    print(predicted)
    '''
    # print(model.intercept_, model.coef_)
    #print(course.values[drop[0]])
    # print(course[drop[0]])
    # print(model.coef_, model.intercept_)
