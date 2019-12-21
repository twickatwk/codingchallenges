
# Write a method to replace all spaces in a string with '%20'

# Time: O(N) | Space: O(N)
def urlify(string, length):
    
    string = string[0:13]
    string = string.replace(" ", "%20")

    return string

print(urlify("Mr John Smith    ", 13))