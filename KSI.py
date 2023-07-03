import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('KSI .csv')


# Identify the rows with missing values in the "ACCNUM" column
missing_accnum = data['ACCNUM'].isnull()

# Group the rows by their common values in the "LONGITUDE," "LATITUDE," and "YEAR" columns
grouped = data.groupby(['LONGITUDE', 'LATITUDE', 'YEAR'])

# Assign unique numbers to each group of rows with the same common values
unique_numbers = grouped.ngroup() + 1

# Replace the missing values in the "ACCNUM" column with the generated unique numbers
data.loc[missing_accnum, 'ACCNUM'] = unique_numbers[missing_accnum]


data['Street_intersection']  = data['STREET1'].str.cat(data['STREET2'], sep=' & ', na_rep='')



top_10 = data[data['YEAR'] == '2022']['Street_intersection'].value_counts().nlargest(10)