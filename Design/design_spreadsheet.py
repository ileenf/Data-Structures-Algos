class Spreadsheet:
    def __init__(self, rows: int):
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.spreadsheet = dict()
        for col in columns:
            for row in range(1, rows+1):
                self.spreadsheet[col+str(row)] = 0
        
    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell] = value
        

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[cell] = 0
        

    def getValue(self, formula: str) -> int:
        val1, val2 = formula.split('=')[1].split('+')

        if val1 in self.spreadsheet:
            val1 = self.spreadsheet[val1]

        if val2 in self.spreadsheet:
            val2 = self.spreadsheet[val2]
        
        return int(val1) + int(val2)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
