from tasks.models import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1
        
    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks[self.next_id] = new_task
        self.next_id += 1
        return self.next_id - 1