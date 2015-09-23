#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from manager import m_app

if __name__ == '__main__':
  WSGIServer(m_app, bindAddress='/tmp/flaskr-fcgi.sock').run()