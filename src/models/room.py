"""
Room model - represents a hotel room.
"""

from .base import BaseModel

# OOP – Inheritance: Room extends BaseModel
# SOLID – SRP: Room class only manages room data and availability
class Room(BaseModel):
    """
    Represents a hotel room with its properties.
    Demonstrates encapsulation by keeping room data private and accessible via methods.
    """
    
    def __init__(self, number, room_type, price_per_night, capacity=2):
        # OOP – Inheritance: Calls parent to get unique ID
        super().__init__()
        # OOP – Encapsulation: Room state stored in instance variables
        self.number = number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.capacity = capacity
        self.is_available = True
    
    # OOP – Polymorphism: Room-specific serialization
    def to_dict(self):
        """Convert room to dictionary for storage."""
        return {
            "id": self.id,
            "number": self.number,
            "room_type": self.room_type,
            "price_per_night": self.price_per_night,
            "capacity": self.capacity,
            "is_available": self.is_available
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create room from dictionary."""
        room = cls(
            number=data["number"],
            room_type=data["room_type"],
            price_per_night=data["price_per_night"],
            capacity=data.get("capacity", 2)
        )
        room.id = data["id"]
        room.is_available = data.get("is_available", True)
        return room
    
    def __str__(self):
        status = "Available" if self.is_available else "Occupied"
        return f"Room {self.number} ({self.room_type}) - ${self.price_per_night}/night - {status}"

