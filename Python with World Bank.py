#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 파이썬에서 world bank data를 받을 수 있는 package를 먼저 설치해야함.
# conda install wbdata 혹은 pip install wbdata 둘 중 한가지를 명령어 창에 입력하면 자동으로 설치됨.
#설치 완료후, 
import wbdata # wbdata package 불러오기
import pandas as pd, numpy as np # dataframe 수정하는데 사용하는 pandas와 numpy 불러오기
import os # 작업할 문서공간 설정 불러오기
from matplotlib import pyplot as plt # 그래프 그리는데 필요한 package


# In[2]:


os.chdir('/Users/kyuyeonhwang/Desktop/Data/World bank') # 작업할 폴더공간 설정


# In[3]:


wbdata.get_topic() # world bank data중 어떤 파일을 불러올지 확인


# In[4]:


wbdata.get_indicator(topic=3) 
# 위에서 관심있는 카테고리를 선택했으면, 해당 카테고리에서 제공하는 구체적인 데이터가 무엇이 있는지 확인
# 여기서는 예시로 경제성장과 관련된 카테고리를 선택할 것임.


# In[5]:


indicators={"DT.TDS.DECT.EX.ZS":"debt", "FP.CPI.TOTL.ZG":"inflation", "NY.GDP.PCAP.KD.ZG":"gdp growth per"}
# 이중에서 원하는 데이터를 indicator로 설정. 하나를 설정해도 되고, 여러개를 설정해도 됨. 여기에서는 세가지 정도를 선택해 보겠음.
# indicators={"id":"내가 설정하고 싶은 명칭"}


# In[6]:


wbdata.get_country()
# 어느나라 데이터를 불러올것인지 나라목록을 살펴볼 수 있음.


# In[7]:


countries=['LIC','LMC','LMY','HIC']
# indicator와 마찬가지로 나라 1개를 선택해도 되고, 여러 국가를 선택해도 됨.
# 여기서는 특정국가보다는, High income, low income, lower-middle income, low&middle income 국가의 묶음들을 선택하겠음.


# In[8]:


df = wbdata.get_dataframe(indicators, country=countries)
# data indicator와 국가를 선택했으니, 이걸 이용하여 dataframe을 만들어볼 것임.
# 이 dataframe을 바로 사용하여 그래프로 그려봐도 되지만, 누락된 데이터는 없는지, 누락된 데이터를 없애고 그래프화 시키는 것 등등을 시행해 보겠음.


# In[9]:


df2 = df.copy()
# 우선 위에 df 데이터 프레임을 복사하여 df2라는 데이터 프레임을 생성.


# In[10]:


df2


# In[11]:


df2.reset_index(inplace=True)
# df의 기존 인덱스는 country와 date로 되어있지만, 이를 재설정해줌. 이래야 나중에 데이터로 plot하기 편해짐.
df2


# In[12]:


df2['text']=df2['country']+df2['date']
# df2 데이터 프레임에 text라는 새로운 항목을 만들어 줌.
# 이거는 각각의 데이터들(debt, inflation, gdp growth per)이 위에 내가 고른 나라들 중 어떤 국가의 어떤 시점의 데이터인지를 표시해줌.


# In[13]:


df2['inflation'].mean()
# df2 데이터 프레임을 활용하여 평균이나, 기초통계정보를 확인 할 수 있음.


# In[14]:


df2['gdp growth per'].describe()
# df2 데이터 프레임을 활용하여 평균이나, 기초통계정보를 확인 할 수 있음.


# In[15]:


df2['debt'].mean()


# In[16]:


df_selyrs=df2[(df2['date']>=2000)]
# 원하는 데이터들의 기간도 정할 수 있음. 
# 만약, 어떤 기간과 기간사이의 데이터값을 원하면, 
# df_selyrs=df2[(df2['date']>=2000) & (df2['date']<=2016)] 
# 위와같이 설정하여 데이터를 활용할 수 있음.


