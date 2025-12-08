# GRASP – Pure Fabrication: Main module handles UI presentation layer
from src.services.reservation_service import ReservationService
from src.utils.logging_config import setup_logging, get_logger


def print_menu():
    print("\n" + "="*50)
    print("     HOTEL RESERVATION SYSTEM")
    print("="*50)
    print("1. Add Room")
    print("2. View Rooms")
    print("3. Update Room")
    print("4. Delete Room")
    print("5. Add Guest")
    print("6. View Guests")
    print("7. Update Guest")
    print("8. Delete Guest")
    print("9. Create Reservation")
    print("10. View Reservations")
    print("11. Update Reservation")
    print("12. Delete Reservation")
    print("13. Cancel Reservation")
    print("14. Make Payment")
    print("15. View Payments")
    print("16. Delete Payment")
    print("0. Exit")
    print("="*50)


# GRASP – Controller: Function delegates to service layer
def add_room(service):
    logger = get_logger(__name__)
    print("\n--- Add Room ---")
    try:
        number = input("Room number: ")
        room_type = input("Room type (standard/deluxe/suite): ")
        price = float(input("Price per night: "))
        capacity = int(input("Capacity: "))
        
        logger.info(f"User adding room #{number}")
        room = service.add_room(number, room_type, price, capacity)
        print(f"✓ Room added successfully! ID: {room.id}")
    except Exception as error:
        logger.error(f"Error adding room: {error}")
        print(f"✗ Error: {error}")

# GRASP – Low Coupling: UI functions only interact with service, not repositories
def view_rooms(service):
    print("\n--- All Rooms ---")
    try:
        rooms = service.get_all_rooms()
        if not rooms:
            print("No rooms found.")
            return
        
        for room in rooms:
            print(room)
    except Exception as error:
        print(f"✗ Error: {error}")


def update_room(service):
    logger = get_logger(__name__)
    print("\n--- Update Room ---")
    try:
        rooms = service.get_all_rooms()
        if not rooms:
            print("No rooms found.")
            return
        
        print("Rooms:")
        for i, room in enumerate(rooms, 1):
            print(f"{i}. {room}")
        
        choice_input = input(f"Select from list (1-{len(rooms)}): ").strip()
        choice = int(choice_input) - 1
        
        if choice < 0 or choice >= len(rooms):
            print(f"✗ Invalid selection. Please enter a number between 1 and {len(rooms)}")
            return
        selected_room = rooms[choice]
        
        print("\nLeave blank to keep current value")
        number = input(f"Room number [{selected_room.number}]: ").strip()
        room_type = input(f"Room type [{selected_room.room_type}]: ").strip()
        price = input(f"Price per night [{selected_room.price_per_night}]: ").strip()
        capacity = input(f"Capacity [{selected_room.capacity}]: ").strip()
        available = input(f"Available [{selected_room.is_available}] (yes/no): ").strip().lower()
        
        logger.info(f"User updating room: {selected_room.id}")
        service.update_room(
            selected_room.id,
            number=number if number else None,
            room_type=room_type if room_type else None,
            price_per_night=float(price) if price else None,
            capacity=int(capacity) if capacity else None,
            is_available=(available == 'yes') if available else None
        )
        print("✓ Room updated successfully!")
    except ValueError:
        print("✗ Invalid input. Please enter a valid number.")
    except Exception as error:
        logger.error(f"Error updating room: {error}")
        print(f"✗ Error: {error}")


