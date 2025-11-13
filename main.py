from models.model import Model, table
from core.auth.auth import Authentication

@table(table_name="user", user=True)
class User(Model):
    def __init__(self, name: str, password: str):
        super().__init__()
        '''

        Lógica para puxar id do banco

        '''
        self.name: str = name
        self.password: str = password

user = User("Enzo", "eadaasd")

print(Authentication.get_token(user))
