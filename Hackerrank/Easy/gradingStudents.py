# https://www.hackerrank.com/challenges/grading/problem

# Time: O(n) | Space: O(n)
def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        if grade < 35:
            result.append(grade)
        else:
            ones = str(grade)[1]
            tens = str(grade)[0]
            if int(ones) >= 5 :
                if 10 - int(ones) < 3:
                    result.append(str(int(tens)+1) + "0")
                else:
                    result.append(grade)
            else:
                if 5 - int(ones) < 3:
                    result.append(tens + "5")
                else:
                    result.append(grade)

    return result