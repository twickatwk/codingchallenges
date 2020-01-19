
# Average Case: O(N^2) | Space: O(N)
# Worst Case: O(N^3) | Space: O(N)
def fourNumberSum(A, targetSum):
    # Write your code here.

    # Use a similar technique as the 2 sum problem, except you group two values as a single number

    result = []
    dictSums = {}

    for i in range(len(A)-1):
        # Inner loop 1 generates the pairs for the current element (i), however, you do not add the currentpair sum into the hash table
        for j in range(i+1, len(A)):
            num1 = A[i]
            num2 = A[j]
            pairSum = num1 + num2
            residualSum = targetSum - pairSum
            if residualSum in dictSums:
                residualPairs = dictSums[residualSum]
                for pair in residualPairs:
                    result.append([num1, num2, pair[0], pair[1]])
        
        # Inner loop 2 stores the pairs before the current element (i) to prevent duplicates, 
        # and this will be used by the first inner loop to check for residual sum
        for j in range(0,i):
            num1 = A[i]
            num2 = A[j]
            pairSum = num1 + num2
            if pairSum in dictSums:
                dictSums[pairSum].append([num1, num2])
            else:
                dictSums[pairSum] = [[num1, num2]]

    return result

