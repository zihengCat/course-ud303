import http.server as hs
import urllib.parse as up

msg = None
class MessageHandler(hs.BaseHTTPRequestHandler):
    def do_GET(self):
        html_file = open("./message_board_part_three.html", "r")
        html_data = html_file.read()

        html_data = \
        html_data[:html_data.find("<pre>") + len("<pre>")] + \
        str(msg) + \
        html_data[html_data.find("</pre>"):]

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers();
        self.wfile.write((html_data).encode('utf-8'))
        html_file.close()

    def do_POST(self):
        length = int(self.headers.get('Content-length', 0))
        data = self.rfile.read(length).decode('utf-8')
        message = up.parse_qs(data)["message"][0]
        global msg
        msg = message
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = hs.HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()

