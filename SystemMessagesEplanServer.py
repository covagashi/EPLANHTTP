from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

class SimpleServer(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/log':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            print(f"Received at {datetime.now()}: {post_data}")
            
            
            with open('eplan_log.txt', 'a') as f:
                f.write(f"{datetime.now()}: {post_data}\n")
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Log received')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Route not found')

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleServer)
    print(f'Started server with port: {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()