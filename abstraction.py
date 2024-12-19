from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete implementations
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processed credit card payment of ${amount}"

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processed PayPal payment of ${amount}"

# Using the abstraction
def make_payment(payment: Payment, amount):
    print(payment.process_payment(amount))

# Usage
make_payment(CreditCardPayment(), 100)
make_payment(PayPalPayment(), 250)
