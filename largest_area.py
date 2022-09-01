"""
Container with most water.

Each point is 1 space apart with variable heights.
The goal is to find the maximum area that can be filled with water.

https://leetcode.com/problems/container-with-most-water/
"""
points = [ [1,1], [2,8], [3,6], [4,2], [5,5], [6,4], [7,8], [8,3], [9,7] ]

biggest = 0
biggest_set = []

for index, i in enumerate(points):
    for k in range(index, len(points)):

        length = abs( points[k][0] - i[0] ) # length between the 2 points, absolute value (no negatives)
        height = min(i[1], points[k][1]) # tallest between the 2 points
        area = length * height

        if area > biggest:
            biggest = area
            biggest_set = [i, points[k]]
        print(biggest)
        print(biggest_set)