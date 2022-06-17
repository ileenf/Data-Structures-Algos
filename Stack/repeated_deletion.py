class Solution:
    def solve(self, s, k):
        stack = []
                
        for ch in s:
            if not stack and k != 1:
                stack.append([ch, 1])
            else:
                if stack:
                    prev_ch, count = stack[-1]

                    if prev_ch == ch:
                        count += 1
                        stack.pop()

                        if count == k:
                            continue
                        else:
                            stack.append([prev_ch, count])
                    else:
                        stack.append([ch, 1])

        result = ''
        for ch, count in stack:
            for _ in range(count):
                result += ch
        return result