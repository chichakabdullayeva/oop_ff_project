from .base import BaseModel
from ..utils.logging_config import get_logger

# OOP – Inheritance: Base class for all payment types
# SOLID – SRP: Payment class handles only payment processing logic
# GRASP – Information Expert: Payment knows how to process itself
class Payment(BaseModel):
    
    def __init__(self, reservation_id, amount):
        super().__init__()
        # OOP – Encapsulation: Payment state stored internally
        self.reservation_id = reservation_id
        self.amount = amount
        self.status = "pending"
        self.payment_type = "generic"
        self.logger = get_logger(self.__class__.__name__)
    
        if amount < 0:
            self.logger.error(f"Invalid amount: ${amount}")
            raise ValueError("Payment amount cannot be negative")
        if amount == 0:
            self.logger.error(f"Invalid amount: ${amount}")
            raise ValueError("Payment amount cannot be zero")
    
    # OOP – Polymorphism: Subclasses override this with specific payment logic
    # GRASP – Information Expert: Payment processes itself
    def process(self):
        self.logger.info(f"Processing payment {self.id}: ${self.amount:.2f}")
        try:
            self.status = "completed"
            self.logger.info(f"Payment {self.id} completed")
            return True
        except Exception as error:
            self.status = "failed"
            self.logger.error(f"Payment {self.id} failed: {error}", exc_info=True)
            return False
    
    def to_dict(self):
        return {
            "id": self.id,
            "reservation_id": self.reservation_id,
            "amount": self.amount,
            "status": self.status,
            "payment_type": self.payment_type
        }
    
    @classmethod
    def from_dict(cls, data):
        payment_type = data.get("payment_type", "generic")
        
        if payment_type == "cash":
            payment = CashPayment(
                reservation_id=data["reservation_id"],
                amount=data["amount"]
            )
        elif payment_type == "card":
            payment = CardPayment(
                reservation_id=data["reservation_id"],
                amount=data["amount"],
                card_number=data.get("card_number", "")
            )
        else:
            payment = cls(
                reservation_id=data["reservation_id"],
                amount=data["amount"]
            )
        
        payment.id = data["id"]
        payment.status = data.get("status", "pending")
        return payment
    
    def __str__(self):
        return f"Payment {self.id}: ${self.amount} for Reservation {self.reservation_id} - {self.status}"


class CashPayment(Payment):
    
    def __init__(self, reservation_id, amount):
        super().__init__(reservation_id, amount)
        self.payment_type = "cash"
    
    def process(self):
        self.logger.info(f"💵 Processing cash payment {self.id}: ${self.amount:.2f}")
        try:
            print(f"Processing cash payment of ${self.amount}")
            self.status = "completed"
            self.logger.info(f"✅ Cash payment {self.id} successful")
            return True
        except Exception as error:
            self.status = "failed"
            self.logger.error(f"❌ Cash payment {self.id} failed: {error}", exc_info=True)
            return False
    
    def __str__(self):
        return f"Cash Payment {self.id}: ${self.amount} - {self.status}"


class CardPayment(Payment):
    
    def __init__(self, reservation_id, amount, card_number=""):
        super().__init__(reservation_id, amount)
        self.payment_type = "card"
        
        if card_number and len(card_number) < 13:
            raise ValueError("Card number must be at least 13 digits")
        
        self.card_number = card_number
    
    def process(self):
        masked_card = f"****{self.card_number[-4:]}" if len(self.card_number) >= 4 else "XXXX"
        self.logger.info(f"💳 Processing card payment {self.id}: ${self.amount:.2f} ({masked_card})")
        try:
            print(f"Processing card payment of ${self.amount}")
            print(f"Card ending in: {self.card_number[-4:] if len(self.card_number) >= 4 else 'XXXX'}")
            self.status = "completed"
            self.logger.info(f"✅ Card payment {self.id} successful")
            return True
        except Exception as error:
            self.status = "failed"
            self.logger.error(f"❌ Card payment {self.id} failed: {error}", exc_info=True)
            return False
    
    def to_dict(self):
        data = super().to_dict()
        data["card_number"] = self.card_number
        return data
    
    def __str__(self):
        return f"Card Payment {self.id}: ${self.amount} - {self.status}"

