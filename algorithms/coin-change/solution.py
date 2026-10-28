class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda p: p[1])
        arrows = 1
        last = points[0][1]
        for start, end in points:
            if start > last:
                arrows += 1
                last = end
        return arrows
        