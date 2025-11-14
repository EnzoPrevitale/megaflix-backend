from core import router

def request_mapping(uri: str = "/"):
    def wrapper(cls):
        cls._uri = uri
        return cls
    return wrapper

def get_mapping(uri: str = "/"):
        def wrapper(func):
            func._http_method = 'GET'
            func._method_uri = uri
            return func
        return wrapper
    
def post_mapping(uri: str = "/"):
    def wrapper(func):
        func._http_method = 'POST'
        func._method_uri = uri
        return func
    return wrapper
    
def put_mapping(uri: str = "/"):
    def wrapper(func):
        func._http_method = 'PUT'
        func._method_uri = uri
        return func
    return wrapper
    
def patch_mapping(uri: str = "/"):
    def wrapper(func):
        func._http_method = 'PATCH'
        func._method_uri = uri
        return func
    return wrapper
    
def delete_mapping(uri: str = "/"):
    def wrapper(func):
        func._http_method = 'DELETE'
        func._method_uri = uri
        return func
    return wrapper

class Controller:
    def __init__(self):
        self.uri = self._uri
        router.get_routes(self.__class__)
