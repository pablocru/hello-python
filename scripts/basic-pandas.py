# Import Pandas library after installed it running "pip install pandas"
from pandas import DataFrame

# Create a DataFrame: 2 dimension and tagged data structure from Pandas.
data = {
  'Name': ['Pablo', 'Daniel'],
  'Age': [27, 21]
}

# Print the DataFrame as a table
df = DataFrame(data)
print(df)
