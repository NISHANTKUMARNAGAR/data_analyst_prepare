import pandas as pd
import numpy as np

'''min and max func return column wise data not any particular rows'''

#accessing column and sort_values
"""marks=[[0,1,3],[3,5,2],[6,7,6],[8,10,4],[12,13,9],[15,16,7]]
data=pd.DataFrame(marks)
print(data)
data1=pd.DataFrame(marks,columns=['marks','chem','eng'])
print(data1)
data1.rename(columns={'chem':'Chemistry','eng':'English'},inplace=True)
print(data1)
print(data1['Chemistry'])
print(data1['Chemistry'][1])
print(data1.head())
print(data1.tail())
print(data1.sort_values(by='English'))
print(data1.sort_values(by='English',ascending=False))
print(data1.sort_values(by='English',ignore_index=True))
print(data1.sort_values(by=['marks','chem'],ascending=[False,True]))"""

#fillna,ffill,bfill,describe,drop,pop,loc,creating row/column
"""data=pd.read_csv('book2.csv')
print(data)
print(data['name'])
print(data.sr)
print(data.columns)
print(data.columns.tolist())
print(data['marks'].max())
print(data['marks'].min())
print(data['marks'].count())
print(data['marks'].mean())
print(type(data['marks']))
print(type(data))
print(data.loc[[2,4,6],:])
print(data[data.marks>20])
#format is just dataframe[column][condition],a list for multiple columns
print(data[['name','gender']][data.marks>20])
print(data[data.gender=='M'])
#all dataframe nan are filled
data1=data['name'].fillna(0)
print(data1)
#filling specific columns with a value
#data['name']=data['name'].fillna('alias')
#print(data)
#specific column with specific value
data.fillna({'name':'random','gender':'unknown'},inplace=True)
print(data)
df5=pd.DataFrame({'ord_no':[70001.0,np.nan,70002.0,70004.0,np.nan,70005.0,np.nan,70010.0,70003.0,70012.0,np.nan,70013.0],
'purch_amt':[150.50,np.nan,65.26,110.50,948.50,np.nan,5760.00,1983.43,np.nan,250.45,75.29,3045.60],
'sale_amt':[10.50,20.65,np.nan,11.50,98.50,np.nan,57.00,19.43,np.nan,25.45,75.29,35.60],
'ord_date':['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
'salesman_id':[5002.0,5003.0,5001.0,np.nan,5002.0,5001.0,5001.0,np.nan,5003.0,5002.0,5003.0,np.nan]})
print(df5)
print(df5.ffill())
print(df5.assign(ord_no=df5.ord_no.ffill()))
print(df5.bfill())
#removing a row
#data=data.drop(6)
#print(data)
#removing a column and it also return column as Series and we can store it
dataframename.pop(columnname)
print(data.describe())
print('----assigning values in dataframe----')
print(data)
#both of below are not advised,
#check pandas extended point 2
#data.marks[5]=120
#data['marks'][4]=200
data.loc[6,'marks']=169 #this should be used
print(data)
print(d7.index)
#if a index or column does exist it updates and if not it creates
df=pd.DataFrame({'name':['A','B'],'no.':[1,2]})
df.loc[2]=['C',3]
print(df)
df.loc[:,'marks']=[10,20,30]
print(df)"""

#read and write in csv
"""data=pd.read_csv("book2.csv")
print(data)
data=pd.read_csv("book2.csv",skiprows=1)
print(data)
data=pd.read_csv("book2.csv",header=0)
print(data)
data=pd.read_csv("book2.csv",header=1)
print(data)
print(data.columns)
data=pd.read_csv("book2.csv",header=None)
print(data)
data=pd.read_csv("book2.csv",header=None,names=['sr','names','marks','gender'])
print(data)
data=pd.read_csv("book2.csv",header=0,names=['sr','names','marks','gender'])
print(data)
data=pd.read_csv("book2.csv",nrows=2)
print(data)
data=pd.read_csv("book2.csv",na_values=["null"])
print(data)
data=pd.read_csv("book2.csv",na_values={'name':['null'],'gender':['null']})
print(data)
data.to_csv("check_csv")
#d9.to_csv('test.csv',sep="\t",index=False) #does not take index of d9 as a seperate column
data=pd.read_csv("check_csv")
print(data)#has unnamed 0th column as from prev to_csv also saved row numbers"""

#replace
#can also tell how many times to replace data
"""data4=pd.read_csv('carsdata.csv')
print(data4)
data5=data4.replace('[A-Za-z]','',regex=True)
print(data5)
data6=data4.replace({'temp':'[a-zA-Z]','speed':'[0-9a-zA-Z]'},'',regex=True)
print(data6)
print('----handling data having missing items or random values----')
data=pd.read_csv("missingvalues.csv")
print(data)
data1=data.replace(-999,value=None)
print(data1)
data2=data.replace(['n.a.',-999],value=None)
print(data2)
data3=data.replace({'marks':[-999],'name':['n.a.']},{'name':'D','marks':40})
print(data3)"""

#groupby
"""data=pd.read_csv('groupby.csv')
print(data)
g1=data.groupby('weather')
print(g1) #groupby object
for weather,weather_df in g1:
    print(weather)
    print(weather_df)
print('to get only one group from groupby object')
print(g1.get_group('rain'))
print(g1.max()) #max from every column separately
print(g1.min()) #max from every column separately
print(g1.describe()) #describe gives statistical info
print(data.info()) #info gives structural info
g2=data.groupby(['weather','city']) #now groups are combination of two column values
print(g2) #groupby object
for cityweather,cityweather_df in g2:
    print(cityweather)
    print(cityweather_df)
print(list(g2)) #makes grouped dataframe in a list representation
print(g2.size()) #gives number of records in each group
print(g2.size().reset_index()) #gives reach group as a seperate index
print(df1.groupby(['customer_id','salesman_id']).agg({'purch_amt':'sum'})) #it gives dataframe output
print(df1.groupby(['customer_id','salesman_id'])['purch_amt'].agg('sum')) #it gives series output
df4=pd.DataFrame({'id': [1, 2, 1, 1, 2, 1, 2],
                  'type': [10, 15, 11, 20, 21, 12, 14],
                  'book': ['Math','English','Physics','Math','English','Physics','English']})
print(df4.groupby(['id','type','book']).size())
print(df4.groupby(['id','type','book']).size().unstack(fill_value=0))
g3=df4.groupby("id")
print(g3.groups.keys()) #to get all key values
#how to apply a custom function over a column
df8=pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.50,270.65,65.26,110.50,948.50,2400.60,5760.00,1983.43,2480.40,250.45,75.29,3045.60],
'ord_date':['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],
'customer_id':['C3001','C3001','D3005','D3001','C3005','D3001','C3005','D3001','D3005','C3001','D3005','D3005'],
'salesman_id':[5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
print(df8)
print(df8.groupby('customer_id').agg({'customer_id':lambda x:x.str.startswith('C').sum(),'ord_no':list,'purch_amt':lambda y:y.max()-y.min()}))
#groupby over a categorical range
df9=pd.DataFrame({'salesman_id':[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012],                         
'sale_jan':[150.50,270.65,65.26,110.50,948.50,2400.60,1760.00,2983.43,480.40,1250.45,75.29,1045.60]})                  
print(df9.groupby(pd.cut(df9['salesman_id'],bins=[0,5006,np.inf],labels=['S1','S2']),observed=False)['sale_jan'].sum())
df9=pd.DataFrame({'school':['s001','s002','s003','s001','s002','s004'],
                      'class':['V','V','VI','VI','V','VI'],
                      'name':['Alberto Franco','Gino Mcneill','Ryan Parkes',
                              'Eesha Hinton','Gino Mcneill','David Parkes'],
                      'date_Of_Birth':['15/05/2002','17/05/2002','16/02/1999',
                                       '25/09/1998','11/05/2002','15/09/1997'],
                      'age': [12, 12, 13, 13, 14, 12],
                      'weight': [173, 192, 186, 167, 151, 159],
                      'height': [30, np.nan, 33, 30, np.nan, 32],
                      'address': ['street1','street2','street3','street1',
                                  'street2','street4']}
                      ,index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
print(df9)
print(df9.groupby('height',dropna=False).filter(lambda x:pd.notnull(x.name)))
df10=pd.DataFrame({'dept':['A','A','B','B','B','C'],'salary':[10,20,30,40,50,60]})
print(df10.groupby('dept').filter(lambda x:len(x)>2))
df11=pd.DataFrame({'dept':['A','A','B','B','B'],'salary':[10,20,30,40,50]})
df11['dept_avg']=df11.groupby('dept')['salary'].transform('mean')
print(df11)
"""

#apply() - for both dataframe and series
"""df=pd.DataFrame({'serial':['p','r','s'],'marks':[100,80,55]})
print(df)
def add5(x):
    return x+5
print(df['marks'].apply(add5))
df['marks']=df['marks'].apply(lambda x:x+5)
#instead use vectorized operation like df['marks']=df['marks']+5
print(df)
df['serial']=df['serial'].apply(lambda x:x.upper())
print(df)
def grade(x):
    if x>=90:
        return 'A'
    elif x>=75:
        return 'B'
    else:
        return 'C'
print(df['marks'].apply(grade))
df1=pd.DataFrame({'english':[10,40,60],'math':[100,80,55]})
print(df1)
print(df1.apply(np.sum))
#as apply is not a reduction function
print(df1.apply(np.sum,axis=0)) #for column
print(df1.apply(np.sum,axis=1)) #for row
df2=pd.DataFrame({'name':['A','B','C'],'english':[10,40,60],'math':[100,80,55]})
print(df2)
print(df2.apply(lambda x:x['english']+x['math'],axis=1))"""

#map() - for specifically series
"""s=pd.Series(['M','F','M','F'])
print(type(s))
print(s)
gender_map={'M':'Male','F':'Female'}
s=s.map(gender_map)
print(s)
df1=pd.read_csv('test1.csv')
print(df1)
mapping={'Male':0,'Female':1}
df1['Gender']=df1['Gender'].map(mapping)
print(df1)
df2=pd.DataFrame({'serial':[1,2,3],'marks':[100,20,120]})
print(df2)
df2['marks']=df2['marks'].map(lambda x:x+5)
print(df2)"""

#agg()  #full form aggregation
"""df=pd.read_csv('agg.csv')
print(df)
print(df['Salary'].agg('mean'))
print(df['Salary'].agg(['min','max','mean']))
#print(df['Salary'].agg([np.min,np.max,np.mean]))
print(df.agg({'Salary':'mean','Age':['max','min']}))
print(df.groupby('Department')['Salary'].agg(['count','min','max','mean']))
print(df.groupby('Department').agg({'Salary':['mean','max','min'],'Age':['max','min']}))"""

#concat
"""raj_weather=pd.DataFrame({'city':['kota','jaipur'],'temp':[32,34],'humidity':[80,56]})
hr_weather=pd.DataFrame({'city':['panipat','rhotak'],'temp':[35,36],'wind':[60,45]})
df=pd.concat([raj_weather,hr_weather])
print(df)
#correct indexing
df=pd.concat([raj_weather,hr_weather],ignore_index=True)
print(df)
#printing dataframe wise or state wise
df=pd.concat([raj_weather,hr_weather],keys=['rajasthan','haryana'])
print(df)
#printing particular data
print(df.loc['rajasthan'])
#sorting
df=pd.concat([raj_weather,hr_weather],sort=True)
print(df)
df=pd.concat([raj_weather,hr_weather],axis=1,sort=True)
print(df)
df=pd.concat([raj_weather,hr_weather],axis=1,join='inner',sort=True)
print(df)
s1 = pd.Series([0, 1, 2, 3], name='col1')
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5], name='col3')
df1=pd.concat([s1, s2, s3], axis=1, keys=['column1', 'column2', 'column3'])
print(df1)
"""

