# importing pandas as pd 
import pandas as pd 
  
# Creating the dataframe  
df = pd.read_csv("property data.csv") 
  
# Print the dataframe 
print(df) 
# skewness along the index axis 
df.skew(axis = 0, skipna = True) 