"""
Reservation repository for managing reservation data.
"""

from .base_repository import BaseRepository
from ..models.reservation import Reservation

# OOP – Inheritance: ReservationRepository inherits CRUD operations
# SOLID – SRP: Handles only Reservation persistence
# GRASP – Pure Fabrication: Repository separates domain from persistence
class ReservationRepository(BaseRepository):
    """
    Repository for Reservation model.
    Demonstrates single responsibility principle - handles only reservation data access.
    """
    
    def __init__(self, storage):
        super().__init__(storage, "reservations", Reservation)

