from database.database import Database
from models.model import Model

session = Database.session()

class MySQLRepository:
    def __init__(self, model: Model.__class__):
        self.model = model

    def save():
        ...
