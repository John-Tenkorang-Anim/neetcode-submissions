"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        events = []

        for it in intervals:
            events.append((it.start, 1))
            events.append((it.end, -1))
        
        events.sort()

        active = 0
        max_rooms = 0

        for time , change in events:
            active += change
            max_rooms = max(max_rooms, active)
            
        return max_rooms



        