
#https://www.hackerrank.com/challenges/countingsort2/problem

# Write a function that sorts the list using the counting method
# Time: O(n) | Space: O(1)
def countingSort(arr):
    count_arr = [0] * 100
    for i in range(len(arr)):
        count_arr[arr[i]] += 1
    
    sorted_result = []
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            sorted_result.append(i)
    
    return sorted_result

print(countingSort([4,2,1]))