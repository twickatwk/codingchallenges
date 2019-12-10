# Time: O(n) | Space: O(n)
def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        difference = ord('a') - ord('A')
        print(difference)
        result = []
        #O(n)
        for char in str:
            if ord(char) > 90 or ord(char) < 65:
                # O(1)
                result.append(char)
            else:
                result.append(chr(ord(char)+difference))
        # O(n)
        return "".join(result)

# Time: O(n^2) | Space: O(n)
def toLowerCase2(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        difference = ord('a') - ord('A')
        print(difference)
        result = ""
        #O(n)
        for char in str:
            if ord(char) > 90 or ord(char) < 65:
                # O(n)
                result += char
            else:
                result += chr(ord(char)+difference)
        
        return result