#merge
"""in if on is None or not mentioned it merges on common col and on a common col with diff values uses _x or _y"""
"""city_weather=pd.DataFrame({'city':['kota','jaipur','bundi'],'temperature':[32,28,34]})
city_humidity=pd.DataFrame({'city':['kota','jaipur','bundi'],'humidity':[80,56,76]})
#below both same output as on=None takes common column as keys and city is that
df=pd.merge(city_weather,city_humidity,on='city')
print(df)
df=pd.merge(city_weather,city_humidity,on=None)
print(df)
#below with multiple common columns
DF1=pd.DataFrame({'city':['kota','jaipur'],'year':[2024,2025],'temperature':[32,38]})
DF2=pd.DataFrame({'city':['kota','jaipur'],'year':[2025,2024],'humidity':[80,56]})
df=pd.merge(DF1,DF2,on=None) #empty as multiple common and year not same
print(df)
df=pd.merge(DF1,DF2,on='year') #based on year
print(df)
df=pd.merge(DF1,DF2,on='city') #based on city
print(df)
#'how' parameter to tell join
city_weather1=pd.DataFrame({'city':['kota','jaipur','ajmer','baran'],'temperature':[32,28,34,36]})
city_humidity1=pd.DataFrame({'city':['kota','jaipur','bundi'],'humidity':[80,56,76]})
# on city column by default inner join
df=pd.merge(city_weather1,city_humidity1,on='city')
print(df)
#outer join on city so all cities
df=pd.merge(city_weather1,city_humidity1,on='city',how='outer')
print(df)
#left join so all from 1st dataframe and common 1st and 2nd dataframe
df=pd.merge(city_weather1,city_humidity1,on='city',how='left')
print(df)
#right join so all from 2nd dataframe and common 1st and 2nd dataframe
df=pd.merge(city_weather1,city_humidity1,on='city',how='right')
print(df)
#cross join so cross product of every record/row
df=pd.merge(city_weather1,city_humidity1,how='cross')
print(df)
#indicator=True shows record from which dataframe
df=pd.merge(city_weather1,city_humidity1,on='city',how='outer',indicator=True)
print(df)
#showing custom suffix
summer_weather=pd.DataFrame({'city':['kota','jaipur','ajmer','baran'],'data':[1,32,32,33]})
winter_weather=pd.DataFrame({'city':['kota','jaipur','bundi'],'data':[2,13,12]})
df=pd.merge(summer_weather,winter_weather,on='city',suffixes=["_summer","_winter"])
print(df)"""

#join
"""df4=pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2']},index=['K0','K1','K2'])
df5=pd.DataFrame({'C':['C0','C2','C3'],'D':['D0','D2','D3']},index=['K0','K2','K3'])
print(df4)
print(df5)
print(df4.join(df5))
print(df4.join(df5,how='inner'))
print(df4.join(df5,how='left'))
print(df4.join(df5,how='right'))"""

#combine_first()
"""df6=pd.DataFrame({'A':[np.nan,0.0,np.nan],'B':[3,4,5]})
df7=pd.DataFrame({'A':[1,1,3],'B':[3.0,np.nan,3.0]})
print(df6)
print(df7)
print(df6.combine_first(df7))"""

#pivot and pivot_table
#pivot- if duplicates throws error
#pivot-table -- allow duplicate handling by aggfunc
"""df=pd.read_csv('pivot.csv')
print(df)
df1=df.pivot(index='date',columns='city')
print(df1)
df1=df.pivot(index='date',columns='city',values='humidity')
print(df1)
df2=pd.read_csv("pivot1.csv")
print(df2)
df3=df2.pivot_table(index='city',columns='date',aggfunc='count')
print(df3)
df3=df2.pivot_table(index='date',columns='city',aggfunc=['sum','mean'])
print(df3)
df3=df2.pivot_table(index='city',columns='date',margins=True)
#adds new column called all which has average of each row data
#by default aggfunc is mean
print(df3)
df2['date'] = pd.to_datetime(df2['date'], format='%d-%m-%Y')
df4=df2.pivot_table(index=pd.Grouper(freq='ME',key='date'),columns='city')
print(df4)
# pd.Grouper(freq='ME', key='date'):
# - Group the datetime 'date' column by Month-End (ME)
# - Use the monthly groups as the pivot table index
# - columns='city' creates separate columns for each city
# - values defaults to all numeric columns
# - aggfunc defaults to mean
df1=pd.DataFrame({'OrderDate':['1-6-18','1-23-18','2-9-18','2-26-18','3-15-18','4-1-18','4-18-18','5-5-18','5-22-18','6-8-18','6-25-18','7-12-18','7-29-18','8-15-18','9-1-18','9-18-18','10-5-18','10-22-18','11-8-18','11-25-18','12-12-18','12-29-18','1-15-19','2-1-19','2-18-19','3-7-19','3-24-19','4-10-19','4-27-19','5-14-19','5-31-19','6-17-19','7-4-19','7-21-19','8-7-19','8-24-19','9-10-19','9-27-19','10-14-19','10-31-19','11-17-19','12-4-19','12-21-19'],
    'Region':['East','Central','Central','Central','West','East','Central','Central','West','East','Central','East','East','East','Central','East','Central','East','East','Central','Central','East','Central','Central','East','West','Central','Central','East','Central','Central','Central','East','Central','Central','West','Central','West','West','Central','Central','Central','Central'],
    'Manager':['Martha','Hermann','Hermann','Timothy','Timothy','Martha','Martha','Hermann','Douglas','Martha','Hermann','Martha','Douglas','Martha','Douglas','Martha','Hermann','Martha','Douglas','Hermann','Douglas','Douglas','Timothy','Douglas','Martha','Timothy','Hermann','Martha','Martha','Timothy','Timothy','Hermann','Martha','Hermann','Hermann','Timothy','Timothy','Timothy','Douglas','Martha','Hermann','Hermann','Martha'],
    'SalesMan':['Alexander','Shelli','Luis','David','Stephen','Alexander','Steven','Luis','Michael','Alexander','Sigal','Diana','Karen','Alexander','John','Alexander','Sigal','Alexander','Karen','Shelli','John','Karen','David','John','Alexander','Stephen','Luis','Steven','Diana','David','David','Shelli','Alexander','Sigal','Shelli','Stephen','David','Stephen','Michael','Steven','Luis','Luis','Steven'],
    'Item':['Television','Home Theater','Television','Cell Phone','Television','Home Theater','Television','Television','Television','Home Theater','Television','Home Theater','Home Theater','Television','Desk','Video Games','Home Theater','Cell Phone','Cell Phone','Video Games','Television','Video Games','Home Theater','Home Theater','Home Theater','Home Theater','Video Games','Television','Cell Phone','Television','Home Theater','Desk','Video Games','Video Games','Video Games','Desk','Television','Cell Phone','Home Theater','Television','Home Theater','Home Theater','Home Theater'],
    'Units':[95,50,36,27,56,60,75,90,32,60,90,29,81,35,2,16,28,64,15,96,67,74,46,87,4,7,50,66,96,53,80,5,62,55,42,3,7,76,57,14,11,94,28],
    'Unit_price':[1198,500,1198,225,1198,500,1198,1198,1198,500,1198,500,500,1198,125,58.5,500,225,225,58.5,1198,58.5,500,500,500,500,58.5,1198,225,1198,500,125,58.5,58.5,58.5,125,1198,225,500,1198,500,500,500],
    'Sale_amt':[113810,25000,43128,6075,67088,30000,89850,107820,38336,30000,107820,14500,40500,41930,250,936,14000,14400,3375,5616,80266,4329,23000,43500,2000,3500,2925,79068,21600,63494,40000,625,3627,3217.5,2457,375,8386,17100,28500,16772,5500,47000,14000]})
print(df1)
temp1=df1.pivot_table(index=['Region','Manager','SalesMan'],values='Sale_amt',aggfunc='sum')
#1st way for get for douglas
temp2=temp1.reset_index(level=1)
print(temp2[temp2['Manager']=='Douglas'])
#2nd way for get for douglas
print(temp1.query("Manager == 'Douglas'"))
#3rd way
temp3=df1[df1.Manager=='Douglas']
print(temp3.pivot_table(index=['Region','Manager','SalesMan'],values='Sale_amt',aggfunc='sum'))
temp4=df1.query("`Item` =='Television' or `Item` =='Home Theater'")
print(temp4.pivot_table(index=['Region','Item'],values='Units',aggfunc='sum'))
df2=pd.read_csv('titanic.csv')
#print(pd.cut(df2['age'],bins=[0,10,30,60,80]))
#temp=df2.groupby(pd.cut(df2['age'],bins=[0,10,30,60,80]))
#for age,age_df in temp:
#    print(age)
#    print(age_df)
#df2['categ_age']=pd.cut(df2['age'],bins=[0,10,30,60,80])
#print(df2.pivot_table(index=['sex','categ_age'],columns='class',values='survived',aggfunc='sum'))
#print(df2.pivot_table(index=['sex',pd.cut(df2['age'],bins=[0,10,30,60,80])],columns='class',values='survived',aggfunc='mean'))
#categage=pd.cut(df2['age'],bins=[0,10,30,60,80])
#categfare=pd.qcut(df2['fare'],q=2)
#print(df2.pivot_table(index=['sex',categage],columns=['class',categfare],values='survived',aggfunc='mean'))
#can use fiff function for diff columns
print(df2.pivot_table(index=['sex','class'],aggfunc={'survived':'sum','fare':'mean'}))
"""

#datetime
"""df4=pd.read_csv('pivot2.csv')
print(df4)
df4['date']=pd.to_datetime(df4['date'])
print(df4)
s20=pd.Series(['01 Jan 2015','10-02-2016','20180307','2014/05/06','2016-04-12','2019-04-06T11:20'])
print(pd.to_datetime(s20,format='mixed'))
parsed_s20=pd.to_datetime(s20,format='mixed')
print("Day of month:")
print(parsed_s20.dt.day.tolist())
print("Day of year:")
print(parsed_s20.dt.dayofyear.tolist())
print("Week number:")
print(parsed_s20.dt.isocalendar().week.tolist())
print("Day of week:")
print(parsed_s20.dt.day_name().tolist())
s25=pd.Series(pd.date_range('2020-01-01', periods=52, freq='W-SUN'))
print("All Sundays of 2019:")
print(s25)
s=pd.Series(['3/11/2000','3/12/2000','3/13/2000'])
d12=pd.DataFrame(s)
d12[0]=pd.to_datetime(d12[0])
print(d12)
s21=pd.Series(['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'])
s21=pd.to_datetime(s21,format='%d/%m/%Y').dt.strftime('%m/%d/%Y')
print(s21)
d='01/12/2022 00:21:20'
temp=pd.to_datetime(d)
print(temp)
print(temp.date())
print(temp.time())
print(pd.Timestamp.now(tz='Asia/Kolkata'))
print(pd.Timestamp.now(tz='Asia/Kolkata').date())
print(pd.Timestamp.now(tz='Asia/Kolkata').time())
t=pd.Timestamp('2022/09/22 01:22:44')
print(t)
print(t.time())
print(t.date())
print(pd.Timestamp.now()+pd.Timedelta(days=5))
d2=pd.to_datetime("1st of January, 2021")
print(d2)
d3=pd.Timestamp(year=2020, month=12, day=25)
print(d3)
d4=pd.Timestamp("1st of January, 2021")
print(d4)
df=pd.DataFrame({'data':[9,8,7,6,4]},index=pd.date_range(start='2021/01/20',periods=5))
print(df)
p = pd.DatetimeIndex(['2011-09-02', '2012-08-04',
                          '2015-09-03', '2010-08-04',
                          '2015-03-03', '2011-08-04',
                          '2015-04-03', '2012-08-04'])
s = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index=p)
print(s)
print(s['2015'])
print(s.loc['2015'])
s=s.sort_index()
print(s['2012-01-01':'2012-12-31'])
s1=pd.Series(pd.date_range(start='2020-01-01',periods=31,freq='D'))
print(s1)
print(s1.max())
print(s1.min())
s2=pd.Series(pd.date_range(start='2020-01-01',periods=4,freq='3ME'))
print(s2)
s3=pd.Series(pd.timedelta_range(start='1 day',end='2 day',freq='6h'))
print(s3)
s4=pd.Series(pd.date_range(start='00:00:00',end='10:00:00',freq='h'))
print(s4)
s5=pd.Series(pd.timedelta_range(start='00:00:00',end='10:00:00',freq='h'))
print(s5)
print(s5.astype(str).str.split(' ').apply(lambda x:x[2]))
data={"year": [2002, 2003, 2015, 2018],"day_of_the_year": [250, 365, 1, 140]}
df1=pd.DataFrame(data)
df1['year']=df1['year'].astype('str')
df1['day_of_the_year']=df1['day_of_the_year'].astype('str')
df1['date']=pd.to_datetime(df1['year']+df1['day_of_the_year'],format='%Y%j')
df1.pop('year')
df1.pop('day_of_the_year')
print(df1)
df2=pd.DataFrame({'year':[2018, 2019, 2020],'month': [2, 3, 4],
                   'day': [4, 5, 6],'hour': [2, 3, 4]})
#1st way as col are year,month,day,hour explicitly
print(pd.to_datetime(df2))
#2nd way from earlier question
df2=df2.astype('str')
df2['new']=pd.to_datetime(df2['year']+df2['month']+df2['day']+df2['hour'],format='%Y%m%d%I')
print(df2)
print(pd.Timestamp('2026-09-12').dayofweek<5)
print(pd.bdate_range('2026-09-12','2026-09-15'))
print(pd.date_range("2026-09-12",periods=9,freq='B'))
print(pd.date_range('2021-01-01', periods=12, freq='BME'))
print(pd.timedelta_range(0, periods=3, freq="1h20min"))
t5=pd.Timestamp('2012-09-11').tz_localize('Europe/Berlin')
print(t5.tz_convert(None))
print(t5.tz_localize(None))
t6=pd.Timestamp('2012-09-11').tz_localize('Asia/Calcutta')
print(t5-t6)
print(pd.date_range('2020-01-01',periods=5, freq="W-THU"))
t6=pd.Timestamp('2020-01-01')
temp1=t6+pd.Timedelta(days=1)
print(temp1)
for i in range(4):
    temp1=temp1+pd.Timedelta(days=7)
    print(temp1)
print(pd.date_range('2020-01-01',periods=4,freq='BQE'))
print(pd.date_range('2020-01-01',periods=4,freq='BQS'))
print(pd.date_range('2020-01-01',periods=4,freq='1d1h1min'))
t7=pd.Timestamp('2026-02-07')
print(t7.day_name())
t7=t7+pd.Timedelta(days=2)
print(t7+pd.offsets.BDay(1))
s6=pd.to_datetime([1329806505, 129806505],unit='s')
print(s6)
t8=pd.Timestamp(2020, 1, 4)
print(pd.date_range(t8,periods=3,freq='B'))
print(pd.date_range(t8,periods=1,freq='BME'))
s=pd.Timestamp(2020,1,1)
e=pd.Timestamp(2020,12,31)
p=pd.Period('2021-11','M')
print(p)
dataset=pd.period_range(s,e,freq='M')
print(dataset)
for d in dataset:
    print(d.start_time,d.end_time)
dataset1=pd.period_range('2029','2031',freq='M')
print(dataset1)
s7=pd.Series(range(25),index=dataset1)
print(s7['2030'])
p1=pd.Period('2026','Y')
print(p1)
"""

