"""
Guest repository for managing guest data.
"""

from .base_repository import BaseRepository
from ..models.guest import Guest

# OOP – Inheritance: GuestRepository extends BaseRepository
# SOLID – SRP: Only handles Guest data access
# GRASP – Pure Fabrication: Repository is not a domain concept but needed for architecture
class GuestRepository(BaseRepository):
    """
    Repository for Guest model.
    Demonstrates single responsibility principle - handles only guest data access.
    """
    
    def __init__(self, storage):
        # SOLID – DIP: Depends on storage abstraction, not concrete class
        super().__init__(storage, "guests", Guest)

