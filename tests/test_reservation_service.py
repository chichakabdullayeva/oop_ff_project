"""
Unit tests for ReservationService.
Tests service layer and repository operations.
"""

import unittest
import os
from src.services.reservation_service import ReservationService
from src.factories.payment_factory import PaymentFactory


class TestReservationService(unittest.TestCase):
    """Test ReservationService operations."""
    
    def setUp(self):
        """Setup test service with a temporary data file."""
        # Use a test data file
        self.test_data_file = "src/data/test_hotel_data.json"
        self.service = ReservationService()
    
    def tearDown(self):
        """Clean up test data file."""
        if os.path.exists(self.test_data_file):
            try:
                os.remove(self.test_data_file)
            except:
                pass
    
    def test_add_room(self):
        """Test adding a room with unique number."""
        import uuid
        unique_number = f"TEST-{uuid.uuid4().hex[:6]}"
        room = self.service.add_room(unique_number, "standard", 100.0, 2)
        self.assertIsNotNone(room.id)
        self.assertEqual(room.number, unique_number)
    
    def test_add_guest(self):
        """Test adding a guest."""
        import uuid
        unique_email = f"test-{uuid.uuid4().hex[:8]}@example.com"
        guest = self.service.add_guest("John Doe", unique_email, "1234567890")
        self.assertIsNotNone(guest.id)
        self.assertEqual(guest.name, "John Doe")
    
    def test_get_all_rooms(self):
        """Test getting all rooms."""
        import uuid
        room_num1 = f"TEST-{uuid.uuid4().hex[:6]}"
        room_num2 = f"TEST-{uuid.uuid4().hex[:6]}"
        self.service.add_room(room_num1, "standard", 100.0, 2)
        self.service.add_room(room_num2, "deluxe", 150.0, 2)
        rooms = self.service.get_all_rooms()
        self.assertGreaterEqual(len(rooms), 2)


class TestPaymentFactory(unittest.TestCase):
    """Test PaymentFactory - demonstrates Factory pattern."""
    
    def test_create_cash_payment(self):
        """Test factory creates CashPayment."""
        payment = PaymentFactory.create_payment("cash", "reservation-1", 100.0)
        self.assertEqual(payment.payment_type, "cash")
    
    def test_create_card_payment(self):
        """Test factory creates CardPayment."""
        payment = PaymentFactory.create_payment("card", "reservation-1", 200.0, "4111111111111111")
        self.assertEqual(payment.payment_type, "card")
    
    def test_factory_polymorphism(self):
        """Test factory creates different types correctly."""
        cash = PaymentFactory.create_payment("cash", "res-1", 100.0)
        card = PaymentFactory.create_payment("card", "res-2", 200.0, "4111111111111111")
        
        self.assertTrue(hasattr(cash, 'process'))
        self.assertTrue(hasattr(card, 'process'))


if __name__ == "__main__":
    unittest.main()

