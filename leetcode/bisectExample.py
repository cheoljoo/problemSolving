from bisect import bisect_left, bisect_right

nums = [2, 3, 5, 5, 5, 5, 5, 5, 5, 6]

print("len(nums):",len(nums))

n = 4 
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n)) 

n = 5 
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n)) 

n = 1 
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n)) 

n = 17
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n)) 