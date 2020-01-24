
# Approach 2: Uses pre-computed data of the distances for each requirement for each block
# Time: O(BR) | Space: O(BR)
def apartmentHunting(blocks, reqs):
    # Write your code here.
	
    apartmentIndex = None
    minDistance = float("inf")

    distances = {}

    # Generate the dictionary to keep track of the distances for each requirement
    for req in reqs:
        distances[req] = [None] * len(blocks)

    for req in reqs:
        # left to right
        for i in range(len(blocks)):
            if blocks[i][req]:
                distances[req][i] = 0
                continue
            # if its the first house, there are no other houses to the left
            if i == 0:
                continue
            if distances[req][i-1] is not None:
                distances[req][i] = distances[req][i-1] + 1
        # right to left
        
        index = len(blocks)-1
        for i in range(index, -1, -1):
            if blocks[i][req]:
                distances[req][i] = 0
                continue
                # if its the last house, there is no houses to the right of it
            if i == len(blocks) - 1:
                continue
            
            if distances[req][i+1] is not None:
                if distances[req][i] is None:
                    distances[req][i] = distances[req][i+1]+1
                else:
                    distances[req][i] = min(distances[req][i], distances[req][i+1]+1)

    for i in range(len(blocks)):
        localMaxDistance = float("-inf")
        for req in reqs:
            if distances[req][i] > localMaxDistance:
                localMaxDistance = distances[req][i]
        if localMaxDistance < minDistance:
            minDistance = localMaxDistance
            apartmentIndex = i

    return apartmentIndex




# Approach 1: For each block, for each requirement, search through all the other blocks, to determine the nearest requirement
# Time: O(B^2R) or O(N^3) | Space: O(1) | This solution is not optimal
def apartmentHunting2(blocks, reqs):
    # Write your code here.
	
    apartmentIndex = None
    minDistance = float("inf")


    for i in range(len(blocks)):
        apartment = blocks[i]
        distances = dict.fromkeys(reqs, None)
        for req in reqs:
            if apartment[req]:
                distances[req] = 0
                continue
            # check apartments to the left
            pos = i
            dist = 0
            while (pos-1 >= 0):
                dist += 1
                pos -= 1
                nextApartment = blocks[pos]
                if nextApartment[req]:
                    distances[req] = dist
                    break
            pos = i
            dist = 0
            
            while (pos + 1 < len(blocks)):
                dist += 1
                pos += 1
                nextApartment = blocks[pos]
                if nextApartment[req]:
                    if distances[req] is None:
                        distances[req] = dist
                    else:
                        distances[req] = min(dist, distances[req])
            
        if None in distances.values():
            continue

        if max(distances.values()) < minDistance:
            minDistance = max(distances.values())
            apartmentIndex = i
        
    return apartmentIndex

blocks = [
    {
    "gym": False,
    "school": True,
    "store": False,
    },
    {
    "gym": True,
    "school": False,
    "store": False,
    },
    {
    "gym": True,
    "school": True,
    "store": False,
    },
    {
    "gym": False,
    "school": True,
    "store": False,
    },
    {
    "gym": False,
    "school": True,
    "store": True,
    },
]
reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks, reqs))