def delete_room(service):
    logger = get_logger(__name__)
    print("\n--- Delete Room ---")
    try:
        rooms = service.get_all_rooms()
        if not rooms:
            print("No rooms found.")
            return
        
        print("Rooms:")
        for i, room in enumerate(rooms, 1):
            print(f"{i}. {room}")
        
        choice_input = input(f"Select from list (1-{len(rooms)}): ").strip()
        choice = int(choice_input) - 1
        
        if choice < 0 or choice >= len(rooms):
            print(f"✗ Invalid selection. Please enter a number between 1 and {len(rooms)}")
            return
        selected_room = rooms[choice]
        
        confirm = input(f"Delete room {selected_room.number}? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            logger.info(f"User deleting room: {selected_room.id}")
            service.delete_room(selected_room.id)
            print("✓ Room deleted successfully!")
        else:
            print("Deletion cancelled.")
    except ValueError:
        print("✗ Invalid input. Please enter a valid number.")
    except Exception as error:
        logger.error(f"Error deleting room: {error}")
        print(f"✗ Error: {error}")


def add_guest(service):
    logger = get_logger(__name__)
    print("\n--- Add Guest ---")
    try:
        name = input("Guest name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        
        logger.info(f"User registering guest: {name}")
        guest = service.add_guest(name, email, phone)
        print(f"✓ Guest added successfully! ID: {guest.id}")
    except Exception as error:
        logger.error(f"Error adding guest: {error}")
        print(f"✗ Error: {error}")


def view_guests(service):
    print("\n--- All Guests ---")
    try:
        guests = service.get_all_guests()
        if not guests:
            print("No guests found.")
            return
        
        for guest in guests:
            print(guest)
    except Exception as error:
        print(f"✗ Error: {error}")


def update_guest(service):
    logger = get_logger(__name__)
    print("\n--- Update Guest ---")
    try:
        guests = service.get_all_guests()
        if not guests:
            print("No guests found.")
            return
        
        print("Guests:")
        for i, guest in enumerate(guests, 1):
            print(f"{i}. {guest}")
        
        choice_input = input(f"Select from list (1-{len(guests)}): ").strip()
        choice = int(choice_input) - 1
        
        if choice < 0 or choice >= len(guests):
            print(f"✗ Invalid selection. Please enter a number between 1 and {len(guests)}")
            return
        selected_guest = guests[choice]
        
        print("\nLeave blank to keep current value")
        name = input(f"Guest name [{selected_guest.name}]: ").strip()
        email = input(f"Email [{selected_guest.email}]: ").strip()
        phone = input(f"Phone [{selected_guest.phone}]: ").strip()
        
        logger.info(f"User updating guest: {selected_guest.id}")
        service.update_guest(
            selected_guest.id,
            name=name if name else None,
            email=email if email else None,
            phone=phone if phone else None
        )
        print("✓ Guest updated successfully!")
    except Exception as error:
        logger.error(f"Error updating guest: {error}")
        print(f"✗ Error: {error}")


def delete_guest(service):
    logger = get_logger(__name__)
    print("\n--- Delete Guest ---")
    try:
        guests = service.get_all_guests()
        if not guests:
            print("No guests found.")
            return
        
        print("Guests:")
        for i, guest in enumerate(guests, 1):
            print(f"{i}. {guest}")
        
        choice_input = input(f"Select from list (1-{len(guests)}): ").strip()
        choice = int(choice_input) - 1
        
        if choice < 0 or choice >= len(guests):
            print(f"✗ Invalid selection. Please enter a number between 1 and {len(guests)}")
            return
        selected_guest = guests[choice]
        
        confirm = input(f"Delete guest {selected_guest.name}? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            logger.info(f"User deleting guest: {selected_guest.id}")
            service.delete_guest(selected_guest.id)
            print("✓ Guest deleted successfully!")
        else:
            print("Deletion cancelled.")
    except Exception as error:
        logger.error(f"Error deleting guest: {error}")
        print(f"✗ Error: {error}")


# GRASP – Controller: Delegates complex reservation logic to service
def create_reservation(service):
    logger = get_logger(__name__)
    print("\n--- Create Reservation ---")
    try:
        rooms = service.get_all_rooms()
        available_rooms = [r for r in rooms if r.is_available]
        
        if not available_rooms:
            print("No available rooms.")
            return
        
        print("Available rooms:")
        for i, room in enumerate(available_rooms, 1):
            print(f"{i}. {room}")
        
        room_choice = int(input(f"Select from list (1-{len(available_rooms)}): "))
        if room_choice < 1 or room_choice > len(available_rooms):
            raise ValueError(f"Please select a number between 1 and {len(available_rooms)}")
        selected_room = available_rooms[room_choice - 1]
        
        guests = service.get_all_guests()
        if not guests:
            print("No guests found. Please add a guest first.")
            return
        
        print("\nGuests:")
        for i, guest in enumerate(guests, 1):
            print(f"{i}. {guest}")
        
        guest_choice = int(input(f"Select from list (1-{len(guests)}): "))
        if guest_choice < 1 or guest_choice > len(guests):
            raise ValueError(f"Please select a number between 1 and {len(guests)}")
        selected_guest = guests[guest_choice - 1]
        
        check_in = input("Check-in date (YYYY-MM-DD): ")
        check_out = input("Check-out date (YYYY-MM-DD): ")
        
        logger.info(f"User creating reservation: {selected_guest.name} → Room #{selected_room.number}")
        reservation = service.create_reservation(
            selected_guest.id,
            selected_room.id,
            check_in,
            check_out
        )
        print(f"✓ Reservation created successfully! ID: {reservation.id}")
    except ValueError as error:
        logger.error(f"Invalid input for reservation: {error}")
        print(f"✗ Error: {error}")
    except Exception as error:
        logger.error(f"Error creating reservation: {error}")
        print(f"✗ Error: {error}")


def view_reservations(service):
    print("\n--- All Reservations ---")
    try:
        reservations = service.get_all_reservations()
        if not reservations:
            print("No reservations found.")
            return
        
        for i, reservation in enumerate(reservations, 1):
            # Get guest and room details for readable display
            guest = service.guest_repo.get_by_id(reservation.guest_id)
            room = service.room_repo.get_by_id(reservation.room_id)
            
            guest_name = guest.name if guest else "Unknown Guest"
            room_number = room.number if room else "Unknown Room"
            
            print(f"{i}. Guest: {guest_name} | Room: {room_number} | {reservation.check_in_date} to {reservation.check_out_date} | Status: {reservation.status}")
    except Exception as error:
        print(f"✗ Error: {error}")


def update_reservation(service):
    logger = get_logger(__name__)
    print("\n--- Update Reservation ---")
    try:
        reservations = service.get_all_reservations()
        if not reservations:
            print("No reservations found.")
            return
        
        print("Reservations:")
        for i, reservation in enumerate(reservations, 1):
            guest = service.guest_repo.get_by_id(reservation.guest_id)
            room = service.room_repo.get_by_id(reservation.room_id)
            guest_name = guest.name if guest else "Unknown"
            room_number = room.number if room else "Unknown"
            print(f"{i}. Guest: {guest_name} | Room: {room_number} | {reservation.check_in_date} to {reservation.check_out_date} | Status: {reservation.status}")
        
        choice_input = input(f"Select from list (1-{len(reservations)}): ").strip()
        choice = int(choice_input) - 1
        
        if choice < 0 or choice >= len(reservations):
            print(f"✗ Invalid selection. Please enter a number between 1 and {len(reservations)}")
            return
        selected_reservation = reservations[choice]
        
        print("\nLeave blank to keep current value")
        check_in = input(f"Check-in date [{selected_reservation.check_in_date}] (YYYY-MM-DD): ").strip()
        check_out = input(f"Check-out date [{selected_reservation.check_out_date}] (YYYY-MM-DD): ").strip()
        
        logger.info(f"User updating reservation: {selected_reservation.id}")
        service.update_reservation(
            selected_reservation.id,
            check_in_date=check_in if check_in else None,
            check_out_date=check_out if check_out else None
        )
        print("✓ Reservation updated successfully!")
    except Exception as error:
        logger.error(f"Error updating reservation: {error}")
        print(f"✗ Error: {error}")


def delete_reservation(service):
    logger = get_logger(__name__)
    print("\n--- Delete Reservation ---")
    try:
        reservations = service.get_all_reservations()
        if not reservations:
            print("No reservations found.")
            return
        
        print("Reservations:")
        for i, reservation in enumerate(reservations, 1):
            guest = service.guest_repo.get_by_id(reservation.guest_id)
            room = service.room_repo.get_by_id(reservation.room_id)
            guest_name = guest.name if guest else "Unknown"
            room_number = room.number if room else "Unknown"
            print(f"{i}. Guest: {guest_name} | Room: {room_number} | {reservation.check_in_date} to {reservation.check_out_date} | Status: {reservation.status}")
        
        choice_input = input(f"Select from list (1-{len(reservations)}): ").strip()
        choice = int(choice_input) - 1
        
        if choice < 0 or choice >= len(reservations):
            print(f"✗ Invalid selection. Please enter a number between 1 and {len(reservations)}")
            return
        selected_reservation = reservations[choice]
        
        confirm = input(f"Delete reservation {selected_reservation.id}? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            logger.info(f"User deleting reservation: {selected_reservation.id}")
            service.delete_reservation(selected_reservation.id)
            print("✓ Reservation deleted successfully!")
        else:
            print("Deletion cancelled.")
    except Exception as error:
        logger.error(f"Error deleting reservation: {error}")
        print(f"✗ Error: {error}")


def cancel_reservation(service):
    logger = get_logger(__name__)
    print("\n--- Cancel Reservation ---")
    try:
        reservations = service.get_all_reservations()
        if not reservations:
            print("No reservations found.")
            return
        
        print("Reservations:")
        for i, reservation in enumerate(reservations, 1):
            guest = service.guest_repo.get_by_id(reservation.guest_id)
            room = service.room_repo.get_by_id(reservation.room_id)
            guest_name = guest.name if guest else "Unknown"
            room_number = room.number if room else "Unknown"
            print(f"{i}. Guest: {guest_name} | Room: {room_number} | {reservation.check_in_date} to {reservation.check_out_date} | Status: {reservation.status}")
        
        choice_input = input(f"Select from list (1-{len(reservations)}): ").strip()
        choice = int(choice_input) - 1
        
        if choice < 0 or choice >= len(reservations):
            print(f"✗ Invalid selection. Please enter a number between 1 and {len(reservations)}")
            return
        selected_reservation = reservations[choice]
        
        logger.info(f"User cancelling reservation: {selected_reservation.id}")
        service.cancel_reservation(selected_reservation.id)
        print("✓ Reservation cancelled successfully!")
    except Exception as error:
        logger.error(f"Error cancelling reservation: {error}")
        print(f"✗ Error: {error}")


# GRASP – Controller: Coordinates payment creation through service and factory
def make_payment(service):
    logger = get_logger(__name__)
    print("\n--- Make Payment ---")
    try:
        reservations = service.get_all_reservations()
        if not reservations:
            print("No reservations found.")
            return
        
        print("Reservations:")
        for i, reservation in enumerate(reservations, 1):
            guest = service.guest_repo.get_by_id(reservation.guest_id)
            room = service.room_repo.get_by_id(reservation.room_id)
            guest_name = guest.name if guest else "Unknown"
            room_number = room.number if room else "Unknown"
            
            # Calculate total cost and paid amount
            from datetime import datetime
            check_in = datetime.strptime(reservation.check_in_date, "%Y-%m-%d")
            check_out = datetime.strptime(reservation.check_out_date, "%Y-%m-%d")
            nights = (check_out - check_in).days
            total_cost = room.price_per_night * nights if room else 0
            
            # Get existing payments for this reservation
            all_payments = service.payment_repo.get_all()
            paid_amount = sum(p.amount for p in all_payments if p.reservation_id == reservation.id and p.status in ["completed", "partial"])
            remaining = total_cost - paid_amount
            
            print(f"{i}. Guest: {guest_name} | Room: {room_number} | {nights} nights | Total: ${total_cost:.2f} | Paid: ${paid_amount:.2f} | Remaining: ${remaining:.2f}")
        
        choice = int(input(f"Select from list (1-{len(reservations)}): "))
        if choice < 1 or choice > len(reservations):
            raise ValueError(f"Please select a number between 1 and {len(reservations)}")
        selected_reservation = reservations[choice - 1]
        
        # Show payment summary for selected reservation
        room = service.room_repo.get_by_id(selected_reservation.room_id)
        check_in = datetime.strptime(selected_reservation.check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(selected_reservation.check_out_date, "%Y-%m-%d")
        nights = (check_out - check_in).days
        total_cost = room.price_per_night * nights if room else 0
        all_payments = service.payment_repo.get_all()
        paid_amount = sum(p.amount for p in all_payments if p.reservation_id == selected_reservation.id and p.status in ["completed", "partial"])
        remaining = total_cost - paid_amount
        
        print(f"\nTotal Cost: ${total_cost:.2f}")
        print(f"Already Paid: ${paid_amount:.2f}")
        print(f"Remaining: ${remaining:.2f}")
        
        amount = float(input("Payment amount: "))
        payment_type = input("Payment type (cash/card): ").lower()
        
        card_number = ""
        if payment_type == "card":
            card_number = input("Card number: ")
        
        logger.info(f"User making {payment_type} payment of ${amount:.2f}")
        payment = service.process_payment(
            selected_reservation.id,
            amount,
            payment_type,
            card_number
        )
        
        # Show updated balance
        new_paid = paid_amount + amount
        new_remaining = total_cost - new_paid
        print(f"✓ Payment processed successfully! ID: {payment.id}")
        print(f"Status: {payment.status}")
        print(f"New Balance - Paid: ${new_paid:.2f} | Remaining: ${new_remaining:.2f}")
        
        if new_remaining > 0:
            print(f"⚠ Remaining balance: ${new_remaining:.2f} - Status: PARTIAL PAYMENT")
        elif new_remaining == 0:
            print("✓ Reservation fully paid! - Status: COMPLETED")
        else:
            print(f"✓ Overpaid by: ${abs(new_remaining):.2f} - Status: COMPLETED")
            
    except Exception as error:
        logger.error(f"Error processing payment: {error}")
        print(f"✗ Error: {error}")


def view_payments(service):
    print("\n--- All Payments ---")
    try:
        payments = service.get_all_payments()
        if not payments:
            print("No payments found.")
            return
        
        for i, payment in enumerate(payments, 1):
            # Get reservation details
            reservation = service.reservation_repo.get_by_id(payment.reservation_id)
            if reservation:
                guest = service.guest_repo.get_by_id(reservation.guest_id)
                room = service.room_repo.get_by_id(reservation.room_id)
                guest_name = guest.name if guest else "Unknown"
                room_number = room.number if room else "Unknown"
                print(f"{i}. ${payment.amount:.2f} ({payment.payment_type}) | Guest: {guest_name} | Room: {room_number} | Status: {payment.status}")
            else:
                print(f"{i}. ${payment.amount:.2f} ({payment.payment_type}) | Status: {payment.status}")
    except Exception as error:
        print(f"✗ Error: {error}")


def delete_payment(service):
    logger = get_logger(__name__)
    print("\n--- Delete Payment ---")
    try:
        payments = service.get_all_payments()
        if not payments:
            print("No payments found.")
            return
        
        print("Payments:")
        for i, payment in enumerate(payments, 1):
            reservation = service.reservation_repo.get_by_id(payment.reservation_id)
            if reservation:
                guest = service.guest_repo.get_by_id(reservation.guest_id)
                room = service.room_repo.get_by_id(reservation.room_id)
                guest_name = guest.name if guest else "Unknown"
                room_number = room.number if room else "Unknown"
                print(f"{i}. ${payment.amount:.2f} ({payment.payment_type}) | Guest: {guest_name} | Room: {room_number} | Status: {payment.status}")
            else:
                print(f"{i}. ${payment.amount:.2f} ({payment.payment_type}) | Status: {payment.status}")
        
        choice_input = input(f"Select from list (1-{len(payments)}): ").strip()
        choice = int(choice_input) - 1
        
        if choice < 0 or choice >= len(payments):
            print(f"✗ Invalid selection. Please enter a number between 1 and {len(payments)}")
            return
        selected_payment = payments[choice]
        
        confirm = input(f"Delete payment {selected_payment.id}? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            logger.info(f"User deleting payment: {selected_payment.id}")
            service.delete_payment(selected_payment.id)
            print("✓ Payment deleted successfully!")
        else:
            print("Deletion cancelled.")
    except Exception as error:
        logger.error(f"Error deleting payment: {error}")
        print(f"✗ Error: {error}")


# GRASP – Controller: Main function coordinates entire application flow
# SOLID – DIP: Main depends on service abstraction
def main():
    setup_logging()
    logger = get_logger(__name__)
    
    logger.info("="*60)
    logger.info("Hotel Reservation System starting up...")
    logger.info("="*60)
    
    # GRASP – Creator: Main creates service instance
    service = ReservationService()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")
        
        logger.debug(f"User selected option: {choice}")
        
        if choice == "1":
            add_room(service)
        elif choice == "2":
            view_rooms(service)
        elif choice == "3":
            update_room(service)
        elif choice == "4":
            delete_room(service)
        elif choice == "5":
            add_guest(service)
        elif choice == "6":
            view_guests(service)
        elif choice == "7":
            update_guest(service)
        elif choice == "8":
            delete_guest(service)
        elif choice == "9":
            create_reservation(service)
        elif choice == "10":
            view_reservations(service)
        elif choice == "11":
            update_reservation(service)
        elif choice == "12":
            delete_reservation(service)
        elif choice == "13":
            cancel_reservation(service)
        elif choice == "14":
            make_payment(service)
        elif choice == "15":
            view_payments(service)
        elif choice == "16":
            delete_payment(service)
        elif choice == "0":
            logger.info("User exiting system")
            print("\nThank you for using Hotel Reservation System!")
            break
        else:
            logger.warning(f"Invalid choice: {choice}")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

