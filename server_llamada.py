from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hola Mundo desde Python!')

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleServer)
    print(f'Iniciando servidor en el puerto {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()