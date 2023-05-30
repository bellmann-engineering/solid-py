class UserService:
    def __init__(self, database):
        self.database = database

    def create_user(self, user):
        self.database.save(user)

class MySQLDatabase():
    def save(self, data):
        # Code zum Speichern der Daten in einer MySQL-Datenbank
        pass

class MongoDBDatabase():
    def save(self, data):
        # Code zum Speichern der Daten in einer MongoDB-Datenbank
        pass


# Erstellung einer Instanz der MySQLDatabase
mysql_db = MySQLDatabase()

# Erstellung einer Instanz der UserService mit einer konkreten MySQLDatabase-Instanz
user_service = UserService(mysql_db)
# Durch die direkte Übergabe einer MySQLDatabase-Instanz an den UserService-Konstruktor 
# entsteht eine starke Kopplung zwischen den beiden Klassen. Wenn in Zukunft eine andere 
# Datenbank implementiert oder verwendet werden soll, 
# müsste der UserService entsprechend angepasst werden, um die neue Datenbank zu akzeptieren.

# Aufruf der create_user-Methode des UserService
user_to_save = {id: 1, 'name': 'kbellmann'}
user_service.create_user(user_to_save)
