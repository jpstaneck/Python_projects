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

####################################

"Some Visuals"

"1) seaborn lineplot Nobel Prize winners by gender"

# winners_yearly = nobel.groupby(['decade', 'sex']).size().reset_index(name='count')
# sns.lineplot(data = winners_yearly, x='decade', y='count', hue='sex',style='sex',  markers=True,  palette={'Male': 'blue', 'Female': 'red'},linewidth=2.5)

# plt.title("Nobel Prize Winners by Gender (1901-2020)")
# plt.ylabel("Number of Winners")
# plt.xlabel("Year")
# plt.grid(True, linestyle="--", alpha=0.7)

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Gender.png', dpi=300, bbox_inches='tight')

# plt.show()

" matplotlib pie chart nobel winners:"

"   2) by birth country (all years)"

# nobel_clean = nobel.dropna(subset=['birth_country'])
# nobel_winners_by_country = nobel_clean.groupby('birth_country')['year'].count()
# nobel_winners_by_country_perc = ((nobel_winners_by_country/len(nobel_clean))*100).sort_values().round(1)
# most_nobel_winners_by_country_perc = nobel_winners_by_country_perc[nobel_winners_by_country_perc>1.0].sort_values().round(1)
# sum_most_nobel_winners_by_country_perc = most_nobel_winners_by_country_perc.sum()
# others = 100-sum_most_nobel_winners_by_country_perc #equal or less than 2%
# # print(sum_most_nobel_winners_by_country_perc)
# # print(others)
# # print(nobel_winners_by_country_perc)
# # print(most_nobel_winners_by_country_perc)

# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United States of America', 'USA')
# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United Kingdom', 'UK')
# labels = list(most_nobel_winners_by_country_perc.index) + ['Others']
# sizes = list(most_nobel_winners_by_country_perc.values) + [others]

# plt.figure(figsize = (10, 8))
# plt.pie(
#     sizes,
#     labels = labels,
#     autopct = '%1.1f%%',
#     counterclock = False,
#     startangle = 45,
#     pctdistance = 0.85,
#     textprops={'fontsize': 12}
# )

# plt.axis('equal')
# plt.title('Nobel Prize Winners by Birth Country', pad = 20, fontsize = 20)

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Country.png', dpi = 300, bbox_inches='tight')

# plt.show()

"   3) by birth country (last 50 years)"

# nobel_clean = nobel.dropna(subset=['birth_country'])
# nobel_last_50=nobel_clean[nobel_clean['year']>=1970]
# nobel_winners_by_country=nobel_last_50.groupby('birth_country')['year'].count()
# nobel_winners_by_country_perc=((nobel_winners_by_country/len(nobel_last_50))*100).sort_values().round(1)
# most_nobel_winners_by_country_perc=nobel_winners_by_country_perc[nobel_winners_by_country_perc>1.0].sort_values().round(1)
# sum_most_nobel_winners_by_country_perc=most_nobel_winners_by_country_perc.sum()
# others=100-sum_most_nobel_winners_by_country_perc #equal or less than 2%
# # print(sum_most_nobel_winners_by_country_perc)
# # print(others)
# # print(nobel_winners_by_country_perc)
# # print(most_nobel_winners_by_country_perc)

# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United States of America', 'USA')
# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United Kingdom', 'UK')
# labels = list(most_nobel_winners_by_country_perc.index) + ['Others']
# sizes = list(most_nobel_winners_by_country_perc.values) + [others]

# plt.figure(figsize=(10, 8))
# plt.pie(
#     sizes,
#     labels=labels,
#     autopct='%1.1f%%',
#     counterclock=False,
#     startangle=45,
#     pctdistance=0.85,
#     textprops={'fontsize': 12}
# )

# plt.axis('equal')
# plt.title('Nobel Prize Winners by Birth Country (last 50 years)', pad=20, fontsize=18)

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Country in the last 50 years.png', dpi=300, bbox_inches='tight')

