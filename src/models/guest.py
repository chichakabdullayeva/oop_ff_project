"""
Guest model - represents a hotel guest.
"""

from .base import BaseModel

# OOP – Inheritance: Guest inherits common behavior from BaseModel
# SOLID – SRP: Guest only handles guest-related data
class Guest(BaseModel):
    """
    Represents a guest staying at the hotel.
    Demonstrates encapsulation by storing guest information.
    """
    
    def __init__(self, name, email, phone):
        super().__init__()
        
        if not name or not name.strip():
            raise ValueError("Guest name cannot be empty")
        if not email or not email.strip():
            raise ValueError("Guest email cannot be empty")
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Invalid email format. Must contain @ and domain")
        if not phone or not phone.strip():
            raise ValueError("Guest phone cannot be empty")
        
        self.name = name.strip()
        self.email = email.strip()
        self.phone = phone.strip()
    
    # OOP – Polymorphism: Overrides parent method with Guest-specific implementation
    def to_dict(self):
        """Convert guest to dictionary for storage."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create guest from dictionary."""
        guest = cls(
            name=data["name"],
            email=data["email"],
            phone=data["phone"]
        )
        guest.id = data["id"]
        return guest
    
    def __str__(self):
        return f"Guest: {self.name} ({self.email})"

