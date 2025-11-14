from core.server import run_server
from controllers.controller import *
from models.model import Model, table

@table(name="tabela")
class RestModel(Model):
    def __init__(self, name: str, age: int):
        super().__init__()
        self.name = name
        self.age = age

@request_mapping("/a")
class RestController(Controller):
    def __init__(self):
        super().__init__()
    
    @get_mapping()
    def get():
        return mod()
    
    @get_mapping("/a")
    def get1():
        return {"get": 1}
    
cont = RestController()
mod = RestModel("model", 0)

if __name__ == '__main__':
    run_server()
