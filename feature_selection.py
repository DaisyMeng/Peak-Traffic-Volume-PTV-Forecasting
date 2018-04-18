import numpy as np
import pickle
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold


f = open('feature_all.pckl', 'rb')
feature = pickle.load(f)
f.close()
#
f = open('reduced.pckl', 'rb')
[v,p,df] = pickle.load(f)
f.close()

###################################################################################
######################### Feature Selection########################################
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

MSE=np.zeros(30)
kf = KFold(n_splits=10)
for i in range(0,30):
    importance=np.zeros(len(feature.columns.values))
    Predict=[]
    for train_index, test_index in kf.split(feature):
        train,test=feature.iloc[train_index],feature.iloc[test_index]
        y_train=y_detrend[train_index]
        y_test=y_detrend[test_index]
    
    
    
        
        # forcast on stationary data
        regr = ExtraTreesRegressor(max_leaf_nodes=7)
        regr.fit(train, y_train)
        y_randomforest_predict=regr.predict(test)
        
        poly = PolynomialFeatures(degree=2)
        X_ = poly.fit_transform(feature[['event','promotion_item']].iloc[train_index])
        predict_ = poly.fit_transform(feature[['event','promotion_item']].iloc[test_index])
        l=linear_model.LinearRegression()
        l.fit(X_,y_train-regr.predict(train)) 
        y_poly_predict=l.predict(predict_)     
    #    y_poly_predict=np.zeros(len(test_index))
        
        y_predict=y_poly_predict+y_randomforest_predict+trend_predict[test_index]
    #        y_train_predict=trend_predict.iloc[train_index]+regr.predict(train)
             
        y_predict=y_randomforest_predict+trend_predict[test_index]
        Predict=np.append(Predict,y_predict)
    #        y_train_predict=trend_predict.iloc[train_index]+regr.predict(train)
        importance+=regr.feature_importances_
    MSE[i]+=mean_squared_error(Predict,df['PTV'])
    print(i)
    print(list(zip(feature.columns.values,importance)))
    index=np.argsort(importance)[1:len(feature.columns.values)]
    feature=feature.iloc[:,index]