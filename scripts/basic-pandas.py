# Import Pandas library after installed it running "pip install pandas"
import pandas as pd

# Create a DataFrame: 2 dimension and tagged data structure from Pandas.
data = {
  'Name': ['Pablo', 'Daniel'],
  'Age': [27, 21]
}

# Print the DataFrame as a table
df = pd.DataFrame(data)
print(df)
