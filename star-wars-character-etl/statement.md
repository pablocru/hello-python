# Star wars ETL statement

## Extraction

- Create a Python script named `etl_star_wars.py`.
- Use Pandas to load the data from the CSV file `characters.csv` into a
  DataFrame.

## Transformation

- Add a new column named "Height (in inches)" that converts height from meters
  to inches (1 meter = 39.37 inches).
- Filter the DataFrame to display only characters older than 30 years.

## Load

- Save the transformed DataFrame to a new CSV file named
  `characters-transformed.csv`.
