class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def formula(a, b, c, x):
            return a*(x**2) + b*x + c
        
        if a == 0:
            nums = [formula(a, b, c, n) for n in nums]
            if b > 0:
                return nums
            else:
                return nums[::-1]
              
        transformed = []  
        i = 0
        j = len(nums)-1
        vertex = -(b/(2*a))
        
        while i <= j:
            dist_i = abs(vertex-nums[i])
            dist_j = abs(vertex-nums[j])
            
            if dist_i >= dist_j:
                transformed.append(formula(a, b, c, nums[i]))
                i += 1
                
            else:
                transformed.append(formula(a, b, c, nums[j]))
                j -= 1
                
        if a > 0:
            return transformed[::-1]
        
        return transformed
