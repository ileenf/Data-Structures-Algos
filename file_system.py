class FileSystem:
    def __init__(self):
        self.paths = dict()
    
    def get_parent_path(self, path):
        for i in range(len(path)-1,-1,-1):
            if path[i] == '/':
                break
        return path[:i]
    
    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False
        parent_path = self.get_parent_path(path)
        if parent_path not in self.paths and parent_path != '':
            return False
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        if path not in self.paths:
            return -1
        return self.paths[path]
