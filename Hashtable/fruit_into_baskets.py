class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 1
        
        # keep track of amount of fruit for each type
        curr_fruits = defaultdict(int)
        curr_fruits[fruits[i]] += 1
        max_fruits = 1

        while i < j and j < len(fruits):
            curr_fruits[fruits[j]] += 1

            if len(curr_fruits) <= 2:
                max_fruits = max(max_fruits, j-i+1)

            else:
                curr_fruits[fruits[i]] -= 1

                if curr_fruits[fruits[i]] == 0:
                    del curr_fruits[fruits[i]]
                i += 1
            # move right pointer always because sliding window is only non decreasing
            j += 1

                
        return max_fruits
