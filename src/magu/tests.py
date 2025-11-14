from core.server import run_server
from controllers.controller import *

@request_mapping("/a")
class RestController(Controller):
    def __init__(self):
        super().__init__()
    
    @get_mapping()
    def get():
        return {"ma": "gu"}
    
    @get_mapping("/a")
    def get1():
        return {"get": 1}
    
    
cont = RestController()


if __name__ == '__main__':
    run_server()
