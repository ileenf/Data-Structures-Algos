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
                    left = mid + 2
                else:
                    right = mid - 1
            
            # if odd idx, duplicate should be on left
            else:
                # correct, misalignment on right half
                if nums[mid-1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 2
        return nums[left]
    
    
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # single element at first even idx that doesn't have a duplicate to right
        # after the single element, all duplicate pairs after will be misaligned
        # FFFFTTTT pattern


        left = 0
        right = len(nums) - 1
        
        # binary search only even indexes
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] != nums[mid+1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]
