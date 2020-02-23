
# \s matches any whitespace character [ \r\n\t\f ]
# \S matches any non-whitespace character

import re
def getMatch(string):

    re_pattern = r"\S\S\s\S\S\s\S\S"

    match = re.search(re_pattern, string)

    print(bool(match))

text = "12 11 15"
getMatch(text)