# In[17]:


# 그런데 간혹가다, 위에 명령어로 기간설정을 할 경우 오류메시지가 나올 수 있는데, 긴장하지 말고 다음과 같이 하면 됨.

df2['date']=pd.to_numeric(df2['date'])
df_selyrs=df2[(df2['date']>=2000)]

# 오류가 나는 이유는, 부등식이 위에식의 행과 열에서 적용이 되지 않아서 그럼. 이럴때는 Unstack을 바로 사용하면 되지만, 지금처럼 해도 괜찮음.


# In[18]:


df_selyrs
# 2000년 이후부터 데이터를 가져왔음.


# In[19]:


df_selyrs.info()
# 2000년 이후로 설정한 새로운 데이터 프레임에 변수가 누락된 기간이 있는지 살펴볼 것임. 필요하다면 누락된 기간을 지울 수 있음.
# 데이터를 보면 debt 숫자만 22개나 부족함, 즉 debt에서 22개의 누락변수가 존재함. 그런데 이것이 한 국가에서 누락된건지, 아니면 4개 국가에서 똑같이 
# 없는지 확인해봐도 됨.


# In[20]:


dfnas=df_selyrs[df_selyrs['debt'].isnull()]
dfnas
# 확인결과 High income 국가에서 debt 자료가 아예 없음, 이때 text를 아까 설정해준 덕분에 확인이 편함.


# In[21]:


df3=df_selyrs.dropna(subset=['debt'])


# In[22]:


df3.shape


# In[23]:


df3


# In[24]:


# 원한다면 특정 년도의 데이터만 뽑아서 볼 수 있음.

df2016=df3[df3['date']==2016]


# In[25]:


df2016.sort_values(by='inflation', ascending=False)
# 2016년도의 데이터를 인플레이션이 높은 기준으로 정렬해봤음. High income 국가는 debt 데이터가 없어서 밑에 표에 표시가 안됨.


# In[26]:


# 이제 우리가 원하는 데이터들을 plot해 보겠음.
# plot하기 전에, python에서는 시계열 데이터의 경우 시간이 row로 설정이 되어있어야 하기 때문에 데이터 프레임을 바꿔줄것임.
dfsu = df_selyrs.unstack(level=0)


# In[27]:


import seaborn as sns
sns.pairplot(data=df3, hue="country")

# pairplot을 통해, 변수간 연도별 진행단계를 확인할 수 있음. date가 x축이라, 보통 첫행 그래프 보는게 편함. 이거를 따로 scatter로 표현도 가능.
# 여기서는 df_selyrs 기간이 짧은거 같아서, 일부러 df3 데이터 프레임을 사용함.


# In[28]:


sns.relplot(data=df3, x="date", y="debt", kind="line", hue="country", col='country')

# 이렇게 원하는 데이터만 나라별로 뽑아서 plot을 할 수 있음.


# In[29]:


sns.relplot(data=df3, x="date", y="inflation", kind="line", hue="country", col='country')

# 이렇게 원하는 데이터만 나라별로 뽑아서 plot을 할 수 있음


# In[30]:


sns.relplot(data=df3, x="date", y="gdp growth per", kind="line", hue="country", col='country')

# 이렇게 원하는 데이터만 나라별로 뽑아서 plot을 할 수 있음
# 1인당 gdp 증가율이 인플레이션과 다르게 움직이고, 부채와도 반대로 움직이는거 같음.


# In[31]:


dfu=df.unstack(level=0)


# In[32]:


# 아까 위에서 데이터 프레임을 unstack으로 바꿔준 데이터를 사용해서 plot을 해보면

dfu.plot(figsize=(15,10));
plt.legend(loc='best');
plt.title("debt, inflation and growth per capita");
plt.xlabel('year');
plt.ylabel('debt, inflation, growth per capita');


# In[ ]:




