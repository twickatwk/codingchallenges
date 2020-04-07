
# Summary Statistics Example Code for Walmart Data
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# sales is the DataFrame that is obtained from Walmart Dataset
# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))