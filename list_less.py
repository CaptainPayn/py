#!/usr/bin/env python3

lessList = []
origList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in origList:
    if item < 5:
        lessList.append(item)
print(lessList)
