import pandas as pd
# this file is an example, you cannot run it successfully

# Sample Data
# TODO: build out the dataframe for each of these separately
# bronze France           475.0
#        Germany          454.0
#        Soviet Union     584.0
#        United Kingdom   505.0
#        United States   1052.0
# gold   Germany          407.0
#        Italy            460.0
#        Soviet Union     838.0
#        United Kingdom   498.0
#        United States   2088.0
# silver France           461.0
#        Italy            394.0
#        Soviet Union     627.0
#        United Kingdom   591.0
#        United States   1195.0

# dictionaries of repsective datasets
bronze = { 'France': [475], 'Germany': [454], 'Soviet Union': [584], 'United Kingdom': [505], 'United States': [1052] }
silver = { 'Germany': [407], 'Italy': [460], 'Soviet Union': [838], 'United Kingdom': [498], 'United States': [2068] }
gold = {'France' : [461], 'Italy': [394], 'Soviet Union': [627], 'United Kingdom': [591], 'United States': [1195]}

# converting dictionrires into dataframes, with the countries as the row indexes
bronze_df = pd.DataFrame.from_dict(bronze, orient='index')
silver_df = pd.DataFrame.from_dict(silver, orient='index')
gold_df = pd.DataFrame.from_dict(gold, orient='index')

print(bronze_df)
# concatenate the respective bronze, silver, and gold df together
medals = pd.concat([bronze_df, silver_df, gold_df], keys=['Bronze', 'Silver', 'Gold'])

print(medals)

# sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)

# print the number of Bronze medals won by Germany
print(medals_sorted.loc[('Bronze','Germany')])

# print data about silver medals
print(medals_sorted.loc['Silver'])

# create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:, 'United Kingdom'],:])