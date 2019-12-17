def underscorifySubstring(string, substring):
    start_of_search_location = 0
    # Checks whether substring still exists
    index = 0
    listOfPositions = []
    
    # Obtain location of all substring in string, storing their indexes.
    while index != -1:
        index = string.find(substring, start_of_search_location)
        if index == -1:
            break
        listOfPositions.append([index, index+len(substring)])
        # -1 because the substring can begin on the same spot
        start_of_search_location = index+1
    print(listOfPositions)
    
    # Merge indexes that overlap, because underscores are only added to the start and end of the string.
    arr = mergeStrings(listOfPositions)
    print(arr)
    index = 0
    new_string = ""
    # Perform the addition of "_" to the beginning and the end.
    for i in range(len(string)):
        if index >= len(arr):
            new_string += string[i]
            continue
        if arr[index][1] - arr[index][0] > 1:
            if i == arr[index][0]:
                new_string += ("_" + string[i])
                continue
            if i == arr[index][1]-1:
                new_string += (string[i] + "_")
                index += 1
                continue
        else:
            if i == arr[index][0]:
                new_string += "_" + string[i] + "_"
                index += 1
                continue
        
        new_string += string[i]

    return new_string

# Time: O(N) | Space: O(N)
def mergeStrings(arr):

    result = []
    if len(arr) == 0:
        return result
    start = arr[0][0]
    end = arr[0][1]
    
    for i in range(1, len(arr)):
        if arr[i][0] <= end:
            end = arr[i][1]
        else:
            result.append([start, end])
            start = arr[i][0]
            end = arr[i][1]
    
    result.append([start, end])

    return result

print(underscorifySubstring("testthis is a testtest to see if testestest it works", "test"))