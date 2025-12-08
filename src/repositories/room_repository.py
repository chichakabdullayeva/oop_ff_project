"""
Room repository for managing room data.
"""

from .base_repository import BaseRepository
from ..models.room import Room

# OOP – Inheritance: RoomRepository extends BaseRepository
# SOLID – SRP: Only handles Room data persistence
# GRASP – Pure Fabrication: Repository pattern for separation of concerns
class RoomRepository(BaseRepository):
    """
    Repository for Room model.
    Demonstrates single responsibility principle - handles only room data access.
    """
    
    def __init__(self, storage):
        # SOLID – DIP: Depends on storage interface, not implementation
        super().__init__(storage, "rooms", Room)

