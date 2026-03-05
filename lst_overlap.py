#!/usr/bin/env python3

lstA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lstB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
aSet = set(lstA)
bSet = set(lstB)
common = aSet.intersection(bSet)
print(common)
