import http.server as hs

class HelloHandler(hs.BaseHTTPRequestHandler):
    def do_GET(self):
        # send a 200 OK response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charser=utf-8')
        self.end_headers()
        self.wfile.write(self.path[1:].encode())

if __name__ == '__main__':
    # Serve on all addresses, port 8000.
    server_address = ('', 8000)  
    httpd = hs.HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()

