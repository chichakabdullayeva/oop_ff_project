"""Edge case and error handling tests"""
from src.services.reservation_service import ReservationService
from src.models.payment import Payment
from src.factories.payment_factory import PaymentFactory

print("="*60)
print("EDGE CASE & ERROR HANDLING TESTS")
print("="*60)

service = ReservationService()

# Edge Case 1: Empty/null values
print("\n[Edge Case 1] Empty values handling")
try:
    guest = service.add_guest("", "test@example.com", "1234567890")
    print("⚠️  WARNING: Empty name accepted")
except Exception as e:
    print(f"✅ Handled: {e}")

# Edge Case 2: Non-existent room booking
print("\n[Edge Case 2] Booking non-existent room")
try:
    reservation = service.create_reservation(
        "fake-guest-id",
        "fake-room-id",
        "2024-01-01",
        "2024-01-05"
    )
    print("❌ BUG: Non-existent room accepted!")
except Exception as e:
    print(f"✅ Handled: {type(e).__name__}")

# Edge Case 3: Double booking same room
print("\n[Edge Case 3] Double booking prevention")
try:
    room = service.add_room("301", "standard", 100.0, 2)
    guest1 = service.add_guest("User1", "user1@test.com", "1111111111")
    guest2 = service.add_guest("User2", "user2@test.com", "2222222222")
    
    res1 = service.create_reservation(guest1.id, room.id, "2024-01-01", "2024-01-05")
    print(f"First reservation: {res1.status}")
    
    try:
        res2 = service.create_reservation(guest2.id, room.id, "2024-01-03", "2024-01-07")
        print("❌ BUG: Double booking allowed!")
    except ValueError as e:
        print(f"✅ Double booking prevented: {e}")
        
except Exception as e:
    print(f"Error in test: {e}")

# Edge Case 4: Zero or very large payment amounts
print("\n[Edge Case 4] Payment boundary values")
try:
    zero_payment = Payment("res1", 0.0)
    print(f"⚠️  WARNING: Zero payment accepted (amount: ${zero_payment.amount})")
except ValueError as e:
    print(f"✅ Zero payment rejected: {e}")

try:
    huge_payment = Payment("res2", 999999999.99)
    print(f"✅ Large payment accepted: ${huge_payment.amount:.2f}")
except Exception as e:
    print(f"Issue with large payment: {e}")

# Edge Case 5: Card number validation
print("\n[Edge Case 5] Card payment validation")
try:
    short_card = PaymentFactory.create_payment('card', 'res3', 50.0, '123')
    print("⚠️  WARNING: Short card number accepted (may cause issues in masking)")
except ValueError as e:
    print(f"✅ Card number validation working: {e}")

# Edge Case 6: Canceling already canceled reservation
print("\n[Edge Case 6] Multiple cancellations")
try:
    room = service.add_room("401", "deluxe", 150.0, 2)
    guest = service.add_guest("User3", "user3@test.com", "3333333333")
    res = service.create_reservation(guest.id, room.id, "2024-02-01", "2024-02-05")
    
    service.cancel_reservation(res.id)
    print(f"First cancellation: {res.status}")
    
    service.cancel_reservation(res.id)
    print("⚠️  WARNING: Double cancellation allowed")
    
except ValueError as e:
    print(f"✅ Double cancellation prevented: {e}")
except Exception as e:
    print(f"Error: {e}")

# Edge Case 7: Same dates for check-in and check-out
print("\n[Edge Case 7] Same date check-in/check-out")
try:
    from src.models.reservation import Reservation
    res = Reservation("g1", "r1", "2024-01-01", "2024-01-01")
    print("❌ BUG: Same date reservation accepted!")
except ValueError as e:
    print(f"✅ Same date rejected: {e}")

print("\n" + "="*60)
print("EDGE CASE TESTING COMPLETE")
print("="*60)
