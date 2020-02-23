
import re 

def getMatches(string):
    # this regex will match a specific text in the entire, 
    # and return the result as an array of all substrings that matches
    re_pattern = r'hackerrank'
    match  = re.findall(re_pattern, string)
    print("Number of matches: " + str(len(match)))

text = "The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on the planet. We rank programmers based on their coding skills, helping companies source great programmers and reduce the time to hire. As a result, we are revolutionizing the way companies discover and evaluate talented engineers. The hackerrank platform is the destination for the best engineers to hone their skills and companies to find top engineers."
getMatches(text)