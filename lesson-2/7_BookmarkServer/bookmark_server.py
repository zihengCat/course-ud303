import http.server
import requests
import urllib

form_html = '''
<!DOCTYPE html>
<html>
<head>
<title>Bookmark Server</title>
</head>
<body>
<form method="POST">
    <label>Long URI:
        <input name="longuri">
    </label>
    <br>
    <label>Short Name:
        <input name="shortname">
    </label>
    <br>
    <button type="submit">Save it</button>
</form>
<p>URIs I know about: </p>
<pre>
    {}
</pre>
</body>
</html>
'''

url_memory = {}

def check_URL(url, time_out=5):
    '''
    Check whether the URL is reachable
    '''
    try:
        r = requests.get(url, timeout=time_out)
        return r.status_code == 200
    except:
        return False

class shortener(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        name = urllib.parse.unquote(self.path[1:])
        if name != "":
            if name in url_memory:
                self.send_response(303)
                self.send_header("Location", url_memory[name])
                self.end_headers()
            else:
                self.send_response(404)
                self.send_header("Content-type", "text/plain, charset=utf-8")
                self.end_headers()
                self.wfile.write(("Unknow {}".format(name)).encode("utf-8"))

        else:



if __name__ == '__main__':
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, shortener)
    httpd.serve_forever()

