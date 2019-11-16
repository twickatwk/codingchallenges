# Time: O(N) | Space: O(1)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

def power2(x, n):
    if n == 0:
        return 1
    if n%2 == 0:
        y = power2(x, n/2)
        return y * y
    else:
        return x * power2(x, n-1)

def test_power():
    assert power(2, 3) == 8, "This should be 8"
    assert power2(2, 4) == 16, "This should be 8"
    print("Output is correct")

test_power()

""" Conceptual Overview: O(N) implementation
power(2, 3)
2 * power(2, 2) - 4 = 8
2 * power(2, 1) - 2 = 4
2 * power(2, 0) - 1 = 2
"""


""" Conceptual Overview: O(Log N) implementation
power2(2, 4)
power2(2, 2) - 4 * power2(2, 2) - 4 = 16
power2(2, 1) - 2 * power2(2, 1) - 2 = 4
2 * power2(2, 0) - 1 = 2 = 2

"""