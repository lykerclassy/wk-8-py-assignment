"""
analysis.py
Basic analysis of CORD-19 metadata.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load only first 50,000 rows to avoid memory errors
df = pd.read_csv('metadata.csv', nrows=50000, low_memory=False)

# Basic info
print("Shape of data:", df.shape)
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

# Extract publication year
df['year'] = pd.to_datetime(df['publish_time'], errors='coerce').dt.year

# Count papers by year
year_counts = df['year'].value_counts().sort_index()
print("\nPublications by Year:\n", year_counts)

# Plot publications by year
plt.figure(figsize=(10,5))
plt.bar(year_counts.index, year_counts.values)
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.tight_layout()
plt.savefig('publications_by_year.png')
plt.close()

# Save a cleaned sample for the app
df_sample = df[['title','abstract','journal','publish_time','year']].copy()
df_sample.to_csv('metadata_sample.csv', index=False)
print("Saved sample to metadata_sample.csv")
