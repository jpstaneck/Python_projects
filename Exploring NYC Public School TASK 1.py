# -*- coding: utf-8 -*-
#
#   Exploring NYC Public School Test Results Scores

#   TASK 1) Which NYC schools have the best math results?
#           - The best math results are at least 80% of the *maximum possible score of 800* for math.
#           - Save your results in a pandas DataFrame called best_math_schools, including "school_name" and "average_math" columns, 
#           sorted by "average_math" in descending order.What are the top 10 performing schools based on the combined SAT scores?

import pandas as pd
schools = pd.read_csv('C:/Users/Juan!/Desktop/Juan/Git/schools.csv') #Import .csv to DataFrame

# Preview the data
print(schools.head())

math_schools=schools[["school_name", "average_math"]]
max_math_score=math_schools["average_math"].max()
best_math_schools=math_schools[math_schools["average_math"]>=(0.8*800)]     # 80% of the maximum possible value 800 
best_math_schools=best_math_schools.sort_values(by="average_math", ascending=False)
print(best_math_schools.school_name.head(10))    # Answer to final question

best_math_schools=best_math_schools.to_csv("C:/Users/Juan!/Desktop/Juan/Git/best_math_schools.csv", index=False)   #Export Dataframe to .csv

