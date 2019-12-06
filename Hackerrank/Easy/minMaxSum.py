#https://www.hackerrank.com/challenges/mini-max-sum/problem

# Time: O(n) | Space: O(1)
def miniMaxSum(arr):
    min_num = float("inf")
    max_num = float("-inf")
    min_sum = 0
    max_sum = 0
    for i in range(len(arr)-1):
        if arr[i] < min_num:
            min_num = arr[i]
        if arr[i] > max_num:
            max_num = arr[i]
        min_sum += arr[i]
        max_sum += arr[i]

    if arr[-1] > min_num:
        max_sum -= min_num
        max_sum += arr[-1]
    if arr[-1] < max_num:
        min_sum -= max_num
        min_sum += arr[-1]

    print(str(min_sum) + " " + str(max_sum))