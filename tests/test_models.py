"""
Unit tests for model classes.
Tests basic functionality and OOP concepts.
"""

import unittest
from src.models.room import Room
from src.models.guest import Guest
from src.models.reservation import Reservation
from src.models.payment import Payment, CashPayment, CardPayment


class TestRoomModel(unittest.TestCase):
    """Test Room model."""
    
    def test_room_creation(self):
        """Test creating a room."""
        room = Room("101", "standard", 100.0, 2)
        self.assertEqual(room.number, "101")
        self.assertEqual(room.room_type, "standard")
        self.assertEqual(room.price_per_night, 100.0)
        self.assertTrue(room.is_available)
    
    def test_room_to_dict(self):
        """Test room serialization."""
        room = Room("101", "standard", 100.0, 2)
        data = room.to_dict()
        self.assertEqual(data["number"], "101")
        self.assertEqual(data["room_type"], "standard")
    
    def test_room_from_dict(self):
        """Test room deserialization."""
        data = {
            "id": "test-id",
            "number": "101",
            "room_type": "standard",
            "price_per_night": 100.0,
            "capacity": 2,
            "is_available": True
        }
        room = Room.from_dict(data)
        self.assertEqual(room.id, "test-id")
        self.assertEqual(room.number, "101")


class TestGuestModel(unittest.TestCase):
    """Test Guest model."""
    
    def test_guest_creation(self):
        """Test creating a guest."""
        guest = Guest("John Doe", "john@example.com", "1234567890")
        self.assertEqual(guest.name, "John Doe")
        self.assertEqual(guest.email, "john@example.com")
        self.assertIsNotNone(guest.id)


class TestReservationModel(unittest.TestCase):
    """Test Reservation model."""
    
    def test_reservation_creation(self):
        """Test creating a reservation."""
        reservation = Reservation("guest-1", "room-1", "2024-01-01", "2024-01-05")
        self.assertEqual(reservation.guest_id, "guest-1")
        self.assertEqual(reservation.status, "pending")
    
    def test_reservation_validation(self):
        """Test reservation date validation."""
        with self.assertRaises(ValueError):
            Reservation("guest-1", "room-1", "2024-01-05", "2024-01-01")
    
    def test_reservation_confirm(self):
        """Test confirming a reservation."""
        reservation = Reservation("guest-1", "room-1", "2024-01-01", "2024-01-05")
        reservation.confirm()
        self.assertEqual(reservation.status, "confirmed")


class TestPaymentModels(unittest.TestCase):
    """Test Payment hierarchy - demonstrates inheritance and polymorphism."""
    
    def test_base_payment(self):
        """Test base Payment class."""
        payment = Payment("reservation-1", 100.0)
        self.assertEqual(payment.amount, 100.0)
        self.assertEqual(payment.status, "pending")
    
    def test_payment_validation(self):
        """Test payment amount validation."""
        with self.assertRaises(ValueError):
            Payment("reservation-1", -50.0)
    
    def test_cash_payment_inheritance(self):
        """Test CashPayment inherits from Payment."""
        cash_payment = CashPayment("reservation-1", 100.0)
        self.assertIsInstance(cash_payment, Payment)
        self.assertEqual(cash_payment.payment_type, "cash")
    
    def test_card_payment_inheritance(self):
        """Test CardPayment inherits from Payment."""
        card_payment = CardPayment("reservation-1", 100.0, "4111111111111111")
        self.assertIsInstance(card_payment, Payment)
        self.assertEqual(card_payment.payment_type, "card")
    
    def test_payment_polymorphism(self):
        """Test polymorphism - different payment types process differently."""
        cash_payment = CashPayment("reservation-1", 100.0)
        card_payment = CardPayment("reservation-1", 200.0, "4111111111111111")
        
        cash_result = cash_payment.process()
        card_result = card_payment.process()
        
        self.assertTrue(cash_result)
        self.assertTrue(card_result)
        self.assertEqual(cash_payment.status, "completed")
        self.assertEqual(card_payment.status, "completed")


if __name__ == "__main__":
    unittest.main()

