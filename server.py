#!/bin/env python
# -*- coding: utf-8 -*-

from tornado.options import define, options

import tornado.ioloop
import tornado.web
import tornado.httpserver

from api import ping_hander
from api import echo_hander

class ServerApp:

    def application(self):
        application = tornado.web.Application([
            (r"/echo", echo_hander.EchoHandler),
            (r"/ping", ping_hander.PingHandler)
        ])
        return application

def main():
    define('port', type=int, default='8000', help='Port Number')
    options.parse_command_line()

    server = tornado.httpserver.HTTPServer(ServerApp().application())
    server.bind(options.port)
    server.start(0) # run in parallel
    print("LISTEN: %s" % options.port)

    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
