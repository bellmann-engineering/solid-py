class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save_to_database(self, user):
        # Code zum Speichern des Benutzers in der Datenbank
        pass

class EmailService:
    def send_email(self, user, message):
        # Code zum Senden einer E-Mail an den Benutzer
        pass

class SalaryCalculator:
    def calculate_salary(self, user):
        # Code zur Berechnung des Benutzergehalts
        pass

# Anwendungslogik
user_repository = UserRepository()
email_service = EmailService()
salary_calculator = SalaryCalculator()

def register_user(name, email):
    user = User(name, email)
    user_repository.save_to_database(user)
    email_service.send_email(user, "Willkommen!")
    salary = salary_calculator.calculate_salary(user)
