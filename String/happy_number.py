class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        seen = set()

        while num != '1':
            if num in seen:
                return False
            
            seen.add(num)
            
            total = 0
            for digit in num:
                total += (int(digit)**2)
            
            num = str(total)
        
        return True
