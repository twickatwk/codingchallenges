
# Luck Balance - Hackerrank
# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

# Time: O(n) | Space: O(n)
def luckBalance(k, contests):

    luck_points = 0
    losses = 0
    deduction = 0
    stack = []
    for contest in contests:
        if contest[1] == 0:
            luck_points += contest[0]
        else:
            if k == 0:
                deduction += contest[0]
                continue
            if losses < k:
                stack.append(contest[0])
                stack.sort(reverse=True)
                losses += 1
            else:
                if contest[0] > stack[-1]:
                    deduction += stack.pop()
                    stack.append(contest[0])
                    stack.sort(reverse=True)
                else:
                    deduction += contest[0]
                    continue

    luck_points += sum(stack)
    luck_points -= deduction
    return luck_points