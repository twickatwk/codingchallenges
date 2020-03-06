
# Time: O(NM) | Space: O(1)
def findTheMinimumWinter(A):

    maxTemperature = None

    for i in range(len(A)):
        if maxTemperature is None:
            maxTemperature = A[i]
        if A[i] > maxTemperature:
            maxTemperature = A[i]
        print("Current Temperature: " + str(A[i]))
        for j in range(len(A)-1, i, -1):
            print("Comparing Temperature: " + str(A[j]))
            if A[j] < maxTemperature:
                print("Temp: " + str(A[j]) + "---MaxTemp: " + str(maxTemperature))
                break
            if j == i+1:
                return i+1

print(findTheMinimumWinter([5, -2, 3, 8, 6]))
print(findTheMinimumWinter([-5,-5,-5,-42, 6]))

