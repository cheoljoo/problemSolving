class Solution:
    def trap(self, height: List[int]) -> int:
        # find max (leftIndex , RightIndex of Max)
        mx1 = -1
        for i in range(len(height)):
            if mx1 < height[i]:
                mx1 = height[i]
                leftIndex = i
        for i in reversed(range(len(height))):
            if mx1 == height[i]:
                rightIndex = i
                break
        mx = 0
        sum = 0
        # print(leftIndex,rightIndex)

        # Left
        for i in range(leftIndex):
            if mx < height[i]:
                mx = height[i]
            sum += mx - height[i]
        # print(sum)

        # Max to Max
        for i in range(leftIndex,rightIndex):
            sum += mx1 - height[i]
        # print(sum)
        
        # Right 
        mx = 0
        for i in reversed(range(rightIndex,len(height))):
            if mx < height[i]:
                mx = height[i]
            sum += mx - height[i]
        # print(sum)
        return sum