#melt
"""df=pd.read_csv('melt.csv')
print(df)
df1=pd.melt(df,id_vars=['day'])
print(df1)
df2=pd.melt(df,id_vars=['kota'])
print(df2)
df2=df1[df1['variable']=='kota']
print(df2)
df4=pd.melt(df,id_vars=['day'],var_name='city',value_name='temperature')
print(df4)"""

#stack
"""df = pd.DataFrame(
    {
        ("Math", "Marks"): [85, 90],
        ("Math", "Grade"): ["A", "A+"],
        ("Science", "Marks"): [88, 91],
        ("Science", "Grade"): ["A", "A+"]},index=["Raj", "Aman"])
print(df)
print(df.stack(level=0,future_stack=True))
print(df.stack(level=1,future_stack=True))
#about future_stack
#pandas.DataFrame.stack() -> future_stack parameter

#Legacy behavior (future_stack=False):
#- May introduce unnecessary NaN values when stacking multiple levels.
#- Automatically sorts the resulting MultiIndex.
#- dropna= and sort= parameters can be used.

#Future behavior (future_stack=True):
#- Does NOT introduce unnecessary NaN values.
#- Never sorts MultiIndex levels automatically.
#- dropna and sort cannot be specified; they must remain unspecified.

#Recommendation:
#- Use future_stack=True for the new, predictable behavior.
#- It is the implementation that future versions of pandas will use.
"""

#crosstab
"""df=pd.read_excel('crosstab.xlsx')
print(df)
#crosstab(index,column)
df1=pd.crosstab(df.State,df.Handedness)
print(df1)
df2=pd.crosstab(df.Gender,df.Handedness)
print(df2)
df3=pd.crosstab(df.State,df.Gender)
print(df3)
df4=pd.crosstab(df.State,df.Gender,margins=True,margins_name='Total')
print(df4)
df5=pd.crosstab(df.Handedness,[df.State,df.Gender],margins=True)
print(df5)
df6=pd.crosstab([df.State,df.Gender],df.Handedness,margins=True)
print(df6)
df7=pd.crosstab(df.Gender,df.Handedness,normalize='index')
print(df7)
df8=pd.crosstab(df.Gender,df.Handedness,values=df.Age,aggfunc=np.average)
print(df8)"""

#pandas extended
"""df=pd.read_csv('test.csv')
print(df)
print(df.info())
print(df.shape)
print(df.index)
print(df.columns)
print(df.dtypes)"""

#iloc()
#df.iloc(row selection,column selection)
"""d4=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]},index=['I','II','III'])
print(d4)
print(d4.iloc[0,1]) #0th row,1st value or 0th row,1st column's value
print(d4.iloc[0:2]) #first two rows
print(d4.iloc[0:2,:]) #same as above
print(d4.iloc[:,1]) #all row and 1st column
#every numbering is based on 0 based indexing
"""

#isnull() and notnull()
"""df=pd.read_csv('test.csv')
print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())
print(df['Age'].isnull())
print(df.loc[2].isnull())
print(df.notnull())"""

#dropna()
"""df=pd.read_csv('test.csv')
print(df)
print('dropping all row with nan values')
print(df.dropna())
print('using on particularly row/column')
#as dropna is reduction function
print(df.dropna(axis=0)) #row
print(df.dropna(axis=1)) #column
print('how to drop')
#any one in row missing drop row,default value
print(df.dropna(how='any'))
#drop row if all values in row are missing
print(df.dropna(how='all'))
print('removing if a specific column has missing value')
print(df.dropna(subset=['Salary']))
print('keep row with at least this many filled/existing values')
print(df.dropna(thresh=3))
print('to modify original dataframe')
print(df.dropna(inplace=True)) #or #df=df.dropna()
print(df)"""

#assign()
"""df5=pd.DataFrame({'ord_no':[70001.0,np.nan,70002.0,70004.0,np.nan,70005.0,np.nan,70010.0,70003.0,70012.0,np.nan,70013.0],
'purch_amt':[150.50,np.nan,65.26,110.50,948.50,np.nan,5760.00,1983.43,np.nan,250.45,75.29,3045.60],
'sale_amt':[10.50,20.65,np.nan,11.50,98.50,np.nan,57.00,19.43,np.nan,25.45,75.29,35.60],
'ord_date':['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
'salesman_id':[5002.0,5003.0,5001.0,np.nan,5002.0,5001.0,5001.0,np.nan,5003.0,5002.0,5003.0,np.nan]})
print(df5)
print(df5.assign(ord_no=df5.ord_no.ffill()))"""

#value_counts()
"""df=pd.read_csv('test1.csv')
print(df)
print(df['Gender'].value_counts())
print(df['Gender'].value_counts())
#to return percentage
print(df['Gender'].value_counts(normalize=True))
#to sort counted data
print(df['Gender'].value_counts(ascending=True))
#to ignore missing data
print(df['Gender'].value_counts(dropna=True)) #True is default
print(df['Gender'].value_counts(dropna=False))"""

#unique() and nunique()
"""df=pd.read_csv('test1.csv')
print(df)
print(df['Gender'].unique())
print(type(df['Gender'].unique()))
print(df['Gender'].nunique())
print(df['Gender'].nunique(dropna=False))"""

#astype()
"""df=pd.DataFrame({'serial':[1,2,3],'marks':['100','20','120']})
print(df['marks'].dtype)
#print(df['marks'].mean()) #would give error
df['marks']=df['marks'].astype(int)
print(df['marks'].dtype)
print(df['marks'].mean())
print("converting multiple column's datatypes")
df=df.astype({'serial':str,'marks':float})
print(df['serial'].dtype)
print(df['marks'].dtype)
s=pd.Series(['hr','it','hr','sales'])
s=s.astype('category')
print(s.dtype)
s1=pd.Series(['1','2','3','a'])
s1=pd.to_numeric(s1,errors='coerce')
#s1=s1.astype(int)
print(s1)
print(type(s1[2]))
print(type(s1[3]))"""

#string methods
"""df=pd.read_csv('pandas_string_methods.csv')
print(df)
print(df['Name'].str.lower())
print(df['Name'].str.upper())
print(df['City'].str.strip())
print(df['City'].str.lstrip())
print(df['City'].str.rstrip())
print(df['Email'].str.replace('gmail','hotmail'))
print(df['Email'].str.contains('gmail'))
print(df['Name'].str.startswith('A'))
print(df["Email"].str.endswith(".com"))
print(df["Name"].str.split(" "))
print(df["Name"].str.strip().str.split(" "))
print(df['City'].str.len())
print(df['City'].str.title())
print(df['Name'].str.capitalize())
#also works on lists
d22 =pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]})
print(d22)
d22.columns=d22.columns.str.lower().str.rstrip()
print(d22)
s4 = pd.Series(['10', '250', '3000', '40000', '500000'])
print(s4.str.pad(8,'left','0'))
s5=pd.Series(['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'])
print(s5.str.count('2'))
print(s5.str.find('22'))
print(s5.str.find('22',2,10))
s6=pd.Series(['Company','Company a001','Company 123', '1234', 'Company 12'])
print(s6.str.isalnum())
print(s6.str.isalpha())
print(s6.str.isdigit())
print(s6.apply(lambda x:True if type(x)==int else False))
s7=pd.Series(['ABCD','EFGF', 'hhhh', 'abcd', 'EAWQaaa','Love',' '])
print(s7.str.isupper())
print(s7.str.islower())
print(s7.str.istitle())
print(s7.str.isspace())
print(s7.str.swapcase())

"""

#duplicated() and drop_duplicates()
"""df=pd.read_csv('pandas_duplicates.csv')
print(df)
print(df['Name'].duplicated())
print(df[df['Name'].duplicated()])
print(df.drop_duplicates(subset=['Name']))
print(df.drop_duplicates(subset=['Name'],keep='last'))
print(df.drop_duplicates(subset=['Name'],keep=False))
print(df.duplicated(subset=["Department", "Salary"]))"""

#set_index() and reset_index()
"""df=pd.read_csv('setresetindex.csv')
print(df)
df1=df.set_index('EmpID')
print(df1)
print(df1.index)
df2=df.set_index(['EmpID','Age'])
print(df2)
print(df2.index)
df1=df1.reset_index()
print(df1)
df2=df2.reset_index(drop=True)
print(df2)"""

#query()
"""df=pd.read_csv('agg.csv')
print(df.query("Salary > 65000"))
print(df.query("Department == 'IT'"))
print(df.query("Department == 'IT' and Salary > 60000"))
print(df.query("Age > 28 or Department == 'Finance'"))
salary=75000
print(df.query('Salary > @salary'))"""

#sample()
"""df=pd.read_excel('sample_practice.xlsx')
print(df)
print(df.sample)
print(df.sample(2))
print(df.sample(frac=0.5))
print(df.sample(2,random_state=9))
print(df.sample(n=3,replace=True,random_state=80))"""

#isin()
"""df=pd.read_csv('isin_practice.csv')
print(df)
print(df['Dept'].isin(["IT"]))
print(df[df['Dept'].isin(["IT"])])
print(df[~df["Dept"].isin(["IT"])])
print(df[df["Name"].isin(["Aman", "Sonia"])])"""

#diff()
"""s19=pd.Series([1, 3, 5, 8, 10, 11, 15])
print(s19.diff())
print(pd.Series([1, 3, 5, 8, 10, 11, 15]).diff())"""

#shift()
"""s23=pd.Series([1,8,7,5,6,5,3,4,7,1]).astype(float)
result = s23[(s23 > s23.shift(1)) & (s23 > s23.shift(-1))].index.tolist()
print(s23)"""

#to_frame()
"""
s27=pd.Series(list('ABCDE'))
print(s27.to_frame().reset_index())
"""

#iterrows()
"""d7=pd.DataFrame([{'name':'Ana','score':12.5},{'name':'Dima','score':9},{'name':'Kat','score':16.5}])
for index,row in d7.iterrows():
    print(row['name'],row['score'])"""

#to_string()
"""dict1={'name':['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
'attempts':[1,3,2,3,2,3,1,1,2,1],
'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']}
index1=['a','b','c','d','e','f','g','h','i','j']
d5=pd.DataFrame(dict1,index1)
print(d5.to_string(index=False))"""

#insert() - only for columns
"""d16=pd.DataFrame({'col2':[4,5],'col3':[2,123]})
#16.loc[:,'col1']=[1,2,3,4,5]
#d16=d16[['col1','col2','col3']]
d16.insert(0,'col1',[1,2])
d16.insert(2,'newcol','hello')
d16.insert(4,'col1',[9,10],allow_duplicates=True)
print(d16)
print(d16.col1)"""

