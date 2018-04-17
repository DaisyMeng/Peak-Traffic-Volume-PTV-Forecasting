import numpy as np
import pickle
from datetime import datetime

sleep_start=0
sleep_end=7
###############################################################################
######################## Find features #######################################
###############################################################################
f = open('reduced.pckl', 'rb')
[v,p,df] = pickle.load(f)
f.close()

#   1. promotion_average_discount: promotion weighted by hours
df['promotion_price'] = np.zeros(len(df))
df['promotion_rebate'] = np.zeros(len(df))
df['promotion_discount'] = np.zeros(len(df))
df['promotion_item'] = np.zeros(len(df))
df['promotion_hour'] = np.zeros(len(df))
for i in range(0,len(p)):
    print(i)
    S=(p['start_time'][i]-df['date'][0]).days
    E=(p['end_time'][i]-df['date'][0]).days
    SH=p['start_time'][i].hour
    EH=p['end_time'][i].hour
    tmpp=p['promotion_price'][i]
    tmpr=p['rebate'][i]
    dis=p['discount_percent'][i]
    duration=E-S
    
    

    if S==365:
        continue

    if duration==0:
        df['promotion_item'][S]+=1
        if SH>sleep_end:
            df['promotion_hour'][S]+=(EH-SH)
            df['promotion_price'][S]+=tmpp*(EH-SH)
            df['promotion_rebate'][S]+=tmpr*(EH-SH)
            df['promotion_discount'][S]+=dis*(EH-SH)
        else:
            df['promotion_hour'][S]+=(EH-sleep_end)
            df['promotion_price'][S]+=tmpp*(EH-sleep_end)
            df['promotion_rebate'][S]+=tmpr*(EH-sleep_end)
            df['promotion_discount'][S]+=dis*(EH-sleep_end)
       
    elif duration==1:
        df['promotion_item'][S]+=1
        if SH>sleep_end:
            df['promotion_hour'][S]+=24-SH
            df['promotion_price'][S]+=tmpp*(24-SH)
            df['promotion_rebate'][S]+=tmpr*(24-SH)
            df['promotion_discount'][S]+=dis*(24-SH)
        else:
            df['promotion_hour'][S]+=24-sleep_end
            df['promotion_price'][S]+=tmpp*(24-sleep_end)
            df['promotion_rebate'][S]+=tmpr*(24-sleep_end)
            df['promotion_discount'][S]+=dis*(24-sleep_end)
        if EH>sleep_end and E<365:
            df['promotion_hour'][E]+=(EH-sleep_end)
            df['promotion_item'][E]+=1
            df['promotion_price'][E]+=tmpp*(EH-sleep_end)
            df['promotion_rebate'][E]+=tmpr*(EH-sleep_end)
            df['promotion_discount'][E]+=dis*(EH-sleep_end)
    else:
        df['promotion_item'][S:E]+=1
        if SH>sleep_end:
            df['promotion_hour'][S]+=24-SH
            df['promotion_price'][S]+=tmpp*(24-SH)
            df['promotion_rebate'][S]+=tmpr*(24-SH)
            df['promotion_discount'][S]+=dis*(24-SH)
        else:
            df['promotion_hour'][S]+=(24-sleep_end)
            df['promotion_price'][S]+=tmpp*(24-sleep_end)
            df['promotion_rebate'][S]+=tmpr*(24-sleep_end)
            df['promotion_discount'][S]+=dis*(24-sleep_end)
        df['promotion_hour'][S+1:E]+=(24-sleep_end)
        df['promotion_price'][S+1:E]+=tmpp*(24-sleep_end)
        df['promotion_rebate'][S+1:E]+=tmpr*(24-sleep_end)
        df['promotion_discount'][S+1:E]+=dis*(24-sleep_end)
        if EH>sleep_end and E<365:
            df['promotion_hour'][E]+=(EH-sleep_end)
            df['promotion_item'][E]+=1
            df['promotion_price'][E]+=tmpp*(EH-sleep_end)
            df['promotion_rebate'][E]+=tmpr*(EH-sleep_end)
            df['promotion_discount'][E]+=dis*(EH-sleep_end)
    
for i in range(0,len(df)):
    if df['promotion_hour'].iloc[i]==0:
        df['promotion_price'].iloc[i]=0
        df['promotion_rebate'].iloc[i]=0
        df['promotion_discount'].iloc[i]=0
    else:
        df['promotion_price'].iloc[i]=df['promotion_price'].iloc[i]/df['promotion_hour'].iloc[i]
        df['promotion_rebate'].iloc[i]=df['promotion_rebate'].iloc[i]/df['promotion_hour'].iloc[i]
        df['promotion_discount'].iloc[i]=df['promotion_discount'].iloc[i]/df['promotion_hour'].iloc[i]

    
f = open('df_promotion.pckl', 'wb')
pickle.dump(df, f)
f.close()
    
f = open('df_promotion.pckl', 'rb')
df = pickle.load(f)
f.close()       
print(df)

