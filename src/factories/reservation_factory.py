"""
Payment Factory - implements Factory design pattern.
Creates different types of payment objects based on payment method.
"""

from ..models.payment import Payment, CashPayment, CardPayment


class PaymentFactory:
    """
    Factory class for creating payment objects.
    Demonstrates Factory design pattern - creates objects without specifying exact class.
    """
    
    @staticmethod
    def create_payment(payment_type, reservation_id, amount, card_number=""):
        """
        Create a payment object based on the payment type.
        This is the factory method that decides which class to instantiate.
        
        Args:
            payment_type: Type of payment (cash, card)
            reservation_id: ID of the reservation
            amount: Payment amount
            card_number: Card number for card payments (optional)
        
        Returns:
            Payment object (CashPayment or CardPayment)
        """
        if payment_type.lower() == "cash":
            return CashPayment(reservation_id, amount)
        elif payment_type.lower() == "card":
            return CardPayment(reservation_id, amount, card_number)
        else:
            # Default to basic payment if type is unknown
            return Payment(reservation_id, amount)

