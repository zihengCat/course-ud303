import urllib
import http.server
import http.cookies
import html

html_form = '''
<html>
<head>
<title>I Remember You</title>
</head>
<body>
<p>
  {}
<p>
  <form method="POST">
    <label>
    What's your name again?
    <input type="text" name="input_name">
    </label>
    <br>
    <button type="submit">Tell me</button>
  </form>
</body>
</html>
'''

class name_handler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # How Long was the POST data
        length = int(self.headers.get("Content-length", 0))

        # Read and parse the POST data
        data = self.rfile.read(length).decode()
        name = urllib.parse.parse_qs(data)["input_name"][0]

        # Create Cookie
        c = http.cookies.SimpleCookie()
        c['inputname'] = name
        c['inputname']['domain'] = "localhost"
        c['inputname']['max-age'] = 60

        # Send a 303 to the root page
        self.send_response(303)
        self.send_header("Location", "/")
        self.send_header("Set-Cookie", c["inputname"].OutputString())
        self.end_headers()

    def do_GET(self):
        msg = "I don't know you yet!"
        if "cookie" in self.headers:
            try:
                c = http.cookies.SimpleCookie(self.headers['cookie'])
                n = c["inputname"].value
                msg = "Hello, " + n + "!"
            except:
                msg = "I don't know who you are"
                print("Read Cookies Error...")

        # Send a 200 OK
        self.send_response(200)
        # Send headers
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        # Send HTML content with msg
        html_data = html_form.format(msg)
        self.wfile.write(html_data.encode("utf-8"))


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, name_handler)
    httpd.serve_forever()

