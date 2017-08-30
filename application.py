from wsgiref.simple_server import make_server

from app import app


server = make_server('0.0.0.0', 8081, app)
server.serve_forever()
