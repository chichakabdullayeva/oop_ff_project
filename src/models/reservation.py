
"""
Reservation model - represents a room reservation.
"""

from datetime import datetime
from .base import BaseModel

# OOP – Inheritance: Reservation inherits from BaseModel
# SOLID – SRP: Reservation only manages booking data and validation
# GRASP – Information Expert: Reservation knows its own dates and status
class Reservation(BaseModel):
    """
    Represents a reservation linking a guest to a room for specific dates.
    Demonstrates encapsulation and validation.
    """
    
    def __init__(self, guest_id, room_id, check_in_date, check_out_date):
        super().__init__()
        # OOP – Encapsulation: Reservation state stored internally
        self.guest_id = guest_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = "pending"
        
        if check_out_date <= check_in_date:
            raise ValueError("Check-out date must be after check-in date")
    
    def confirm(self):
        """Confirm the reservation."""
        self.status = "confirmed"
    
    def cancel(self):
        """Cancel the reservation."""
        if self.status == "cancelled":
            raise ValueError("Reservation is already cancelled")
        self.status = "cancelled"
    
    def to_dict(self):
        """Convert reservation to dictionary for storage."""
        return {
            "id": self.id,
            "guest_id": self.guest_id,
            "room_id": self.room_id,
            "check_in_date": self.check_in_date,
            "check_out_date": self.check_out_date,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create reservation from dictionary."""
        check_in = data.get("check_in_date", "")
        check_out = data.get("check_out_date", "")
        
        reservation = cls(
            guest_id=data["guest_id"],
            room_id=data["room_id"],
            check_in_date=check_in,
            check_out_date=check_out
        )
        reservation.id = data["id"]
        reservation.status = data.get("status", "pending")
        return reservation
    
    def __str__(self):
        return f"Reservation {self.id}: Guest {self.guest_id} - Room {self.room_id} ({self.check_in_date} to {self.check_out_date}) - {self.status}"

