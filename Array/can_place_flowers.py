class Solution:
    # N = length of flowerbed
    # time complexity: O(N), scan through flowerbed once
    # space complexity: O(1), only storing bools/ints, and indexing is constant
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = False
        num_placed = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 1:
                placed = True
                continue
            elif not placed and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                num_placed += 1
                placed = True
            else:
                placed = False
                
        return num_placed >= n