#get_loc()
"""d18=pd.DataFrame({'col1':['C1','C1','C2','C2','C3'],'col2':[1,2,3,6,5],'col3':['a','b','c','a','b']})
d18.loc[22]=['C9',9,'z']
print(d18)
print(d18.columns.get_loc('col2'))
print(d18.index.get_loc(22))"""

#nlargest(),nsmallest()
"""d18=pd.DataFrame({'col1':['C1','C1','C2','C2','C3'],'col2':[1,2,3,6,5],'col3':['a','b','c','a','b']})
print(d18)
print(d18.nlargest(3,'col2'))
print(d18.nsmallest(3,'col2))
"""

#add_prefix() and set_prefix()
"""d18=pd.DataFrame({'col1':['C1','C1','C2','C2','C3'],'col2':[1,2,3,6,5],'col3':['a','b','c','a','b']})
print(d18)
print(d18.add_prefix('hello'))
print(d18.add_suffix('hello'))"""

#select_dtypes()
"""d20=pd.DataFrame({'name':['Ali','Gin'],'DOB':['17/05/2002','16/02/1999'],'age':[18.5, 21.2]})
print(d20)
print(d20[d20.columns[d20.dtypes==float]])
print(d20[d20.columns[d20.dtypes==object]])
print(d20[d20.columns[(d20.dtypes==object) | (d20.dtypes==float)]])
print(d20.select_dtypes(include=float))
print(d20.select_dtypes(include=object))
print(d20.select_dtypes(include=[float,object]))"""

#interpolate()
"""d27 = pd.DataFrame({"c1": [120,130,140,150,np.nan,170],
    "c2": [7,np.nan,10,np.nan,5.5,16.5]})
d27.index = pd.date_range("2025-01-01", periods=6)
print(d27.interpolate())"""

#eq(),cummax(),where()
"""s3=pd.Series([5, 2, 8, 6, 9])
print(s3.cummax())
print(s3.eq(s3.cummax()))
print(s3.where(s3>5,0))
print(s3.where(s3.eq(s3.cummax()),0))"""

#autocorrelation
"""s=pd.Series([10,11,12,13,14])
print(s.autocorr())
s1=pd.Series([10,50,5,90,3])
print(s1.autocorr())"""

#ne()
"""d3=pd.DataFrame({'W':[68,75,86,98,None],'X':[78,75,None,80,86]})
s30=pd.Series([68,75,86,80,None])
print(d3.ne(s30,axis=0))"""

#cut() and qcut()
"""df=pd.DataFrame({'Id':[1,2,3,4,5,6],'Name':['Aman','Rahul','Priya','Neha','Rohit','Sonia'],
                 'marks':[35,52,67,74,88,95]})
print(pd.cut(df['marks'],bins=[0,40,60,80,100],labels=['Fail','Average','Good','Excellent']))
print(pd.qcut(df['marks'],q=3))"""

#reindex()
"""s=pd.Series(data=[1,2,3,4,5],index=['a','b','c','d','e'])
print(s)
s=s.reindex(index=['B','A','C','D','E'])
print(s)"""

#factorize
"""s=pd.Series(['A','B','A','C','B'])
labels,uniques=pd.factorize(s)
print(labels)
print(uniques)"""

#any()/all()
"""df=pd.read_csv('world_alcohol.csv')
print(df.loc[:,df.any()])
#above- any value in col to True then whole col True if any single col True then finally True
print(df.loc[:,df.all()])
#above- all value in col to True then whole col True if all col True then finallay True"""

#_append() -internal python method must avoid
"""df=pd.DataFrame({'name':['a'],'id':[1]})
temp=pd.Series(['b',2],index=['name','id'])
print(df._append(temp,ignore_index=True))"""

#.unstack()
"""s=pd.Series([80, 90, 85],index=pd.MultiIndex.from_tuples([('A', 'Math'),
                                                                ('A', 'Physics'),
                                                                    ('B', 'Math')],
                                                    names=['Student', 'Subject']))
print(s)
print(s.unstack(level=1,fill_value=0))"""

#transform()
"""df11=pd.DataFrame({'dept':['A','A','B','B','B'],'salary':[10,20,30,40,50]})
df11['dept_avg']=df11.groupby('dept')['salary'].transform('mean')
print(df11)"""

#------------------------Pandas questions---------------------------
#pandas Series
"""s=pd.Series([1,2,3,4,5,6])
print(s)
print(type(s))
l=s.tolist()
print(l)
print(type(l))
s1=pd.Series([7,8,9,10,11,12])
print(s1-s)
print(s1==s)
s2=pd.Series({'a':100,'b':200,'c':300,'d':400,'e':800})
print(s2)
print(s2.astype(float))
d1=pd.DataFrame({'1s':[1,2,3],'10s':[10,20,30],'100s':[100,200,300]})
print(d1)
print(d1.loc[:,'1s'])
print(type(d1.loc[:,'1s']))
s3=pd.Series(d1['10s'])
print(s3)
a=np.array(s3)
print(a)
s4=pd.Series([[1,2,3],[4,5,6],[7,8,9]])
for i in s4.index:
    for j in s4[i]:
        print(j)
print(s4)
s5=pd.Series([j for i in s4.index for j in s4[i]])
print(s5)
print(s4.apply(pd.Series).stack().reset_index(drop=True))
s6=pd.Series(['100','200','python','300.12','400'])
print(s6.sort_values(ignore_index=True))
s7=pd.Series(['500','php'])
print(pd.concat([s6,s7],ignore_index=True))
s8=pd.Series(range(0,11,1))
new_s8=s8[s8>6]
print(new_s8)
s9=pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
print(s9)
print(s9.sample(5))
d1=pd.DataFrame({'ones':[1,2,3],'tens':[10,20,30]})
print(d1)
print(d1.reindex(index=[2,1,0]))
s10=pd.Series([4,5,8,9,213,12,312,31,31,312])
print(s10.mean())
print(s10.std())
s11=pd.Series([1,2,3,4,5])
s12=pd.Series([2,4,6,8,10])
print(s11[~s11.isin(s12)])
temp1=s11[~s11.isin(s12)]
temp2=s12[~s12.isin(s11)]
print(pd.concat([temp1,temp2],ignore_index=True))
print(s11.describe())
s13=pd.Series([1,2,1,1,2,4,5,6,7,8,4,5,6,4,5,4])
print(s13.value_counts())
s14=pd.Series(np.random.randint(1,5,[10])).astype(object)
print(s14)
temp3=s14.value_counts()
print(temp3)
s14[~s14.isin(s14.value_counts().index[:2])] = 'Other'
print(s14)
s14[~(s14==temp3.index[0])]='other'
print(s14)
s15=pd.Series([1,23,623,46,51,75,63,2,7,4])
print(s15[s15%2==0].tolist())
print(s15)
print(s15[[0,2,4,5]].tolist())
print(s15[9])
s16=pd.Series(range(11))
s17=pd.Series(range(1,9,2))
print(s16[s16.isin(s17)].index.tolist())
s18=pd.Series(['php','python','java','c#'])
print(s18.map(lambda x:x[0].upper()+x[1:-1]+x[-1].upper()))
print(s18.str.len())
s19=pd.Series([1, 3, 5, 8, 10, 11, 15])
print(s19.diff())
print(pd.Series([1, 3, 5, 8, 10, 11, 15]).diff())
s20=pd.Series(['01 Jan 2015','10-02-2016','20180307','2014/05/06','2016-04-12','2019-04-06T11:20'])
print(pd.to_datetime(s20,format='mixed'))
parsed_s20=pd.to_datetime(s20,format='mixed')
print("Day of month:")
print(parsed_s20.dt.day.tolist())
print("Day of year:")
print(parsed_s20.dt.dayofyear.tolist())
print("Week number:")
print(parsed_s20.dt.isocalendar().week.tolist())
print("Day of week:")
print(parsed_s20.dt.day_name().tolist())
s21=pd.Series(['Jan 2015','Feb 2016','Mar 2017','Apr 2018','May 2019'])
print(pd.to_datetime('11 '+s21,format='%d %b %Y'))
s22=pd.Series(['Red','Green','Orange','Pink','Yellow','White'])
def check(x):
    x=x.lower()
    vowels=['a','e','i','o','u']
    f,i=0,0
    while(i<len(vowels)):
        if f==2: #if two vowels found
            return True
        if vowels[i] in x: #if current vowel found replace
            x=x.replace(vowels[i],'v',1)
            f=f+1
        else:#when it did not have this vowel
            i=i+1
    return False

print(s22[s22.apply(check)])
s23=pd.Series([1,8,7,5,6,5,3,4,7,1]).astype(float)
#result = s23[(s23 > s23.shift(1)) & (s23 > s23.shift(-1))].index.tolist()
lower=pd.concat([pd.Series([np.nan]),pd.Series(s23.tolist()[0:-1])])
higher=pd.concat([pd.Series(s23.tolist()[1:]),pd.Series([np.nan])])
d2=pd.DataFrame({'current':s23.tolist(),'lower':lower.tolist(),'higher':higher.tolist()})
print(d2)
print(d2[(d2.current>d2.lower) & (d2.current>d2.higher)].index.tolist())
string='abc def abcdef icd'
s24=pd.Series(list(string))
print(s24)
stringwithoutempty=s24[s24!=' '].value_counts() #finding freq. without empty space
leastfreqinstring=stringwithoutempty.index[-1] #taking least freq. item
print(string.replace(' ',leastfreqinstring)) #replacing empty space with least freq. item
s25=pd.Series(pd.date_range('2020-01-01', periods=52, freq='W-SUN'))
print("All Sundays of 2019:")
print(s25)
s26=pd.DataFrame({'index':range(26),'char':list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')})
print(s26)
s27=pd.Series(list('ABCDE'))
print(s27.to_frame().reset_index())
s28=pd.Series(list('ABHIJ'))
print(pd.DataFrame({'s27':s27.tolist(),'s28':s28.tolist()}))
print(s28==s27)
s29=pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print("index of largest's 1st occurrence",s29[s29==s29.max()].index[0])
print("index of smallest's 1st occurrence",s29[s29==s29.min()].index[0])
d3=pd.DataFrame({'W':[68,75,86,80,None],'X':[78,75,None,80,86]})
print(d3)
s30=pd.Series([68,75,86,80,None])
print(~d3.isin(s30))
print(d3.ne(s30,axis=0))"""

