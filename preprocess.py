import pickle
from datetime import datetime ,timedelta,time
import pandas as pd
import numpy as np

#######################################################################################
###############################  load data #############################################
########################################################################################
#   1. read the data from csv files
df = pd.read_csv('../data/PTV_TTV.csv')
v=pd.read_csv('../data/vouchers.csv')
p=pd.read_csv('../data/promotions.csv')

#   2. convert to datetime 
#       -vouchers
v['start_time'] = v['start_time'].map(lambda x: datetime.strptime(x, '%m/%d/%Y %H:%M'))
v['end_time'] = v['end_time'].map(lambda x: datetime.strptime(x, '%m/%d/%Y %H:%M'))

#       -promotions

for i in range(0,len(p['start_time'])):
    if p['start_time'][i].find('2017')==-1:
        p['start_time'][i] =datetime.strptime(p['start_time'][i], '%d/%m/%y %H:%M')
    else:
        p['start_time'][i] =datetime.strptime(p['start_time'][i], '%d/%m/%Y %H:%M')

for i in range(0,len(p['end_time'])):
    if p['end_time'][i].find('2017')==-1:
        p['end_time'][i] =datetime.strptime(p['end_time'][i], '%d/%m/%y %H:%M')
    else:
        p['end_time'][i] =datetime.strptime(p['end_time'][i], '%d/%m/%Y %H:%M')

#       -PTV data
df['date'] = df['date'].map(lambda x: datetime.strptime(x, '%d/%m/%y'))

with open('incentives.pckl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([v,p,df], f)
f.close

###############################################################################################
############################## correct wrong data #############################################
###############################################################################################
f = open('incentives.pckl', 'rb')
[v,p,df] = pickle.load(f)
f.close()

  
#   1. promotion wrong data: if discount percentage below zero, reset it to zero


for i in range(0,len(p)):
    if p['discount_percent'][i]<0:     
        p['discount_percent'][i]=0
        print(i)

#   2.voucher wrong data: 
#       - year set to 2017
#       - drop the row if end_time<start time
s=list(map(lambda x:x.year,v['start_time'])).count(2017)
e=list(map(lambda x:x.year,v['end_time'])).count(2017)
for i in range(0,len(v)):
    if(v['end_time'][i].year!=2017):
        v['end_time'][i]=datetime(2018,1,1,0,0,0)

# drop the vouchers if end time<start time
id=[10848,10850,36765,36865,37053,45472,54695,64284,80989,85323,100037,108577,114286,116747,125367,146297,147564]
#for i in range(0,len(v)):
#    if (v['end_time']-v['start_time'])[i].days<0:
for i in id:
    v=v.drop(i)
    
with open('corrected.pckl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([v,p,df], f)
f.close


########################################################################################
#################  Voucher: reduce number of data ######################################
######################################################################################## 
f = open('corrected.pckl', 'rb')
[v,p,df] = pickle.load(f)
f.close()
   
#   1.normalize the time: round hours to either 00:00 or 12:00
#   2.combine voucher items: 
#       - for voucher with the same start time, end time, discount, min_price, value, combine the vouchers with usage limit added together
#       - for voucher with the same start time, end time only, mark them with the same number in mark_date column for future usage



tmps=v['start_time'][150033]
tmpe=v['end_time'][150033]
tmpv,tmpd,tmpm,i0,k,ii=0,0,0,0,0,0
v['mark_date'] = np.zeros(len(v))  

while(ii<len(v)):
    i=v.index[ii]
    print(i)
    
    if v['start_time'][i].minute!=0:
        if v['start_time'][i].minute>30:
            v['start_time'][i]=(v['start_time'][i]+timedelta(hours=1)).replace(second=0,minute=0)
        else:
            v['start_time'][i]=v['start_time'][i].replace(second=0,minute=0)
    if v['end_time'][i].minute!=0: 
        if v['end_time'][i].minute>30:
            v['end_time'][i]=(v['end_time'][i]+timedelta(hours=1)).replace(second=0,minute=0)
        else:
            v['end_time'][i]=v['end_time'][i].replace(second=0,minute=0)
   

    if v['start_time'][i]==tmps and v['end_time'][i]==tmpe:
        v['mark_date'][i]=k
        if v['discount'][i]==tmpd and v['min_price'][i]==tmpm and v['value'][i]==tmpv:
             v['usage_limit'][i0]+=v['usage_limit'][i]
             v=v.drop(i)
             j=1
        else:
             tmpd=v['discount'][i]
             tmpm=v['min_price'][i]
             tmpv=v['value'][i]
             i0=i
             j=0
    else:
        k+=1
        v['mark_date'][i]=k
        tmps=v['start_time'][i]
        tmpe=v['end_time'][i]
        tmpd=v['discount'][i]
        tmpm=v['min_price'][i]
        tmpv=v['value'][i]
        i0=i
        j=0
    ii=ii+1-j
    
v.to_csv('reduced.csv')
with open('reduced.pckl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([v,p,df], f)
f.close
