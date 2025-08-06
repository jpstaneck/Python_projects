# -*- coding: utf-8 -*-

#   Exploring NYC Public School Test Results Scores

#   TASK 2) What are the top 10 performing schools based on the combined SAT scores?
#           - Save your results as a pandas DataFrame called top_10_schools containing the "school_name" and a new column named "total_SAT", 
#           with results ordered by "total_SAT" in descending order ("total_SAT" being the sum of math, reading, and writing scores).

import pandas as pd
schools = pd.read_csv('C:/Users/Juan!/Desktop/Juan/Git/schools.csv') # Import .csv to DataFrame

# Preview the data
print(schools.head())

schools["total_SAT"]=(schools["average_math"]+schools["average_reading"]+schools["average_writing"])
top_10_schools=schools[['school_name', 'total_SAT']].sort_values("total_SAT", ascending=False).iloc[:10]
print(top_10_schools) # Preview the resulting DataFrame

top_10_schools=top_10_schools.to_csv("C:/Users/Juan!/Desktop/Juan/Git/top_10_schools.csv", index=False) # Export Dataframe to .csv
