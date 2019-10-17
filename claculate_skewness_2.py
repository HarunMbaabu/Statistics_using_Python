# importing pandas as pd 
import pandas as pd 
  
# Creating the dataframe  
df = pd.read_csv("property data.csv") 
print(df)  
# skip the na values 
# find skewness in each row 
skewness = df.skew(axis = 1, skipna = True)
print(skewness)