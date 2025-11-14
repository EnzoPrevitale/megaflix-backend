from http.server import HTTPServer
from magu.services.handler import Handler
from magu.core.router import Router
import magu.properties as properties

class ServerHandler(Handler):
    def __init__(self, request, client_address, server):
        self.router = Router(self)
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.router.route('GET')
    
    def do_POST(self):
        self.router.route('POST')

    def do_PUT(self):
        self.router.route('PUT')
    
    def do_PATCH(self):
        self.router.route('PATCH')

    def do_DELETE(self):
        self.router.route('DELETE')
        

def run_server():
    httpd = HTTPServer((properties.SERVER_HOST, properties.SERVER_PORT), ServerHandler)
    print(f"[Server] Server running on {properties.SERVER_ADDRESS}")
    httpd.serve_forever()
