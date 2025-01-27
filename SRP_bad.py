import datetime

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def add_bonus(self, amount: float) -> None:
        self.salary += amount

    def save_to_database(self) -> None:
        # Simulating database operations
        print(f"Saving {self.name} to database...")

    def send_notification(self) -> None:
        # Simulating sending email or notification
        print(f"Notifying {self.name} about salary update...")

    def get_payroll_details(self) -> dict:
        return {
            "name": self.name,
            "salary": self.salary
        }
