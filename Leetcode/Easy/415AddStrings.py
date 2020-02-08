
# Time: O(N) | Space: O(N)
def addStrings(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    
    carry = 0
    result = []

    # add the two characters from the both string at the same index, carry forward "1" 
    # if their sum is more than 10
    for i in range(len(num1)):
        total = int(num1[i]) + int(num2[i]) + carry
        if total >= 10:
            carry = 1
            result.append(str(total)[1])
        else:
            carry = 0
            result.append(str(total))
    
    
    # add any additional remaining characters from the longer string into the result
    for i in range(len(num1), len(num2)):
        total = int(num2[i]) + carry
        if total >= 10:
            carry = 1
            result.append(str(total)[1])
        else:
            carry = 0
            result.append(str(total))
    
    # if there is left over carry, you need to include it in front from the result as well
    if carry == 1:
        result.append("1")
    
    result.reverse()
    
    return "".join(result)