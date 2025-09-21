"""
app.py
Simple Streamlit app for CORD-19 exploration
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Load sample instead of full metadata to avoid memory errors
df = pd.read_csv('metadata_sample.csv')

# Sidebar filter
year_min = int(df['year'].min())
year_max = int(df['year'].max())
year_range = st.slider("Select year range", year_min, year_max, (year_min, year_max))

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write("Number of papers:", len(filtered_df))
st.dataframe(filtered_df.head())

# Plot publications by year
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title('Publications by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Papers')
st.pyplot(fig)
