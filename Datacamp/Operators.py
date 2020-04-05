########################################################################################

# Example: Logical Operators: Numpys - logical_or/and/not
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house<10, my_house>18.5))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11, your_house<11))

########################################################################################

# Example: Logical Operators: DataFrame

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# 1 - select column from DataFrame, 2 - filter series using np logical operators, 3 - subsetting in DF
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)