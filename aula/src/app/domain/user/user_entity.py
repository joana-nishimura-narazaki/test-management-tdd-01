from uuid import UUID
from typing import List
from domain.task.task_entity import Task

class User:

    id: UUID
    name: str
    tasks: List[Task]

    def __init__(self,id:UUID, name:str):
        self.id = id
        self.name = name
        self.tasks = []
        self.validade()

    def validade(self):
        if not isinstance(self.id, UUID):
            raise Exception("Id must be an UUID")
        
        if not isinstance(self.name, str) or len(self.name) == 0:
            raise Exception("Name must be a string")
        
    def collect_tasks(self, tasks: List[Task]) -> None:
        self.tasks.extend(tasks)



