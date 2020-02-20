

# Time: O(N) | Space:O(N)
def groupThePeople(groupSizes):
    """
    :type groupSizes: List[int]
    :rtype: List[List[int]]
    """
    
    # this is the final group sizes with people's id
    groupsWithPeople = []
    
    # this is the groupings of people, group size as the key, 
    # and then array of people's id (array) as the value
    groupings = {}
    
    # step 1: go through every one in the group
    for i in range(len(groupSizes)):
        sizeOfGroup = groupSizes[i]
        if sizeOfGroup in groupings:
            groupings[sizeOfGroup].append(i)
            # once the size of the array matches the key, this means that the current group size have been maxed out, store them away
            if sizeOfGroup == len(groupings[sizeOfGroup]):
                groupsWithPeople.append(groupings[sizeOfGroup])
                groupings[sizeOfGroup] = []
        else:
            groupings[sizeOfGroup] = [i]
            if sizeOfGroup == len(groupings[sizeOfGroup]):
                groupsWithPeople.append(groupings[sizeOfGroup])
                groupings[sizeOfGroup] = []
    
    return groupsWithPeople