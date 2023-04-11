class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # if even idx, duplicate should be on right
            if mid % 2 == 0:
                # correct, misalignment on right half
                if mid < len(nums) - 1 and nums[mid+1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # if odd idx, duplicate should be on left
            else:
                # correct, misalignment on right half
                if nums[mid-1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return nums[left]
