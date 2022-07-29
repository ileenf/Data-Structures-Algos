class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        idx_to_search = -1
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                idx_to_search = mid
                break
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        
        if idx_to_search == -1:
            return [-1, -1]
        first = idx_to_search
        last = idx_to_search
        
        while first >= 0:
            if nums[first] == target:
                first -=1
            else:
                break
        while last < len(nums):
            if nums[last] == target:
                last +=1
            else:
                break
        return [first+1, last-1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchFirst(nums, target):
            start = 0
            end = len(nums) - 1
    
            while start <= end:
                mid = (start + end) // 2
                
                if nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            
            return start
        
        def searchLast(nums, target):
            start = 0
            end = len(nums) - 1
            
            while start <= end:
                mid = (start + end) // 2
                
                if nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            
            return end
        
        first = searchFirst(nums, target)
        last = searchLast(nums, target)

        
        if first >= 0 and first < len(nums) and first <= last and nums[first] == target:
            return [first, last]
        else:
            return [-1,-1]
