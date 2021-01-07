"""
Definition of Interval
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        start = [(i.start, 1) for i in airplanes]
        end = [(i.end, -1) for i in airplanes]
        start_end = start+end
        start_end.sort(key = lambda x:(x[0],x[1]))
        in_sky = 0
        max_in_sky = 0
        for time in start_end:
            in_sky += time[1]
            max_in_sky = max(max_in_sky, in_sky)
        return max_in_sky