
# Time: O(N) | Space: O(1)
def peakIndexInMountainArrayIndexInMountainArray(A):
    """
    :type A: List[int]
    :rtype: int
    """
    maxPeakHeight = 0
    maxPeakIndex = 0

    for i in range(len(A)):
        largerThanLeft = True
        largerThanRight = True

        if i-1 >= 0 and A[i] <= A[i-1]:
            largerThanLeft = False
        if i+1 < len(A) and A[i] <= A[i+1]:
            largerThanRight = False

        if largerThanLeft and largerThanRight:
            maxPeakHeight = A[i]
            maxPeakIndex = i

    return maxPeakIndex


print(peakIndexInMountainArrayIndexInMountainArray([0,10]))
