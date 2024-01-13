import pandas as pd

''' Extraction '''
# Get file from .csv file
file_path = 'characters.csv'
df = pd.read_csv(file_path)

# Print the original data
print('\nOriginal data from "' + file_path + '":')
print(df)

''' Transformation '''
# Conversion from meters to inches
df['Height (in inches)'] = df['Height'] * 39.37
print('\nShow the new column of height in inches:')
print(df)

# Filter characters older than 30 years
df_over_30 = df[df['Age'] > 30]
print('\nShow characters older than 30 years:')
print(df_over_30)

''' Load '''
# Save the changes on a .csv
output_height_in_inches = 'characters-height-in-inches.csv'
df.to_csv(output_height_in_inches)

# Save the changes but ignoring the index column because there are less
# elements that the original .csv file
output_over_30 = 'characters-over-30.csv'
df_over_30.to_csv(output_over_30, index=False)
