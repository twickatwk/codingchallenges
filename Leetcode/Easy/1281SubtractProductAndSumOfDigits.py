
# Time: O(N) | Space: O(1)
def subtractProductAndSum(n):

    productTotal = 1
    sumTotal = 0

    for num in str(n):
        productTotal *= int(num)
        sumTotal += int(num)

    return productTotal - sumTotal

print(subtractProductAndSum(234))
