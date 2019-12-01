# https://www.interviewcake.com/question/python/merging-ranges?course=fc1&section=array-and-string-manipulation

"""
Your company built an in-house calendar tool called HiCal. 
You want to add a feature to see the times in a day when everyone is available.
Given for a range of timings as list of tuples.

Example:
Input:   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
Output:   [(0, 1), (3, 8), (9, 12)]
"""

import unittest

# Time: O(n) | Space: O(n)
# Time - You make exactly one run through the list of meeting timings
# Space - You use an additional new list to store all the newly merged intervals as result

def merge_ranges(meetings):

    # Merge meeting ranges

    # Sort the meeting timings by their starting timing
    meetings.sort(key = lambda x : x[0])
    new_merged_interval = None
    new_intervals = []
    
    for i in range(len(meetings)):
        current_interval = meetings[i]

        # Simply add the current interval or new merged interval into the result once you have reached the end of the list
        if i == len(meetings) - 1:
            if new_merged_interval is not None:
                new_intervals.append(new_merged_interval)
            else:
                new_intervals.append(current_interval)
            break
        
        # If there is no new merged interval, check whether if the current timing and the next interval can be merged
        if new_merged_interval is None:
            if meetings[i+1][0] <= current_interval[1]:
                new_merged_interval = (current_interval[0], max(meetings[i+1][1], current_interval[1]))
            else:
                new_intervals.append(current_interval)
            
            continue
        
        # If there is already a new merged interval, simply use that to compare to the next interval instead
        if new_merged_interval is not None:
            if meetings[i+1][0] <= new_merged_interval[1]:
                new_merged_interval = (new_merged_interval[0], max(meetings[i+1][1], new_merged_interval[1]))
            else:
                new_intervals.append(new_merged_interval)
                new_merged_interval = None
            
            continue
    
    return new_intervals




# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)