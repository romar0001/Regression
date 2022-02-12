import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('test.csv')
pre = [32, 45, 57, 64, 94]
u_strand = 'ABM'
dummies = pd.get_dummies(data['Strand'])
for s in dummies.columns.values:
    if s == u_strand:
        pre.append(1)
    else:
        pre.append(0)

merged = pd.concat([data, dummies], axis='columns')
merged = merged.drop(['Course', 'Strand'], axis='columns')


# course = data['Course'].values
course = pd.Series(data['Course'])

y = [i for i in range(len(course.values))]

drop = [-1]
for i in range(10):
    if len(y) <= 0:
        break;
    
    if drop[0] != -1:
        merged = merged.drop(drop, axis='rows').reset_index(drop=True)
        course = pd.Series(data['Course']).drop(drop)
    x = merged.values
    model = LinearRegression()
    model.fit(x, y)
    p = model.predict([pre])
    predicted = round(p[0])
    y.pop()
    if predicted > len(y):
        drop[0] = len(y)-1
    elif predicted < 0:
        drop[0] = 0
    else:
        drop[0] = predicted
    print(course.values[drop[0]])
