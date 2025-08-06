# -*- coding: utf-8 -*-

#   Exploring NYC Public School Test Results Scores

#   TASK 3) Which single borough has the largest standard deviation in the combined SAT score?
#           - Save your results as a pandas DataFrame called largest_std_dev. 
#           - The DataFrame should contain one row, with: 
#                - "borough" - the name of the NYC borough with the largest standard deviation of "total_SAT". 
#                - "num_schools" - the number of schools in the borough. 
#                - "average_SAT" - the mean of "total_SAT". 
#                - "std_SAT" - the standard deviation of "total_SAT".
#           - Round all numeric values to two decimal places.

import pandas as pd
schools = pd.read_csv('C:/Users/Juan!/Desktop/Juan/Git/schools.csv') # Import .csv to DataFrame

# Preview the data
print(schools.head())

schools["total_SAT"]=(schools["average_math"]+schools["average_reading"]+schools["average_writing"])
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

print(largest_std_dev)  # Preview the resulting DataFrame

largest_std_dev=largest_std_dev.to_csv("C:/Users/Juan!/Desktop/Juan/Git/largest_std_dev.csv", index=True) # Export Dataframe to .csv