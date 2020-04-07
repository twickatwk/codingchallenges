
# Summary Statistics Example Code for Walmart Data
import numpy as np
import pandas as pd

sales = pd.read_csv('./datasets/walmart_ds.csv')

def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# sales is the DataFrame that is obtained from Walmart Dataset
# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales.head())
print()
print("########################Summary Statistics########################################")
print(sales[["Temperature", "Fuel_Price", "Unemployment"]].agg([iqr, np.median]))