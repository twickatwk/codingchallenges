
# Time: O(N) | Space: O(N)
def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        
        strx = list(str(x))
        start = 0
        end = len(strx)-1
        output = ''
        while strx[end] == 0:
            end -= 1
        if strx[start] == '-':
            start = 1
            output = '-'
        if start < end:
            strx = strx[start:end+1]
            strx.reverse()
        
        output = int(output + "".join(strx))
        
        if output < pow(-2, 31) or output > pow(2, 31)-1:
            return 0
        
        return output