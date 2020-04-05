
# this code shows an example of building a distribution of coin toss simulation

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

final_tails = []

# 100 games
for i in range(100):
    tails = [0]
    # if 10 coin tosses
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])

plt.hist(final_tails, bins=10)
plt.show()