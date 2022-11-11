class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        after_rotation = []
        
        width = len(box)
        length = len(box[0])
        
        for col in range(length):
            new_row = []
            for row in range(width-1, -1, -1):
                new_row.append(box[row][col])
            after_rotation.append(new_row)
            
        for col in range(width):
            above_obst_pos = length-1
            for row in range(length-1, -1, -1):
                if after_rotation[row][col] == '*':
                    above_obst_pos = row-1
                elif after_rotation[row][col] == '#':
                    after_rotation[row][col] = '.'
                    after_rotation[above_obst_pos][col] = '#'
                    above_obst_pos -= 1
                
        return after_rotation
