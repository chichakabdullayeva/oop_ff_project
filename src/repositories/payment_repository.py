"""
Payment repository for managing payment data.
"""

from .base_repository import BaseRepository
from ..models.payment import Payment

# OOP – Inheritance: PaymentRepository inherits from BaseRepository
# SOLID – SRP: Only responsible for Payment data operations
# GRASP – Pure Fabrication: Separates persistence from business logic
class PaymentRepository(BaseRepository):
    """
    Repository for Payment model.
    Demonstrates single responsibility principle - handles only payment data access.
    """
    
    def __init__(self, storage):
        super().__init__(storage, "payments", Payment)

