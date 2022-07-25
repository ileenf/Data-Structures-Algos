class Solution:
    # N = length of flowerbed
    # time complexity: O(N), scan through flowerbed once
    # space complexity: O(1), only storing ints, and indexing is constant
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num_placed = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                num_placed += 1
                flowerbed[i] = 1
                
        return num_placed >= n
