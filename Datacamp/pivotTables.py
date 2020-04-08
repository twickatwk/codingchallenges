
# this is an example of using Pivot Tables, aggregating them based on rows / cols, and finding out the min and max mean of each category
import pandas as pd

sales = pd.read_csv('./datasets/walmart_ds.csv')

sales['year'] = pd.DatetimeIndex(sales['Date']).year

temp_by_country_city_vs_year = sales.pivot_table(values='Temperature', index='Store', columns='year')

# Get the worldwide mean temp by year
print("############worldwide mean temp by year############")
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis='index')
print(mean_temp_by_year)

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by Store
print("############Get the mean temp by Store############")
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')
print(mean_temp_by_city)

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])