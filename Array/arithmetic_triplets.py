class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplets = 0
        
        hashset = set()
        
        for num in nums:
            if num - diff in hashset and num - diff - diff in hashset:
                triplets += 1
            hashset.add(num)
        return triplets
