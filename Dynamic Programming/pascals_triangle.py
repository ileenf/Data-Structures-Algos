class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        
        for i in range(numRows-1):
            prev_row = rows[i] 
            new_row = [1 for _ in range(len(prev_row)+1)]
            
            for j in range(len(new_row)):
                if j != 0 and j != len(new_row)-1:
                    new_row[j] = prev_row[j-1] + prev_row[j]
                    
            rows.append(new_row)
            
        return rows
