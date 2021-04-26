
#importing all required modules
import pandas as pd
import wget
import matplotlib.pyplot as plt
import os
import altair as alt
from numpy import genfromtxt
import numpy as np
import seaborn as sns

#Urls for COVID Data

urls = [
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
]

#Downloading the Data from URLs
[wget.download(url) for url in urls]

#Fetching Data
confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv')
recovered_df = pd.read_csv('time_series_covid19_recovered_global.csv')


dates = confirmed_df.columns[4:]
confirmed_df_long = confirmed_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=dates,
    var_name='Date',
    value_name='Confirmed')

deaths_df_long = deaths_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=dates,
    var_name='Date',
    value_name='Deaths')

recovered_df_long = recovered_df.melt(
        id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
        value_vars=dates,
        var_name='Date',
        value_name='Recovered')

recovered_df_long = recovered_df_long[recovered_df_long['Country/Region']=='Canada']

# Merging confirmed_df_long and deaths_df_long
full_table = confirmed_df_long.merge(
      right=deaths_df_long,
      how='left',
      on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)

# Merging full_table and recovered_df_long
full_table = full_table.merge(
    right=recovered_df_long,
    how='left',
    on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)

full_table['Date'] = pd.to_datetime(full_table['Date'])

full_table['Recovered'] = full_table['Recovered'].fillna(0)


full_table['Active'] = full_table['Confirmed'] - full_table['Deaths'] - full_table['Recovered']
full_grouped = full_table.groupby(['Date','Province/State'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()

#Selecting Ontario Province Data
ontario = full_grouped[full_grouped['Province/State'] == 'Ontario']

#Saving File
ontario.to_csv('Ontario.csv')


ontario = pd.read_csv('Ontario.csv', parse_dates=['Date'])
on = ontario[ontario['Province/State'] == 'Ontario']


#LineGraph
base = alt.Chart(on).mark_line().encode(x='yearmonthdate(Date):O',).properties(width=500)
red = alt.value("#f54242")
green = alt.value("#32CD32")
base.encode(y='Confirmed').properties(title="Total Confirmed in Ontario") | base.encode(y='Deaths',color=red).properties(title="Total Deaths in Ontario") | base.encode(y='Active',color=green).properties(title="Total Active Cases in Ontario")


#Heatmap
data = pd.read_csv('Ontario.csv')
dates = data.Date.to_list() #Dates List
active = data.Active.to_list() #Active Cases List
data = data.drop(columns=['Unnamed: 0'],axis=1).set_index('Date')
ax = sns.heatmap(data.corr(),annot=True,vmin=0,vmax=1,cmap='Reds')
ax.set(title='COVID Data Correlation')








