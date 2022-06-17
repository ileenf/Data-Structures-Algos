class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr_row = [1]
        
        while rowIndex > 0:
            new_row = [1 for i in range(len(curr_row)+1)]
            
            for j in range(len(new_row)):
                if j != 0 and j != len(new_row)-1:
                    new_row[j] = curr_row[j-1] + curr_row[j]
                    
            curr_row = new_row
            rowIndex -= 1
            
            
        return curr_row
