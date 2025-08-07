# -*- coding: utf-8 -*-

# Investigating Netflix Movies

# Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.

#   1) What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
#   2) A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
netflix = pd.read_csv('C:/Users/Juan!/Desktop/Juan/Git/netflix_data.csv') # Import .csv to DataFrame

# Preview the data
print(netflix.info())
print(netflix.head())

netflix_subset = netflix[netflix['type']=='Movie']
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]
netflix_movies_90=netflix_movies[(netflix_movies['release_year']>=1990) & (netflix_movies['release_year']<2000)]
print(netflix_movies_90.head()) # Preview the DataFrame

statistics=netflix_movies_90['duration'].agg(['mean','std']).round(2) # Just to get a sense of mean and std
print(statistics)

#At this point it's better to visualize the data, let's generate a histogram with bins grouping movies by duration with size of 10 minutes 

plt.figure(figsize=(12,6))

max_duration=netflix_movies_90['duration'].max()
bin_edges=np.arange(0, max_duration + 20, 10)

plt.hist(netflix_movies_90['duration'], 
         bins=bin_edges,
         edgecolor='black',
         linewidth=1.5,
         color='orange',
         alpha=0.8)

plt.title('Movie Duration in the 90s', pad=15, fontsize=22)
plt.xlabel('Duration (minutes)', labelpad=10, fontsize=16)
plt.ylabel('Number of Movies', labelpad=10, fontsize=16)

xticks = np.arange(0, max_duration + 20, 10)  # Label every 10 minutes
plt.xticks(xticks, fontsize=12)
plt.xlim(left=0)
plt.yticks(fontsize=12)

plt.grid(axis='y', alpha=0.3)

plt.tight_layout()

plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/90s_movie_durations_histogram.png', dpi=300, bbox_inches='tight')

plt.show()



