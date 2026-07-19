"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        length = len(intervals)
        count = 0
        max_count = 0
        s,e = 0,0
        while s<length and e<length:
            if start[s]<end[e]:
                count+=1
                s+=1
                max_count = max(max_count, count)
            else:
                count -=1
                e+=1
            
        return max_count

        




        