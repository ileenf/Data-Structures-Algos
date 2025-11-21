class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.database = {name: {} for name in names}
        self.table_to_column = {names[i]: columns[i] for i in range(len(names))}
        self.curr_row_idxs = {name: 1 for name in names}

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.database or len(row) != self.table_to_column[name]:
            return False
        
        self.database[name][self.curr_row_idxs[name]] = row
        self.curr_row_idxs[name] += 1
        return True
        

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.database or rowId not in self.database[name]:
            return
        
        del self.database[name][rowId]
        

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.database or rowId not in self.database[name]:
            return "<null>"
        
        if columnId > len(self.database[name][rowId]):
            return "<null>"
            
        return self.database[name][rowId][columnId-1]
        

    def exp(self, name: str) -> List[str]:
        if name not in self.database:
            return []
        
        export = []
        for row_id, row in self.database[name].items():
            export.append(str(row_id)+','+','.join(row))
        return export

        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)
