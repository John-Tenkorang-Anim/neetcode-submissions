"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i: i.start)

        prev_end = float('-inf')
        for it in intervals:
            if prev_end <= it.start:
                prev_end = it.end
            else:
                return False

        return True

