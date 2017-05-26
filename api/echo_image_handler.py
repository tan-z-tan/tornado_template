import tornado.web
from PIL import Image
import urllib.request
import io

class EchoImageHandler(tornado.web.RequestHandler):

    def get(self):
        path = self.get_argument("path", "")

        if path == "":
          raise tornado.web.HTTPError(422)

        with urllib.request.urlopen(path) as url:
            img = Image.open(url)
            print(img.size)

            fobj = io.BytesIO()
            img.save(fobj, format="png")
            self.set_header("Content-type",  "image/png")
            self.write(fobj.getvalue())
