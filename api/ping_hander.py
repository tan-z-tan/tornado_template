import tornado.web

class PingHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("ping")

    def post(self):
        self.write("ping")