# plt.show()

"   4) by birth country (first 30 years)"

# nobel_clean = nobel.dropna(subset=['birth_country'])
# nobel_first_30=nobel_clean[nobel_clean['year']<=(nobel_clean['year'].min()+30)]
# nobel_winners_by_country=nobel_first_30.groupby('birth_country')['year'].count()
# nobel_winners_by_country_perc=((nobel_winners_by_country/len(nobel_first_30))*100).sort_values().round(1)
# most_nobel_winners_by_country_perc=nobel_winners_by_country_perc[nobel_winners_by_country_perc>2].sort_values().round(1)
# sum_most_nobel_winners_by_country_perc=most_nobel_winners_by_country_perc.sum()
# others=100-sum_most_nobel_winners_by_country_perc #equal or less than 2%
# # print(sum_most_nobel_winners_by_country_perc)
# # print(others)
# # print(nobel_winners_by_country_perc)
# # print(most_nobel_winners_by_country_perc)

# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United States of America', 'USA')
# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United Kingdom', 'UK')
# labels = list(most_nobel_winners_by_country_perc.index) + ['Others']
# sizes = list(most_nobel_winners_by_country_perc.values) + [others]

# plt.figure(figsize=(10, 8))
# plt.pie(
#     sizes,
#     labels=labels,
#     autopct='%1.1f%%',
#     counterclock=False,
#     startangle=45,
#     pctdistance=0.85,
#     textprops={'fontsize': 12}
# )

# plt.axis('equal')
# plt.title('Nobel Prize Winners by Birth Country (first 30 years)', pad=20, fontsize=18)

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Country in the first 30 years.png', dpi=300, bbox_inches='tight')

# plt.show()

"   5) by category (all years)"

# nobel_clean = nobel.dropna(subset=['category'])
# nobel_winners_by_category=nobel_clean.groupby('category')['year'].count()
# nobel_winners_by_category_perc=((nobel_winners_by_category/len(nobel_clean))*100).sort_values().round(1)
# most_nobel_winners_by_category_perc=nobel_winners_by_category_perc[nobel_winners_by_category>5.0].sort_values().round(1)
# sum_most_nobel_winners_by_category_perc=most_nobel_winners_by_category_perc.sum()

# labels = list(most_nobel_winners_by_category_perc.index)
# sizes = list(most_nobel_winners_by_category_perc.values)

# plt.figure(figsize=(10, 8))
# plt.pie(
#     sizes,
#     labels=labels,
#     autopct='%1.1f%%',
#     counterclock=False,
#     startangle=45,
#     pctdistance=0.85,
#     textprops={'fontsize': 12}
# )

# plt.axis('equal')
# plt.title('Nobel Prize Winners by Category', pad=20, fontsize=20)

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Category.png', dpi=300, bbox_inches='tight')

# plt.show()

"   6) by category (last 50 years)"

# nobel_clean = nobel.dropna(subset=['category'])
# nobel_last_50=nobel_clean[nobel_clean['year']>=1970]
# nobel_winners_by_category=nobel_last_50.groupby('category')['year'].count()
# nobel_winners_by_category_perc=((nobel_winners_by_category/len(nobel_last_50))*100).sort_values().round(1)
# most_nobel_winners_by_category_perc=nobel_winners_by_category_perc[nobel_winners_by_category>5.0].sort_values().round(1)
# sum_most_nobel_winners_by_category_perc=most_nobel_winners_by_category_perc.sum()

# labels = list(most_nobel_winners_by_category_perc.index)
# sizes = list(most_nobel_winners_by_category_perc.values)

# plt.figure(figsize=(10, 8))
# plt.pie(
#     sizes,
#     labels=labels,
#     autopct='%1.1f%%',
#     counterclock=False,
#     startangle=45,
#     pctdistance=0.85,
#     textprops={'fontsize': 12}
# )