#python pandas dataframe
"""d4=pd.DataFrame({'a':[1,2,3,4],'b':[4,5,6,7]},index=['I','II','III','IV'])
print(d4)
print(d4.info())
print(d4.iloc[0,1]) #0th row,1st value or 0th row,1st column's value
print(d4.iloc[0:2]) #first two rows
print(d4.loc[:,['a','b']]) #specific columns
print(d4.loc[['II','III'],['a']]) #specific row and column
dict1={'name':['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
'attempts':[1,3,2,3,2,3,1,1,2,1],
'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']}
index1=['a','b','c','d','e','f','g','h','i','j']
d5=pd.DataFrame(dict1,index1)
print(d5)
print(d5[d5.attempts>2])
print('number of row',len(d5))
print('number of columns',len(d5.columns))
print(d5[d5.score.isnull()]) #rows with missing score
print(d5[(15<d5.score) & (d5.score<=20)]) #score btw 15,20 inc.
print(d5[(15<d5.score) & (d5.attempts<2)])
d5.iloc[3,1]=11.5
print(d5)
d5.iloc[3,1]=np.nan
print(d5.attempts.sum()) #directly
print(d5['attempts'].sum()) #using df of attempts column's sum
print(d5['attempts'].agg("sum")) #using agg() method
print(d5.score.mean())
#name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"
temp=pd.DataFrame({'name':"Suresh","score":15.5,"attempts":1,"qualify":"yes"},index=["k"])
print(pd.concat([d5,temp],axis=0))
d6=pd.DataFrame({'name':['A','B'],'no.':[1,2]})
print(d6)
#adding a row
d6.loc[2]=['C',3]
print(d6)
#adding a column
d6.loc[:,'marks']=[10,20,30] #or d6['marks']=[10,20,30]
print(d6)
d6=d6.drop(2)
print(d6)
d6.pop('marks')
print(d6)
print(d5.sort_values(by=['name','score'],ascending=[False,True]))
print(d5)
d5.qualify=d5.qualify.map({'yes':True,'no':False})
print(d5)
d5.loc[d5[d5.name=='James'].index[0],'name']='Suresh'
print(d5)
d7=pd.DataFrame([{'name':'Ana','score':12.5},{'name':'Dima','score':9},{'name':'Kat','score':16.5}])
print(d7)
for i in range(len(d7)):
    print(d7.iloc[i,0],d7.iloc[i,1])
    #print(d7.loc[i,'name'],d7.loc[i,'score'])
for index,row in d7.iterrows():
    print(row['name'],row['score'])

print(d5.columns.values)
print(d5.index.values)
d8=pd.DataFrame({'no.':[1,2,3],'score':[10,20,30]})
print(d8)
#data1.rename(columns={'chem':'Chemistry','eng':'English'},inplace=True)
d8.rename(columns={'no.':'serial','score':'marks'},inplace=True)
print(d8)
d9=pd.DataFrame({'col1':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]})
print(d9[d9.col1==4])
print(d9)
#way to swap col3 and col1 --- 1st way
d9.col1,d9.col3=d9.col3,d9.col1
#d9.loc[:,'col1'],d9.loc[:,'col3']=d9.loc[:,'col3'],d9.loc[:,'col1']
d9.rename(columns={'col1':'col3','col3':'col1'},inplace=True)
#or way 2nd
d9=d9[['col3','col2','col1']]
print(d9)
d9.loc[5]=[10,11,12]
print(d9)
d9.drop(5)
d9.to_csv('test.csv',sep='\t',index=False)
d10 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
print(d10)
temp1=d10.groupby('city').count()
temp1.rename(columns={'name':'number of people'},inplace=True)
print(temp1)
print(d9)
print(d9[d9.col1==1].index[0])
#d9=d9[d9.col1!=1]
d9=d9.drop(d9[d9.col1==1].index[0])
print(d9)
print(d9[d9.index.values==2])
print(d9.iloc[1])
print(d5)
d5.score=d5.score.fillna(0)
print(d5)
d5=d5.reset_index()
print(d5)
print(d5.to_string(index=False))
d5.loc[8,'score']=10.0
print(d5)
d5.loc[8,'score']=np.nan
d5.loc[2,'index']=np.nan
d5.loc[5,'attempts']=np.nan
print(d5['score'].isnull().sum())
print(d5.isnull().sum().sum())
print(d9)
d9=d9.drop([1,2])
print(d9)
d10=pd.DataFrame(np.random.randn(10,2))
print(d10)
print(d10.sample(frac=0.7))
print(d10.sample(frac=0.3))
s1=pd.Series(['100','200','python','300.12','400'])
s2=pd.Series(['10','20','php','30.12','40'])
d11=pd.DataFrame([s1.to_list(),s2.to_list()],index=[0,1])
print(d11)
d11=pd.DataFrame({0:s1.to_list(),1:s2.to_list()})
print(d11)
print(d5)
print(d5.sample(frac=1))
print(d5)
print(d5.sample(frac=0.3,random_state=1))
s=pd.Series(['3/11/2000','3 Dec 2000','3/13/2000'])
d12=pd.DataFrame(s)
d12[0]=pd.to_datetime(d12[0],format='mixed')
print(d12)
print(d9)
d9.rename(columns={'col3':'column3'},inplace=True)
print(d9)
print(d9.column3.tolist())
d13=pd.DataFrame({'a':[0,1],'b':[0,1]},columns=['a','b'],index=[2,3]).astype({'a':int,'b':float})
#d13=pd.DataFrame({'a':[0,1],'b':[0,1]},columns=['intdata','floatdata'],index=[2,3]).astype({'int':int,'float':float})
print(d13)
print(d13.info())
print(d9)
#argmax gives 0-based row number(what iloc uses)
#idxmax gives actual row index(what loc uses)
print('Row where col1 has maximum value:')
print(d9.col1.argmax())
print(d9.col1.idxmax())
print('Row where col2 has maximum value:')
print(d9.col2.argmax())
print(d9.col2.idxmax())
print('Row where column3 has maximum value:')
print(d9.column3.argmax())
print(d9.column3.idxmax())
print(d5)
print('index' in d5.columns.values)
print(d9.iloc[0])
for i in d5:
    print(i,d5[i].dtype)
print(d5.dtypes)
print(d9.dtypes)
d14=pd.DataFrame()
print(d14)
d14.loc[:,'col1']=[1,2,3]
d14.loc[:,'col2']=[5,6,7]
d14.loc[3]=[4,8]
d14.loc[:,'col3']=[9.9,10.0,11.1,12.2]
print(d14)
d15=pd.concat([d14,d9],ignore_index=True)
print(d15)
print(d14)
d14.col3=d14.col3.astype(int)
print(d14)
d15=pd.DataFrame([1000,2000,3000,-4000,np.inf,-np.inf])
print(d15)
d15[0]=d15[0].replace([np.inf,-np.inf],np.nan)
print(d15)
d16=pd.DataFrame({'col2':[4,5],'col3':[2,123]})
#16.loc[:,'col1']=[1,2,3,4,5]
#d16=d16[['col1','col2','col3']]
d16.insert(0,'col1',[1,2])
d16.insert(2,'newcol','hello') #single value get repeated
d16.insert(4,'col1',[9,10],allow_duplicates=True)
print(d16)
print(d16.col1)
d17=pd.DataFrame([[2, 4], [1, 3]],columns=['1st','2nd'])
print(d17)
d18=pd.DataFrame({'col1':['C1','C1','C2','C2','C3'],'col2':[1,2,3,6,5],'col3':['a','b','c','a','b']})
print(d18)
#list of data of col2 per value of col1
#1st way
temp2=d18.groupby('col1')
print('C1',temp2.get_group('C1').col2.tolist())
print('C2',temp2.get_group('C2').col2.tolist())
print('C3',temp2.get_group('C3').col2.tolist())
#2nd way
print(d18.groupby('col1')['col2'].apply(list))
print(d18.groupby('col1')[['col2','col3']].agg(list))
#index of col2
#1st way
j=0
for i in d18:
    if i=='col2':
        print(j)
    j=j+1
#2nd way
print(d18.columns.values)
for i in range(len(d18.columns.values)):
    if d18.columns.values[i]=='col2':
        print(i)
#3rd way
print(d18.columns.get_loc('col2'))
d18.loc[22]=['C9',9,'z']
print(d18)
print(d18.index.get_loc(22))
print('no of columns in d18 :',len(d18.columns))
print(d18.loc[:,d18.columns[~(d18.columns=='col2')]])
print(d18.loc[:,d18.columns!='col2'])
print(d18)
print(d18.iloc[:5,:]) #first 5 rows or d18.head(5)
print(len(d18))
print(d18.iloc[-5:,:]) #last 5 rows, its subtracts 5 from len(d18) i.e 6
#or d18.tail(5)
print(d18.nlargest(3,'col2'))
print(d18.nsmallest(3,'col2'))
print(d18)
d18=d18.drop(d18.index[:3])
print(d18)
print(d18.add_prefix('hello'))
print(d18.add_suffix('hello'))
d19=pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
print(d19)
temp3=d19.columns.values
print(d19[temp3[::-1]]) #reversed columns or d19.loc[:,::-1]
temp3=d19.index.values
print(d19.loc[temp3[::-1]]) #reversed rows or d19.loc[::-1] or d19[::-1]
print(d19.loc[temp3[::-1]].reset_index(drop=True)) #d19.loc[::-1].reset_index(drop=True)
d20=pd.DataFrame({'name':['Ali','Gin'],'DOB':['17/05/2002','16/02/1999'],'age':[18.5, 21.2]})
print(d20)
print(d20[d20.columns[d20.dtypes==float]])
print(d20[d20.columns[d20.dtypes==object]])
print(d20[d20.columns[(d20.dtypes==object) | (d20.dtypes==float)]])
print(d20.select_dtypes(include=float))
print(d20.select_dtypes(include=object))
print(d20.select_dtypes(include=[float,object]))
d21=pd.DataFrame({'name':['A','B','C','D','E'],'DOB':[1,2,3,4,5],'age':['17','16','20','21','25']})
temp4=d21.sample(frac=0.6) #60percent of d21
print(temp4)
#removes that 60percent data
print(d21.drop(temp4.index)) #remaining 40percent of d21
#keeps orignal data intact
print(d21[~d21.index.isin(temp4.index)]) #boolean mask to get rem40percent
d22 =pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]})
d22.columns=d22.columns.str.lower().str.rstrip()
print(d22)
d23=d22.drop([0,1])
print(d23)
d24=d22.drop([2])
print(d24)
print(pd.merge(d23,d24,validate='one_to_one'))
print(pd.merge(d23,d24,validate='one_to_many'))
print(pd.merge(d23,d24,validate='many_to_one'))
d25=pd.DataFrame({'Name':['Alberto','Gino','Ryan','Eesha','Syed'],'Age':[18,22,50,80,5]})
print(d25)
print('distribution according to age group')
def age_group(x):
    if x<10:
        return 'child'
    elif x<20:
        return 'teen'
    elif x<=50:
        return 'adult'
    else:
        return 'elderly'
print(d25.Age.apply(age_group))
d25.info()
s1=pd.Series(['php', 'python', 'java', 'c#', 'c++'])
s2=pd.Series([1, 2, 3, 4, 5])
print(pd.DataFrame(s1,s2).reset_index())
print(pd.concat([s1,s2],axis=1))
print(pd.DataFrame({'col1':s1,'col2':s2}))
d26=pd.DataFrame({"c1":[120, 130 ,140, 150, np.nan, 170], "c2":[7, np.nan, 10, np.nan, 5.5, 16.5]})
print(d26)
d27 = pd.DataFrame({"c1": [120,130,140,150,np.nan,170],
    "c2": [7,np.nan,10,np.nan,5.5,16.5]})
d27.index = pd.date_range("2025-01-01", periods=6)
print(d27.interpolate())
print(d19)
temp5=d19.W.max()
print(d19.query('W<@temp5'))
s3=pd.Series([5, 2, 8, 6, 9])
print(s3.cummax())
print(s3.eq(s3.cummax()))
print(s3.where(s3>5,0))
print(s3.where(s3.eq(s3.cummax()),0))"""

#pandas dataframe filtering
"""pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
df=pd.read_csv('world_alcohol.csv')
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.iloc[:2,:]) #first 2 rows
print(df.iloc[:,:2]) #first 2 columns
print(df.iloc[:2,:2]) #first 2 row with first 2 col.
print(df.loc[:,['Year','Country']]) #specific columns
print(df.loc[:np.random.randint(0,100),:]) #random number of rows
print(df.dropna(axis=0)) #rows with na dropped
print(df.dropna(axis=1)) #col. with na dropped
print(df.isnull()) #find null data
print(df.drop_duplicates(subset='WHO region'))
print(df.drop_duplicates(subset='WHO region').to_string(index=False))
print(df[(df.Year==1987) | (df.Year==1989)])
print(df[(df.Year==1985) & (df['WHO region']=='Americas')])
print(df[(df.Year==1986) & (df['WHO region']=='Western Pacific') & (df.Country=='Viet Nam')])
print(df[((df.Year==1985) | (df.Year==1986)) & (df['WHO region']=='Americas')])
print(df.query('(Year==1985 or Year==1986) and `WHO region`=="Americas"'))
print(df.query('(Year==1985 or Year==1986) and (`WHO region`=="Americas" or `WHO region`=="Europe")'))
print(df[((df.Year==1985) | (df.Year==1986)) & ((df['WHO region']=='Americas') | (df['WHO region']=='Europe'))].loc[:,['WHO region','Country','Beverage Types']])
print(df[(df.Year.isin([1985,1986]) & (df['WHO region'].isin(['Americas','Europe'])))].loc[:,['WHO region','Country','Beverage Types']])
print(df.query('`Beverage Types`=="Beer" and `Display Value`>=5'))
print(df[(df['Display Value']>=4) & (df['Beverage Types'].isin(['Beer', 'Wine', 'Spirits']))])
print(df[df['WHO region'].str.contains("Ea")])
print(df[df['WHO region'].isin(['Africa','Eastern Mediterranean','Europe'])])
print(df[~df['WHO region'].isin(['Africa','Eastern Mediterranean','Europe'])])
print(df.query('`Display Value`>=0.5 and `Display Value`<=2.50'))
print(df.query('`Display Value`>2 and `Beverage Types`=="Wine"'))
print(df[df.index.values%10==0])
print(df.rename(columns={'Year':'p','Country':'q'}))
#print(df.rename(columns={('Year','Country'):'try'})) not work as no column named ('Year','Country') in df
#print which year has any non-zero values
for year,year_df in df.groupby('Year'):
    if year_df['Display Value'].isin([0]).any():
        print(year)
#print which year has all non-zero values
for year,year_df in df.groupby('Year'):
    if not year_df['Display Value'].isin([0]).any():
        print(year)
print(df.loc[df['Display Value'].notnull(),:])
print(df.dropna(how='any'))
print(df.iloc[:,::2])
print(df.iloc[2::5,:])"""

