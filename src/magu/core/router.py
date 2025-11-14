from controllers.controller import Controller
from services.handler import Handler
import inspect

routes: dict[str, Controller.__class__] = {}

def get_routes(controller: Controller.__class__):
     for _, func in inspect.getmembers(controller, inspect.isfunction):
          if hasattr(func, "_http_method"):
            if func._method_uri.strip() != "/":
                route = f"{func._http_method} /{controller._uri.replace("/", "")}/{func._method_uri.replace("/", "")}"
            else:
                route = f"{func._http_method} /{controller._uri.replace("/", "")}"
            routes[route] = func

def get_methods(uri: str, method: str):
        methods = []
        for name in routes:
            route_method = name.split(" ")[0]
            route_uri = name.split(" ")[1]
            if route_method.strip() == method and route_uri.strip() == uri:
                methods.append(routes[name])
             
        return methods


class Router:
    def route(self, handler: Handler, http_method: str):
        server_path = handler.path
        parse_path = handler.parse_path(server_path)
        gets = get_methods(parse_path["path"], http_method)

        for func in gets:
            handler.send_json(func())
            break
