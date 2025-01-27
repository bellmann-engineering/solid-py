import datetime

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def add_bonus(self, amount: float) -> None:
        self.salary += amount

    def get_payroll_details(self) -> dict:
        return {
            "name": self.name,
            "salary": self.salary
        }

class DatabaseOperator:
    def save_employee_to_database(self, employee: Employee) -> None:
        # Simulating database operations
        print(f"Saving {employee.name} to database...")

class NotificationService:
    def send_notification(self, employee: Employee) -> None:
        # Simulating sending email or notification
        print(f"Notifying {employee.name} about salary update...")
