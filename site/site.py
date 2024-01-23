import http.server
from urllib.parse import urlparse, parse_qs

registered_user = {'username': 'user123', 'password': 'abc'}

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if not query_params:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('/site/home.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            if 'username' in query_params and 'password' in query_params:
                username = query_params['username'][0]
                password = query_params['password'][0]

                if username == registered_user['username'] and password == registered_user['password']:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'Login successful!')
                else:
                    self.send_response(401)
                    self.end_headers()
                    self.wfile.write(b'Invalid credentials')

if __name__ == '__main__':
    http.server.test(HandlerClass=MyHandler)
