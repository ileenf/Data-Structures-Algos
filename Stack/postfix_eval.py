class Solution:
    def solve(self, exp):
        stack = []
        operators = {'+': add, '-': sub, '*': mul, '/': truediv}

        for val in exp:
            if not stack or val not in operators:
                stack.append(int(val))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(int(operators[val](num1, num2)))
                
        return stack[0]
