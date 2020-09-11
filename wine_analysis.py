# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
from plotly.offline import plot

pd.set_option('display.max_columns', None)

df = pd.read_csv('./data/wine_data.csv')

# %%

df = df[['country', 'designation', 'points', 'price', 'taster_name', 'variety',
         'winery']]

#%%
df.head()
df.describe(include=['object'])
df.describe()
df = df[df['price'].notnull()]

#%%

fig = px.scatter(data_frame=df, x='price', y='points',
                 marginal_x='violin', marginal_y='box',
                 title='How price corespond to taste', trendline='ols', 
                 hover_data=['taster_name','variety','winery'], 
                 range_y=[80,105])
plot(fig)

#%%

fig2=px.box(df, x='country', y='price')
plot(fig2)
# %%

fig2=px.box(df, x='country', y='points')
plot(fig2)

# %%

fig3 = px.histogram(df, x='price', nbins=100, title='Rozkład zmiennej cena', 
                    color='points', log_y = True,
                    category_orders={'points':list(range(100))},
                    color_discrete_sequence=['#'+str(4*x).zfill(2)+'1010' 
                                             for x in range(24)]
                    )
plot(fig3)

# %%

fig4 = px.violin(data_frame=df, x='taster_name', y='points')
plot(fig4)
