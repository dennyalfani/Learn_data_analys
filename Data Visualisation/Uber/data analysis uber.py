#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn


# # Load CSV file into memory

# In[2]:


data = pandas.read_csv('~/Documents/python/uber-raw-data-apr14.csv')


# In[3]:


data.tail()


# #convert datetime and insert coloumn

# In[4]:


dt = '4/30/2014 23:22:00'


# In[5]:


d, t = dt.split (' ')
print (d)
print (t)


# In[6]:


m, d, y = dt.split('/')


# In[7]:


d


# In[8]:


int(d)


# In[9]:


dt = pandas.to_datetime(dt)


# In[10]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[11]:


data.tail()


# In[12]:


def get_dom(dt):
    return dt.day
data ['dom'] = data['Date/Time'].map(get_dom)


# In[13]:


data.tail()


# In[14]:


def get_weekday(dt):
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)

data.tail()


# # Analisa

# ## Analisa berdasar tanggal

# In[15]:


hist(data.dom, bins = 30, rwidth=.8, range=(0.5, 30.5))
xlabel('Date of the month')
ylabel('frequency')
title('Frequency Data Uber 2014')


# In[16]:


#for k, rows in data.groupby('dom'):
#    print((k, rows))
#    print((k, len(rows)))

def count_rows(rows):
    return len(rows)


by_date = data.groupby('dom').apply(count_rows)
by_date


# In[17]:


plot(by_date)


# In[18]:


bar(range(1, 31), by_date)


# In[19]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[20]:


bar(range(1, 31), by_date_sorted)


# In[21]:


bar(range(1, 31), by_date_sorted)
xticks(range(1, 31), by_date_sorted.index)
xlabel('Date of the month')
ylabel('frequency')
title('Frequency Data Uber 2014')
("")


# ## Analisa berdasar jam(hour)

# In[30]:


hist(data.hour, bins=24, range=(.5, 24))


# In[ ]:





# ## analisa weekday

# In[33]:


hist(data.weekday, bins=7, range =(-.5, 6.5), rwidth=.8, color='#AA6666', alpha=.4)
xticks(range(7), 'Mon Tue Wed Thue Fri Satur Sun'.split())


# In[35]:


data.groupby('hour weekday'.split()).apply(count_rows)


# In[36]:


data.groupby('hour weekday'.split()).apply(count_rows).unstack()


# In[40]:


data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[41]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[42]:


seaborn.heatmap(by_cross)


# #by Lat and lon

# In[44]:


hist(data['Lat'])


# In[47]:


hist(data['Lat'], bins=100, range=(40.5, 41))
("")


# In[49]:


hist(data['Lon'], bins=100)
("")


# In[54]:


hist(data['Lon'], bins=100, range=(-74.1, -73.9))
("")


# In[60]:


hist(data['Lat'], bins=100, range=(40.5, 41), color= 'g', alpha=.5)
twiny()
hist(data['Lon'], bins=100, range=(-74.1, -73.9), color='r', alpha=.5)
("")


# In[66]:


hist(data['Lat'], bins=100, range=(40.5, 41), color= 'g', alpha=.5, label ='latitude')
grid()
legend(loc='upper left')
twiny()
hist(data['Lon'], bins=100, range=(-74.1, -73.9), color='r', alpha=.5, label ='longitude')
grid()
legend(loc='best')
("")


# In[79]:


plot(data['Lat'], data['Lon'], '.', ms=3, color='green', alpha=.5)


# In[84]:


figure(figsize=(20, 20))
plot(data['Lon'], data['Lat'], '.', ms=1, color='green', alpha=.5)
xlim(-74.2, -73.7)
ylim(40.7, 41 )


# In[ ]:




