#from magu.database.database import Database as db
from magu.models.model import Model

class MySQLRepository:
    def __init__(self, model: Model.__class__):
        self.model = model

    def save(self):
        table = self.model.__class__._table

        for attr in self.model.__dict__:
            print(attr, self.model.__dict__[attr])

        #with db.session() as session:
            ...#session.execute("INSERT INTO %s VALUEs ()", (table,))
