from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        """Charge the customer"""
        pass

class Refundable(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        """Refund the customer"""
        pass

class PaypalProcessor(PaymentProcessor, Refundable):
    def pay(self, amount: float) -> None:
        print(f"Charging ${amount:.2f} via PayPal")

    def refund(self, amount: float) -> None:
        print(f"Refunding ${amount:.2f} via PayPal")

class BitcoinProcessor(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Charging {amount:.6f} BTC on the blockchain")

# Client code
def handle_payment(processor: PaymentProcessor, amount: float):
    processor.pay(amount)

def handle_refund(processor: Refundable, amount: float):
    processor.refund(amount)

# Usage
pp = PaypalProcessor()
btc = BitcoinProcessor()

handle_payment(pp,   50.00)  # OK
handle_refund(pp,    50.00)  # OK

handle_payment(btc,   0.005) # OK
# handle_refund(btc, 0.005)  → type error at design time (no refund!), not runtime crash
