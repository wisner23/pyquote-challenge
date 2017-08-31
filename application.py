from wsgiref.simple_server import make_server
from app import app
import config

server = make_server(config.SERVER_HOST, config.SERVER_PORT, app)
server.serve_forever()