# plt.axis('equal')
# plt.title('Nobel Prize Winners by Category (last 50 years)', pad=20, fontsize=20)

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Category in the 50 years.png', dpi=300, bbox_inches='tight')

# plt.show()

"   7) by category (first 30 years)"

# nobel_clean = nobel.dropna(subset=['category'])
# nobel_first_30=nobel_clean[nobel_clean['year']<=(nobel_clean['year'].min()+30)]
# nobel_winners_by_category=nobel_first_30.groupby('category')['year'].count()
# nobel_winners_by_category_perc=((nobel_winners_by_category/len(nobel_first_30))*100).sort_values().round(1)
# most_nobel_winners_by_category_perc=nobel_winners_by_category_perc[nobel_winners_by_category>5.0].sort_values().round(1)
# sum_most_nobel_winners_by_category_perc=most_nobel_winners_by_category_perc.sum()

# labels = list(most_nobel_winners_by_category_perc.index)
# sizes = list(most_nobel_winners_by_category_perc.values)

# plt.figure(figsize=(10, 8))
# plt.pie(
#     sizes,
#     labels=labels,
#     autopct='%1.1f%%',
#     counterclock=False,
#     startangle=45,
#     pctdistance=0.85,
#     textprops={'fontsize': 12}
# )

# plt.axis('equal')
# plt.title('Nobel Prize Winners by Category (first 30 years)', pad=20, fontsize=20)

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Category in the first 30 years.png', dpi=300, bbox_inches='tight')

# plt.show()

" matplotlib horizontal bar chart:"

"   8) nobel winners by birth country (All) (sorted)"

# nobel_clean = nobel.dropna(subset=['birth_country'])
# nobel_winners_by_country=nobel_clean.groupby('birth_country')['year'].count()
# nobel_winners_by_country_perc=((nobel_winners_by_country/len(nobel_clean))*100).sort_values().round(1)
# most_nobel_winners_by_country_perc=nobel_winners_by_country_perc[nobel_winners_by_country_perc>1.0].sort_values().round(1)
# sum_most_nobel_winners_by_country_perc=most_nobel_winners_by_country_perc.sum()

# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United States of America', 'USA')
# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United Kingdom', 'UK')

# countries = most_nobel_winners_by_country_perc.index.tolist()
# percentages = most_nobel_winners_by_country_perc.values.tolist()

# plt.figure(figsize=(10, 6))
# bars = plt.barh(countries, percentages, color='#A31A00')

# for bar in bars:
#     width = bar.get_width()
#     plt.text(width + 0.5,  
#              bar.get_y() + bar.get_height()/2,  # y-position (center of bar)
#              f'{width}%', 
#              va='center',
#              fontsize=11)

# plt.xlabel('Percentage of Nobel Prize Winners')
# plt.title('Nobel Prize Winners by Birth Country')
# plt.xlim(0, max(percentages) * 1.1)  # Add 10% padding
# plt.grid(axis='x', linestyle='--', alpha=0.5)
# plt.tight_layout()

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Birth Country (bar).png', dpi=300, bbox_inches='tight')

# plt.show()


"   9) nobel winners by category (All) (sorted)"

# nobel_clean = nobel.dropna(subset=['birth_country'])
# nobel_winners_by_category=nobel_clean.groupby('category')['year'].count()
# nobel_winners_by_category_perc=((nobel_winners_by_category/len(nobel_clean))*100).sort_values().round(1)

# categories = nobel_winners_by_category_perc.index.tolist()
# percentages = nobel_winners_by_category_perc.values.tolist()

# plt.figure(figsize=(10, 6))
# bars = plt.barh(categories, percentages, color='#D57628')

# for bar in bars:
#     width = bar.get_width()
#     plt.text(width + 0.5,  
#              bar.get_y() + bar.get_height()/2,  # y-position (center of bar)
#              f'{width}%', 
#              va='center',
#              fontsize=11)

