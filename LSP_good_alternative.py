from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class RefundStrategy(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

class RealRefundStrategy(RefundStrategy):
    def refund(self, amount: float) -> None:
        print(f"Refunding ${amount:.2f}")

class NoRefundStrategy(RefundStrategy):
    def refund(self, amount: float) -> None:
        print(f"Refund of ${amount:.2f} requested, but this processor does not support refunds.")

class PaypalProcessor(PaymentProcessor):
    def __init__(self):
        self.refunder = RealRefundStrategy()

    def pay(self, amount: float) -> None:
        print(f"Charging ${amount:.2f} via PayPal")

class BitcoinProcessor(PaymentProcessor):
    def __init__(self):
        self.refunder = NoRefundStrategy()

    def pay(self, amount: float) -> None:
        print(f"Charging {amount:.6f} BTC on the blockchain")
