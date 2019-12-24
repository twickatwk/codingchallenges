# 1.6 

# Time: O(N) | Space: O(N)
def stringCompression(string):
    index = 0
    count = 1
    result = []
    while index < len(string):
        currentChar = string[index]
        if index == len(string) - 1:
            result.append(currentChar)
            if count > 1:
                result.append(str(count))
            break
        if currentChar == string[index+1]:
            count +=1
        else:
            result.append(currentChar)
            if count > 1:
                result.append(str(count))
            count = 1
        
        index += 1

    result_string = "".join(result)

    print(result_string)

stringCompression("aaabbc")
# Expected Output: a3b2c
stringCompression("abc")
# Expected Output: abc
stringCompression("abbaac")
# Expected Output: ab2a2c