# plt.xlabel('Percentage of Nobel Prize Winners')
# plt.title('Nobel Prize Winners by Category')
# plt.xlim(0, max(percentages) * 1.1)  # Add 10% padding
# plt.grid(axis='x', linestyle='--', alpha=0.5)
# plt.tight_layout()

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Category (bar).png', dpi=300, bbox_inches='tight')

# plt.show()

"   10) Amount of Physics winners by birth country"

# nobel_clean = nobel.dropna(subset=['birth_country'])
# nobel_physics = nobel_clean[nobel_clean['category']=='Physics']
# nobel_winners_by_country = nobel_physics.groupby('birth_country')['year'].count()
# nobel_winners_by_country_perc=((nobel_winners_by_country/len(nobel_physics))*100).sort_values().round(1)
# most_nobel_winners_by_country_perc=nobel_winners_by_country_perc[nobel_winners_by_country_perc>1.0].sort_values().round(1)

# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United States of America', 'USA')
# most_nobel_winners_by_country_perc.index = most_nobel_winners_by_country_perc.index.str.replace('United Kingdom', 'UK')

# countries = most_nobel_winners_by_country_perc.index.tolist()
# percentages = most_nobel_winners_by_country_perc.values.tolist()

# plt.figure(figsize=(10, 6))
# bars = plt.barh(countries, percentages, color='#8BCB24')

# for bar in bars:
#     width = bar.get_width()
#     plt.text(width + 0.5,  
#              bar.get_y() + bar.get_height()/2,  # y-position (center of bar)
#              f'{width}%', 
#              va='center',
#              fontsize=11)

# plt.xlabel('Percentage of Nobel Prize Winners in Physics')
# plt.title('Nobel Prize Winners in Physics by Birth Country')
# plt.xlim(0, max(percentages) * 1.1)  # Add 10% padding
# plt.grid(axis='x', linestyle='--', alpha=0.5)
# plt.tight_layout()

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners in Physics by Birth Country (bar).png', dpi=300, bbox_inches='tight')

# plt.show()

" 11) matplotlib stacked bar chart: % of female and male winners per category overall"

# nobel_clean = nobel.dropna(subset=['sex', 'category'])
# gender_by_category = (nobel_clean.groupby(['category', 'sex'])['year'].count().unstack())
# gender_pct = (gender_by_category.div(gender_by_category.sum(axis=1), axis=0) * 100).round(1)

# gender_by_category = gender_by_category.loc[gender_by_category.sum(axis=1).sort_values(ascending=True).index]

# plt.figure(figsize=(12, 6))

# x = np.arange(len(gender_by_category))  # This was missing in your original code

# bar_width = 0.35


# male_bars = plt.bar(
#     x + bar_width/2, 
#     gender_pct['Male'], 
#     width=bar_width,
#     label='Male',
#     color='#2659B8',
#     edgecolor='black'
# )

# female_bars = plt.bar(
#     x - bar_width/2, 
#     gender_pct['Female'], 
#     width=bar_width,
#     label='Female',
#     color='#B83C26',
#     edgecolor='black'
# )

# # Customize the chart
# plt.title('Nobel Prize Winners by Category and Gender', pad=10, fontsize = 18)
# plt.ylabel('Percentage of Winners', fontsize=18)
# plt.xticks(x, gender_pct.index, ha='center', fontsize=16)
# plt.legend()

# # Add value labels on top of bars
# def add_labels(bars):
#     for bar in bars:
#         height = bar.get_height()
#         plt.text(
#             bar.get_x() + bar.get_width()/2., 
#             height,
#             f'{height}%',
#             ha='center', 
#             va='bottom',
#             fontsize=10,
#         )

# add_labels(male_bars)
# add_labels(female_bars)

# plt.grid(axis='y', linestyle='--', alpha=0.3)
# plt.tight_layout()

# plt.savefig('C:/Users/Juan!/Desktop/Juan/Git/Nobel Prize Winners by Category and Gender.png', dpi=300, bbox_inches='tight')

# plt.show()

