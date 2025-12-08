from ..models.room import Room
from ..models.guest import Guest
from ..models.reservation import Reservation
from ..repositories.sqlite_storage import SQLiteStorage
from ..repositories.room_repository import RoomRepository
from ..repositories.guest_repository import GuestRepository
from ..repositories.reservation_repository import ReservationRepository
from ..repositories.payment_repository import PaymentRepository
from ..factories.payment_factory import PaymentFactory
from ..utils.logging_config import get_logger

# GRASP – Controller: Service coordinates operations between repositories and models
# SOLID – SRP: Service only handles business logic, not persistence or presentation
# SOLID – DIP: Depends on repository abstractions, not concrete implementations
class ReservationService:
    
    def __init__(self):
        self.logger = get_logger(__name__)
        self.logger.info("Setting up hotel reservation service...")
        
        self.storage = SQLiteStorage()
        self.room_repo = RoomRepository(self.storage)
        self.guest_repo = GuestRepository(self.storage)
        self.reservation_repo = ReservationRepository(self.storage)
        self.payment_repo = PaymentRepository(self.storage)
        
        self.logger.info("Hotel reservation service ready")
    
    # GRASP – Creator: Service creates Room objects
    # GRASP – Controller: Orchestrates room creation between model and repository
    def add_room(self, number, room_type, price_per_night, capacity=2):
        self.logger.info(f"Adding new room #{number} ({room_type}) - ${price_per_night}/night for {capacity} guests")
        try:
            existing_rooms = self.room_repo.get_all()
            for existing_room in existing_rooms:
                if existing_room.number == number:
                    error_msg = f"Room number {number} already exists"
                    self.logger.warning(error_msg)
                    raise ValueError(error_msg)
            
            room = Room(number, room_type, price_per_night, capacity)
            result = self.room_repo.create(room)
            self.logger.info(f"Room #{number} added successfully")
            return result
        except Exception as error:
            self.logger.error(f"Failed to add room #{number}: {error}", exc_info=True)
            raise
    
    # GRASP – Information Expert: Service delegates to repository
    def get_all_rooms(self):
        self.logger.debug("Loading all rooms...")
        try:
            rooms = self.room_repo.get_all()
            self.logger.info(f"Found {len(rooms)} rooms in the system")
            return rooms
        except Exception as error:
            self.logger.error(f"Error loading rooms: {error}", exc_info=True)
            raise
    
    def get_room(self, room_id):
        self.logger.debug(f"Searching for room: {room_id}")
        try:
            room = self.room_repo.get_by_id(room_id)
            if room:
                self.logger.info(f"Room found: {room_id}")
            else:
                self.logger.warning(f"Room not found: {room_id}")
            return room
        except Exception as error:
            self.logger.error(f"Error searching for room: {error}", exc_info=True)
            raise
    
    def update_room(self, room_id, number=None, room_type=None, price_per_night=None, capacity=None, is_available=None):
        self.logger.info(f"Updating room: {room_id}")
        try:
            room = self.room_repo.get_by_id(room_id)
            if not room:
                self.logger.warning(f"Room {room_id} not found")
                raise ValueError("Room not found")
            
            if number is not None:
                room.number = number
            if room_type is not None:
                room.room_type = room_type
            if price_per_night is not None:
                room.price_per_night = price_per_night
            if capacity is not None:
                room.capacity = capacity
            if is_available is not None:
                room.is_available = is_available
            
            result = self.room_repo.update(room)
            self.logger.info(f"Room {room_id} updated successfully")
            return result
        except Exception as error:
            self.logger.error(f"Failed to update room: {error}", exc_info=True)
            raise
    
    def delete_room(self, room_id):
        self.logger.info(f"Deleting room: {room_id}")
        try:
            result = self.room_repo.delete(room_id)
            self.logger.info(f"Room {room_id} deleted successfully")
            return result
        except Exception as error:
            self.logger.error(f"Failed to delete room: {error}", exc_info=True)
            raise
    
    # GRASP – Creator: Service creates Guest objects
    def add_guest(self, name, email, phone):
        self.logger.info(f"Registering new guest: {name} ({email})")
        try:
            # Check for duplicate email
            all_guests = self.guest_repo.get_all()
            for existing_guest in all_guests:
                if existing_guest.email == email:
                    error_msg = f"Guest with email {email} already exists"
                    self.logger.warning(error_msg)
                    raise ValueError(error_msg)
            
            guest = Guest(name, email, phone)
            result = self.guest_repo.create(guest)
            self.logger.info(f"Guest {name} registered successfully")
            return result
        except Exception as error:
            self.logger.error(f"Failed to register guest {name}: {error}", exc_info=True)
            raise
    
    def get_all_guests(self):
        self.logger.debug("Loading all guests...")
        try:
            guests = self.guest_repo.get_all()
            self.logger.info(f"Found {len(guests)} guests in the system")
            return guests
        except Exception as error:
            self.logger.error(f"Error loading guests: {error}", exc_info=True)
            raise
    
    def get_guest(self, guest_id):
        self.logger.debug(f"Searching for guest: {guest_id}")
        try:
            guest = self.guest_repo.get_by_id(guest_id)
            if guest:
                self.logger.info(f"Guest found: {guest_id}")
            else:
                self.logger.warning(f"Guest not found: {guest_id}")
            return guest
        except Exception as error:
            self.logger.error(f"Error searching for guest: {error}", exc_info=True)
            raise
    
    def update_guest(self, guest_id, name=None, email=None, phone=None):
        self.logger.info(f"Updating guest: {guest_id}")
        try:
            guest = self.guest_repo.get_by_id(guest_id)
            if not guest:
                self.logger.warning(f"Guest {guest_id} not found")
                raise ValueError("Guest not found")
            
            if name is not None:
                guest.name = name
            if email is not None:
                guest.email = email
            if phone is not None:
                guest.phone = phone
            
            result = self.guest_repo.update(guest)
            self.logger.info(f"Guest {guest_id} updated successfully")
            return result
        except Exception as error:
            self.logger.error(f"Failed to update guest: {error}", exc_info=True)
            raise
    
    def delete_guest(self, guest_id):
        self.logger.info(f"Deleting guest: {guest_id}")
        try:
            result = self.guest_repo.delete(guest_id)
            self.logger.info(f"Guest {guest_id} deleted successfully")
            return result
        except Exception as error:
            self.logger.error(f"Failed to delete guest: {error}", exc_info=True)
            raise
    
    # GRASP – Controller: Coordinates reservation creation across multiple objects
    # CUPID – Predictable: Validates room availability before creating reservation
    def create_reservation(self, guest_id, room_id, check_in_date, check_out_date):
        self.logger.info(f"Creating reservation: Guest {guest_id} → Room {room_id} ({check_in_date} to {check_out_date})")
        try:
            room = self.room_repo.get_by_id(room_id)
            if not room:
                self.logger.warning(f"Room {room_id} doesn't exist")
                raise ValueError("Room not found")
            if not room.is_available:
                self.logger.warning(f"Room {room_id} is already booked")
                raise ValueError("Room is not available")
            
            # GRASP – Creator: Service creates Reservation
            reservation = Reservation(guest_id, room_id, check_in_date, check_out_date)
            saved_reservation = self.reservation_repo.create(reservation)
            
            # GRASP – Controller: Service coordinates room status update
            room.is_available = False
            self.room_repo.update(room)
            
            self.logger.info(f"Reservation confirmed! Booking ID: {saved_reservation.id}")
            return saved_reservation
        except Exception as error:
            self.logger.error(f"Reservation failed: {error}", exc_info=True)
            raise
    
    def get_all_reservations(self):
        self.logger.debug("Loading all reservations...")
        try:
            reservations = self.reservation_repo.get_all()
            self.logger.info(f"Found {len(reservations)} active reservations")
            return reservations
        except Exception as error:
            self.logger.error(f"Error loading reservations: {error}", exc_info=True)
            raise
    
    def get_reservation(self, reservation_id):
        self.logger.debug(f"Searching for reservation: {reservation_id}")
        try:
            reservation = self.reservation_repo.get_by_id(reservation_id)
            if reservation:
                self.logger.info(f"Reservation found: {reservation_id}")
            else:
                self.logger.warning(f"Reservation not found: {reservation_id}")
            return reservation
        except Exception as error:
            self.logger.error(f"Error searching for reservation: {error}", exc_info=True)
            raise
    
    def update_reservation(self, reservation_id, check_in_date=None, check_out_date=None):
        self.logger.info(f"Updating reservation: {reservation_id}")
        try:
            reservation = self.reservation_repo.get_by_id(reservation_id)
            if not reservation:
                self.logger.warning(f"Reservation {reservation_id} not found")
                raise ValueError("Reservation not found")
            
            if check_in_date is not None:
                reservation.check_in_date = check_in_date
            if check_out_date is not None:
                reservation.check_out_date = check_out_date
            
            result = self.reservation_repo.update(reservation)
            self.logger.info(f"Reservation {reservation_id} updated successfully")
            return result
        except Exception as error:
            self.logger.error(f"Failed to update reservation: {error}", exc_info=True)
            raise
    
    def delete_reservation(self, reservation_id):
        self.logger.info(f"Deleting reservation: {reservation_id}")
        try:
            reservation = self.reservation_repo.get_by_id(reservation_id)
            if not reservation:
                self.logger.warning(f"Reservation {reservation_id} not found")
                raise ValueError("Reservation not found")
            
            room = self.room_repo.get_by_id(reservation.room_id)
            if room:
                room.is_available = True
                self.room_repo.update(room)
            
            result = self.reservation_repo.delete(reservation_id)
            self.logger.info(f"Reservation {reservation_id} deleted successfully")
            return result
        except Exception as error:
            self.logger.error(f"Failed to delete reservation: {error}", exc_info=True)
            raise
    
    # GRASP – Controller: Orchestrates cancellation across reservation and room
    def cancel_reservation(self, reservation_id):
        self.logger.info(f"Cancelling reservation: {reservation_id}")
        try:
            reservation = self.reservation_repo.get_by_id(reservation_id)
            if not reservation:
                self.logger.warning(f"Reservation {reservation_id} not found")
                raise ValueError("Reservation not found")
            
            reservation.cancel()
            self.reservation_repo.update(reservation)
            
            # GRASP – Controller: Service updates room availability
            room = self.room_repo.get_by_id(reservation.room_id)
            if room:
                room.is_available = True
                self.room_repo.update(room)
            
            self.logger.info(f"Reservation {reservation_id} cancelled successfully")
            return reservation
        except Exception as error:
            self.logger.error(f"Cancellation failed: {error}", exc_info=True)
            raise
    
    # GRASP – Controller: Coordinates payment processing via factory
    # SOLID – OCP: Uses factory to create payment types without modifying service
    def process_payment(self, reservation_id, amount, payment_type, card_number=""):
        self.logger.info(f"Processing ${amount:.2f} {payment_type} payment for reservation {reservation_id}")
        try:
            # Get reservation to calculate total cost
            reservation = self.reservation_repo.get_by_id(reservation_id)
            if not reservation:
                raise ValueError("Reservation not found")
            
            room = self.room_repo.get_by_id(reservation.room_id)
            if not room:
                raise ValueError("Room not found")
            
            # Calculate total cost
            from datetime import datetime
            check_in = datetime.strptime(reservation.check_in_date, "%Y-%m-%d")
            check_out = datetime.strptime(reservation.check_out_date, "%Y-%m-%d")
            nights = (check_out - check_in).days
            total_cost = room.price_per_night * nights
            
            # Calculate total paid amount (including this payment)
            all_payments = self.payment_repo.get_all()
            paid_amount = sum(p.amount for p in all_payments if p.reservation_id == reservation_id)
            total_paid = paid_amount + amount
            
            # GRASP – Creator: Delegates payment creation to factory
            payment = PaymentFactory.create_payment(payment_type, reservation_id, amount, card_number)
            
            # Set status based on whether reservation is fully paid
            if total_paid >= total_cost:
                payment.status = "completed"
                self.logger.info(f"Reservation fully paid: ${total_paid:.2f} of ${total_cost:.2f}")
            else:
                payment.status = "partial"
                self.logger.info(f"Partial payment: ${total_paid:.2f} of ${total_cost:.2f}")
            
            saved_payment = self.payment_repo.create(payment)
            
            self.logger.info(f"Payment ${amount:.2f} processed successfully")
            return saved_payment
        except Exception as error:
            self.logger.error(f"Payment failed: {error}", exc_info=True)
            raise
    
    def get_all_payments(self):
        self.logger.debug("Loading payment history...")
        try:
            payments = self.payment_repo.get_all()
            self.logger.info(f"Found {len(payments)} payment records")
            return payments
        except Exception as error:
            self.logger.error(f"Error loading payments: {error}", exc_info=True)
            raise
    
    def get_payment(self, payment_id):
        self.logger.debug(f"Searching for payment: {payment_id}")
        try:
            payment = self.payment_repo.get_by_id(payment_id)
            if payment:
                self.logger.info(f"Payment found: {payment_id}")
            else:
                self.logger.warning(f"Payment not found: {payment_id}")
            return payment
        except Exception as error:
            self.logger.error(f"Error searching for payment: {error}", exc_info=True)
            raise
    
    def delete_payment(self, payment_id):
        self.logger.info(f"Deleting payment: {payment_id}")
        try:
            result = self.payment_repo.delete(payment_id)
            self.logger.info(f"Payment {payment_id} deleted successfully")
            return result
        except Exception as error:
            self.logger.error(f"Failed to delete payment: {error}", exc_info=True)
            raise

