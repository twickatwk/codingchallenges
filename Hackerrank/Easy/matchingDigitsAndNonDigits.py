
# write a method that matches digits and non digits
# xxXxxXxxxx
# where x denotes digit from 0-9 and X denotes non-digits

import re

def getMatch(string):

    re_pattern = r'\d\d\D\d\d\D\d\d\d\d'

    # re.search returns a Match object
    match = re.search(re_pattern, string)

    print(match)
    print(match.string)
    print(bool(match))

text = "06-11-2016"

getMatch(text)