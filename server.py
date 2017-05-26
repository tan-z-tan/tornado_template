#!/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser

import tornado.ioloop
import tornado.web
import tornado.httpserver
from api import ping_handler
from api import echo_handler
from api import echo_image_handler


class ServerApp:

    def application(self):
        application = tornado.web.Application([
            (r"/echo", echo_handler.EchoHandler),
            (r"/ping", ping_handler.PingHandler),
            (r"/echo_image", echo_image_handler.EchoImageHandler),
        ])
        return application


# python server.py -p 8000
def main():
    parser = OptionParser()
    parser.add_option("-p", "--port", type="int", dest="port", default=8000)
    options, args = parser.parse_args()

    server = tornado.httpserver.HTTPServer(ServerApp().application())
    server.bind(options.port)
    server.start(0)  # run in parallel
    print("LISTEN: %s" % options.port)

    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
