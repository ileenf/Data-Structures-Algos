class Solution:
    # M = length of string 
    # N = n
    # time complexity: O(MN) since we are looping N times,
    # and each time iterating over M characters in string. 
    # space complexity: O(K) where K is the longest string
    # sequence until n
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        
        res = ''
        temp_ch = s[0]
        count = 0
        for ch in s:
            if ch == temp_ch:
                count += 1
            else:
                res += (str(count) + temp_ch)
                count = 1
                temp_ch = ch
     
        res += (str(count) + temp_ch)
        return res