#   2. vounchers
#       -hourly
df['voucher_value'] = np.zeros(len(df))                         # time weighted average voucher value
df['voucher_min'] = np.zeros(len(df))                           # time weighted average voucher minimum price
df['voucher_discount'] = np.zeros(len(df))                      # time weighted average voucher discount
df['voucher_total'] = np.zeros(len(df))                          # time weighted average voucher number
df['voucher_hour']= np.zeros(len(df))
df['voucher_number']= np.zeros(len(df))                         # number of vouchers per day
df['voucher_value_n'] = np.zeros(len(df))                          # number weighted average voucher value
df['voucher_min_n'] = np.zeros(len(df))                          # number weighted average voucher value
df['voucher_discount_n']= np.zeros(len(df))

#Assume people sleep during 00:00-06:00
i=0
while(i<len(v)):
    print(i)
    S=(v['start_time'].iloc[i]-df['date'][0]).days
    E=(v['end_time'].iloc[i]-df['date'][0]).days
    if S==365:
        i+=1
        continue
    SH=v['start_time'].iloc[i].hour
    EH=v['end_time'].iloc[i].hour
    duration=E-S
    
    

    j=i
    va,dis,mp,ul,uv,d,m,vv=0,0,0,0,0,0,0,0
    while(j<len(v) and v['mark_date'].iloc[j]==v['mark_date'].iloc[i]):
        va+=v['value'].iloc[j]
        dis+=v['discount'].iloc[j]
        mp+=v['min_price'].iloc[j]
        ul+=v['usage_limit'].iloc[j]
        uv+=ul*va
        d+=v['discount'].iloc[j]*v['usage_limit'].iloc[j]
        m+=v['min_price'].iloc[j]*v['usage_limit'].iloc[j]
        vv+=v['value'].iloc[j]*v['usage_limit'].iloc[j]
        j+=1
    if duration==0:
        df['voucher_number'][S]+=ul
        df['voucher_value_n'][S]+=vv
        df['voucher_min_n'][S]+=m
        df['voucher_discount_n'][S]+=d

        if SH>sleep_end:
            df['voucher_hour'][S]+=(EH-SH)
            df['voucher_value'][S]+=va*(EH-SH)
            df['voucher_discount'][S]+=dis*(EH-SH)
            df['voucher_min'][S]+=mp*(EH-SH)
            df['voucher_total'][S]+=ul*(EH-SH)
        else:
            df['voucher_hour'][S]+=(EH-sleep_end)
            df['voucher_value'][S]+=va*(EH-sleep_end)
            df['voucher_discount'][S]+=dis*(EH-sleep_end)
            df['voucher_min'][S]+=mp*(EH-sleep_end)
            df['voucher_total'][S]+=ul*(EH-sleep_end)
    elif duration==1:
        if SH>sleep_end:
            df['voucher_hour'][S]+=24-SH
            df['voucher_value'][S]+=va*(24-SH)
            df['voucher_discount'][S]+=dis*(24-SH)
            df['voucher_min'][S]+=mp*(24-SH)
            df['voucher_total'][S]+=ul*(24-SH)
        else:
            df['voucher_hour'][S]+=24-sleep_end
            df['voucher_value'][S]+=va*(24-sleep_end)
            df['voucher_discount'][S]+=dis*(24-sleep_end)
            df['voucher_min'][S]+=mp*(24-sleep_end)
            df['voucher_total'][S]+=ul*(24-sleep_end)
        if EH>sleep_end and E<365:
            df['voucher_number'][E]+=ul
            df['voucher_hour'][E]+=EH-sleep_end
            df['voucher_value'][E]+=va*(EH-sleep_end)
            df['voucher_discount'][E]+=dis*(EH-sleep_end)
            df['voucher_min'][E]+=mp*(EH-sleep_end)
            df['voucher_total'][E]+=ul*(EH-sleep_end)
            df['voucher_value_n'][S:E+1]+=vv
            df['voucher_min_n'][S:E+1]+=m
            df['voucher_discount_n'][S:E+1]+=d
            df['voucher_number_n'][S:E+1]+=ul
        elif EH<=sleep_end and E<365:
            df['voucher_value_n'][S:E]+=vv
            df['voucher_min_n'][S:E]+=m
            df['voucher_discount_n'][S:E]+=d
            df['voucher_number_n'][S:E]+=ul            
    else:
        df['voucher_number'][S]+=ul
        if SH>sleep_end:
            df['voucher_hour'][S]+=24-SH
            df['voucher_value'][S]+=va*(24-SH)
            df['voucher_discount'][S]+=dis*(24-SH)
            df['voucher_min'][S]+=mp*(24-SH)
            df['voucher_total'][S]+=ul*(24-SH)
        else:
            df['voucher_hour'][S]+=24-sleep_end
            df['voucher_value'][S]+=va*(24-sleep_end)
            df['voucher_discount'][S]+=dis*(24-sleep_end)
            df['voucher_min'][S]+=mp*(24-sleep_end)
            df['voucher_total'][S]+=ul*(24-sleep_end)
        df['voucher_number'][S+1:E]+=ul    
        df['voucher_hour'][S+1:E]+=24-sleep_end
        df['voucher_value'][S+1:E]+=va*(24-sleep_end)
        df['voucher_discount'][S+1:E]+=dis*(24-sleep_end)
        df['voucher_min'][S+1:E]+=mp*(24-sleep_end)
        df['voucher_total'][S+1:E]+=ul*(24-sleep_end)

        if EH>sleep_end and E<365:
            df['voucher_number'][E]+=ul
            df['voucher_hour'][E]+=EH-sleep_end
            df['voucher_value'][E]+=va*(EH-sleep_end)
            df['voucher_discount'][E]+=dis*(EH-sleep_end)
            df['voucher_min'][E]+=mp*(EH-sleep_end)
            df['voucher_total'][E]+=ul*(EH-sleep_end)
            df['voucher_value_n'][S:E+1]+=vv
            df['voucher_min_n'][S:E+1]+=m
            df['voucher_discount_n'][S:E+1]+=d
            df['voucher_number_n'][S:E+1]+=ul
        elif EH<=sleep_end and E<365:
            df['voucher_value_n'][S:E]+=vv
            df['voucher_min_n'][S:E]+=m
            df['voucher_discount_n'][S:E]+=d
            df['voucher_number_n'][S:E]+=ul   
    i=j
