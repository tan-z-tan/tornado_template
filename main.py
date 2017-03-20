#!/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser

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
    parser = OptionParser()
    parser.add_option("-p", "--port", type="int", dest="port", default=8000)
    options, args = parser.parse_args()

    server = tornado.httpserver.HTTPServer(ServerApp().application())
    server.bind(options.port)
    server.start(0) # run in parallel
    print("LISTEN: %d" % options.port)

    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
