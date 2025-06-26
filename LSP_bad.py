from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        """Charge the customer"""
        pass

    @abstractmethod
    def refund(self, amount: float) -> None:
        """Refund the customer"""
        pass

class PaypalProcessor(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Charging ${amount:.2f} via PayPal")

    def refund(self, amount: float) -> None:
        print(f"Refunding ${amount:.2f} via PayPal")

class BitcoinProcessor(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Charging {amount:.6f} BTC on the blockchain")

    def refund(self, amount: float) -> None:
        # Oops—Bitcoin payments aren’t refundable!
        raise NotImplementedError("Cannot refund Bitcoin payments")
