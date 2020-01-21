
# Time: O(N) | Space: O(N)
def minRewards(scores):
	
	if len(scores) == 1:
		return 1
	
	rewards = [0] * len(scores)
	
	for i in range(len(scores)):
		# left & right scores exists
		if i-1 >= 0 and i+1<len(scores):
			# this means that this point is a local min
			if scores[i] < scores[i-1] and scores[i] < scores[i+1]:
                # from the local min, you have to start giving rewards to the left and right students
				rewardLeft(i, scores, rewards)
				rewardRight(i, scores, rewards)
		# only right scores exists
		elif i-1 < 0 and i+1 < len(scores):
			if scores[i] < scores[i+1]:
				rewardLeft(i, scores, rewards)
				rewardRight(i, scores, rewards)
		# only left scores exists
		elif i+1 >= len(scores) and i-1 >= 0:
			if scores[i] < scores[i-1]:
				rewardLeft(i, scores, rewards)
				rewardRight(i, scores, rewards)
	
	return sum(rewards)
	
def rewardLeft(i, scores, rewards):
	
	currentScore = scores[i]
	rewards[i] = 1
	while i > 0:
        # if the score to the left is larger, you will need to give it 1 score higher than your current reward
		if scores[i-1] > scores[i]:
			rewardToGive = rewards[i] + 1
            # but if the current score of your neighbour is already higher, you just keep their score, otherwise replace it
			if rewardToGive > rewards[i-1]:
				rewards[i-1] = rewardToGive
			i -= 1
		else:
			break

def rewardRight(i, scores, rewards):
	
	currentScore = scores[i]
	rewards[i] = 1
	while i < len(scores)-1:
        # if the score to the left is larger, you will need to give it 1 score higher than your current reward
		if scores[i+1] > scores[i]:
			rewardToGive = rewards[i] + 1
            # but if the current score of your neighbour is already higher, you just keep their score, otherwise replace it
			if rewardToGive > rewards[i+1]:
				rewards[i+1] = rewardToGive
			i += 1
		else:
			break


# Expected: 25 [4,3,2,1,2,3,4,5,1]
print(minRewards([8,4,2,1,3,6,7,9,5]))