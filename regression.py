import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold


f = open('feature_all.pckl', 'rb')
feature = pickle.load(f)
f.close()

f = open('reduced.pckl', 'rb')
[v,p,df] = pickle.load(f)
f.close()

###################################################################################
######################### Regression ##############################################
###################################################################################


time=df[['Unnamed: 0']]
time.rename(index=str, columns={"Unnamed: 0": "day"})

# trend
regr_trend = linear_model.LinearRegression()
regr_trend.fit(time, df['PTV'])
trend_predict=regr_trend.predict(time)
#plt.plot(df['date'][test_index],trend_test_predict,'r',df['date'][test_index],df['PTV'][test_index],'b')

# detrend
y_detrend=df['PTV']-trend_predict

kf = KFold(n_splits=10)

feature_tree=feature[['voucher_total_l','voucher_number_l', 'voucher_discount_l',
 'voucher_value_n', 'voucher_number', 'promotion_hour' ,'monthday',
 'voucher_min_n', 'weekday' ,'promotion_item' ,'event', 'event_l']]
Predict=[]
for train_index, test_index in kf.split(feature_tree):

    train,test=feature_tree.iloc[train_index],feature_tree.iloc[test_index]
    y_train=y_detrend[train_index]
    y_test=y_detrend[test_index]



    
    # forcast on stationary data
    regr = ExtraTreesRegressor(max_leaf_nodes=7)
    regr.fit(train, y_train)
    y_randomforest_predict=regr.predict(test)
   
    poly = PolynomialFeatures(degree=2)
    X_ = poly.fit_transform(feature_tree[['event','promotion_item']].iloc[train_index])
    predict_ = poly.fit_transform(feature_tree[['event','promotion_item']].iloc[test_index])
    polyr=linear_model.LinearRegression()
    polyr.fit(X_,y_train-regr.predict(train)) 
    y_poly_predict=polyr.predict(predict_)     
#    y_poly_predict=np.zeros(len(test_index))
    
    y_predict=y_poly_predict+y_randomforest_predict+trend_predict[test_index]
#        y_train_predict=trend_predict.iloc[train_index]+regr.predict(train)
    
    Predict=np.append(Predict,y_predict)
plt.figure()
plt.title('PTV')
plt.plot(df['date'],Predict,'r',label='predicted PTV')
plt.plot(df['date'],df['PTV'],'b',label='true value of PTV')
plt.legend(loc='best')
plt.show()

print(mean_squared_error(Predict,df['PTV']))
print(feature_tree.columns.values)