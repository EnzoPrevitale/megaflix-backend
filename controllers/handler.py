from http.server import SimpleHTTPRequestHandler
import os
import json
from urllib.parse import urlsplit, unquote

class Handler(SimpleHTTPRequestHandler):
    def send_json(self, data: dict, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def send_token(self, data, token, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Authorization", f"Bearer {token}")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def parse_json_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            return None
        
    
