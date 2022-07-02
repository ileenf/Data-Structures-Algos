class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median_val = sorted(nums)[len(nums)//2]
        moves = 0
        
        for num in nums:
            moves += abs(num-median_val)
        return moves
