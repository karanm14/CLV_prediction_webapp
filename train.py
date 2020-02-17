import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, median_absolute_error, mean_squared_error
import pickle

print("Loading Data")
print("\n\n\n")
df = pd.read_excel('Online Retail.xlsx', sheet_name="Online Retail")
print("Data Loaded")
print("\n\n\n")
df = df[df['Quantity']>0]
df = df[df['CustomerID'].notnull()]

print("Date Range: %s - %s" % (df["InvoiceDate"].min(), df['InvoiceDate'].max()))

df = df[df['InvoiceDate'] <'2011-12-01']

df['Sales'] = df['Quantity'] * df['UnitPrice']

orders_df = df.groupby(['CustomerID', 'InvoiceNo']).agg({'Sales': sum,'InvoiceDate': max})

def groupby_mean(x):
    return x.mean()

def groupby_count(x):
    return x.count()

def purchase_duration(x):
    return (x.max() - x.min()).days

def avg_frequency(x):
    return (x.max() - x.min()).days/x.count()

groupby_mean.__name__ = 'avg'
groupby_count.__name__ = 'count'
purchase_duration.__name__ = 'purchase_duration'
avg_frequency.__name__ = 'purchase_frequency'

#summary_df = orders_df.reset_index().groupby('CustomerID').agg({
#    'Sales': [min, max, sum, groupby_mean, groupby_count],
#    'InvoiceDate': [min, max, purchase_duration, avg_frequency]})

clv_time = '3M'
print("Preparing Data....")
print("\n\n\n")
data_df = orders_df.reset_index().groupby(['CustomerID',
                                 pd.Grouper(key='InvoiceDate',freq=clv_time)]).agg({'Sales': [sum, groupby_mean, groupby_count]})
data_df.columns = ['_'.join(col).lower() for col in data_df.columns]
data_df = data_df.reset_index()
date_month_map = {
    str(x)[:10]: 'M_%s' % (i+1) for i,x in enumerate(
    sorted(data_df.reset_index()['InvoiceDate'].unique(), reverse=True))
}
data_df['M'] = data_df['InvoiceDate'].apply(lambda x: date_month_map[str(x)[:10]])

print("Data prepared")
print("\n\n\n")
print("Features..")
print("\n\n\n")
features_df = pd.pivot_table(data_df[data_df['M']!='M_1'], values=['sales_sum', 'sales_avg', 'sales_count'],columns = 'M', index = 'CustomerID')
features_df = features_df.fillna(0)
features_df.columns = ['_'.join(col) for col in features_df.columns]
print("Target...")
print("\n\n\n")
target_df = data_df[data_df['M'] == 'M_1'][['CustomerID','sales_sum']]
target_df = target_df.set_index('CustomerID')
print("Data for model")
print("\n\n\n")
mldata = features_df.join(target_df,how='left')
mldata = mldata.fillna(0)

mldata = mldata.rename(columns={'sales_sum':'CLV_3M'})

print(mldata['CLV_3M'].describe())
print("\n\n\n")

Y = mldata['CLV_3M']
X = mldata.drop(columns=['CLV_3M'])
print("Loading Model")
print("\n\n\n")

linear_regression = LinearRegression()
print("Training Model")
print("\n\n\n")
linear_regression.fit(X, Y)
print("Model trained")
print("\n\n\n")
print("intercepts",linear_regression.intercept_)
print("\n\n\n")
coef = pd.DataFrame(list(zip(X,linear_regression.coef_)))
coef.columns = ['feature', 'coef']
print("coefficients",coef,"\n\n\n")

train_pred = linear_regression.predict(X)


print('In-Sample R-Squared: %0.4f' % r2_score(y_true=Y, y_pred=train_pred))
print("\n\n\n")
print('In-Sample MAE: %0.4f' % median_absolute_error(y_true=Y, y_pred=train_pred))
print("\n\n\n")
print('In-Sample MSE: %0.4f' % mean_squared_error(y_true=Y, y_pred=train_pred))
print("\n\n\n")
print("\n\n\n")
print("Pickling model")
pickl = {'model': linear_regression}
pickle.dump(pickl, open('model_file' + ".p", "wb"))
print("Model pickled")