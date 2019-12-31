# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

# Medium
# Hash Table - a variant of two sum

# Time: O(N) | Space: O(N)
def whatFlavors(cost, money):
    dict_flavours = {}
    for i in range(len(cost)):
        if money - cost[i] not in dict_flavours:
            dict_flavours[cost[i]] = i + 1
        else:
            print(str(dict_flavours[money-cost[i]]) + " " + str((i+1)))

