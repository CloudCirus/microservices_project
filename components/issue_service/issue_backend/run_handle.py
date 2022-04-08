from wsgiref import simple_server

from issue.composites.issue_api import app

httpd = simple_server.make_server("localhost", 1233, app)

httpd.serve_forever()
