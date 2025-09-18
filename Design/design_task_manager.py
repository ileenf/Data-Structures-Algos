import heapq
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.heap = [(-task[2], -task[1], task[0]) for task in tasks]
        heapq.heapify(self.heap)
        self.active_tasks = {task[1]: (task[2], task[0]) for task in tasks}
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, -taskId, userId))
        self.active_tasks[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
            _, userId = self.active_tasks[taskId]
            heapq.heappush(self.heap, (-newPriority, -taskId, userId))
            self.active_tasks[taskId] = (newPriority, userId)

    def rmv(self, taskId: int) -> None:
        if taskId in self.active_tasks:
            del self.active_tasks[taskId]
        

    def execTop(self) -> int:
        while self.heap:
            top = heapq.heappop(self.heap)
            priority, task, user = top
            if -task in self.active_tasks and self.active_tasks[-task] == (-priority, user):
                del self.active_tasks[-task]
                return user
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
