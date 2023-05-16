class Solution:
    def decodeString(self, s: str) -> str:
        numbers = '1234567890'
        stack = []
        
        for ch in s:
            if ch == ']':

                # get the string to repeat
                string = ''
                while stack and stack[-1] != '[':
                    string += stack.pop()
                stack.pop()

                string = string[::-1]

                # get the amount to repeat k times
                k = 0
                base = 1

                while stack and stack[-1] in numbers:
                    k += (base * int(stack.pop()))
                    base *= 10

                # repeat the string k times and push onto stack
                for i in range(k):
                    for s in string:
                        stack.append(s)


            else:
                stack.append(ch)
        return ''.join(stack)
