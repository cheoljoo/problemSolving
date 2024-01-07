import bisect

nums = [2, 3, 5, 5, 5, 5, 5, 5, 5, 6]

n = 4 
print(bisect.bisect_left(nums, n)) 
print(bisect.bisect_right(nums, n)) 

