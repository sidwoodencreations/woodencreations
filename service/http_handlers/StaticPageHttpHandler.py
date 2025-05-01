import os

import tornado.web


class AngularStaticFileHandler(tornado.web.StaticFileHandler):
    angular_index = None
    def initialize(self, path, default_filename=None, angular_index=None):
        self.angular_index = angular_index
        super(AngularStaticFileHandler, self).initialize(path, default_filename)

    def get(self, path, include_body=True):
        try:
            return super(AngularStaticFileHandler, self).get(path, include_body)
        except tornado.web.HTTPError as error:
            if error.status_code == 404 and '.' not in os.path.basename(path):
                return super(AngularStaticFileHandler, self).get(self.angular_index, include_body)
            raise
