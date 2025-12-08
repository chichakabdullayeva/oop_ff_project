"""Quick bug test script"""
from src.models.payment import Payment
from src.models.reservation import Reservation
from src.factories.payment_factory import PaymentFactory
from src.services.reservation_service import ReservationService

print("="*60)
print("BUG TESTING - Hotel Reservation System")
print("="*60)

# Test 1: Negative payment validation
print("\n[Test 1] Payment validation - negative amount")
try:
    p = Payment('res1', -100)
    print("❌ BUG FOUND: Negative payment was accepted!")
except ValueError as e:
    print(f"✅ PASS: {e}")

# Test 2: Invalid reservation dates
print("\n[Test 2] Reservation date validation")
try:
    r = Reservation('guest1', 'room1', '2024-12-31', '2024-01-01')
    print("❌ BUG FOUND: Invalid dates were accepted!")
except ValueError as e:
    print(f"✅ PASS: {e}")

# Test 3: Payment factory creates correct types
print("\n[Test 3] Payment factory pattern")
cash = PaymentFactory.create_payment('cash', 'res2', 50.0)
card = PaymentFactory.create_payment('card', 'res3', 75.0, '4111111111111111')
unknown = PaymentFactory.create_payment('unknown', 'res4', 100.0)

if cash.payment_type == 'cash':
    print("✅ PASS: Cash payment created correctly")
else:
    print(f"❌ BUG: Cash payment type is {cash.payment_type}")

if card.payment_type == 'card':
    print("✅ PASS: Card payment created correctly")
else:
    print(f"❌ BUG: Card payment type is {card.payment_type}")

if unknown.payment_type == 'generic':
    print("✅ PASS: Unknown payment defaulted to generic")
else:
    print(f"❌ BUG: Unknown payment type is {unknown.payment_type}")

# Test 4: Service layer integration
print("\n[Test 4] Service layer integration")
try:
    service = ReservationService()
    room = service.add_room('201', 'suite', 200.0, 4)
    guest = service.add_guest('Jane Doe', 'jane@test.com', '5555555555')
    
    if room.is_available:
        print("✅ PASS: New room is available")
    else:
        print("❌ BUG: New room not marked as available")
    
    reservation = service.create_reservation(
        guest.id, 
        room.id, 
        '2024-12-01', 
        '2024-12-05'
    )
    
    updated_room = service.get_room(room.id)
    if not updated_room.is_available:
        print("✅ PASS: Room marked unavailable after reservation")
    else:
        print("❌ BUG: Room still available after reservation")
    
    service.cancel_reservation(reservation.id)
    final_room = service.get_room(room.id)
    if final_room.is_available:
        print("✅ PASS: Room available again after cancellation")
    else:
        print("❌ BUG: Room not available after cancellation")
        
except Exception as e:
    print(f"❌ BUG: Service error - {e}")

# Test 5: Payment processing
print("\n[Test 5] Payment processing")
try:
    cash_payment = PaymentFactory.create_payment('cash', 'res5', 150.0)
    result = cash_payment.process()
    
    if result and cash_payment.status == 'completed':
        print("✅ PASS: Cash payment processed successfully")
    else:
        print(f"❌ BUG: Payment status is {cash_payment.status}")
        
    card_payment = PaymentFactory.create_payment('card', 'res6', 250.0, '4111111111111111')
    result2 = card_payment.process()
    
    if result2 and card_payment.status == 'completed':
        print("✅ PASS: Card payment processed successfully")
    else:
        print(f"❌ BUG: Card payment status is {card_payment.status}")
        
except Exception as e:
    print(f"❌ BUG: Payment processing error - {e}")

print("\n" + "="*60)
print("BUG TESTING COMPLETE")
print("="*60)
