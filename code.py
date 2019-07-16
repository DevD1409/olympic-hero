# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)
data = data.rename(index=str,columns={'Total':'Total_Medals'})
data.head(10)
#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',(np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both')))
better_event = data['Better_Event'].value_counts().idxmax()



# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries[:-1]
def top_ten(data,columns):
    country_list=list(data.nlargest(10,columns)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter= top_ten(top_countries,'Total_Winter')
top_10= top_ten(top_countries,'Total_Medals')

common = list(set(top_10_summer)&set(top_10_winter)&set(top_10))


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.plot.bar(x = 'Country_Name',y = 'Total_Summer')
winter_df.plot.bar(x = 'Country_Name',y = 'Total_Winter')
top_df.plot.bar(x = 'Country_Name',y = 'Total_Medals')


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
index_country_gold=summer_df['Golden_Ratio'].idxmax
summer_country_gold = summer_df.loc[index_country_gold,'Country_Name']
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
index_winter_gold=winter_df['Golden_Ratio'].idxmax
winter_country_gold = winter_df.loc[index_winter_gold,'Country_Name']
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
index_top_gold=top_df['Golden_Ratio'].idxmax
top_country_gold = top_df.loc[index_top_gold,'Country_Name']


# --------------
#Code starts here
data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
index_points = data_1['Total_Points'].idxmax
best_country = data_1.loc[index_points,'Country_Name']



# --------------
#Code starts here
best = data.loc[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
best.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



