class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        search_for = mat[0]
        to_search = mat[1:]
        
        n = len(mat)
        
        def bin_search(vals, val):
            left = 0
            right = len(vals)-1
            
            while left <= right:
                mid = (left + right) // 2
                
                if vals[mid] == val:
                    return True
                
                elif vals[mid] < val:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        for num in search_for:
            for row in to_search:
                if not bin_search(row, num):
                    break
            else:
                return num
        return -1
