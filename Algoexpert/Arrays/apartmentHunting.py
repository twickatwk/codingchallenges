
# Time: O(N^3) | Space: O(1) | This solution is not optimal
def apartmentHunting(blocks, reqs):
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