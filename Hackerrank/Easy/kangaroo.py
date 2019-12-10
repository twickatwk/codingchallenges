# https://www.hackerrank.com/challenges/kangaroo/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Time: O(1) |  Space: O(1)
def kangaroo(x1, v1, x2, v2):

    if x1 == x2:
        return "YES"
    if x1 < x2:
        if v1 > v2:
            if (x2 - x1) % (v1 - v2) == 0:
                print(x2 + v2)
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
    else:
        if v2 > v1:
            if (x1 - x2) % (v2 - v1) == 0:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"