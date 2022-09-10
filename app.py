import streamlit as st
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('Scoring.csv', sep=';')
df2007 = df[df.Quality_Attribute_1=="Compatibility"]

st.title('Framework notation visualization')

options = st.sidebar.multiselect(
  'What are the framework scores that need to be displayed ?',
  options = sorted(df.columns.values[-3:]),
  default = ['FPrime_Score'])

options = st.sidebar.multiselect(
  'Which quality attribute categories should be displayed ?',
  options = sorted(set(df['Quality_Attribute_1'])),
  default = ['Compatibility'])

# if(option):

trace1 = go.Scatterpolar(
      r = df['FPrime_Score'],
      theta = df['Quality_Attribute_2'],
      fill = 'toself',
      name = 'F Prime'
    )

trace2 = go.Scatterpolar(
      r = df['cFS_Score'],
      theta = df['Quality_Attribute_2'],
      fill = 'toself',
      name = 'cFS'
    )

trace3 = go.Scatterpolar(
      r = df['TASTE_Score'],
      theta = df['Quality_Attribute_2'],
      fill = 'toself',
      name = 'TASTE'
    )

data = [trace1, trace2, trace3]

layout = go.Layout(
  polar = dict(
    radialaxis = dict(
      visible = False#,
      # range = [0, 5]
    )
  ),
  autosize=True,
  # showlegend = True,
  # legend=dict(
      # orientation="h",
      # yanchor="bottom",
      # y=0.9,
      # xanchor="right",
      # x=1.1
  # )#,
  # margin=dict(
  #       l=120,
  #       r=150#,
  #       # b=50,
  #       # t=50,
  #       # pad=4
  #   )
)

fig = go.Figure(data=data, layout=layout)
st.plotly_chart(fig, use_container_width=True)



