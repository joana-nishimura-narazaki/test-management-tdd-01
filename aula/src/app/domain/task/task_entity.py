from uuid import UUID

class Task:

    id: UUID
    user_id: UUID
    title: str  
    description: str
    completed: bool

    def __init__(self, 
                 id: UUID, 
                 user_id: UUID, 
                 title: str, 
                 description: str, 
                 completed: bool = False):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.completed = completed
        self.validate()

    def validate(self):
        # VERIFICAÇÃO DO ID
        if not isinstance(self.id, UUID):
            raise Exception("Id must be an UUID")

        # VERIFICAÇÃO DO USER_ID
        if not isinstance(self.user_id, UUID):
            raise Exception("user_id must be an UUID")

        # VERIFICAÇÃO DO TÍTULO
        if not isinstance(self.title, str) or len(self.title) == 0:
            raise Exception("Title is required")

        # VERIFICAÇÃO DA DESCRIÇÃO
        if not isinstance(self.description, str) or len(self.description) == 0:
            raise Exception("Description is required")

        # VERIFICAÇÃO DO COMPLETED
        if not isinstance(self.completed, bool):
            raise Exception("invalid completed status: must be a boolean")
    
    def mark_as_completed(self):
        self.completed = True