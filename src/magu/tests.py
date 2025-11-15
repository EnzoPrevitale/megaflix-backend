from magu.core.server import run_server
from magu.controllers.controller import *
from magu.models.model import *
from magu.repositories.repository import MySQLRepository

@table(name="tabela")
class RestModel(Model):
    def __init__(self):
        super().__init__()

    id = Column(int, id=True)
    name = Column(int)
    age = Column(int)

@request_mapping("/")
class RootController(Controller):
    def __init__(self):
        super().__init__()

    @get_mapping("/")
    def get_root(self):
        return {"root": "root"}


@request_mapping("/a")
class RestController(Controller):
    def __init__(self):
        super().__init__()
        self.rep = MySQLRepository(RestModel())

    @get_mapping()
    def get(self):
        mod = RestModel()
        mod.name = "nome"
        mod.age = 1
        self.rep.save()
        return mod()
    
    @get_mapping("/a")
    def get1(self):
        return {"get": 1}
    
cont = RestController()
root = RootController()

if __name__ == '__main__':
    run_server()
