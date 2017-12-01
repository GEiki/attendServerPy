from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('Content-type', 'text')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

def main():
    try:
        server = HTTPServer(('', 80), MyHttpHandler)
        print('Welcome to the machine...')
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == '__main__':
    main()




if __name__ == '__main__':
    print('ok')

#motify2