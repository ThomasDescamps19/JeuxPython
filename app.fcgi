#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from JeuDevin import app

if __name__ == '__main__':
    WSGIServer(app).run()
