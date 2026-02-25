import http.server as http_server

class MyWebServer:
    def __init__(self, http_hander = http_server.SimpleHTTPRequestHandler):
        self.http_handler = http_hander

    def run(self, host='localhost', port=3001):
        httpd = http_server.HTTPServer((host, port), self.http_handler)

        print(f'Servidor rodando em: {host}:{port}')
        httpd.serve_forever()