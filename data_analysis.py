import streamlit as st
#import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('Scoring.csv', sep=';')
df2007 = df[df.Quality_Attribute_1=="Compatibility"]

print(list(df.columns)[-3:])

print(list(df.columns.tolist())[-3:])

print(df.columns.values[-3:])
