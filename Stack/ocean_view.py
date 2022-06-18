class Solution:
  def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        heights = [[height, idx] for idx, height in enumerate(heights)]
        
        for height, idx in heights:
            while stack and height >= stack[-1][0]:
                stack.pop()

            stack.append([height, idx])
        
        return [val[1] for val in stack]
      
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        
        for idx in range(len(heights)):
            while stack and heights[idx] >= heights[stack[-1]]:
                stack.pop()

            stack.append(idx)
        
        return stack
