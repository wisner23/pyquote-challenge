from wsgiref.simple_server import make_server
from app import application
import config


if __name__ == '__main__':
    server = make_server(config.SERVER_HOST, config.SERVER_PORT, application)
    server.serve_forever()
