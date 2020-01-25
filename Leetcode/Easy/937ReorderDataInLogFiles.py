
def reorderLogFiles(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """

    digitLogs = []
    letterLogs = []

    for log in logs:
        log = log.split(" ")
        firstWord = log[1]
        try:
            # if doesn't raise an error, it means that it is a digit log
            int(firstWord)
            digitLogs.append(" ".join(log))
        except ValueError:
            # if this error occurs, this means that it is a letter log
            
            array = log[1:]
            string = " ".join(array) + " " + log[0]
            letterLogs.append(string)
            
    letterLogs.sort()

    for i, log in enumerate(letterLogs):
        array = log.split(" ")
        string = array[-1] + " " + " ".join(array[0:-1])
        letterLogs[i] = string
        
    return letterLogs + digitLogs
