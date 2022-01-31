class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def divide(nums, begin, end):
            if end == begin:
                return nums[end]
            mid = (begin+end)//2
            
            left = divide(nums, begin, mid)
            right = divide(nums, mid+1, end)
            
            if left == right:
                return left
            if nums[begin:mid+1].count(left) > nums[mid+1:end+1].count(right):
                return left
            else:
                return right
            
        return divide(nums, 0, len(nums)-1)
            