df['weekday']=list(map(lambda x:x.weekday(),df['date']))
df['voucher_value']=list(map(lambda x,y:x/y,df['voucher_value'],df['voucher_hour']))
df['voucher_discount']=list(map(lambda x,y:x/y,df['voucher_discount'],df['voucher_hour']))
df['voucher_min']=list(map(lambda x,y:x/y,df['voucher_min'],df['voucher_hour']))
df['voucher_total']=list(map(lambda x,y:x/y,df['voucher_total'],df['voucher_hour']))
df['voucher_value_n']=list(map(lambda x,y:x/y,df['voucher_value_n'],df['voucher_number_n']))
df['voucher_min_n']=list(map(lambda x,y:x/y,df['voucher_min_n'],df['voucher_number_n']))
df['voucher_discount_n']=list(map(lambda x,y:x/y,df['voucher_discount_n'],df['voucher_number_n']))
#f = open('features_pv.pckl', 'wb')
#pickle.dump(df, f)
#f.close()
#
#df.to_csv('features.csv')
#
#f = open('features_pv.pckl', 'rb')
#df = pickle.load(f)
#f.close()
#
#   3. Public holidays and Special Events 
feature=df[['voucher_value_n','voucher_min_n','voucher_discount_n','voucher_number','weekday','voucher_money','voucher_total','voucher_min','voucher_value','voucher_discount','promotion_discount','promotion_rebate','promotion_price','promotion_hour','promotion_item']]
feature['event']=np.ones(len(feature))    # nomal days
feature['event'][(datetime(2017,1,1)-datetime(2017,1,1)).days:(datetime(2017,1,3)-datetime(2017,1,1)).days]=2  # New Year's Day
feature['event'][(datetime(2017,1,26)-datetime(2017,1,1)).days:(datetime(2017,1,31)-datetime(2017,1,1)).days]=0 # Chinese New Year Delivery Stop
#feature['event'][(datetime(2017,2,27)-datetime(2017,1,1)).days:(datetime(2017,3,1)-datetime(2017,1,1)).days]=2
feature['event'][(datetime(2017,4,3)-datetime(2017,1,1)).days:(datetime(2017,4,5)-datetime(2017,1,1)).days]=2 # Tomb Sweeping Day, Children's Day
#feature['event'][(datetime(2017,5,29)-datetime(2017,1,1)).days:(datetime(2017,5,31)-datetime(2017,1,1)).days]=2
#feature['event'][(datetime(2017,10,4)-datetime(2017,1,1)).days:(datetime(2017,10,5)-datetime(2017,1,1)).days]=2
feature['event'][(datetime(2017,10,9)-datetime(2017,1,1)).days:(datetime(2017,10,11)-datetime(2017,1,1)).days]=2 # National Day Holiday
feature['event'][(datetime(2017,11,8)-datetime(2017,1,1)).days:(datetime(2017,11,12)-datetime(2017,1,1)).days]=3 # 11.11
feature['event'][(datetime(2017,12,11)-datetime(2017,1,1)).days:(datetime(2017,12,12)-datetime(2017,1,1)).days]=3 # 12.12

#   4. Promotion events of the previous day
feature_lag=feature.shift(1)
feature_lag.iloc[0]=feature_lag.iloc[1]
feature_lag['weekday'].iloc[0]=5

feature[['voucher_value_n_l','voucher_min_n_l','voucher_discount_n_l','voucher_number_l','weekday_l','voucher_money_l','voucher_total_l','voucher_min_l','voucher_value_l','voucher_discount_l','promotion_discount_l','promotion_rebate_l','promotion_price_l','promotion_hour_l','promotion_item_l','event_l']]=feature_lag

#   5. Day of the month
feature['monthday']=np.zeros(len(feature))
for i in range(0,len(feature)):
    feature['monthday'][i]=df['date'][i].day
    
f = open('feature_all.pckl', 'wb')
pickle.dump(feature, f)
f.close()
