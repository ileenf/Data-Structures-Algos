class Solution:
    def getMaxInterval(self, arr, length):
        if not arr:
            return length
        max_size = -1
        
        for i in range(len(arr)-1):
            max_size = max(max_size, arr[i+1] - arr[i])
        return max_size
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        hCut = [0] + horizontalCuts + [h]
        vCut = [0] + verticalCuts + [w]
        
        maxH = self.getMaxInterval(hCut, h)
        maxV = self.getMaxInterval(vCut, w)
        
        return (maxH * maxV) % (10**9 + 7)
