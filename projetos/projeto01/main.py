from my_webserver import MyWebServer
from http.server import SimpleHTTPRequestHandler
import os

class ManuseioHttpRequest(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write('<p>Olá!</p>'.encode())

        elif self.path == '/pagina1':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write('<p>OLá para a página 1</p>'.encode())
        
        else:
            self.send_error(418)


app = MyWebServer(ManuseioHttpRequest)

if __name__ == "__main__":
    app.run()