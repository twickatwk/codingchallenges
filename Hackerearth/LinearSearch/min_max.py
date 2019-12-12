# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/min-max-8/

# Time: O(N) | Space: O(N)
N = int(input())
arr = list(map(int, input().split()))
highest = float('-inf')
lowest = float('inf')

sum_of_all_ints_before_int = [None] * N

total = 0

for i in range(N):
    sum_of_all_ints_before_int[i] = total
    total += arr[i]

total = 0

for i in range(N-1, -1, -1):
    sum_of_all_ints_before_int[i] += total
    total += arr[i]

for num in sum_of_all_ints_before_int:
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num

print(str(lowest) + " " + str(highest))