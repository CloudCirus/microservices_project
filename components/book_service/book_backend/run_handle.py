from wsgiref import simple_server

from book.composites import book_api

httpd = simple_server.make_server('localhost', 1235, book_api.app)

httpd.serve_forever()
