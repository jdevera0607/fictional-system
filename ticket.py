class Ticket:
    def __init__(self, id, title, description, priority, status="open"):
        self.id = id
        self.title = title
        self.description = description
        self.severity = priority
        self.status = status

    def todict(self):
        return {
            "id" : self.id,
            "title": self.title,
            "description": self.description,
            "severity" : self.priority,
            "status": self.status
        }
    def create_ticket():
        pass
