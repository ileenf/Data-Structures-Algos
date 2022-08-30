class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+': lambda x, y: x+y,
                      '-': lambda x, y: x-y,
                      '*': lambda x, y: x*y,
                      '/': lambda x, y: int(x/y)}
      
        
        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                result = operations[token](num1, num2)
                stack.append(result)
            else:
                stack.append(int(token))
                
        return stack.pop()
