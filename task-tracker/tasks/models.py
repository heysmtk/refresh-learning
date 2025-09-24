from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task:
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.status = TaskStatus.TODO
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def mark_in_progress(self):
        self.status = TaskStatus.IN_PROGRESS
        self.updated_at = datetime.now()
        
    def mark_done(self):
        self.status = TaskStatus.DONE
        self.updated_at = datetime.now()
        
    def edit(self, new_title=None, new_description=None):
        if new_title is not None:
            self.title = new_title
        if new_description is not None:
            self.description = new_description
        self.updated_at = datetime.now()