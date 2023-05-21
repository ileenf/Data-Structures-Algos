class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_idx = dict()

        for idx, num in enumerate(nums):
            if num in num_to_idx:
                prev_idx = num_to_idx[num]

                # check if latest seen duplicate is within k of curr index
                if idx - prev_idx <= k:
                    return True
                    
            # keep track of latest index seen for a given num
            num_to_idx[num] = idx

        return False
