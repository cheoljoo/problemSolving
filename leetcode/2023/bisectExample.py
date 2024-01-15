from bisect import bisect_left, bisect_right

nums = [2, 3, 5, 5, 5, 5, 5, 5, 5, 6, 100]

print("len(nums):",len(nums))

n = 4 
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n),'len(nums)',len(nums)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n),'len(nums)',len(nums)) 

n = 5 
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n),'len(nums)',len(nums)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n),'len(nums)',len(nums)) 

n = 1 
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n),'len(nums)',len(nums)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n),'len(nums)',len(nums)) 

n = 6
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n),'len(nums)',len(nums)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n),'len(nums)',len(nums)) 

n = 81
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n),'len(nums)',len(nums)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n),'len(nums)',len(nums)) 

n = 181
print("nums:",nums,"n:",n,"bisect_left:",bisect_left(nums, n),'len(nums)',len(nums)) 
print("nums:",nums,"n:",n,"bisect_right:",bisect_right(nums, n),'len(nums)',len(nums)) 
