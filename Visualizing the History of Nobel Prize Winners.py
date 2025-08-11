# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 15:20:33 2025

@author: Juan!
"""

import pandas as pd
#import seaborn as sns
import numpy as np
nobel = pd.read_csv('C:/Users/Juan!/Desktop/Juan/Git/nobel.csv') # Import .csv to DataFrame

# Task 1
top_gender = nobel['sex'].value_counts().index[0]
top_country = nobel['birth_country'].value_counts().index[0]
print(f"\n The gender with the most Nobel laureates is: {top_gender}.")
# The gender with the most Nobel laureates is : Male
print(f"\n The most common birth country of Nobel laureates is : {top_country}.") 
# The most common birth country of Nobel laureates is : United States of America

# Task 2
nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America' # new column boolean
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)               # new column 'decade'
prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()  # mean over boolean column grouping by decade, being True=1, False=0 (ratio of Us-born winners over total winners by decade)
max_decade_usa = prop_usa_winners[prop_usa_winners['usa_born_winner'] == prop_usa_winners['usa_born_winner'].max()]['decade'].values[0] # Decade with most us-born winners over total
max_ratio_usa = prop_usa_winners[prop_usa_winners['usa_born_winner'] == prop_usa_winners['usa_born_winner'].max()]['usa_born_winner'].values[0].round(2) # Ratio of most us-born winners over total
print(f"\n The decade with the highest ratio of US-born Nobel Prize winners to total winners in all categories was {max_decade_usa} with {max_ratio_usa} ratio.")
# The decade with the highest ratio of US-born Nobel Prize winners to total winners in all categories was 2000 with 0.42 ratio

# Task 3
nobel['female_winner'] = nobel['sex'] == 'Female' # new column boolean
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean() # mean over boolean column grouping by decade and category, being True=1, False=0 (ratio of female winner by category and decade)
max_female_decade_category = prop_female_winners[prop_female_winners['female_winner'] == prop_female_winners['female_winner'].max()][['decade', 'category', 'female_winner']] # Decade with most female winners by decade and category overall
print("\n The decade with the highest ratio of female winners by category was " + str(max_female_decade_category.values[0,0]) + " in " + str(max_female_decade_category.values[0,1]) + " with " + str(max_female_decade_category.values[0,2]) + " ratio.")
# The decade with the highest ratio of female winners by category was 2020 in Literature with 0.5 ratio

max_female_dict = {max_female_decade_category['decade'].values[0]: max_female_decade_category['category'].values[0]}

# Task 4
nobel_women = nobel[nobel['female_winner']]
min_row = nobel_women[nobel_women['year'] == nobel_women['year'].min()]
first_woman_name = min_row['full_name'].values[0]
first_woman_category = min_row['category'].values[0]
print(f"\n The first woman to win a Nobel Prize was {first_woman_name}, in the category of {first_woman_category}.")
# The first woman to win a Nobel Prize was Marie Curie, née Sklodowska, in the category of Physics.

# Task 5
counts = nobel['full_name'].value_counts()
repeats = counts[counts >= 2].index
repeat_list = list(repeats)
print("\n The repeat winners are :", repeat_list)
# The repeat winners are : ['Comité international de la Croix Rouge (International Committee of the Red Cross)', 'Linus Carl Pauling', 'John Bardeen', 'Frederick Sanger', 'Marie Curie, née Sklodowska', 'Office of the United Nations High Commissioner for Refugees (UNHCR)']