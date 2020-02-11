
# Time: O(N) | Space: O(N)
def caesarCipher(s, k):

    # A - 65 | Z - 90
    # a - 97 | z - 122

    result = ""
    
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            if ord(char) + (k%26) <= 90:
                result += chr(ord(char)+(k%26))
            else:
                # resolves the loopback from the beginning of the sequence
                newChar = (ord(char)+(k%26)-26)
                result += chr(newChar)
            continue
        if ord(char) >= 97 and ord(char) <= 122:
            if ord(char) + (k%26) <= 122:
                result += chr(ord(char)+(k%26))
            else:
                newChar = (ord(char)+(k%26)-26)
                result += chr(newChar)
            continue
        
        result += char
    
    return result