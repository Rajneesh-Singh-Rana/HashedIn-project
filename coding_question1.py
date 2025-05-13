import heapq
class TaskScheduler:
    def _init_(self):
        self.task_heap = []

    def submitTask(self, taskId, estExecutionTime):
        """
        Add a new task to the scheduler.
        """
        heapq.heappush(self.task_heap, (estExecutionTime, taskId))
        print(f"Task {taskId} with estimated time {estExecutionTime} submitted.")

    def getNextTaskToProcess(self):
        """
        Get the task ID with the shortest execution time.
        """
        if not self.task_heap:
            print("No tasks available.")
            return None
        estExecutionTime, taskId = heapq.heappop(self.task_heap)
        print(f"Next task to process: {taskId} (Estimated time: {estExecutionTime})")
        return taskId

scheduler = TaskScheduler()
scheduler.submitTask("Task1", 5)
scheduler.submitTask("Task2", 2)
scheduler.submitTask("Task3", 3)

scheduler.getNextTaskToProcess()  #Task2
scheduler.getNextTaskToProcess()  #Task3
scheduler.getNextTaskToProcess()  #Task1