#pandas joining and merging
"""std1 = pd.DataFrame({'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
                    'name': ['Danniella Fenton','Ryder Storey',
                             'Bryce Jensen','Ed Bernal','Kwame Morin'],
                    'marks': [200, 210, 190, 222, 199]})

std2 = pd.DataFrame({'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
                     'name': ['Scarlette Fisher','Carla Williamson',
                              'Dante Morse','Kaiser William',
                              'Madeeha Preston'],
                     'marks': [201, 200, 198, 219, 201]})
print(std1)
print(std2)
temp=pd.concat([std1,std2],ignore_index=True)
print(temp)
print(pd.concat([std1,std2],axis=1))
std1.loc[6]=['S6','Scarlette Fisher',205]
#temp1=pd.Series(['S6','Scarlette Fisher',205],index=['student_id','name','marks'])
#print(std1._append(temp1,ignore_index=True))
print(std1)
std1=std1.drop(6)
temp2=pd.DataFrame({'student_id':['S6'],'name':['Scarlette Fisher'],'marks':[205]})
print(pd.concat([std1,temp2],ignore_index=True))
exam_data=pd.DataFrame({'student_id':['S1','S2','S3','S4','S5','S7',
                                      'S8','S9','S10','S11','S12','S13'],
                        'exam_id':[23,45,12,67,21,55,33,14,56,83,88,12]})
print(pd.merge(temp,exam_data,on='student_id'))
print(pd.merge(std1,std2,on='student_id'))
df1=pd.DataFrame({'key1':['K0','K0','K1','K2'],'key2':['K0','K1','K0','K1'],'P':['P0','P1','P2','P3'],'Q':['Q0','Q1','Q2','Q3']})
df2=pd.DataFrame({'key1':['K0','K1','K1','K2'],'key2':['K0','K0','K0','K0'],'R':['R0','R1','R2','R3'],'S':['S0','S1','S2','S3']})
print(df1)
print(df2)
print(pd.merge(df1,df2,on=None,how='left'))
print(pd.merge(df1,df2,on=None,how='right'))
s1 = pd.Series([0, 1, 2, 3], name='col1')
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5], name='col3')
df3=pd.concat([s1, s2, s3], axis=1, keys=['column1', 'column2', 'column3'])
print(df3)
print(pd.merge(df1,df2,on='key1'))
df4=pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2']},index=['K0','K1','K2'])
df5=pd.DataFrame({'C':['C0','C2','C3'],'D':['D0','D2','D3']},index=['K0','K2','K3'])
print(df4)
print(df5)
print(df4.join(df5))
print(df4.join(df5,how='inner'))
print(df4.join(df5,how='left'))
print(df4.join(df5,how='right'))
df6=pd.DataFrame({'A':[np.nan,0.0,np.nan],'B':[3,4,5]})
df7=pd.DataFrame({'A':[1,1,3],'B':[3.0,np.nan,3.0]})
print(df6)
print(df7)
print(df6.combine_first(df7))"""

#pandas grouping and aggregating
"""df=pd.DataFrame({'school':['s001','s002','s003','s001','s002','s004'],                                                                                                                                                         
                      'class':['V','V','VI','VI','V','VI'],                                                                                                                                                                    
                      'name':['Alberto Franco','Gino Mcneill','Ryan Parkes',                                                                                                                                                   
                              'Eesha Hinton','Gino Mcneill','David Parkes'],                                                                                                                                                   
                      'date_Of_Birth':['15/05/2002','17/05/2002','16/02/1999',                                                                                                                                                 
                                       '25/09/1998','11/05/2002','15/09/1997'],                                                                                                                                                
                      'age': [12, 12, 13, 13, 14, 12],                                                                                                                                                                         
                      'height': [173, 192, 186, 167, 151, 159],                                                                                                                                                                
                      'weight': [35, 32, 33, 30, 31, 32],                                                                                                                                                                      
                      'address': ['street1','street2','street3','street1',                                                                                                                                                     
                                  'street2','street4']}                                                                                                                                                                        
                      ,index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])                                                                                                                                                             
code=df.groupby('school')                                                                                                                                                                                                      
print(type(code))                                                                                                                                                                                                              
for sc,sc_df in code:                                                                                                                                                                                                          
    print(sc)                                                                                                                                                                                                                  
    print(sc_df)                                                                                                                                                                                                               
print(df.groupby('school')['age'].agg(['mean','min','max']))                                                                                                                                                                   
code1=df.groupby(['school','class'])                                                                                                                                                                                           
for scl,scl_df in code1:                                                                                                                                                                                                       
    print(scl)                                                                                                                                                                                                                 
    print(scl_df)                                                                                                                                                                                                              
code2=df.groupby('school')                                                                                                                                                                                                     
print(list(code2))                                                                                                                                                                                                             
print(code2.size())                                                                                                                                                                                                            
print(code2.get_group('s001'))                                                                                                                                                                                                 
df1=pd.DataFrame({'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],                                                                                                                          
                 'purch_amt':[150.50,270.65,65.26,110.50,948.50,2400.60,5760.00,1983.43,2480.40,250.45,75.29,3045.60],                                                                                                         
                 'ord_date':['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],                                     
                 'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],                                                                                                                                  
                 'salesman_id':[5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})                                                                                                                                 
print(df1)                                                                                                                                                                                                                     
print(df1.groupby('customer_id')['purch_amt'].agg(['mean','max','min']))                                                                                                                                                       
print(df1.groupby(['salesman_id','customer_id']).size().reset_index())                                                                                                                                                         
print(df1.groupby(['salesman_id','customer_id']).size())                                                                                                                                                                       
print(df1.groupby(['salesman_id','customer_id']).agg('count'))                                                                                                                                                                 
print(df1.groupby(['customer_id','salesman_id'])['purch_amt'].agg('sum').sort_values())                                                                                                                                        
print(df1.groupby(['customer_id','salesman_id']).agg({'purch_amt':'sum'})) #it gives dataframe                                                                                                                                 
print(df1.groupby(['customer_id','salesman_id'])['purch_amt'].agg('sum')) #it gives series output                                                                                                                              
print(df1.groupby(['customer_id'])['ord_date'].apply(list))                                                                                                                                                                    
df2=df1.copy()                                                                                                                                                                                                                 
print(df2)                                                                                                                                                                                                                     
#1st for sum of purch_amt for month,year combo based grouping                                                                                                                                                                  
#temp=df2['ord_date']                                                                                                                                                                                                          
#df2['ord_date']=pd.to_datetime(temp).dt.month_name()                                                                                                                                                                          
#df2.loc[:,'ord_year']=pd.to_datetime(temp).dt.year                                                                                                                                                                            
#print(df2)                                                                                                                                                                                                                    
#print(df2.groupby(['ord_date','ord_year']).agg({'purch_amt':'sum'}))                                                                                                                                                          
#2nd                                                                                                                                                                                                                           
df2['ord_date']= pd.to_datetime(df2['ord_date'])                                                                                                                                                                               
#grouping done by finding year and month of ord_Date col                                                                                                                                                                       
print(df2.groupby([df2['ord_date'].dt.year, df2['ord_date'].dt.month]).agg({'purch_amt':'sum'}))                                                                                                                               
df3=pd.DataFrame({'X': [10, 10, 10, 20, 30, 30, 10],                                                                                                                                                                           
                  'Y': [10, 15, 11, 20, 21, 12, 14],                                                                                                                                                                           
                  'Z': [22, 20, 18, 20, 13, 10, 0]})                                                                                                                                                                           
print(df3)                                                                                                                                                                                                                     
print(df3.groupby('X').agg({'Y':list,'Z':list}))                                                                                                                                                                               
df4=pd.DataFrame({'id': [1, 2, 1, 1, 2, 1, 2],                                                                                                                                                                                 
                  'type': [10, 15, 11, 20, 21, 12, 14],                                                                                                                                                                        
                  'book': ['Math','English','Physics','Math','English','Physics','English']})                                                                                                                                  
print(df4.groupby(['id','type','book']).size())                                                                                                                                                                                
print(df4.groupby(['id','type','book']).size().unstack(level=2,fill_value=0))                                                                                                                                                  
df5=pd.DataFrame({'id':[1,1,2,3,3,4,4,4],'value':['a','a','b',None,'a','a',None,'b']})                                                                                                                                         
print(df5.groupby('value').size())                                                                                                                                                                                             
code3=df4.groupby("id")                                                                                                                                                                                                        
print(code3.groups.keys())                                                                                                                                                                                                     
#Write a Pandas program to split the DataFrame into groups based on book_type and                                                                                                                                              
# create a new column containing the count (size) of each group.                                                                                                                                                               
df6=pd.DataFrame({'book_name':['Book1','Book2','Book3','Book4','Book1','Book2','Book3','Book5'],                                                                                                                               
                  'book_type':['Math','Physics','Computer','Science','Math','Physics','Computer','English'],                                                                                                                   
                  'book_id':[1,2,3,4,1,2,3,5]})                                                                                                                                                                                
code4=df6.groupby('book_type').size()                                                                                                                                                                                          
print(code4)                                                                                                                                                                                                                   
print(code4.loc['Math'])                                                                                                                                                                                                       
print(code4[df6.book_type])                                                                                                                                                                                                    
df6.loc[:,'group_count']=list(code4[df6.book_type])                                                                                                                                                                            
print(df6)                                                                                                                                                                                                                     
#Write a Pandas program to divide the purch_amt column into bins and count the number of rows in each bin.                                                                                                                     
df7=pd.DataFrame({                                                                                                                                                                                                             
    'ord_no': [70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],                                                                                                                                       
    'purch_amt': [150.50,270.65,65.26,110.50,948.50,2400.60,5760.00,1983.43,2480.40,250.45,75.29,3045.60],                                                                                                                     
    'customer_id': [3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],                                                                                                                                              
    'sales_id': [5002,5003,5004,5003,5002,5001,5005,5007,5008,5004,5005,5001]})                                                                                                                                                
print(df7)                                                                                                                                                                                                                     
#1st                                                                                                                                                                                                                           
temp=df7['purch_amt'].min()-0.1                                                                                                                                                                                                
sizeofbin=(df7['purch_amt'].max()-df7['purch_amt'].min())/12                                                                                                                                                                   
df7['label']=pd.cut(df7['purch_amt'],bins=[df7['purch_amt'].min()-0.1]+[temp:=temp+sizeofbin for i in range(11)]+[df7['purch_amt'].max()+1],labels=['A','B','C','D','E','F','G','H','I','J','K','L'])                          
#2nd                                                                                                                                                                                                                           
#mn = df7['purch_amt'].min()                                                                                                                                                                                                   
#mx = df7['purch_amt'].max()                                                                                                                                                                                                   
#width = (mx - mn) / 12                                                                                                                                                                                                        
#b=[mn + i * width for i in range(13)]                                                                                                                                                                                         
#df7['label']=pd.cut(df7['purch_amt'],bins=b,labels=['A','B','C','D','E','F','G','H','I','J','K','L'])                                                                                                                         
#3rd                                                                                                                                                                                                                           
#df7['label']=pd.cut(df7['purch_amt'],bins=12,labels=['A','B','C','D','E','F','G','H','I','J','K','L'])                                                                                                                        
print(df7)                                                                                                                                                                                                                     
print(df7.groupby('label',observed=False).size())                                                                                                                                                                              
df8=pd.DataFrame({                                                                                                                                                                                                             
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],                                                                                                                                            
'purch_amt':[150.50,270.65,65.26,110.50,948.50,2400.60,5760.00,1983.43,2480.40,250.45,75.29,3045.60],                                                                                                                          
'ord_date':['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],                                                      
'customer_id':['C3001','C3001','D3005','D3001','C3005','D3001','C3005','D3001','D3005','C3001','D3005','D3005'],                                                                                                               
'salesman_id':[5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})                                                                                                                                                  
print(df8)                                                                                                                                                                                                                     
print(df8.groupby('customer_id').agg({'customer_id':lambda x:x.str.startswith('C').sum(),'ord_no':list,'purch_amt':lambda y:y.max()-y.min()}))                                                                                 
print(df)                                                                                                                                                                                                                      
def combine(x):                                                                                                                                                                                                                 
    new_dict=dict()                                                                                                                                                                                                            
    for i in x.columns:                                                                                                                                                                                                        
        new_dict[i]=list(x[i])                                                                                                                                                                                                 
    return new_dict                                                                                                                                                                                                            
print(df.groupby(['school','class']).apply(combine,include_groups=False))                                                                                                                                                      
df9=pd.DataFrame({'salesman_id':[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012],                                                                                                                                 
'sale_jan':[150.50,270.65,65.26,110.50,948.50,2400.60,1760.00,2983.43,480.40,1250.45,75.29,1045.60]})                                                                                                                          
print(df9.groupby(pd.cut(df9['salesman_id'],bins=[0,5006,np.inf],labels=['S1','S2']),observed=False)['sale_jan'].sum())                                                                                                        
print(df8)                                                                                                                                                                                                                     
df8['ord_date']=pd.to_datetime(df8.ord_date,format='mixed')                                                                                                                                                                    
print(df8.groupby('salesman_id')['ord_date'].agg('min'))                                                                                                                                                                       
df8['ord_date']=df8['ord_date'].astype(str)                                                                                                                                                                                    
print(df8)
df9=pd.DataFrame({'school':['s001','s002','s003','s001','s002','s004'],
                      'class':['V','V','VI','VI','V','VI'],
                      'name':['Alberto Franco','Gino Mcneill','Ryan Parkes',
                              'Eesha Hinton','Gino Mcneill','David Parkes'],
                      'date_Of_Birth':['15/05/2002','17/05/2002','16/02/1999',
                                       '25/09/1998','11/05/2002','15/09/1997'],
                      'age': [12, 12, 13, 13, 14, 12],
                      'weight': [173, 192, 186, 167, 151, 159],
                      'height': [30, np.nan, 33, 30, np.nan, 32],
                      'address': ['street1','street2','street3','street1',
                                  'street2','street4']}
                      ,index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
print(df9)
print(df9.groupby('height',dropna=False).filter(lambda x:pd.notnull(x.name)))
df10=pd.DataFrame({'dept':['A','A','B','B','B','C'],'salary':[10,20,30,40,50,60]})
print(df10.groupby('dept').filter(lambda x:len(x)>2))
df11=pd.DataFrame({'dept':['A','A','B','B','B'],'salary':[10,20,30,40,50]})
df11['dept_avg']=df11.groupby('dept')['salary'].transform('mean')
print(df11)
"""

