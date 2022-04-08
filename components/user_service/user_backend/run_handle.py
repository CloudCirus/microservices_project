from wsgiref import simple_server

from user.composites.user_api import app

httpd = simple_server.make_server('localhost', 1234, app)  # change for localhost

# httpd = simple_server.make_server('0.0.0.0', 1234, app)  # change for docker

httpd.serve_forever()
