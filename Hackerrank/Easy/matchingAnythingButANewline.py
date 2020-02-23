
# write a method that gets a string in the form of abc.def.ghi.jkx
# where abcdefghijkx can be any single character except the newline

import re

def getMatch(string):

    re_pattern = r'...\....\....\....'

    match = re.match(re_pattern, string)

    print(match is not None)

text = "123.456.abc.def"
text2 = "1123.456.abc.def"
getMatch(text)