#string and regular expression
"""s1 = pd.Series(['X', 'Y', 'Z', 'Aaba', 'Baca', np.nan, 'CABA', None, 'bird', 'horse', 'dog'])
print(s1.str.upper())
print(s1.str.lower())
print(s1.str.len())
s2 = pd.Index([' Green', 'Black ', ' Red ', 'White', ' Pink '])
print(s2.str.strip().values)
print(s2.str.rstrip().values)
print(s2.str.lstrip().values)
s3=pd.Series([10, 250, 3000, 40000, 500000])
def addleadzero(x):
    temp=8-len(str(x))
    if temp>0:
        return ('0'*temp)+str(x)
    else:
        return str(x)
print(s3.apply(addleadzero))
print(s3.apply(lambda x:'{0:0>8}'.format(x)))
s4=pd.Series(['10', '250', '3000', '40000', '500000'])
print(s4.str.pad(8,'left','0'))
df=pd.DataFrame({'name': ['alberto','gino','ryan', 'Eesha', 'syed'],
                 'age': [18.5, 21.2, 22.5, 22, 23]})
df['name']=df['name'].str.capitalize()
print(df)
s5=pd.Series(['22/05/2022','16/02/1999','25/09/1998','12/02/2022','15/09/1997'])
print(s5.str.count('2'))
print(s5.str.find('22'))
print(s5.str.find('22',2,10))
s6=pd.Series(['Company','Company a001','Company 123', '1234', 'Company 12'])
print(s6.str.isalnum())
print(s6.str.isalpha())
print(s6.str.isdigit())
print(s6.apply(lambda x:True if type(x)==int else False))
s7=pd.Series(['ABCD','EFGF', 'hhhh', 'abcd', 'EAWQaaa','Love',' '])
print(s7.str.isupper())
print(s7.str.islower())
print(s7.str.istitle())
print(s7.str.isspace())
print(s7.str.len())
print(s7.str.swapcase())
print(s7.str.title())
s8=pd.Series([12348.5, 233331.2, 22.5, 2566552.0, 23.0])
print(s8.astype(str).str.len())
s9=pd.Series(['zereter','sdsaeelp'])
print(s9.str.startswith('ze'))
print(s9.str.endswith('lp'))
s10=pd.Series(['a','b','c'])
print(s10.str.replace('a','z'))
s11=pd.Series(['a b c','p q','a'])
print(s11.str.split(" ",expand=True))

#regex for email
s12=pd.Series(['Alberto Franco af@gmail.com blabla@bla.bla','Gino Mcneill gm@yahoo.com','Ryan Parkes rp@abc.io','Eesha Hinton','Gino Mcneill gm@github.com'])
print(s12.str.findall(r'[\w\.-]+@[\w-]+\.[\w]+'))

#regex for all hashtags
s13=pd.Series(['#Obama says goodbye','Retweets for #cash','A political endorsement in #Indonesia', '1 dog = many #retweets', 'Just a simple #egg'])
print(s13.str.findall(r'(?<=#)\w+'))

#regex for numbers in address
df1=pd.DataFrame({'address': ['7277 Surrey Ave.', '920 N. Bishop Ave.', '9910 Golden Star St.', '25 Dunbar St.',
            '17 West Livingston Court']})
df1['numbers']=df1.address.str.findall(r'\d+')
print(df1)

#regex for phone number
s14=pd.Series(['Company1-Phone no. 4695168357 2','Company2-Phone no. 8088729013','Company3-Phone no. 6204658086', 'Company4-Phone no. 5159530096', 'Company5-Phone no. 9037952371'])
print(s14.str.findall(r'\d{10}'))

#regex to find number btw 1800 and 2200
s15=pd.Series(['year 1800','year 1700','year 2300', 'year 1900', 'year 2200'])
def check(x):
    p=re.findall(r'\d{4}',x)
    if p and 2200>=int(p[0])>=1800:
        return p[0]
print(s15.apply(check))

#regex to find other than alphanumeric cleaning data
s16=pd.Series(['c0001#','c00@0^2','$c0003', 'c0003', '&c0004'])
print(s16.str.findall(r'[^a-zA-Z0-9]'))

#regex to find punchuation
s17=pd.Series(['c0001.','c000,2','c0003', 'c0003#', 'c0004,'])
print(s17.str.findall(r'[^\w\s]'))

#regex to remove repetition
s18=pd.Series(['She livedd a long life.','How oold is your father?','What is tthe problem?','TThhis desk is used by Tom.'])
print(s18.str.replace(r'(.)\1+',r'\1',regex=True))

#regex to find numbers greater than 940
s19=pd.Series(['7277 Surrey Ave.1111','920 N. Bishop Ave.','9910 Golden Star St.', '1025 Dunbar St.', '1700 West Livingston Court'])
print(s19.str.findall(r'9[4-9][1-9]|9[5-9][0-9]|[1-9]\d{3,}'))

#'regex to find nunber less than 100' then 'regex to find phrase containing Ave and 92'
s20=pd.Series(['72 Surrey Ave.11','92 N. Bishop Ave.','9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court'])
print(s20.str.findall(r'\b[0-9]{1,2}\b'))
print(s20.str.findall(r'(?=.*Ave.)(?=92).*'))

#regex to find date of format mm-dd-yyyy
s21=pd.Series(['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'])
print(s21.str.findall(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|[3][01])/[0-9]\d{3}$'))

#regex to find all words
s22=pd.Series(['72 Surrey Ave.11','92 N. Bishop Ave.','9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court'])
print(s22.str.findall(r'\b[a-zA-Z]+\b'))

#contains word avenue
s23=pd.Series(['9910 Surrey Avenue','92 N. Bishop Avenue','9910 Golden Star Avenue', '102 Dunbar St.', '17 West Livingston Court'])
print(s23[s23.str.contains('Avenue')])

#words starting with Capital letter
s24=pd.Series(['9910 Surrey venue','92 N. ishop Avenue','9910 Golden Star Avenue', '102 Dunbar St.', '17 West ivingston Court'])
print(s24.str.findall(r'\b[A-Z][a-z]*\b'))

#remove html tags
s25=pd.Series(['9910 Surrey <b>Avenue</b>','92 N. Bishop Avenue','9910 <br>Golden Star Avenue', '102 Dunbar <i></i>St.', '17 West Livingston Court'])
print(s25.str.replace(r'</?[a-z]{1,2}>','',regex=True))"""

#time series
"""d='01/12/2022 00:21:20'
temp=pd.to_datetime(d)
print(temp)
print(temp.date())
print(temp.time())
print(pd.Timestamp.now(tz='Asia/Kolkata'))
print(pd.Timestamp.now(tz='Asia/Kolkata').date())
print(pd.Timestamp.now(tz='Asia/Kolkata').time())
t=pd.Timestamp('2022/09/22 01:22:44')
print(t)
print(t.time())
print(t.date())
print(pd.Timestamp.now()+pd.Timedelta(days=5))
d2=pd.to_datetime("1st of January, 2021")
print(d2)
t2=pd.Timestamp(year=2020, month=12, day=25)
print(t2)
t3=pd.Timestamp("1st of January, 2021")
print(t3)
t4=pd.Timestamp("2029/09/30")+pd.Timedelta(days=1)
print(t4)
print('time difference:',t4-t3)
df=pd.DataFrame({'data':[9,8,7,6,4]},index=pd.date_range(start='2021/01/20',periods=5))
print(df)
print(df.index)
p = pd.DatetimeIndex(['2011-09-02', '2012-08-04',
                          '2015-09-03', '2010-08-04',
                          '2015-03-03', '2011-08-04',
                          '2015-04-03', '2012-08-04'])
s = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index=p)
print(s)
print(s['2015'])
print(s.loc['2015'])
print(s)
s=s.sort_index()
print(s)
print(s['2010-01-01':'2012-12-31'])
print(pd.date_range(start="2020-09-22",periods=300))
s1=pd.Series(pd.date_range(start='2020-01-01',periods=31,freq='D'))
print(s1)
print(s1.max())
print(s1.min())
s2=pd.Series(pd.date_range(start='2020-01-01',periods=4,freq='3ME'))
print(s2)
s3=pd.Series(pd.timedelta_range(start='1 day',end='2 day',freq='6h'))
print(s3)
s4=pd.Series(pd.date_range(start='00:00:00',end='10:00:00',freq='h'))
print(s4)
s5=pd.Series(pd.timedelta_range(start='00:00:00',end='10:00:00',freq='h'))
print(s5)
print(s5.astype(str).str.split(' ').apply(lambda x:x[2]))
data={"year": [2002, 2003, 2015, 2018],"day_of_the_year": [250, 365, 1, 140]}
df1=pd.DataFrame(data)
df1['year']=df1['year'].astype('str')
df1['day_of_the_year']=df1['day_of_the_year'].astype('str')
df1['date']=pd.to_datetime(df1['year']+df1['day_of_the_year'],format='%Y%j')
df1.pop('year')
df1.pop('day_of_the_year')
print(df1)
df2=pd.DataFrame({'year':[2018, 2019, 2020],'month': [2, 3, 4],
                   'day': [4, 5, 6],'hour': [2, 3, 4]})
#1st way as col are year,month,day,hour explicitly
print(pd.to_datetime(df2))
#2nd way from earlier question
df2=df2.astype('str')
df2['new']=pd.to_datetime(df2['year']+df2['month']+df2['day']+df2['hour'],format='%Y%m%d%I')
print(df2)
print(pd.Timestamp('2026-09-12').dayofweek<5)
print(pd.bdate_range('2026-09-12','2026-09-15'))
print(pd.date_range("2026-09-12",periods=9,freq='B'))
print(pd.date_range('2021-01-01', periods=12, freq='BME'))
print(pd.timedelta_range(0, periods=3, freq="1h20min"))
t5=pd.Timestamp('2012-09-11').tz_localize('Europe/Berlin')
print(t5.tz_convert(None))
print(t5.tz_localize(None))
t6=pd.Timestamp('2012-09-11').tz_localize('Asia/Calcutta')
print(t5-t6)
print(pd.date_range('2020-01-01',periods=5, freq="W-THU"))
t6=pd.Timestamp('2020-01-01')
temp1=t6+pd.Timedelta(days=1)
print(temp1)
for i in range(4):
    temp1=temp1+pd.Timedelta(days=7)
    print(temp1)
print(pd.date_range('2020-01-01',periods=4,freq='BQE'))
print(pd.date_range('2020-01-01',periods=4,freq='BQS'))
print(pd.date_range('2020-01-01',periods=4,freq='1d1h1min'))
t7=pd.Timestamp('2026-02-07')
print(t7.day_name())
t7=t7+pd.Timedelta(days=2)
print(t7+pd.offsets.BDay(1))
#print(pd.date_range(t7+pd.Timedelta(days=1),periods=1,freq='B'))
s6=pd.to_datetime([1329806505, 129806505],unit='s')
print(s6)
t8=pd.Timestamp(2020, 1, 4)
print(pd.date_range(t8,periods=3,freq='B'))
print(pd.date_range(t8,periods=1,freq='BME'))
s=pd.Timestamp(2020,1,1)
e=pd.Timestamp(2020,12,31)
p=pd.Period('2021-11','M')
print(p)
print(dir(p))
dataset=pd.period_range(s,e,freq='M')
print(dataset)
for d in dataset:
    print(d.start_time,d.end_time)
dataset1=pd.period_range('2029','2031',freq='M')
print(dataset1)
s7=pd.Series(range(25),index=dataset1)
print(s7['2030'])
p1=pd.Period('2026','Y')
print(p1)"""

