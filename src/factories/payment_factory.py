from ..models.payment import Payment, CashPayment, CardPayment
from ..utils.logging_config import get_logger

# OOP – Factory Pattern: Creates payment objects without exposing creation logic
# SOLID – OCP: Can add new payment types without modifying this class
# GRASP – Creator: Factory decides which payment subclass to create
class PaymentFactory:
    
    logger = get_logger(__name__)
    
    # SOLID – SRP: Static method only creates payment objects
    # OOP – Polymorphism: Returns different subclasses based on type
    @staticmethod
    def create_payment(payment_type, reservation_id, amount, card_number=""):
        PaymentFactory.logger.info(f"Creating {payment_type} payment of ${amount:.2f}")
        
        try:
            # SOLID – OCP: Adding new payment types requires only extending, not modifying
            if payment_type.lower() == "cash":
                payment = CashPayment(reservation_id, amount)
                PaymentFactory.logger.info(f"Cash payment created: {payment.id}")
                return payment
            elif payment_type.lower() == "card":
                payment = CardPayment(reservation_id, amount, card_number)
                PaymentFactory.logger.info(f"Card payment created: {payment.id}")
                return payment
            else:
                PaymentFactory.logger.warning(f"Unknown payment type '{payment_type}', using generic")
                payment = Payment(reservation_id, amount)
                PaymentFactory.logger.info(f"Generic payment created: {payment.id}")
                return payment
        except Exception as error:
            PaymentFactory.logger.error(f"Payment creation failed: {error}", exc_info=True)
            raise

