from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        # Code zum Speichern der Daten in einer MySQL-Datenbank
        pass

class MongoDBDatabase(Database):
    def save(self, data):
        # Code zum Speichern der Daten in einer MongoDB-Datenbank
        pass

class UserService:
    def __init__(self, database: Database):
        self.database = database

    def create_user(self, user):
        self.database.save(user)


# Erstellung einer Instanz der MySQLDatabase
mysql_db = MySQLDatabase()

# bleibt gleich
user_service = UserService(mysql_db)
# kann aber einfach ausgetauscht werden durch
# user_service = UserService(MongoDBDatabase())

# Aufruf der create_user-Methode des UserService
user_to_save = {id: 1, 'name': 'kbellmann'}
user_service.create_user(user_to_save)