#handling missing values
"""df1=pd.DataFrame({'ord_no':[70001.0,np.nan,70002.0,70004.0,np.nan,70005.0,np.nan,70010.0,70003.0,70012.0,np.nan,70013.0],
'purch_amt':[150.50,270.65,65.26,110.50,948.50,2400.60,5760.00,1983.43,2480.40,250.45,75.29,3045.60],
'ord_date':['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
'salesman_id':[5002.0,5003.0,5001.0,np.nan,5002.0,5001.0,5001.0,np.nan,5003.0,5002.0,5003.0,np.nan]})
print(df1)
print(df1.isnull())
print(df1.isnull().any(axis=1)) #row wise atleast 1 empty check
print(df1.isnull().any(axis=0)) #col. wise atleast 1 empty check
print(df1.isnull().sum()) #find no. of null col wise(counting each row's null as one) meaning axis=row default
df2=df=pd.DataFrame({'ord_no':[70001,np.nan,70002,70004,np.nan,70005,'--',70010,70003,70012,np.nan,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,np.nan,12.43,2480.4,250.45,3045.6],
'ord_date':[np.nan,'2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,'--',3002,3001,3001],
'salesman_id':[5002,5003,'?',5001,np.nan,5002,5001,'?',5003,5002,5003,'--']})
print(df2)
print(df2.replace(['?','--'],np.nan).isnull())
print(df1)
print(df1.dropna(axis=0)) #drop row
print(df1.dropna(axis='rows')) #drop row
print(df1.dropna(axis=1)) #drop col
print(df1.dropna(axis='columns')) #drop col
df3=pd.DataFrame({'ord_no':[np.nan,np.nan,70002.0,70004.0,np.nan,70005.0,np.nan,70010.0,70003.0,70012.0,np.nan,70013.0],
'purch_amt':[np.nan,270.65,65.26,110.50,948.50,2400.60,5760.00,1983.43,2480.40,250.45,75.29,3045.60],
'ord_date':[np.nan,'2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[np.nan,3001.0,3001.0,3003.0,3002.0,3001.0,3001.0,3004.0,3003.0,3002.0,3001.0,3001.0]})
print(df3)
print(df3.dropna(axis='rows',how='all')) #drop rows with all missing values
df4=pd.DataFrame({'ord_no':[np.nan,np.nan,70002.0,np.nan,np.nan,70005.0,np.nan,70010.0,70003.0,70012.0,np.nan,np.nan],
'purch_amt':[np.nan,270.65,65.26,np.nan,948.50,2400.60,5760.00,1983.43,2480.40,250.45,75.29,np.nan],
'ord_date':[np.nan,'2012-09-10',np.nan,np.nan,'2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17',np.nan],
'customer_id':[np.nan,3001.0,3001.0,np.nan,3002.0,3001.0,3001.0,3004.0,3003.0,3002.0,3001.0,np.nan]})
print(df4)
print(df4[df4.isnull().sum(axis='columns')>=2]) #keep rows with atleast 2 missing values
print(df4.dropna(subset=['ord_no','customer_id']))
print(df4.dropna())
print(df4.isnull().sum().sum())
df4['ord_no']=df4['ord_no'].fillna(0)
print(df4)
df5=pd.DataFrame({'ord_no':[70001.0,np.nan,70002.0,70004.0,np.nan,70005.0,np.nan,70010.0,70003.0,70012.0,np.nan,70013.0],
'purch_amt':[150.50,np.nan,65.26,110.50,948.50,np.nan,5760.00,1983.43,np.nan,250.45,75.29,3045.60],
'sale_amt':[10.50,20.65,np.nan,11.50,98.50,np.nan,57.00,19.43,np.nan,25.45,75.29,35.60],
'ord_date':['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
'salesman_id':[5002.0,5003.0,5001.0,np.nan,5002.0,5001.0,5001.0,np.nan,5003.0,5002.0,5003.0,np.nan]})
print(df5)
print(df5.ffill())
print(df5.assign(ord_no=df5.ord_no.ffill()))
print(df5.bfill())
print(df5)
print(df5.fillna({'purch_amt':df5['purch_amt'].mean(),'sale_amt':df5['sale_amt'].median()}))
print(df5['purch_amt'].interpolate(method='linear',direction='forward'))
print(df5['purch_amt'].interpolate())
print(df5['ord_no'].isnull().sum())
print(df5.isnull().sum().sum())
print(df5)
print(df5[df5.isnull().any(axis='columns')].index.values)
print(df5.fillna(df5.mode().iloc[0]))
df6=pd.DataFrame({'A': [1, 1, 2, 2, np.nan],'B': ['x', 'x', 'y', np.nan, np.nan]})
print(df6.fillna(df6.mode()))
print(df6.fillna(df6.mode().iloc[0]))"""

#pivot-table questions
"""df1=pd.DataFrame({'OrderDate':['1-6-18','1-23-18','2-9-18','2-26-18','3-15-18','4-1-18','4-18-18','5-5-18','5-22-18','6-8-18','6-25-18','7-12-18','7-29-18','8-15-18','9-1-18','9-18-18','10-5-18','10-22-18','11-8-18','11-25-18','12-12-18','12-29-18','1-15-19','2-1-19','2-18-19','3-7-19','3-24-19','4-10-19','4-27-19','5-14-19','5-31-19','6-17-19','7-4-19','7-21-19','8-7-19','8-24-19','9-10-19','9-27-19','10-14-19','10-31-19','11-17-19','12-4-19','12-21-19'],
    'Region':['East','Central','Central','Central','West','East','Central','Central','West','East','Central','East','East','East','Central','East','Central','East','East','Central','Central','East','Central','Central','East','West','Central','Central','East','Central','Central','Central','East','Central','Central','West','Central','West','West','Central','Central','Central','Central'],
    'Manager':['Martha','Hermann','Hermann','Timothy','Timothy','Martha','Martha','Hermann','Douglas','Martha','Hermann','Martha','Douglas','Martha','Douglas','Martha','Hermann','Martha','Douglas','Hermann','Douglas','Douglas','Timothy','Douglas','Martha','Timothy','Hermann','Martha','Martha','Timothy','Timothy','Hermann','Martha','Hermann','Hermann','Timothy','Timothy','Timothy','Douglas','Martha','Hermann','Hermann','Martha'],
    'SalesMan':['Alexander','Shelli','Luis','David','Stephen','Alexander','Steven','Luis','Michael','Alexander','Sigal','Diana','Karen','Alexander','John','Alexander','Sigal','Alexander','Karen','Shelli','John','Karen','David','John','Alexander','Stephen','Luis','Steven','Diana','David','David','Shelli','Alexander','Sigal','Shelli','Stephen','David','Stephen','Michael','Steven','Luis','Luis','Steven'],
    'Item':['Television','Home Theater','Television','Cell Phone','Television','Home Theater','Television','Television','Television','Home Theater','Television','Home Theater','Home Theater','Television','Desk','Video Games','Home Theater','Cell Phone','Cell Phone','Video Games','Television','Video Games','Home Theater','Home Theater','Home Theater','Home Theater','Video Games','Television','Cell Phone','Television','Home Theater','Desk','Video Games','Video Games','Video Games','Desk','Television','Cell Phone','Home Theater','Television','Home Theater','Home Theater','Home Theater'],
    'Units':[95,50,36,27,56,60,75,90,32,60,90,29,81,35,2,16,28,64,15,96,67,74,46,87,4,7,50,66,96,53,80,5,62,55,42,3,7,76,57,14,11,94,28],
    'Unit_price':[1198,500,1198,225,1198,500,1198,1198,1198,500,1198,500,500,1198,125,58.5,500,225,225,58.5,1198,58.5,500,500,500,500,58.5,1198,225,1198,500,125,58.5,58.5,58.5,125,1198,225,500,1198,500,500,500],
    'Sale_amt':[113810,25000,43128,6075,67088,30000,89850,107820,38336,30000,107820,14500,40500,41930,250,936,14000,14400,3375,5616,80266,4329,23000,43500,2000,3500,2925,79068,21600,63494,40000,625,3627,3217.5,2457,375,8386,17100,28500,16772,5500,47000,14000]})
print(df1)
print(df1.pivot_table(index=['Item','Unit_price'],aggfunc='count'))
print(df1.pivot_table(index=['Region','Manager'],values='Sale_amt',aggfunc='sum'))
print(df1.pivot_table(index=['Region','Manager','SalesMan'],values='Sale_amt',aggfunc='sum'))
print(df1.pivot_table(index='Item',values='Units',aggfunc='sum'))
print(df1.pivot_table(index='Region',values='Sale_amt',aggfunc='sum'))
print(df1.pivot_table(index=['Region','Item'],values='Units',aggfunc='sum'))
print(df1.pivot_table(index='Manager',values='Sale_amt',aggfunc=['count','mean']))
print(df1.pivot_table(index=['Manager','SalesMan'],values='Sale_amt',aggfunc='sum',margins=True))
temp1=df1.pivot_table(index=['Region','Manager','SalesMan'],values='Sale_amt',aggfunc='sum')
#1st way for get for douglas
temp2=temp1.reset_index(level=1)
print(temp2[temp2['Manager']=='Douglas'])
#2nd way for get for douglas
print(temp1.query("Manager == 'Douglas'"))
#3rd way
temp3=df1[df1.Manager=='Douglas']
print(temp3.pivot_table(index=['Region','Manager','SalesMan'],values='Sale_amt',aggfunc='sum'))
temp4=df1.query("`Item` =='Television' or `Item` =='Home Theater'")
print(temp4.pivot_table(index=['Region','Item'],values='Units',aggfunc='sum'))
print(df1.pivot_table(index='Item',values='Sale_amt',aggfunc=['max','min']))

df2=pd.read_csv('titanic.csv')
print(df2)
print(df2.info())
print(df2.columns)
print(len(df2)) #no of records/rows
print(len(df2.columns)) #no of columns
print(df2.dtypes)
print(df2.pivot_table(index=['sex','age'],aggfunc='count'))
print(df2.pivot_table(index='sex',columns='class',values='survived',aggfunc='mean'))
print(df2.pivot_table(index='sex',values='survived',aggfunc='mean'))
print(df2.pivot_table(index=['sex','age'],columns='class',values='survived',aggfunc='mean'))
print(pd.cut(df2['age'],bins=[0,10,30,60,80]))
temp=df2.groupby(pd.cut(df2['age'],bins=[0,10,30,60,80]))
for age,age_df in temp:
    print(age)
    print(age_df)
df2['categ_age']=pd.cut(df2['age'],bins=[0,10,30,60,80])
print(df2.pivot_table(index=['sex','categ_age'],columns='class',values='survived',aggfunc='sum'))
print(df2.pivot_table(index=['sex',pd.cut(df2['age'],bins=[0,10,30,60,80])],columns='class',values='survived',aggfunc='mean'))
categage=pd.cut(df2['age'],bins=[0,10,30,60,80])
categfare=pd.qcut(df2['fare'],q=2)
print(df2.pivot_table(index=['sex',categage],columns=['class',categfare],values='survived',aggfunc='mean'))
print(df2.pivot_table(index='sex',columns='class',aggfunc='size'))
print(df2.pivot_table(index=['sex','class'],values='survived',aggfunc='mean'))
print(df2.pivot_table(index='class',values='survived',aggfunc='sum'))
print(df2.pivot_table(index='sex',columns='class',aggfunc='size'))
print(df2.pivot_table(index=['sex','class'],aggfunc={'survived':'sum','fare':'mean'}))
print(df2.value_counts('who'))
print(df2.pivot_table(index='who',aggfunc='size'))
print(df2.pivot_table(index='sex',columns='alone',values='survived',aggfunc='mean'))"""