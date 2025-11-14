from magu.controllers.controller import Controller
from magu.services.handler import Handler
import inspect

routes: dict[str, tuple] = {}

def get_routes(controller: Controller.__class__):
     for _, func in inspect.getmembers(controller, inspect.isfunction):
          if hasattr(func, "_http_method"):
            if func._method_uri.strip() != "/":
                route = f"{func._http_method} /{controller._uri.replace("/", "")}/{func._method_uri.replace("/", "")}"
            else:
                route = f"{func._http_method} /{controller._uri.replace("/", "")}"
            routes[route] = (func, controller)

def get_methods(uri: str, method: str):
        methods = []
        for name in routes:
            route_method = name.split(" ")[0]
            route_uri = name.split(" ")[1]
            controller = routes[name]
            if route_method.strip() == method and route_uri.strip() == uri:
                methods.append((routes[name], controller))
             
        return methods


class Router:
    def __init__(self, handler: Handler):
        self.handler = handler
        self.server_path = self.handler.path
        self.parse_path = handler.parse_path(self.server_path)

        try:
            self.gets = get_methods(self.parse_path["path"], "GET")[0]
        except IndexError:
            handler.send_json({"404": "Not Found"}, status=404)
            return
        
        try:
            self.posts = get_methods(self.parse_path["path"], "POST")[0]
        except IndexError:
            handler.send_json({"404": "Not Found"}, status=404)
            return
        
        try:
            self.puts = get_methods(self.parse_path["path"], "PUT")[0]
        except IndexError:
            handler.send_json({"404": "Not Found"}, status=404)
            return
        
        try:
            self.patches = get_methods(self.parse_path["path"], "PATCH")[0]
        except IndexError:
            handler.send_json({"404": "Not Found"}, status=404)
            return
        
        try:
            self.deletes = get_methods(self.parse_path["path"], "DELETE")[0]
        except IndexError:
            handler.send_json({"404": "Not Found"}, status=404)
            return
    
    def route(self, handler: Handler, http_method: str):
        if http_method == 'GET':
            for func, cont in self.gets:
                instance = cont()
                handler.send_json(func(instance))
                break
        elif http_method == 'POST':
            for func, cont in self.posts:
                instance = cont()
                handler.send_json(func(instance))
                break
        elif http_method == 'PUT':
            for func, cont in self.puts:
                instance = cont()
                handler.send_json(func(instance))
                break
        elif http_method == 'PATCH':
            for func, cont in self.patches:
                instance = cont()
                handler.send_json(func(instance))
                break
        elif http_method == "DELETE":
            for func, cont in self.patches:
                instance = cont()
                handler.send_json(func(instance))
                break
