import json
import tornado.web

class EchoHandler(tornado.web.RequestHandler):

    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        self.write(data)
