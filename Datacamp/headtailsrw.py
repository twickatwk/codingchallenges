# this code simulates a random walk of head or tails

import numpy as np

np.random.seed(123)

tails = [0]

# perform coin flip simulation 10 times
for x in range(10):
    coin = np.random.randint(0,2)
    # this adds a tail to the total number of tails from the previous value in the list
    tails.append(tails[x] + coin)

print(tails)