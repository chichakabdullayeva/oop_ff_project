import uuid

# OOP – Inheritance: Base class for all domain models
# GRASP – Information Expert: Knows how to generate unique IDs for all entities
class BaseModel:

    def __init__(self):
        # OOP – Encapsulation: ID is set internally
        self.id = str(uuid.uuid4())
    
    # OOP – Polymorphism: Subclasses override this method with their specific data
    def to_dict(self):

        return {"id": self.id}
    
    # OOP – Polymorphism: Factory method pattern - subclasses customize object creation
    @classmethod
    def from_dict(cls, data):
        
        return cls()

